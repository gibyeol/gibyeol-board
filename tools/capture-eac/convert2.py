import json, os
from PIL import Image, ImageDraw, ImageFilter
R='/home/user/gibyeol-board/static/fig'
UP,DOWN,PAD=72,16,36
OPT={1:{'keep_top':True,'noveil':True},5:{'noveil':True},6:{'keep_top':True},8:{'noveil':True},9:{'noveil':True,'crop':False},11:{'crop':False,'keep_top':True},12:{'crop':False,'keep_top':True}}
def edit(lang,n):
    o=OPT.get(n,{})
    im=Image.open(f'raw/{lang}-shot-{n}.png').convert('RGB')
    j=json.load(open(f'raw/{lang}-shot-{n}.json')); c=j['clip']; s=im.width/c['width']
    if not j['rects'] and n=='4b': j['rects']=json.load(open(f'raw/{lang}-shot-4a.json'))['rects']
    j['rects']=[r for r in j['rects'] if r[3]>c['y'] and r[1]<c['y']+c['height']]
    bands=[]
    for l,t,r,b in j['rects']:
        y0=max(0,int((t-c['y'])*s)-UP); y1=min(im.height,int((b-c['y'])*s)+DOWN)
        if y1>0 and y0<im.height: bands.append([y0,y1])
    bands.sort(); merged=[]
    for b in bands:
        if merged and b[0]<=merged[-1][1]+24: merged[-1][1]=max(merged[-1][1],b[1])
        else: merged.append(b)
    soft=im.filter(ImageFilter.GaussianBlur(3)); veil=Image.new('RGB',im.size,(255,255,255))
    soft=Image.blend(soft,veil,0.55)
    mask=Image.new('L',im.size,0); d=ImageDraw.Draw(mask)
    if o.get('keep_top') and merged: merged[0][0]=0
    for y0,y1 in merged: d.rectangle((0,y0,im.width,y1),fill=255)
    out=im if o.get('noveil') else Image.composite(im,soft,mask)
    if merged and o.get('crop',True):  # crop to what matters
        top=max(0,merged[0][0]-PAD); bot=min(im.height,merged[-1][1]+PAD)
        out=out.crop((0,top,im.width,bot))
    return out
import sys
LANGS=sys.argv[1:] or ['en','ko']
OUTN={'jp':'ja','ch':'zh-tw'}
for lang in LANGS:
    os.makedirs(f'{R}/{OUTN.get(lang,lang)}',exist_ok=True)
    shots={n:edit(lang,n) for n in (1,2,5,6,7,8,9,10,11,12)}
    a,b=edit(lang,'4a'),edit(lang,'4b'); gap=44
    m=Image.new('RGB',(a.width,a.height+gap+b.height),'white'); m.paste(a,(0,0)); m.paste(b,(0,a.height+gap))
    d=ImageDraw.Draw(m); y=a.height+gap//2
    for x in range(20,a.width-20,18): d.line((x,y,x+9,y),fill=(150,150,150),width=3)
    shots[4]=m
    for n,im in shots.items():
        if im.width>780: im=im.resize((780,round(im.height*780/im.width)))
        out=f'{R}/{OUTN.get(lang,lang)}/e-arrival-card-shot-{n}.webp'; im.save(out,'WEBP',quality=80,method=6)
        print(lang,n,im.size,os.path.getsize(out)//1024,'KB')
