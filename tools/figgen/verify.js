// usage: node verify.js <srcdir> [pngdir]   renders each SVG at 340px wide and checks text
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const src=process.argv[2], png=process.argv[3]; const WIDTH=340;
(async()=>{const b=await chromium.launch(); const results=[]; let bad=0;
 for(const l of ['en','ko','ja','zh-tw']) for(const f of fs.readdirSync(path.join(src,l)).filter(x=>x.endsWith('.svg')).sort()){
  const svg=fs.readFileSync(path.join(src,l,f),'utf8');
  const p=await b.newPage({viewport:{width:WIDTH,height:900}});
  await p.setContent(`<html><body style="margin:0;background:#fff"><div style="width:${WIDTH}px">${svg.replace('<svg ','<svg style="width:100%;height:auto;display:block" ')}</div></body></html>`);
  await p.evaluate(()=>document.fonts.ready);
  const r=await p.evaluate(()=>{const s=document.querySelector('svg');const vb=s.viewBox.baseVal;
    const scale=s.getBoundingClientRect().width/vb.width; const issues=[]; let minFs=1e9, minRectH=1e9;
    const hasWH=s.hasAttribute('width')||s.hasAttribute('height');
    const rects=[...s.querySelectorAll('rect')].map(r=>({x:+r.getAttribute('x')||0,y:+r.getAttribute('y')||0,w:+r.getAttribute('width'),h:+r.getAttribute('height')})).filter(r=>!(r.w>=vb.width&&r.h>=vb.height));
    const texts=[...s.querySelectorAll('text')]; const boxes=[];
    for(const t of texts){const fsz=parseFloat(t.getAttribute('font-size'))*scale; minFs=Math.min(minFs,fsz);
      const cr=t.getBoundingClientRect(); minRectH=Math.min(minRectH,cr.height);
      const bb=t.getBBox(); const lab=t.textContent.slice(0,40); boxes.push([bb,lab]);
      if(bb.x<0||bb.y<0||bb.x+bb.width>vb.width||bb.y+bb.height>vb.height) issues.push(`VIEWBOX ${lab} [${bb.x.toFixed(0)},${bb.y.toFixed(0)},${bb.width.toFixed(0)}]`);
      const ax=bb.x+bb.width/2, ay=bb.y+bb.height/2;
      const cont=rects.filter(r=>ax>=r.x&&ax<=r.x+r.w&&ay>=r.y&&ay<=r.y+r.h).sort((a,b)=>a.w*a.h-b.w*b.h)[0];
      if(cont){const tol=1; if(bb.x<cont.x-tol||bb.x+bb.width>cont.x+cont.w+tol||bb.y<cont.y-tol||bb.y+bb.height>cont.y+cont.h+tol) issues.push(`BOX ${lab} text[${bb.x.toFixed(0)}-${(bb.x+bb.width).toFixed(0)},${bb.y.toFixed(0)}-${(bb.y+bb.height).toFixed(0)}] rect[${cont.x}-${cont.x+cont.w},${cont.y}-${cont.y+cont.h}]`);}
    }
    for(let i=0;i<boxes.length;i++)for(let j=i+1;j<boxes.length;j++){const [a,la]=boxes[i],[c,lc]=boxes[j];
      const ox=Math.min(a.x+a.width,c.x+c.width)-Math.max(a.x,c.x), oy=Math.min(a.y+a.height,c.y+c.height)-Math.max(a.y,c.y);
      if(ox>1&&oy>3) issues.push(`OVERLAP "${la}" / "${lc}"`);}
    return {vbw:vb.width,vbh:vb.height,scale,minFs,minRectH,issues,hasWH,n:texts.length};});
  if(png){fs.mkdirSync(png,{recursive:true});await p.locator('div').first().screenshot({path:path.join(png,`${l}-${f.replace('.svg','')}.png`)});}
  await p.close();
  const ok=r.vbw===400&&r.minFs>=13&&!r.issues.length&&!r.hasWH; if(!ok)bad++;
  results.push(`${ok?'OK ':'BAD'} ${l}/${f} vb=${r.vbw}x${r.vbh} texts=${r.n} minFont=${r.minFs.toFixed(2)}px minGlyphBoxH=${r.minRectH.toFixed(1)}px${r.hasWH?' HAS_WH':''}${r.issues.length?'\n    '+r.issues.join('\n    '):''}`);
 }
 console.log(results.join('\n')); console.log('bad files:',bad); await b.close();})();
