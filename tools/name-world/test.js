// node test.js <port>  — serves nothing itself; expects dist served on the port
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const PORT = process.argv[2] || 8765, OUT = path.join(__dirname, 'shots');
fs.mkdirSync(OUT, { recursive: true });
const cases = [
  { lang: 'en', path: '/name/', names: ['Sophia', 'James', 'Stella', '김민지', '田中 花子'] },
  { lang: 'ko', path: '/ko/name/', names: ['Sophia', 'James', 'Stella', '김민지', '田中 花子'] },
  { lang: 'ja', path: '/ja/name/', names: ['Sophia', 'James', 'Stella', '김민지', '田中 花子'] },
  { lang: 'zh-tw', path: '/zh-tw/name/', names: ['Sophia', 'James', 'Stella', '김민지', '田中 花子'] }
];
(async () => {
  const browser = await chromium.launch();
  const report = [];
  for (const c of cases) {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, acceptDownloads: true, locale: c.lang === 'zh-tw' ? 'zh-TW' : c.lang });
    const page = await ctx.newPage();
    const errors = [], requests = [];
    page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    page.on('pageerror', e => errors.push('pageerror: ' + e.message));
    page.on('request', r => requests.push(r.url()));
    for (const n of c.names) {
      await page.goto(`http://127.0.0.1:${PORT}${c.path}`, { waitUntil: 'networkidle' });
      requests.length = 0;
      await page.fill('#namer-in', n);
      await page.click('.namer-form button');
      await page.waitForTimeout(300);
      if (n === '김민지') { // pick hanja: 敏 then 智 (wisdom) if offered
        const picks = await page.$$('.namer-pick');
        for (const p of picks) {
          const b = (await p.$('button[data-h="智"]')) || (await p.$('button[data-h="敏"]')) || (await p.$('button'));
          if (b) await b.click();
        }
        await page.waitForTimeout(200);
      }
      const info = await page.evaluate(() => {
        const q = s => Array.from(document.querySelectorAll(s));
        return {
          world: q('.namer-world').map(s => ({ h: s.querySelector('.namer-h').textContent, regions: Array.from(s.querySelectorAll(':scope > ul > li')).map(li => li.getAttribute('data-r')), links: Array.from(s.querySelectorAll('a[href^="/"]')).map(a => a.getAttribute('href')), srcLinks: s.querySelectorAll('.namer-step a[href^="http"]').length })),
          born: q('.namer-born .namer-h').map(h => h.textContent + ' / ' + h.parentNode.querySelectorAll('li').length),
          chainKo: q('.namer-chain:not(.namer-world) .namer-h').map(h => h.textContent)
        };
      });
      // outbound requests after typing (privacy: nothing typed leaves the browser)
      const external = requests.filter(u => !u.startsWith(`http://127.0.0.1:${PORT}`) && !u.startsWith('data:'));
      const leaks = requests.filter(u => u.includes(encodeURIComponent(n)) || u.includes(n));
      // card
      let card = null;
      const btn = await page.$('.namer-save');
      if (btn) {
        const [dl] = await Promise.all([page.waitForEvent('download', { timeout: 10000 }).catch(() => null), btn.click()]);
        if (dl) { const f = path.join(OUT, `card-${c.lang}-${n.replace(/\s/g, '_')}.png`); await dl.saveAs(f); card = { file: f, size: fs.statSync(f).size }; }
      }
      const shot = path.join(OUT, `${c.lang}-${n.replace(/\s/g, '_')}.png`);
      await page.screenshot({ path: shot, fullPage: true });
      report.push({ lang: c.lang, name: n, ...info, external, leaks, card, shot });
    }
    report.push({ lang: c.lang, consoleErrors: errors });
    await ctx.close();
  }
  await browser.close();
  fs.writeFileSync(path.join(OUT, 'report.json'), JSON.stringify(report, null, 1));
  for (const r of report) console.log(JSON.stringify(r));
})();
