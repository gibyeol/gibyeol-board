const L=require('./lib.js');
(async()=>{
  for (const loc of ['EN','KO']) {
  const {b,p}=await L.open(loc);
  await L.toForm(p,loc); await L.fixCss(p); await L.closePop(p);
  const n = await p.locator('button.btnToolTip').count();
  const out=[];
  for (let i=0;i<n;i++){ const bt=p.locator('button.btnToolTip').nth(i); if(!(await bt.isVisible())) continue;
    const before = await p.evaluate(()=>document.body.innerText);
    await bt.click().catch(()=>{}); await p.waitForTimeout(500);
    const after = await p.evaluate(()=>[...document.querySelectorAll('div,p,ul')].filter(e=>{const s=getComputedStyle(e); const r=e.getBoundingClientRect(); return r.height>0 && (s.position==='absolute'||s.position==='fixed') && e.innerText.trim().length>10 && e.innerText.length<1500;}).map(e=>e.innerText.trim()).join('\n---\n'));
    out.push('## tip '+i+'\n'+after);
    await p.keyboard.press('Escape'); await bt.click().catch(()=>{}); await p.waitForTimeout(300);
  }
  require('fs').writeFileSync('raw/tips-'+loc+'.txt', out.join('\n\n'));
  await b.close();
  }
})();
