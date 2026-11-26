const L=require('./lib.js');
const loc=process.argv[2]||'EN'; const only=(process.argv[3]||'').split(',').filter(Boolean);
const OUT='raw/'+loc.toLowerCase()+'-';
const want=n=>!only.length||only.includes(String(n));
const INJ = () => {
  if (window.__mk) return;
  const st=document.createElement('style');
  st.textContent='.__mk{outline:4px solid #b8392f!important;outline-offset:3px!important;border-radius:4px}.__bd{position:absolute;z-index:2147483647;width:32px;height:32px;border-radius:50%;background:#b8392f;color:#fff;font:700 18px/26px Arial,sans-serif;text-align:center;border:3px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.45);box-sizing:border-box;pointer-events:none}';
  document.head.appendChild(st);
  window.__mk=(el,n,pos)=>{ const r=el.getBoundingClientRect(); const fx=!!pos&&pos.fixed; const sx=fx?0:scrollX, sy=fx?0:scrollY;
    const o=document.createElement('div'); o.className='__bx'; o.style.cssText=`position:${fx?'fixed':'absolute'};z-index:2147483646;left:${r.left+sx-5}px;top:${r.top+sy-5}px;width:${r.width+10}px;height:${r.height+10}px;border:4px solid #b8392f;border-radius:7px;box-sizing:border-box;pointer-events:none`; document.body.appendChild(o);
    (window.__rects=window.__rects||[]).push([r.left+sx,r.top+sy,r.right+sx,r.bottom+sy]); if(n===null) return [r.left+sx,r.top+sy-6,r.right+sx,r.bottom+sy+6];
    const b=document.createElement('div'); b.className='__bd'; b.textContent=n; b.style.position=fx?'fixed':'absolute';
    let left=r.right+sx-24, top=r.top+sy-20;
    if(pos&&pos.outL){left=r.left+sx-38; top=r.top+sy+r.height/2-16;}
    if(pos&&pos.outR){left=r.right+sx+8; top=r.top+sy+r.height/2-16;}
    if(pos&&pos.inL){left=r.left+sx-14; top=r.top+sy-20;}
    b.style.left=Math.max(2,Math.min(left, innerWidth-34))+'px'; b.style.top=top+'px'; document.body.appendChild(b); return [r.left+sx,r.top+sy-22,r.right+sx,r.bottom+sy+6];};
  window.__small=(re,root)=>{re=new RegExp(re); let best=null,ba=1e12; (root||document).querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect(); if(r.width<=0||r.height<=0)return; if(!re.test(e.innerText||''))return; const a=r.width*r.height; if(a<ba){ba=a;best=e;}}); return best;};
};
async function mark(p, handle, n, pos){ await p.evaluate(INJ); return handle.evaluate((e,a)=>window.__mk(e,a[0],a[1]), [n,pos||null]); }
async function markSel(p, sel, n, pos, up){ const h = await p.locator(sel).filter({visible:true}).first().elementHandle(); const t = up? await h.evaluateHandle((e,u)=>e.closest(u)||e, up) : h; return mark(p,t,n,pos); }
async function markText(p, re, n, pos){ await p.evaluate(INJ); const h=await p.evaluateHandle(r=>window.__small(r), re); if(!(await h.evaluate(e=>!!e))) {console.log('NOTFOUND',re); return null;} return mark(p,h,n,pos); }
async function clipShot(p, name, y0, y1, fixed, x0){ x0=x0||0; if(!fixed) await p.evaluate(()=>{document.querySelectorAll('body *').forEach(e=>{const c=getComputedStyle(e).position; if((c==='fixed'||c==='sticky')&&!e.classList.contains('__bd')&&!e.classList.contains('__bx')){e.dataset.hid=1;e.style.visibility='hidden';}}); document.querySelectorAll('a[href="#container"]').forEach(e=>e.style.visibility='hidden');}); const opt={path:OUT+name+'.png', clip:{x:x0,y:Math.max(0,y0),width:390-x0,height:y1-Math.max(0,y0)}}; const rects=await p.evaluate(()=>{const r=window.__rects||[]; window.__rects=[]; return r;}); require('fs').writeFileSync(OUT+name+'.json', JSON.stringify({clip:opt.clip, rects})); if(!fixed) opt.fullPage=true; await p.screenshot(opt); console.log('saved',name,Math.round(y0),Math.round(y1)); await p.evaluate(()=>document.querySelectorAll('[data-hid]').forEach(e=>{e.style.visibility='';delete e.dataset.hid;})); }
const box = (...r)=>{r=r.filter(Boolean); return [Math.min(...r.map(a=>a[1])), Math.max(...r.map(a=>a[3]))];};

(async()=>{
  const {b,p}=await L.open(loc);
  // ---- main page ----
  if (want(0)||want(1)||want(2)||want(3)||want(12)) {
    for (let k=0;k<4;k++){
      await p.goto('https://www.e-arrivalcard.go.kr/portal/main/index.do?locale='+loc,{waitUntil:'networkidle',timeout:90000});
      await L.ready(p); await L.fixCss(p); await p.waitForTimeout(1500);
      if (!want(1)) break;
      if (await p.locator('#btnPopClose').filter({visible:true}).count()) break; console.log('no popup, retry');
    }
    if (want(1)) {
      const pop = p.locator('#btnPopClose').filter({visible:true}).first(); await pop.waitFor({timeout:15000});
      await p.evaluate(INJ);
      const a = await markText(p,'e-arrivalcard\\.go\\.kr',1,{fixed:true,outL:true});
      const c = await markSel(p,'#btnPopConfirm',2,{fixed:true});
      const top = await p.evaluate(()=>{const e=document.querySelector('#btnPopConfirm'); let c=e; while(c&&c.parentElement&&c.getBoundingClientRect().height<300) c=c.parentElement; return c.getBoundingClientRect().top;});
      await clipShot(p,'shot-1',top-12,c[3]+14,true);
      await p.evaluate(()=>{document.querySelectorAll('.__bd').forEach(x=>x.remove());document.querySelectorAll('.__bx').forEach(x=>x.remove());});
    }
    await L.closePop(p);
    if (want(0)) {
      await p.evaluate(()=>scrollTo(0,0));
      await p.evaluate(INJ);
      const t = await p.evaluateHandle(()=>window.__small('^\\s*Korea Electronic Arrival Card'));
      const tr = await t.evaluate(e=>{const r=e.getBoundingClientRect(); return r.top+scrollY;});
      const f = await markText(p,'(No fee required|수수료)[\\s\\S]*(3 days|3일)',null);
      const s0 = await markSel(p,'#btnApplyP',null);
      await clipShot(p,'shot-0',tr-16,s0[3]+24);
      await p.evaluate(()=>{document.querySelectorAll('.__bd').forEach(x=>x.remove());document.querySelectorAll('.__bx').forEach(x=>x.remove());});
    }
    if (want(2)) {
      await p.evaluate(()=>scrollTo(0,0));
      const a = await markText(p,'(Official Website|공식 전자정부|官方电子政府|電子政府|公式)',1,{outL:true});
      const d = await markText(p,'(No fee required|수수료|无手续费|手数料)[\\s\\S]*NOV[\\s\\S]*NOV[\\s\\S]*NOV',2);
      const s = await markSel(p,'#btnApplyP',3);
      await clipShot(p,'shot-2',0,s[3]+40);
      await p.evaluate(()=>{document.querySelectorAll('.__bd').forEach(x=>x.remove());document.querySelectorAll('.__bx').forEach(x=>x.remove());});
    }
    if (want(12)) {
      const c = await markSel(p,'#btnSearchNModify',1);
      const top = await p.evaluate(()=>{let e=document.querySelector('#btnSearchNModify'); while(e.parentElement&&e.getBoundingClientRect().height<200) e=e.parentElement; return e.getBoundingClientRect().top+scrollY;});
      await clipShot(p,'shot-12',top-12,c[3]+40);
      await p.evaluate(()=>{document.querySelectorAll('.__bd').forEach(x=>x.remove());document.querySelectorAll('.__bx').forEach(x=>x.remove());});
    }
    if (want(3)) {
      await p.evaluate(()=>scrollTo(0,0));
      await p.locator('button.btnLnb').filter({visible:true}).first().click(); await p.waitForTimeout(800);
      const d = p.locator('a:has-text("Declaration"), a:has-text("신고")').filter({visible:true}).filter({hasNotText:/Check|조회|Guide|안내/}).first();
      await d.click(); await p.waitForTimeout(800);
      const m1 = await mark(p, await d.elementHandle(), 1, {fixed:true});
      const sub = p.locator('a[href*="agreementPolicy.do?applyType=P&type=MOB"]').filter({visible:true}).first();
      const m2 = await mark(p, await sub.elementHandle(), 2, {fixed:true});
      const mx = await p.evaluate(()=>{const e=[...document.querySelectorAll('a')].find(a=>/agreementPolicy.do\?applyType=P&type=MOB/.test(a.getAttribute('href')||'')&&a.getBoundingClientRect().height>0); let c=e; while(c.parentElement&&c.getBoundingClientRect().width<250) c=c.parentElement; return c.getBoundingClientRect().left;}); await clipShot(p,'shot-3',84,m2[3]+30,true,Math.max(0,Math.round(mx)-2));
    }
  }
  // ---- agreement ----
  await p.goto('https://www.e-arrivalcard.go.kr/portal/apply/agreementPolicy.do?applyType=P&type=MOB&locale='+loc,{waitUntil:'networkidle',timeout:90000});
  await p.waitForSelector('#chkAgreementAll',{state:'attached',timeout:90000}); await L.ready(p); await L.fixCss(p);
  await p.check('#chkAgreementAll',{force:true});
  await p.fill('#emlAddr1','hong.gildong@example.com'); await p.fill('#emlAddr2','hong.gildong@example.com');
  if (want(4)) {
    await p.evaluate(INJ);
    const a = await markSel(p,'#chkAgreementAll',1,{outR:true},'div,li,p');
    const e1 = await markSel(p,'#emlAddr1',2);
    const e2 = await markSel(p,'#emlAddr2',3);
    const ok = await markSel(p,'#btnOk',4);
    await clipShot(p,'shot-4a',a[1]-110,a[3]+30);
    await clipShot(p,'shot-4b',e1[1]-120,ok[3]+24);
  }
  await p.click('#btnOk'); await p.waitForURL(/individual/,{timeout:90000}); await p.waitForLoadState('networkidle'); await L.ready(p); await L.fixCss(p);
  await L.closePop(p);
  const V = s => p.locator(s).filter({visible:true}).first();
  if (want(5)) {
    await p.evaluate(()=>scrollTo(0,0));
    await V('button.btnOcrScan').click(); await p.waitForTimeout(1200);
    const ph = await markSel(p,'#btnPhoto',1,{fixed:true});
    const up = await markSel(p,'#btnOcrFileUpload',2,{fixed:true});
    const cl = await markSel(p,'#btnPopClose',3,{fixed:true,outL:true});
    const top = await p.evaluate(()=>{let c=document.querySelector('#btnPopClose'); while(c.parentElement&&c.getBoundingClientRect().height<300) c=c.parentElement; return c.getBoundingClientRect().top;});
    await clipShot(p,'shot-5',top-14,ph[3]+30,true);
    await p.evaluate(()=>{document.querySelectorAll('.__bd').forEach(x=>x.remove());document.querySelectorAll('.__bx').forEach(x=>x.remove());});
    await L.closePop(p);
  }
  // ---- fill sample (obviously fake) ----
  await V('input[name=ps_fmnm]').fill('HONG'); await V('input[name=ps_gvnm]').fill('GILDONG');
  const pickSel = async (sel, how) => { const h=await V(sel).elementHandle(); await h.evaluate((s,how)=>{ let i; const o=[...s.options].map(x=>x.text.trim());
      if(how.text) i=o.indexOf(how.text); if(how.after) i=o.indexOf(how.after)+1; if(how.idx!==undefined) i=how.idx; if(i<0||i===undefined) i=1; s.selectedIndex=i; s.dispatchEvent(new Event('change',{bubbles:true}));}, how); await p.waitForTimeout(300); };
  await pickSel('select.btd_year',{text:'1990'}); await pickSel('select.btd_month',{after:'00'}); await pickSel('select.btd_day',{text:'01'});
  try { await V('.info_nat').click(); await p.waitForTimeout(500); await V('.info-nat-options p[data-natenchr3poscd="USA"]').click(); } catch(e){ console.log('nat fail', e.message.slice(0,80)); }
  await V('input[name=ps_no]').fill('M00000000');
  const sexSel = await p.locator('select').filter({visible:true}).filter({hasText:/Male|남|男/}).first().elementHandle();
  await sexSel.evaluate(s=>{s.selectedIndex=2; s.dispatchEvent(new Event('change',{bubbles:true}));});
  const tdOf = async (sel) => (await V(sel).elementHandle()).evaluateHandle(e=>e.closest('td')||e.parentElement);
  // expiry selects: those after sex
  await p.evaluate(()=>{ const ss=[...document.querySelectorAll('select')].filter(s=>s.getBoundingClientRect().height>0); const i=ss.findIndex(s=>/Male|남|男/.test(s.innerText)); const [y,m,d]=ss.slice(i+1,i+4);
     const set=(s,k)=>{s.selectedIndex=k; s.dispatchEvent(new Event('change',{bubbles:true}));}; const yi=[...y.options].findIndex(o=>o.text.trim()==='2034'); set(y,yi>0?yi:5); set(m,12); });
  await p.waitForTimeout(300);
  await p.evaluate(()=>{ const ss=[...document.querySelectorAll('select')].filter(s=>s.getBoundingClientRect().height>0); const i=ss.findIndex(s=>/Male|남|男/.test(s.innerText)); const d=ss[i+3]; d.selectedIndex=d.options.length-1; d.dispatchEvent(new Event('change',{bubbles:true}));});
  if (want(6)) {
    const r=[];
    r.push(await mark(p, await V('input[name=ps_fmnm]').elementHandle(),1));
    r.push(await mark(p, await V('input[name=ps_gvnm]').elementHandle(),2));
    r.push(await mark(p, await V('#fmnmChk1').evaluateHandle(e=>e.closest('.checkbox-area')||e.parentElement),3,{outR:true}));
    const usfk = await p.evaluateHandle(()=>window.__small('USFK'));
    r.push(await mark(p, usfk, 4, {outR:true}));
    r.push(await mark(p, await V('input[name=ps_no]').elementHandle(),null));
    const ub = await V('button.btnOcrScan').boundingBox(); const sy=await p.evaluate(()=>scrollY);
    const h5=await p.evaluate(()=>document.querySelector('h5.infoBox').getBoundingClientRect().top+scrollY); await clipShot(p,'shot-6',r[0][1]-50,r[4][3]+20);
  }
  // arrival/departure
  await V('input[name=ent_prr_ymd]').evaluate(e=>{e.removeAttribute('readonly'); e.value='2026-11-28'; e.dispatchEvent(new Event('change',{bubbles:true}));});
  await V('input[name=dep_prr_ymd]').evaluate(e=>{e.removeAttribute('readonly'); e.value='2026-12-05'; e.dispatchEvent(new Event('change',{bubbles:true}));});
  const fl = p.locator('input[placeholder^="Example"], input[placeholder*="KE000"]').filter({visible:true});
  await fl.first().fill('KE000');
  if (want(7)) {
    await p.evaluate(INJ);
    const air = await p.evaluateHandle(()=>{const bs=[...document.querySelectorAll('button')].filter(b=>b.getBoundingClientRect().height>0&&/^AIR$|항공/.test(b.innerText.trim())); return bs[0];});
    const r1 = await mark(p, air, 1);
    const r2 = await mark(p, await V('input[name=ent_prr_ymd]').elementHandle(), 2);
    const r3 = await mark(p, await p.locator('.ent_cno_cd').filter({visible:true}).first().elementHandle(), 3);
    const r4 = await mark(p, await fl.first().elementHandle(), 4);
    const r5 = await mark(p, await V('input[name=dep_prr_ymd]').elementHandle(), 5);
    const flights = p.locator('input[placeholder^="Example"], input[placeholder*="KE000"]').filter({visible:true});
    const r6 = await mark(p, await flights.nth(1).elementHandle(), 6);
    const hdr = await p.evaluate(()=>{const h=[...document.querySelectorAll('h5.infoBox')].find(h=>h.classList.contains('idp')); return h.getBoundingClientRect().top+scrollY;});
    await clipShot(p,'shot-7',hdr-10,r6[3]+80);
  }
  // purpose, stay, job
  await pickSel('select:has(option:has-text("Tourism")), select:has(option:has-text("관광")), select:has(option:has-text("観光")), select:has(option:has-text("旅游"))',{idx:1}).catch(e=>console.log('purpose',e.message.slice(0,80)));
  await p.locator('input[name=appl_addr_gbcd_applyNo01]').filter({visible:true}).first().check({force:true}); await p.waitForTimeout(600);
  const jobSel = 'select:has(option:has-text("Office worker")), select:has(option:has-text("회사원")), select:has(option:has-text("会社員")), select:has(option:has-text("上班族"))';
  await pickSel(jobSel,{idx:1}).catch(e=>console.log('job',e.message.slice(0,80)));
  if (want(8)) {
    await p.evaluate(INJ);
    const r=[];
    const purp = await p.locator('select:has(option:has-text("Tourism")), select:has(option:has-text("관광")), select:has(option:has-text("観光")), select:has(option:has-text("旅游"))').filter({visible:true}).first().elementHandle();
    r.push(await mark(p, purp,1));
    r.push(await mark(p, await V('#visa_no01').evaluateHandle(e=>{let c=e.parentElement; while(c.parentElement && !c.querySelector('button')) c=c.parentElement; return c;}),2));
    const radio = await p.locator('input[name=appl_addr_gbcd_applyNo01]').filter({visible:true}).first().elementHandle();
    r.push(await mark(p, await radio.evaluateHandle(e=>{let c=e; while(c.parentElement && [...c.querySelectorAll('input[type=radio]')].filter(x=>x.getBoundingClientRect().height>0).length<3) c=c.parentElement; return c;}),3));
    const bs = await p.locator('input[name=soj_prrpl_rnm_bs_addr]').filter({visible:true}).first().elementHandle();
    r.push(await mark(p, await bs.evaluateHandle(e=>{let c=e.parentElement; while(c.parentElement && !c.querySelector('button')) c=c.parentElement; return c.querySelector('button');}),4));
    r.push(await mark(p, await V('input[name=soj_prrpl_rnm_det_addr]').elementHandle(),5));
    r.push(await mark(p, await V('input[name=soj_prrar_tel]').elementHandle(),6));
    const js = await p.locator(jobSel).filter({visible:true}).first().elementHandle();
    r.push(await mark(p, js,7));
    await clipShot(p,'shot-8',r[0][1]-34,r[6][3]+24);
    await p.evaluate(()=>{document.querySelectorAll('.__bd').forEach(x=>x.remove());document.querySelectorAll('.__bx').forEach(x=>x.remove());});
  }
  if (want(10)) {
    const em = await mark(p, await V('input[name=rep_eml_addr]').elementHandle(),1);
    const sb = await mark(p, await V('#btnSubmit').elementHandle(),2);
    await clipShot(p,'shot-10',em[1]-130,sb[3]+30);
    await p.evaluate(()=>{document.querySelectorAll('.__bd').forEach(x=>x.remove());document.querySelectorAll('.__bx').forEach(x=>x.remove());});
  }
  if (want(11)) {
    await p.evaluate(()=>scrollTo(0,0));
    await p.evaluate(INJ);
    const add = await p.locator('button:has-text("Add declarant"), button:has-text("申告者を追加"), button:has-text("添加申报人"), button:has-text("신고인 추가"), button:has-text("추가")').filter({visible:true}).first().elementHandle();
    const r1 = await mark(p, add, 1);
    await clipShot(p,'shot-11',140,r1[3]+80);
    await p.evaluate(()=>{document.querySelectorAll('.__bd').forEach(x=>x.remove());document.querySelectorAll('.__bx').forEach(x=>x.remove());});
  }
  if (want(9)) {
    const eng = p.locator('input[name=soj_prrpl_rnm_bs_addr]').filter({visible:true}).first();
    const btn = await eng.evaluateHandle(e=>{let c=e.parentElement; while(c.parentElement && !c.querySelector('button')) c=c.parentElement; return c.querySelector('button');});
    console.log('addrbtn', await btn.evaluate(e=>e.outerHTML.slice(0,300)));
    const spans = await btn.evaluate(e=>[...e.querySelectorAll('span,em')].map(s=>s.innerText));
    console.log('spans',spans);
    // click the ENG half for EN page, KOR half for KO page
    await p.setViewportSize({width:390,height:1200}); await p.waitForTimeout(300); const bb = await btn.boundingBox(); await btn.click({position:{x:(loc!=='KO'? bb.width*0.75 : bb.width*0.25), y:bb.height/2}});
    await p.waitForTimeout(1500);
    await V('#keywordAddr').fill('08013'); await V('#btnSearchAddr').click(); await p.waitForTimeout(2500); await L.ready(p).catch(()=>{});
    const k = await markSel(p,'#keywordAddr',8,{fixed:true},'div');
    const row = await p.evaluateHandle(()=>{const k=document.querySelector('#keywordAddr'); const kb=k.getBoundingClientRect().bottom; return [...document.querySelectorAll('li,tr,a,div')].filter(x=>{const r=x.getBoundingClientRect(); return r.height>20&&r.height<90&&r.top>kb+20&&/08013/.test(x.innerText)&&x.offsetParent;}).sort((a,b)=>a.getBoundingClientRect().top-b.getBoundingClientRect().top || b.getBoundingClientRect().width-a.getBoundingClientRect().width)[0]||null;});
    let r2=null; if (await row.evaluate(e=>!!e)) r2 = await mark(p,row,9,{fixed:true}); else console.log('no result row');
    const t2 = await markSel(p,'#twoTab',10,{fixed:true});
    const top = await p.evaluate(()=>{let c=document.querySelector('#twoTab'); while(c.parentElement&&c.getBoundingClientRect().height<350) c=c.parentElement; return c.getBoundingClientRect().top;});
    const bot = r2 ? r2[3]+60 : 900;
    await clipShot(p,'shot-9',top-14,Math.min(bot,1200),true);
  }
  await b.close();
})().catch(e=>{console.error('ERR',e.message.slice(0,600)); process.exit(1);});
