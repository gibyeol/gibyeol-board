// Deal cards for Threads image posts, rendered from data/deals.json.
//   node tools/make_cards.js <lang> [YYYY-MM-DD]
// Writes static/cards/<date>/<lang>-board.png (one card: deals ending soonest) and
// <lang>-code-<id>.png (one card per deal with a public code). 1080x1350 (Threads 4:5).
// Needs Playwright (Claude sessions have it); run before committing, Cloudflare only copies the PNGs.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..');
const lang = process.argv[2] || 'ko';
const today = process.argv[3] || new Date(Date.now() + 9 * 3600e3).toISOString().slice(0, 10);
const D = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/deals.json'), 'utf8'));
const T = {
  ko: { head: '이번 주 마감 세일', sub: '마감 임박 순 · 출처 확인', ends: n => n === 0 ? '오늘 마감' : `D-${n}`, starts: n => `${n}일 뒤 시작`, exp: '예정', code: '할인 코드', foot: '전체 일정과 출처는 Nadri 할인 상황판', url: 'nadri-guide.pages.dev/ko/deals' },
  en: { head: 'Korea sales ending soon', sub: 'Sorted by end date · sources checked', ends: n => n === 0 ? 'Ends today' : `${n}d left`, starts: n => `Starts in ${n}d`, exp: 'expected', code: 'Code', foot: 'Full list and sources on Nadri', url: 'nadri-guide.pages.dev/deals' },
  ja: { head: 'まもなく終わる韓国セール', sub: '終了が近い順 · 出典確認済み', ends: n => n === 0 ? '今日まで' : `残り${n}日`, starts: n => `${n}日後に開始`, exp: '予定', code: 'コード', foot: '全リストと出典は Nadri で', url: 'nadri-guide.pages.dev/ja/deals' },
  'zh-tw': { head: '即將截止的韓國特賣', sub: '依截止日排序 · 已確認來源', ends: n => n === 0 ? '今天截止' : `剩 ${n} 天`, starts: n => `${n} 天後開始`, exp: '預計', code: '代碼', foot: '完整清單與來源在 Nadri', url: 'nadri-guide.pages.dev/zh-tw/deals' },
}[lang];
const day = s => new Date(s + 'T00:00:00');
const t0 = day(today);
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const plain = s => s.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1');
const items = D.items.filter(d => d.text[lang] && day(d.end) >= t0);
const live = items.filter(d => day(d.start) <= t0).sort((a, b) => a.end.localeCompare(b.end));
const soon = items.filter(d => day(d.start) > t0).sort((a, b) => a.start.localeCompare(b.start));
const fmt = s => { const x = day(s); return `${x.getMonth() + 1}/${x.getDate()}`; };
const dd = d => day(d.start) > t0 ? T.starts(Math.round((day(d.start) - t0) / 864e5)) : T.ends(Math.round((day(d.end) - t0) / 864e5));
const CSS = `
@font-face{font-family:Brico;src:url(file://${ROOT}/static/fonts/bricolage-latin.woff2)}
*{box-sizing:border-box}body{margin:0;width:1080px;height:1350px;font-family:Brico,"Noto Sans CJK KR","Noto Sans CJK JP","Noto Sans CJK TC",sans-serif;color:#172536;background:#EEF3F1;word-break:keep-all}
.wrap{height:100%;padding:72px 72px 56px;display:flex;flex-direction:column;gap:28px}
.top{display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:30px}
.brand{display:flex;gap:14px;align-items:center}.dot{width:34px;height:34px;border-radius:8px;background:conic-gradient(#5E9C8B 0 25%,#F0B93A 0 50%,#9C3D63 0 75%,#9DC3E6 0)}
.date{color:#4A5866;font-weight:500}
h1{font-size:74px;line-height:1.08;margin:8px 0 0;letter-spacing:-.02em}
.sub{font-size:28px;color:#4A5866}
.rows{display:flex;flex-direction:column;gap:14px;flex:1}
.row{display:grid;grid-template-columns:170px 1fr;gap:24px;align-items:center;background:#fff;border-radius:18px;padding:22px 28px}
.pill{justify-self:start;font-weight:800;font-size:30px;padding:10px 18px;border-radius:999px;background:#172536;color:#fff;white-space:nowrap}
.pill.hot{background:#9C3D63}.pill.tbc{background:#4A5866}
.t{font-weight:800;font-size:34px;line-height:1.2}.m{font-size:25px;color:#4A5866;margin-top:4px}
.code{display:inline-block;margin-top:8px;font:700 26px ui-monospace,monospace;border:3px dashed #9C3D63;border-radius:8px;padding:2px 10px;color:#9C3D63}
.foot{display:flex;justify-content:space-between;align-items:center;font-size:26px;color:#4A5866;border-top:3px solid #fff;padding-top:22px}.foot b{color:#172536}
.big{flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px}
.big .label{font-size:34px;color:#4A5866;font-weight:700}
.big .val{font:800 92px ui-monospace,monospace;color:#9C3D63;border:6px dashed #9C3D63;border-radius:24px;padding:24px 36px;align-self:flex-start;background:#fff}
.big .note{font-size:32px;line-height:1.5;max-width:900px}`;
const page = body => `<!doctype html><meta charset=utf-8><style>${CSS}</style><div class=wrap>
<div class=top><div class=brand><span class=dot></span>Nadri</div><div class=date>${today}</div></div>${body}
<div class=foot><span>${esc(T.foot)}</span><b>${esc(T.url)}</b></div></div>`;
(async () => {
  const out = path.join(ROOT, 'static/cards', today); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  const shot = async (html, name) => { await p.setContent(html); await p.waitForTimeout(150); await p.screenshot({ path: path.join(out, name) }); console.log(path.join('static/cards', today, name)); };
  const board = [...live, ...soon].slice(0, 7).map(d => {
    const n = Math.round((day(d.end) - t0) / 864e5), up = day(d.start) > t0;
    const cls = up ? 'tbc' : (n <= 3 ? 'hot' : '');
    const code = (d.code || []).map(c => `<span class=code>${esc(c.value)}</span> `).join('');
    return `<div class=row><span class="pill ${cls}">${esc(dd(d))}</span><div><div class=t>${esc(d.text[lang].title)}${d.status === 'expected' ? ` <span class=m>(${T.exp})</span>` : ''}</div><div class=m>${fmt(d.start)} – ${fmt(d.end)}</div>${code}</div></div>`;
  }).join('');
  await shot(page(`<div><h1>${esc(T.head)}</h1><div class=sub>${esc(T.sub)}</div></div><div class=rows>${board}</div>`), `${lang}-board.png`);
  for (const d of [...live, ...soon].filter(d => d.code)) {
    const codes = d.code.map(c => `<div class=val>${esc(c.value)}</div>${c.note && c.note[lang] ? `<div class=label>${esc(c.note[lang])}</div>` : ''}`).join('');
    await shot(page(`<div class=big><div class=label>${esc(T.code)} · ${esc(dd(d))} · ~${fmt(d.end)}</div><h1>${esc(d.text[lang].title)}</h1>${codes}<div class=note>${esc(plain(d.text[lang].note))}</div></div>`), `${lang}-code-${d.id}.png`);
  }
  await b.close();
})();
