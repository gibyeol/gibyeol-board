const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage();
  const files = process.argv.slice(2);
  let bad = 0;
  fs.mkdirSync('shots', {recursive: true});
  for (const f of files) {
    const svg = fs.readFileSync(f, 'utf8');
    for (const w of [340, 360, 720]) {
      await pg.setViewportSize({width: w, height: 800});
      await pg.setContent(`<html><body style="margin:0">${svg.replace('<svg ', `<svg style="width:${w}px;display:block" `)}</body></html>`);
      const r = await pg.evaluate(() => {
        const s = document.querySelector('svg'); const vb = s.viewBox.baseVal;
        const scale = s.getBoundingClientRect().width / vb.width;
        const out = [];
        let minPx = 99;
        for (const t of s.querySelectorAll('text')) {
          const bb = t.getBBox(); const fs = parseFloat(t.getAttribute('font-size'));
          minPx = Math.min(minPx, fs * scale);
          if (bb.x < 10 || bb.x + bb.width > vb.width - 24) out.push(`${t.textContent} [${bb.x.toFixed(0)}..${(bb.x+bb.width).toFixed(0)}]`);
          if (fs < 16) out.push('small font ' + fs + ' ' + t.textContent);
        }
        const ts=[...s.querySelectorAll('text')].map(t=>({t:t.textContent,b:t.getBBox()}));
        for (let i=0;i<ts.length;i++) for (let j=i+1;j<ts.length;j++) {
          const a=ts[i].b, c=ts[j].b;
          const ox=Math.min(a.x+a.width,c.x+c.width)-Math.max(a.x,c.x), oy=Math.min(a.y+a.height,c.y+c.height)-Math.max(a.y,c.y);
          if (ox>1 && oy>3) out.push('OVERLAP '+ts[i].t+' / '+ts[j].t);
        }
        return {out, minPx, h: s.getBoundingClientRect().height};
      });
      if (w === 340) {
        if (r.out.length || r.minPx < 13) { bad++; console.log('BAD', path.basename(path.dirname(f)) + '/' + path.basename(f), r.minPx.toFixed(1), r.out.join(' | ')); }
        await pg.screenshot({path: `shots/${path.basename(path.dirname(f))}-${path.basename(f, '.svg')}-${w}.png`, fullPage: true});
      } else if (w === 360) {
        await pg.screenshot({path: `shots/${path.basename(path.dirname(f))}-${path.basename(f, '.svg')}-${w}.png`, fullPage: true});
      } else {
        await pg.screenshot({path: `shots/${path.basename(path.dirname(f))}-${path.basename(f, '.svg')}-${w}.png`, fullPage: true});
      }
    }
  }
  console.log('checked', files.length, 'bad', bad);
  await b.close();
})();
