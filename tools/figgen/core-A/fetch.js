const { chromium } = require('playwright');
(async () => {
  const p = process.env.HTTPS_PROXY || process.env.https_proxy;
  const b = await chromium.launch(p ? {proxy:{server:p}} : {});
  const pg = await b.newPage({ignoreHTTPSErrors:true});
  await pg.goto(process.argv[2], {waitUntil:'networkidle', timeout:60000});
  await pg.waitForTimeout(parseInt(process.env.W||"3000"));
  const t = await pg.evaluate(()=>document.body.innerText);
  require('fs').writeFileSync(process.argv[3], t);
  console.log(t.length);
  await b.close();
})().catch(e=>{console.error(e.message);process.exit(1)});
