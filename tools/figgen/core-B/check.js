// usage: node check.js name1 name2 ...  (figure base names) ; renders each lang at 340/360/720
const {chromium}=require('playwright'); const fs=require('fs');
const OUT='/tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/core-B/png';
(async()=>{
 const b=await chromium.launch(); let bad=0;
 for (const name of process.argv.slice(2)) for (const lang of ['en','ko','ja','zh-tw']) for (const w of [340,360,720]){
  const svg=fs.readFileSync(`/home/user/gibyeol-board/static/fig/${lang}/${name}.svg`,'utf8');
  const p=await b.newPage({viewport:{width:w,height:900}});
  await p.setContent(`<!doctype html><html><body style="margin:0;background:#fff"><div id="f" style="width:${w}px">${svg.replace(/<svg /,'<svg style="display:block;width:100%;height:auto" ')}</div></body></html>`);
  const res=await p.evaluate((w)=>{const s=document.querySelector('svg');const vb=s.viewBox.baseVal;const sc=w/vb.width;const out=[];
    const texts=[...s.querySelectorAll('text')];
    texts.forEach(t=>{const fs=parseFloat(t.getAttribute('font-size')); if(fs*sc<13 && w==340) out.push('SMALL '+t.textContent+' '+(fs*sc).toFixed(1));
      const bb=t.getBBox(); if(bb.x<4||bb.x+bb.width>vb.width-4||bb.y<0||bb.y+bb.height>vb.height) out.push('OUT '+t.textContent+' '+bb.x.toFixed(0)+'..'+(bb.x+bb.width).toFixed(0));});
    const rects=[...s.querySelectorAll('rect')].slice(1).map(r=>r.getBBox()).filter(r=>r.width<vb.width-10);
    texts.forEach(t=>{const bb=t.getBBox(); const cy=bb.y+bb.height/2, cx=bb.x+bb.width/2;
      const cand=rects.filter(r=>cx>r.x&&cx<r.x+r.width&&cy>r.y&&cy<r.y+r.height).sort((a,b)=>a.width*a.height-b.width*b.height);
      const r=cand[0]; if(r && (bb.x<r.x+2||bb.x+bb.width>r.x+r.width-2)) out.push('BOX '+t.textContent+' '+bb.x.toFixed(0)+'..'+(bb.x+bb.width).toFixed(0)+' in '+r.x.toFixed(0)+'..'+(r.x+r.width).toFixed(0));});
    for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){const a=texts[i].getBBox(),c=texts[j].getBBox(); const ov=Math.min(a.x+a.width,c.x+c.width)-Math.max(a.x,c.x), oh=Math.min(a.y+a.height,c.y+c.height)-Math.max(a.y,c.y); if(ov>1&&oh>2) out.push('OVERLAP '+texts[i].textContent+' / '+texts[j].textContent);}
    return out;},w);
  if(res.length){bad++; console.log(name,lang,w,'\n  '+res.join('\n  '));}
  await (await p.$('#f')).screenshot({path:`${OUT}/${name}-${lang}-${w}.png`}); await p.close();
 }
 await b.close(); console.log(bad? 'ISSUES '+bad : 'all clean');
})();
