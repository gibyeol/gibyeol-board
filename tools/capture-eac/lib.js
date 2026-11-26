const { chromium } = require('playwright');
exports.open = async (locale) => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport:{width:390,height:844}, deviceScaleFactor:2, isMobile:true, hasTouch:true, locale: locale==='KO'?'ko-KR':'en-US' });
  const p = await ctx.newPage();
  p.on('dialog', async d => { console.log('DIALOG:', d.message()); await d.accept(); });
  return {b,p};
};
exports.dump = async (p) => p.evaluate(()=>{
  const out=[];
  document.querySelectorAll('input,select,textarea,button,a.btn,label').forEach(e=>{
    const r=e.getBoundingClientRect(); if(!(r.width>0&&r.height>0)) return;
    const t=(e.innerText||e.value||e.placeholder||e.getAttribute('title')||'').trim().replace(/\s+/g,' ').slice(0,70);
    out.push(`${e.tagName}${e.type?'['+e.type+']':''} #${e.id} name=${e.name||''} y=${Math.round(r.top+scrollY)} |${t}| ${e.getAttribute('onclick')||''}`.slice(0,220));
  });
  return out.join('\n');
});
exports.ready = async (p) => { await p.waitForFunction(()=>{const l=document.querySelector('.loadingBox'); return !l || getComputedStyle(l).display==='none' || l.getBoundingClientRect().height===0;},null,{timeout:90000}); await p.waitForTimeout(300); };
exports.toForm = async (p, loc) => {
  await p.goto('https://www.e-arrivalcard.go.kr/portal/apply/agreementPolicy.do?applyType=P&type=MOB&locale='+loc,{waitUntil:'networkidle',timeout:90000});
  await p.waitForSelector('#chkAgreementAll',{state:'attached',timeout:90000});
  await exports.ready(p);
  await p.check('#chkAgreementAll',{force:true});
  await p.fill('#emlAddr1','hong.gildong@example.com'); await p.fill('#emlAddr2','hong.gildong@example.com');
  await p.click('#btnOk'); await p.waitForURL(/individual/,{timeout:90000}); await p.waitForLoadState('networkidle');
  await exports.ready(p);
};
exports.closePop = async (p) => { const c=p.locator('#btnPopClose').filter({visible:true}); try{ await c.first().waitFor({timeout:5000}); await c.first().click(); await p.waitForTimeout(400);}catch(e){} };
exports.fixCss = async (p) => {
  for (let k=0;k<6;k++){
    const bad = await p.evaluate(()=>[...document.querySelectorAll('link[rel=stylesheet]')].filter(l=>{try{return !l.sheet||l.sheet.cssRules.length===0}catch(e){return true}}).map(l=>l.href));
    if(!bad.length) return;
    console.log('refetch css', bad.map(x=>x.split('/').pop()));
    await p.evaluate(async (bad)=>{ await Promise.all(bad.map(h=>new Promise(res=>{const old=[...document.querySelectorAll('link[rel=stylesheet]')].find(l=>l.href===h); const n=document.createElement('link'); n.rel='stylesheet'; n.href=h+'&r='+Math.random(); n.onload=n.onerror=res; old.after(n); old.remove();})));}, bad);
    await p.waitForTimeout(500);
  }
};
