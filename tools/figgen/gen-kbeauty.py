import html
FONT='system-ui, -apple-system, &quot;Noto Sans KR&quot;, &quot;Noto Sans JP&quot;, &quot;Noto Sans TC&quot;, sans-serif'
INK,RED,PAPER,MUTED,RULE,WHITE,SOFT='#16151a','#b8392f','#f4f0e6','#5f5b55','#c9c1b2','#ffffff','#e9e2d3'
W=400
def e(s): return html.escape(s,quote=False)
def text(x,y,lines,size=16,fill=INK,bold=False,anchor='start',lh=None):
    lh=lh or round(size*1.4)
    if isinstance(lines,str): lines=[lines]
    fw='bold' if bold else 'normal'
    if len(lines)==1:
        return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{fw}" text-anchor="{anchor}">{e(lines[0])}</text>'
    ts=''.join(f'<tspan x="{x}" dy="{0 if i==0 else lh}">{e(l)}</tspan>' for i,l in enumerate(lines))
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{fw}" text-anchor="{anchor}">{ts}</text>'
def svg(title,h,body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" role="img" aria-label="{e(title)}" font-family="{FONT}">\n'
            f'<title>{e(title)}</title>\n<rect width="{W}" height="{h}" fill="{PAPER}"/>\n'+'\n'.join(body)+'\n</svg>\n')
def num(cx,cy,n):
    return f'<circle cx="{cx}" cy="{cy}" r="13" fill="{RED}"/>'+text(cx,cy+6,str(n),16,WHITE,True,'middle')

L={
'en':dict(
 f1t='How to read a Korean cosmetics label (example, no real brand)', f1h='Back of the box (example)',
 f1n=[['"기능성화장품" (functional cosmetic):','words or the official symbol'],
      ['Function reviewed by or reported','to MFDS (here: UV protection)'],
      ['SPF and PA: see the sunscreen','section'],
      ['Full ingredients. Listed fragrance','allergens are named one by one'],
      ['100 mL or less fits the cabin','liquids bag']],
 f2t='Choose by what you want the product to do', f2q=['What do you want it to do?'],
 f2=[(['Block sun'],['Check: SPF + PA on the box,','plus "기능성화장품"'],False),
     (['Brighten or smooth wrinkles'],['Check: "기능성화장품" and an','efficacy line naming that function'],False),
     (['Fragrance bothers your skin'],['Check: ingredients for "향료"','and allergen names'],False),
     (['Ad says "cell regeneration",','"anti-inflammatory", "Botox"'],['Skip it. A cosmetic is','not a medicine'],True)],
 f2note=['Skin condition or prescription?','Ask a doctor or pharmacist first.'],
 f3t='Reading SPF and PA on Korean sunscreen', spf='SPF = UVB', spfn=['Whole numbers.','50 or higher is written "50+".'],
 pa='PA = UVA', pan='More + = higher UVA grade', g='MFDS guide: match it to your day',
 rows=[(['Indoors, short walks'],'SPF15 / PA+ or more'),(['Hiking, beach, long hours'],'SPF50+ / PA+++ or PA++++')],
 f3note=['Also check "기능성화장품" on the box.']),
'ko':dict(
 f1t='한국 화장품 라벨 읽는 법(예시, 실제 브랜드 아님)', f1h='상자 뒷면(예시)',
 f1n=[["'기능성화장품' 글자 또는 도안"],
      ['식약처 심사를 받거나 보고한 기능','(여기선 자외선 차단)'],
      ['SPF·PA: 선크림 부분 참고'],
      ['전성분. 목록에 있는 향료 알레르기','유발성분은 이름이 따로 적혀요'],
      ['100mL 이하면 기내 액체 봉투에 OK']],
 f2t='기능별로 고르기', f2q=['이 제품에 무엇을 기대하나요?'],
 f2=[(['햇빛 차단'],["확인: 상자의 SPF·PA와","'기능성화장품' 표시"],False),
     (['미백·주름 개선'],["확인: '기능성화장품' 표시와","그 기능이 적힌 효능 문구"],False),
     (['향료에 피부가 예민해요'],["확인: 전성분의 '향료'와","알레르기 유발성분 이름"],False),
     (["'세포재생' '항염' '바르는 보톡스'",'광고'],['거르세요. 화장품은','의약품이 아니에요'],True)],
 f2note=['피부 질환이 있거나 처방약을 쓰면','의사·약사에게 먼저 물어보세요.'],
 f3t='한국 선크림의 SPF·PA 읽는 법', spf='SPF = 자외선B', spfn=['정수로 표시.',"50 이상은 '50+'."],
 pa='PA = 자외선A', pan='+가 많을수록 등급이 높아요', g='식약처 안내: 하루 일정에 맞춰 고르기',
 rows=[(['실내, 짧은 산책'],'SPF15 / PA+ 이상'),(['등산·해수욕, 오랜 야외'],'SPF50+ / PA+++ 또는 PA++++')],
 f3note=["상자의 '기능성화장품' 표시도 확인하세요."]),
'ja':dict(
 f1t='韓国コスメのラベルの読み方(例。実在ブランドではありません)', f1h='箱の裏面(例)',
 f1n=[['「기능성화장품」(機能性化粧品)の','文字か図案'],
      ['食薬処の審査・報告を経た機能','(ここでは紫外線カット)'],
      ['SPF・PA:日焼け止めの項を参照'],
      ['全成分。リストにある香料アレルゲン','は成分名で表示'],
      ['100mL以下なら機内の液体用袋に']],
 f2t='目的別の選び方', f2q=['その製品に何を求めますか?'],
 f2=[(['日焼けを防ぐ'],['確認:箱のSPF・PAと','「기능성화장품」の表示'],False),
     (['美白・シワ改善'],['確認:「기능성화장품」と、','その機能を書いた効能表示'],False),
     (['香料で肌が荒れやすい'],['確認:全成分の「향료(香料)」と','アレルゲン成分名'],False),
     (['「細胞再生」「抗炎症」','「塗るボトックス」の広告'],['見送る。化粧品は','医薬品ではない'],True)],
 f2note=['肌の病気がある、処方薬を使っている','場合は、先に医師・薬剤師へ。'],
 f3t='韓国の日焼け止めのSPF・PAの読み方', spf='SPF = 紫外線B波', spfn=['整数で表示。','50以上は「50+」。'],
 pa='PA = 紫外線A波', pan='+が多いほどA波の防止等級が高い', g='食薬処の案内:その日の過ごし方で選ぶ',
 rows=[(['室内・短い散歩'],'SPF15 / PA+ 以上'),(['登山・海水浴・長時間'],'SPF50+ / PA+++ か PA++++')],
 f3note=['箱の「기능성화장품」表示もあわせて確認。']),
'zh-tw':dict(
 f1t='韓國保養品標籤怎麼看(範例,非真實品牌)', f1h='盒子背面(範例)',
 f1n=[['「기능성화장품」(機能性化妝品)','文字或圖案'],
      ['經食藥處審查或報告的功效','(此例:防曬)'],
      ['SPF・PA:看防曬那一節'],
      ['全成分。清單內的香料致敏成分','會逐一寫出名稱'],
      ['100mL 以下可放進登機液體袋']],
 f2t='依需求挑選', f2q=['你希望這個產品做到什麼?'],
 f2=[(['防曬'],['確認:盒上的 SPF・PA,','加上「기능성화장품」'],False),
     (['美白、改善皺紋'],['確認:「기능성화장품」加上','寫明該功效的效能說明'],False),
     (['對香料容易敏感'],['確認:全成分的「향료(香料)」','和致敏成分名稱'],False),
     (['廣告寫「細胞再生」「抗發炎」','「塗抹式肉毒」'],['跳過。化妝品','不是藥品'],True)],
 f2note=['有皮膚疾病或在用處方藥?','先問醫師或藥師。'],
 f3t='韓國防曬的 SPF・PA 怎麼看', spf='SPF = UVB', spfn=['以整數標示。','50 以上寫成「50+」。'],
 pa='PA = UVA', pan='+ 越多,UVA 防護等級越高', g='韓國食藥處建議:依當天行程選',
 rows=[(['室內、短時間散步'],'SPF15 / PA+ 以上'),(['登山、海邊、長時間戶外'],'SPF50+ / PA+++ 或 PA++++')],
 f3note=['也要確認盒上有「기능성화장품」標示。']),
}

def fig1(d):
    b=[text(20,32,d['f1h'],16,MUTED,True)]
    y0=46; b.append(f'<rect x="20" y="{y0}" width="360" height="370" rx="10" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>')
    b.append(text(40,86,'수분 선크림',22,INK,True)); b.append(text(40,110,'(예시 제품)',16,MUTED))
    b.append(f'<rect x="40" y="126" width="130" height="36" rx="4" fill="{WHITE}" stroke="{RED}" stroke-width="2"/>'+text(105,150,'기능성화장품',17,RED,True,'middle')); b.append(num(350,144,1))
    b.append(text(40,196,'효능·효과: 자외선 차단',17)); b.append(num(350,190,2))
    b.append(f'<rect x="40" y="214" width="250" height="48" rx="6" fill="{SOFT}"/>'+text(165,246,'SPF50+  PA++++',22,INK,True,'middle')); b.append(num(350,238,3))
    b.append(text(40,292,'전성분:',16,INK,True)); b.append(text(40,316,['정제수, 글리세린, …,','향료, 시트로넬올, 리모넨'],16,MUTED,lh=22)); b.append(num(350,310,4))
    b.append(f'<line x1="40" y1="356" x2="360" y2="356" stroke="{RULE}"/>'); b.append(text(40,392,'용량: 50mL',17,INK,True)); b.append(num(350,386,5))
    y=448
    for i,lines in enumerate(d['f1n'],1):
        b.append(num(33,y-6,i)); b.append(text(56,y,lines,16,INK,lh=22)); y+=22*len(lines)+16
    return svg(d['f1t'],y-4,b)

def fig2(d):
    b=[f'<rect x="20" y="16" width="360" height="44" rx="22" fill="{INK}"/>'+text(200,44,d['f2q'][0],17,WHITE,True,'middle')]
    y=76
    for goal,check,warn in d['f2']:
        gh=16+22*len(goal); ch=16+22*len(check)
        b.append(f'<rect x="20" y="{y}" width="360" height="{gh}" rx="8" fill="{SOFT}"/>'+text(36,y+29,goal,17 if True else 16,INK,True,lh=22))
        ay=y+gh; col=RED if warn else INK
        b.append(f'<line x1="200" y1="{ay}" x2="200" y2="{ay+12}" stroke="{col}" stroke-width="2"/><polygon points="193,{ay+10} 207,{ay+10} 200,{ay+20}" fill="{col}"/>')
        cy=ay+22
        b.append(f'<rect x="20" y="{cy}" width="360" height="{ch}" rx="8" fill="{WHITE}" stroke="{RED if warn else RULE}" stroke-width="2"/>'+text(36,cy+28,check,16,RED if warn else INK,warn,lh=22))
        y=cy+ch+20
    b.append(text(200,y+12,d['f2note'],16,MUTED,False,'middle',lh=22))
    return svg(d['f2t'],y+12+22*len(d['f2note']),b)

def fig3(d):
    b=[f'<rect x="20" y="16" width="360" height="160" rx="10" fill="{WHITE}" stroke="{RULE}" stroke-width="2"/>',
       text(40,50,d['spf'],20,INK,True),
       f'<rect x="40" y="64" width="150" height="44" rx="6" fill="{SOFT}"/>'+text(115,95,'SPF50+',24,INK,True,'middle'),
       text(40,134,d['spfn'],16,INK,lh=22)]
    b.append(f'<rect x="20" y="192" width="360" height="200" rx="10" fill="{WHITE}" stroke="{RULE}" stroke-width="2"/>'); b.append(text(40,226,d['pa'],20,INK,True))
    for i,(lab,w) in enumerate([('PA+',40),('PA++',85),('PA+++',130),('PA++++',175)]):
        yy=260+i*28; b.append(text(40,yy,lab,16,INK,True)); b.append(f'<rect x="130" y="{yy-14}" width="{w}" height="16" rx="3" fill="{RED if i==3 else MUTED}"/>')
    b.append(text(40,372,d['pan'],16,MUTED))
    y=428; b.append(text(20,y,d['g'],17,INK,True)); y+=14
    for i,(sit,val) in enumerate(d['rows']):
        h=70
        b.append(f'<rect x="20" y="{y}" width="360" height="{h}" rx="6" fill="{SOFT if i==0 else WHITE}" stroke="{RULE}"/>'+text(36,y+28,sit,16,INK)+text(36,y+54,val,17,INK,True))
        y+=h+10
    b.append(text(20,y+18,d['f3note'],16,RED,True))
    return svg(d['f3t'],y+34,b)

import sys
out=sys.argv[1]
for lang,d in L.items():
    for n,f in ((1,fig1),(2,fig2),(3,fig3)):
        open(f'{out}/{lang}/kbeauty-how-to-choose-{n}.svg','w').write(f(d))
print('ok')
