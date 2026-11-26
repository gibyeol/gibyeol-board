import sys
sys.path.insert(0, '/tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/core-B/tools')
from figlib import *

O = {
 'en': dict(
  t1=['The Olive Young year'], months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  lg1='Olive Young Sale, about 7 days', lg2='Olive Young Day, 25th–27th',
  f1=['Dec 2026 dates: on our deals board', 'once Olive Young announces them'],
  t2=['Tax refund at the till,', 'per receipt'],
  r2=[('Under ₩15,000', ['No refund'], MUTED), ('₩15,000 – ₩1,000,000', ['Tax comes off at the till', 'Show your physical passport'], RED),
      ('Over ₩1,000,000', ['Pay full price, claim at', 'a kiosk or the airport'], INK)],
  f2=['Each receipt counts on its own.', 'Receipts from different stores', 'do not add up.'],
  t3=['Reading a 1+1 shelf tag'], badge='1+1', name='Product name', price='Price',
  n3=['Which item or set does', 'the deal cover? Check here'],
  f3=['1+1: buy one, get one', '2+1: buy two, get one'],
  t4=['A starter basket of three'],
  items=[('Sunscreen', ['You use it daily, so', 'you finish it']), ('Toner pads', ['One container,', 'easy to pack']),
         ('Sheet masks', ['Cheap, flat,', 'one use each'])],
  f4=['Left out: viral items and rankings'],
  t5=['Reorder from home'],
  q5=['Do you live in the US?'],
  y5=['Olive Young US', 'Global stopped US service', 'on 29 May 2026'],
  n5=['Olive Young Global', 'Check delivery to your', 'country at checkout'],
  yes='Yes', no='No'),
 'ko': dict(
  t1=['올리브영의 1년'], months=[f'{i}월' for i in range(1, 13)],
  lg1='올영세일, 약 7일', lg2='올영데이, 매달 25~27일',
  f1=['2026년 12월 날짜는 발표되면', '할인 상황판에 올려요'],
  t2=['계산대 즉시 환급,', '영수증 한 장 기준'],
  r2=[('15,000원 미만', ['환급 없음'], MUTED), ('15,000원 ~ 1,000,000원', ['계산대에서 세금이 바로 빠져요', '여권 실물을 보여 줘요'], RED),
      ('1,000,000원 초과', ['전액 결제 후 키오스크나', '공항에서 환급'], INK)],
  f2=['영수증마다 따로 계산해요.', '다른 매장 영수증은', '합쳐지지 않아요.'],
  t3=['1+1 가격표 읽는 법'], badge='1+1', name='상품명', price='가격',
  n3=['어느 상품·세트에 적용되는지', '여기서 확인해요'],
  f3=['1+1: 하나 사면 하나 더', '2+1: 두 개 사면 하나 더'],
  t4=['처음 장바구니 세 가지'],
  items=[('선크림', ['매일 쓰니까', '끝까지 써요']), ('토너 패드', ['용기 하나라', '챙기기 쉬워요']),
         ('시트 마스크', ['싸고 납작하고', '한 번에 한 장'])],
  f4=['뺀 것: 유행하는 상품과 랭킹'],
  t5=['집에서 다시 사려면'],
  q5=['미국에 사나요?'],
  y5=['올리브영 US', '2026년 5월 29일부터', '글로벌몰은 미국 서비스 중단'],
  n5=['올리브영 글로벌', '결제할 때 내 나라로', '배송되는지 확인'],
  yes='예', no='아니요'),
 'ja': dict(
  t1=['オリーブヤングの1年'], months=[f'{i}月' for i in range(1, 13)],
  lg1='オリーブヤングセール、約7日', lg2='オリーブヤングデー、25〜27日',
  f1=['2026年12月の日程は発表後に', 'セール情報に載せます'],
  t2=['レジでの即時還付、', '1レシートごと'],
  r2=[('15,000ウォン未満', ['還付なし'], MUTED), ('15,000〜1,000,000ウォン', ['レジで税金分が引かれる', 'パスポートの実物を見せる'], RED),
      ('1,000,000ウォン超', ['全額を払い、キオスクか', '空港で還付'], INK)],
  f2=['レシートは1枚ずつ数えます。', '別のお店のレシートは', '合算できません。'],
  t3=['1+1の値札の読み方'], badge='1+1', name='商品名', price='価格',
  n3=['どの商品・セットが対象か', 'ここで確かめる'],
  f3=['1+1:1つ買うともう1つ', '2+1:2つ買うと1つ'],
  t4=['最初のかごに3つ'],
  items=[('日焼け止め', ['毎日使うので', '最後まで使い切れる']), ('トナーパッド', ['容器ひとつで', '持ち帰りやすい']),
         ('シートマスク', ['手頃で薄く、', '1回1枚'])],
  f4=['省いたもの:話題の商品とランキング'],
  t5=['家から買い足すなら'],
  single=['オリーブヤンググローバル', '日本への配送や条件は', '注文時に公式サイトで確認']),
 'zh-tw': dict(
  t1=['Olive Young 的一年'], months=[f'{i}月' for i in range(1, 13)],
  lg1='Olive Young Sale,約7天', lg2='Olive Young Day,每月25–27日',
  f1=['2026年12月的日期公布後', '會更新在優惠看板'],
  t2=['收銀台現場退稅,', '以單張收據計'],
  r2=[('未滿15,000韓元', ['不能退稅'], MUTED), ('15,000〜1,000,000韓元', ['結帳時直接扣稅', '出示護照正本'], RED),
      ('超過1,000,000韓元', ['先付全額,再到退稅機', '或機場辦退稅'], INK)],
  f2=['每張收據分開計算。', '不同門市的收據', '不能合併。'],
  t3=['1+1 價籤怎麼看'], badge='1+1', name='商品名稱', price='價格',
  n3=['適用哪一件、哪一組?', '看這裡確認'],
  f3=['1+1:買一送一', '2+1:買二送一'],
  t4=['第一次的購物籃:三樣'],
  items=[('防曬', ['每天擦,', '一定用得完']), ('化妝棉片', ['一個容器,', '好帶']),
         ('面膜', ['便宜、扁平,', '一次一片'])],
  f4=['沒列的:爆紅商品和排行榜'],
  t5=['回國後要回購'],
  single=['Olive Young Global', '有配送到台灣,', '運費和條件結帳時確認']),
}

DF = {
 'en': dict(
  t1=['From order to pickup'],
  s1=[('Order online', 'Passport number + flight'), ('By the evening before', 'Check your real deadline'),
      ('Departure day: check in', 'Then security, passport control'), ('Pickup counter, 4F', 'Passport, boarding pass, voucher'),
      ('Check items, then sign', 'Liquids stay in the sealed bag')],
  t2=['Incheon pickup counters, 4F'],
  c2=[('T1 East', 'Across from gates 10–11'), ('T1 West', 'Across from gates 43–45'),
      ('T1 Concourse', 'Near gate 119, by shuttle train'), ('T2', 'Next to gate 252, across a bridge')],
  f2=['Your voucher names the counter.', 'Shilla: come 1–2 hours before departure.'],
  t3=['US allowance per person'],
  a3=[('$800', 'Goods', 'Abroad 48 h+, not used in 31 days'), ('1 L', 'Alcohol', 'Age 21+, personal use'),
      ('200 + 100', 'Cigarettes + cigars', 'Age 21+')],
  f3=['Duty-free shop buys count too.'],
  t4=['Duty-free or tax-free?'],
  c4=[('Duty-free shop', ['Only for people leaving Korea', 'Goods handed over after', 'passport control']),
      ('Tax-free shop', ['Normal shops, e.g. Olive Young', 'Take the goods with you now', 'Part of the 10% VAT back'])],
  f4=['One or the other per purchase'],
  t5=['The sealed duty-free bag'], bag='Sealed bag',
  n5=['Keep it sealed until your', 'final destination', 'Changing planes? Do not open it', 'Over 1 L: declare it at home']),
 'ko': dict(
  t1=['주문부터 인도까지'],
  s1=[('인터넷으로 주문', '여권번호 + 항공편'), ('출국 전날 저녁까지', '실제 마감은 사이트에서'),
      ('출국날 체크인', '보안검색, 출국심사'), ('4층 인도장', '여권, 탑승권, 교환권'),
      ('품명·수량 확인 후 서명', '액체류는 밀봉 봉투 그대로')],
  t2=['인천공항 인도장, 4층'],
  c2=[('1터미널 동편', '10~11번 게이트 맞은편'), ('1터미널 서편', '43~45번 게이트 맞은편'),
      ('1터미널 탑승동', '119번 게이트 옆, 셔틀트레인'), ('2터미널', '252번 게이트 옆, 구름다리 건너')],
  f2=['어느 인도장인지는 교환권에 있어요.', '신라: 출발 1~2시간 전까지'],
  t3=['귀국할 때 1인 면세범위'],
  a3=[('800달러', '물품', '1인 기준'), ('2L', '술', '별도, 400달러 이하'),
      ('200개비', '담배(궐련)', '별도'), ('100ml', '향수', '별도')],
  f3=['만 19세 미만은 술·담배 면세 없음'],
  t4=['면세점? 택스리펀드?'],
  c4=[('면세점', ['출국하는 사람에게만 판매', '물건은 출국심사 뒤에', '인도장에서 받아요']),
      ('택스리펀드 매장', ['올리브영 같은 일반 매장', '물건은 바로 들고 가요', '부가세 10% 일부 환급'])],
  f4=['한 번 산 물건엔 둘 중 하나만'],
  t5=['면세 밀봉 봉투'], bag='밀봉 봉투',
  n5=['최종 목적지까지', '뜯지 마세요', '환승한다면 더더욱', '면세범위를 넘으면 신고']),
 'ja': dict(
  t1=['注文から受け取りまで'],
  s1=[('オンラインで注文', 'パスポート番号+便名'), ('出発前日の夜までに', '実際の締め切りはサイトで'),
      ('出国当日、チェックイン', '保安検査、出国審査'), ('4階の引き渡し場', 'パスポート、搭乗券、引換券'),
      ('品名・数量を確かめてサイン', '液体物は密封袋のまま')],
  t2=['仁川空港の引き渡し場(4階)'],
  c2=[('第1ターミナル東側', '10〜11番ゲート向かい'), ('第1ターミナル西側', '43〜45番ゲート向かい'),
      ('第1ターミナル搭乗棟', '119番ゲート付近、シャトル'), ('第2ターミナル', '252番ゲート横、ブリッジの先')],
  f2=['どこで受け取るかは引換券に。', '新羅:出発の1〜2時間前までに'],
  t3=['日本の免税範囲(1人)'],
  a3=[('20万円', 'その他の品物', '海外市価の合計'), ('3本', 'お酒', '1本760ml程度'),
      ('200本', '紙巻たばこ', '20歳以上'), ('2オンス', '香水', '約56ml')],
  f3=['韓国の免税店で買った物も含まれます'],
  t4=['免税店?タックスフリー?'],
  c4=[('免税店', ['韓国を出国する人だけ', '品物は出国審査のあと', '引き渡し場で受け取る']),
      ('タックスフリーのお店', ['オリーブヤングなど普通のお店', '品物はその場で持ち帰る', '付加価値税10%の一部が戻る'])],
  f4=['1回の買い物で使えるのはどちらか一方'],
  t5=['免税の密封袋'], bag='密封袋',
  n5=['最終目的地まで', '開けない', '乗り継ぎがあるならなおさら', '範囲を超えたら申告']),
 'zh-tw': dict(
  t1=['從下單到提貨'],
  s1=[('線上下單', '護照號碼+航班'), ('出發前一天晚上前', '實際截止看網站'),
      ('出境當天報到', '安檢、出境審查'), ('4樓提貨處', '護照、登機證、提貨單'),
      ('核對品名數量再簽名', '液體留在密封袋裡')],
  t2=['仁川機場提貨處(4樓)'],
  c2=[('第1航廈東側', '10〜11號登機門對面'), ('第1航廈西側', '43〜45號登機門對面'),
      ('第1航廈登機長廊', '119號登機門附近,搭接駁列車'), ('第2航廈', '252號登機門旁,走過天橋')],
  f2=['去哪個提貨處,看提貨單。', '新羅:起飛前1〜2小時去領'],
  t3=['回台灣入境免稅(每人)'],
  a3=[('NT$35,000', '其他自用物品', '完稅價格總值'), ('1公升', '酒', '資料不一致,以較嚴計'),
      ('200支', '捲菸', '年滿20歲')],
  f3=['在免稅店買的也算在額度內'],
  t4=['免稅店?退稅商店?'],
  c4=[('免稅店', ['只賣給要出境的人', '過出境審查後', '在提貨處拿到']),
      ('退稅商店', ['Olive Young 等一般商店', '東西當場帶走', '退還部分10%加值稅'])],
  f4=['同一筆購買只能用其中一種'],
  t5=['免稅密封袋'], bag='密封袋',
  n5=['到最終目的地前', '不要拆', '轉機的人特別注意', '超過額度要申報']),
}

for lang, d in O.items():
    # 1 calendar
    f = Fig(d['t1'])
    f.add(R(20, f.y, 26, 16, RED, 'none', 0, 3)); f.add(T(56, f.y + 14, d['lg1'], 16))
    f.y += 26
    f.add(R(20, f.y, 26, 16, SOFT, INK, 1, 3)); f.add(T(56, f.y + 14, d['lg2'], 16))
    f.y += 34
    x0, x1 = 80, 380
    dx = (x1 - x0) / 31
    for i, m in enumerate(d['months']):
        y = f.y + 30 * i
        sale = i in (2, 5, 8, 11)
        f.add(T(20, y + 17, m, 16, '700' if sale else '400', RED if sale else INK))
        f.add(f'<line x1="{x0}" y1="{y + 11}" x2="{x1}" y2="{y + 11}" stroke="{RULE}" stroke-width="2"/>\n')
        if sale:
            f.add(R(x0, y + 2, dx * 7, 18, RED, 'none', 0, 3))
        f.add(R(x0 + dx * 24, y + 3, dx * 3, 16, SOFT, INK, 1, 3))
    f.y += 30 * 12
    f.footer(d['f1'], gap=-2)
    write(lang, 'olive-young-1', f.svg())

    # 2 refund ranges
    f = Fig(d['t2'])
    for head, lines, col in d['r2']:
        h = 44 + 22 * len(lines)
        f.add(R(16, f.y, 368, h, WHITE, col, 2.5 if col == RED else 1.5))
        f.add(R(16, f.y, 10, h, col, 'none', 0, 3))
        f.add(T(40, f.y + 28, head, 17, '700', col if col != MUTED else INK))
        for i, s in enumerate(lines):
            f.add(T(40, f.y + 52 + 22 * i, s, 16, '400', INK if col == RED else MUTED))
        f.y += h + 10
    f.footer(d['f2'], gap=-6)
    write(lang, 'olive-young-2', f.svg())

    # 3 shelf tag
    f = Fig(d['t3'])
    f.add(R(16, f.y, 368, 120, WHITE, INK, 2, 6))
    f.add(R(28, f.y + 14, 64, 40, RED, 'none', 0, 6))
    f.add(T(60, f.y + 42, d['badge'], 20, '700', WHITE, 'middle'))
    f.add(T(108, f.y + 32, d['name'], 16, '700'))
    f.add(R(108, f.y + 42, 180, 12, SOFT, 'none', 0, 3))
    f.add(T(28, f.y + 92, d['price'], 16, '400', MUTED))
    f.add(R(100, f.y + 80, 110, 16, SOFT, 'none', 0, 3))
    f.add(f'<rect x="104" y="{f.y + 8}" width="270" height="56" rx="8" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="5 4"/>\n')
    f.y += 120
    f.add(arrow(240, f.y - 56, f.y + 2, RED)) if False else None
    f.y += 14
    for i, s in enumerate(d['n3']):
        f.add(T(20, f.y + 18 + 22 * i, s, 16, '700', RED))
    f.y += 22 * len(d['n3']) + 4
    f.footer(d['f3'], gap=6)
    write(lang, 'olive-young-3', f.svg())

    # 4 basket
    f = Fig(d['t4'])
    for k, (name, lines) in enumerate(d['items']):
        h = 92
        f.add(R(16, f.y, 368, h, WHITE, RULE, 1.5))
        cx, cy = 52, f.y + h / 2
        if k == 0:
            f.add(R(cx - 12, cy - 30, 24, 52, SOFT, INK, 2, 6) + R(cx - 7, cy + 22, 14, 10, INK, 'none', 0, 2))
        elif k == 1:
            f.add(f'<ellipse cx="{cx}" cy="{cy - 14}" rx="24" ry="7" fill="{SOFT}" stroke="{INK}" stroke-width="2"/>\n'
                  + R(cx - 24, cy - 14, 48, 34, SOFT, INK, 2, 4))
        else:
            f.add(R(cx - 22, cy - 26, 44, 52, SOFT, INK, 2, 3)
                  + f'<line x1="{cx - 14}" y1="{cy - 12}" x2="{cx + 14}" y2="{cy - 12}" stroke="{INK}" stroke-width="2"/>\n')
        f.add(T(96, f.y + 30, f'{k + 1}. {name}', 17, '700', RED))
        for i, s in enumerate(lines):
            f.add(T(96, f.y + 54 + 22 * i, s, 16))
        f.y += h + 10
    f.footer(d['f4'], gap=-6)
    write(lang, 'olive-young-4', f.svg())

    # 5 reorder
    f = Fig(d['t5'])
    if 'single' in d:
        h = 20 + 26 * len(d['single'])
        f.add(R(16, f.y, 368, h, WHITE, RED, 2.5))
        for i, s in enumerate(d['single']):
            f.add(T(32, f.y + 32 + 26 * i, s, 18 if i == 0 else 16, '700' if i == 0 else '400', RED if i == 0 else INK))
        f.y += h
    else:
        h = 52
        f.add(R(16, f.y, 368, h, SOFT, RULE, 1.5)); f.add(T(32, f.y + 33, d['q5'][0], 17, '700'))
        f.y += h
        for k, (lab, lines, col) in enumerate(((d['yes'], d['y5'], INK), (d['no'], d['n5'], RED))):
            f.add(arrow(60, f.y, f.y + 30)); f.add(T(72, f.y + 22, lab, 16, '700', RED if k else MUTED))
            f.y += 30
            bh = 20 + 22 * len(lines)
            f.add(R(16, f.y, 368, bh, WHITE, col, 2))
            for i, s2 in enumerate(lines):
                f.add(T(32, f.y + 28 + 22 * i, s2, 17 if i == 0 else 16, '700' if i == 0 else '400'))
            f.y += bh
            if k == 0:
                f.y += 6
    write(lang, 'olive-young-5', f.svg())

for lang, d in DF.items():
    # 1 flow
    f = Fig(d['t1'])
    for i, (a, b) in enumerate(d['s1']):
        f.add(f'<circle cx="38" cy="{f.y + 24}" r="16" fill="{RED if i == 3 else INK}"/>\n')
        f.add(T(38, f.y + 30, str(i + 1), 16, '700', WHITE, 'middle'))
        f.add(T(66, f.y + 22, a, 17, '700'))
        f.add(T(66, f.y + 45, b, 16, '400', MUTED))
        if i < len(d['s1']) - 1:
            f.add(f'<line x1="38" y1="{f.y + 42}" x2="38" y2="{f.y + 70}" stroke="{RULE}" stroke-width="3"/>\n')
        f.y += 70
    f.y -= 10
    write(lang, 'duty-free-1', f.svg())

    # 2 counters
    f = Fig(d['t2'])
    for i, (a, b) in enumerate(d['c2']):
        f.add(R(16, f.y, 368, 66, WHITE, RULE, 1.5))
        f.add(R(16, f.y, 10, 66, INK if i < 3 else RED, 'none', 0, 3))
        f.add(T(40, f.y + 27, a, 17, '700'))
        f.add(T(40, f.y + 51, b, 16, '400', MUTED))
        f.y += 74
    f.footer(d['f2'], gap=-6)
    write(lang, 'duty-free-2', f.svg())

    # 3 allowance
    f = Fig(d['t3'])
    for big, lab, sub in d['a3']:
        f.add(R(16, f.y, 368, 96, WHITE, RULE, 1.5))
        f.add(T(32, f.y + 36, big, 24, '700', RED))
        f.add(T(32 + 14 * len(big) + 40 if False else 210, f.y + 34, lab, 17, '700'))
        f.add(T(32, f.y + 74, sub, 16, '400', MUTED))
        f.y += 104
    f.footer(d['f3'], gap=-6, fill=INK)
    write(lang, 'duty-free-3', f.svg())

    # 4 duty vs tax
    f = Fig(d['t4'])
    for k, (head, lines) in enumerate(d['c4']):
        h = 44 + 24 * len(lines)
        f.add(R(16, f.y, 368, h, WHITE, RED if k == 0 else INK, 2))
        f.add(T(32, f.y + 30, head, 18, '700', RED if k == 0 else INK))
        for i, s in enumerate(lines):
            f.add(T(32, f.y + 56 + 24 * i, s, 16))
        f.y += h + 12
    f.footer(d['f4'], gap=-10, fill=INK)
    write(lang, 'duty-free-4', f.svg())

    # 5 sealed bag
    f = Fig(d['t5'])
    top = f.y + 6
    f.add(f'<path d="M30,{top + 20} L150,{top + 20} L142,{top + 170} L38,{top + 170} z" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>\n')
    f.add(R(26, top + 8, 128, 16, RED, 'none', 0, 3))
    f.add(R(62, top + 70, 26, 70, SOFT, INK, 1.5, 4) + R(92, top + 90, 26, 50, SOFT, INK, 1.5, 4))
    f.add(T(90, top + 196, d['bag'], 16, '700', RED, 'middle'))
    f.y = top + 206
    for i, s in enumerate(d['n5']):
        f.add(T(20, f.y + 22 * (i + 1), s, 16, '700' if i < 2 else '400', INK))
    f.y += 22 * len(d['n5'])
    write(lang, 'duty-free-5', f.svg())
print('done')
