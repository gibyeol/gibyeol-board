const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({viewport:{width:390,height:800}});
  for (const p of process.argv.slice(2)) {
    await pg.goto('http://localhost:8791/'+p, {waitUntil:'networkidle'}); await pg.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60));}}); await pg.waitForTimeout(500);
    const broken = await pg.evaluate(()=>[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src));
    const fw = await pg.evaluate(()=>[...document.querySelectorAll('figure.fig img')].map(i=>Math.round(i.getBoundingClientRect().width)));
    console.log(p, 'broken', broken.join(' '), 'fig widths', fw.join(','));
    await pg.screenshot({path: '../page-'+p.replace(/\//g,'_')+'.png', fullPage:true});
  }
  await b.close();
})();
