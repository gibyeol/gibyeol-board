# New figures for seoul-subway (1 fixed, 4-8 new) and seoul-bus (4-5 new). Usage: python3 gen_transit.py <outdir>
import importlib.util, sys, os
spec = importlib.util.spec_from_file_location('g4', '/home/user/gibyeol-board/tools/figgen/gen-4pages.py')
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
from importlib import reload
T, R, block, wrap, lh, num, arrow, title_block, write = g.T, g.R, g.block, g.wrap, g.lh, g.num, g.arrow, g.title_block, g.write
INK, RED, PAPER, MUTED, RULE, WHITE, SOFT, W, PAD = g.INK, g.RED, g.PAPER, g.MUTED, g.RULE, g.WHITE, g.SOFT, g.W, g.PAD
PINK = '#e7a3b4'
LANGS = ['en', 'ko', 'ja', 'zh-tw']

def items_list(y, items, colors=None):
    """numbered rows under a drawing. items: list of str (first line bold if contains '\t': head\tbody)."""
    body = ''
    TX = 62; TWID = W - PAD - 8 - TX
    for i, it in enumerate(items):
        head, _, rest = it.partition('\t')
        hl = wrap(head, 17, TWID, True)
        rl = wrap(rest, 16, TWID) if rest else []
        th = len(hl) * lh(17) + len(rl) * lh(16)
        h = max(th + 20, 50)
        body += R(PAD, y, W - 2 * PAD, h, WHITE, RULE, 2)
        c = colors[i] if colors and colors[i] else RED
        body += num(38, round(y + h / 2), i + 1, c)
        ty = y + (h - th) / 2
        s, hh = block(TX, ty, hl, 17, INK, True); body += s
        s, _ = block(TX, ty + hh, rl, 16, MUTED); body += s
        y += h + 8
    return body, y

def foot(y, text, red=False):
    lines = wrap(text, 16 if not red else 17, W - 2 * PAD - 28, red)
    size = 17 if red else 16
    h = len(lines) * lh(size) + 22
    body = R(PAD, y, W - 2 * PAD, h, WHITE if red else SOFT, RED if red else None, 2)
    s, _ = block(W / 2, y + 11, lines, size, RED if red else INK, red, 'middle')
    return body + s, y + h

# ---------------------------------------------------------------- subway-4: the gate
SUB4 = {
 'en': dict(title='At the gate', bal='Balance ₩ …', items=['Touch your card to the reader', 'The reader shows your balance', 'Walk through'], foot='At your stop, tap out the same way'),
 'ko': dict(title='개찰구에서', bal='잔액 … 원', items=['카드를 단말기에 대요', '단말기에 잔액이 떠요', '그대로 지나가요'], foot='내릴 역에서도 같은 방법으로 찍고 나와요'),
 'ja': dict(title='改札で', bal='残高 … ウォン', items=['カードを読み取り機にかざす', '読み取り機に残高が出る', 'そのまま通る'], foot='降りる駅でも同じようにタッチして出ます'),
 'zh-tw': dict(title='在閘門', bal='餘額 … 韓元', items=['把卡靠上感應器', '感應器顯示餘額', '直接走過去'], foot='到站時用同樣方式嗶卡出站'),
}
def b_sub4(lang, d):
    body, y = title_block(d['title'])
    top = y; H = 210
    body += R(PAD, top, W - 2 * PAD, H, WHITE, RULE, 2)
    base = top + 190
    # cabinets
    body += R(80, top + 84, 66, base - top - 84, INK, None, 6)
    body += R(254, top + 84, 66, base - top - 84, INK, None, 6)
    # flaps
    body += R(146, top + 120, 40, 14, MUTED, None, 4) + R(214, top + 120, 40, 14, MUTED, None, 4)
    # reader on the left cabinet + card
    body += R(92, top + 62, 42, 26, RED, None, 5)
    body += f'<rect x="96" y="{top+22}" width="36" height="24" rx="4" fill="{WHITE}" stroke="{INK}" stroke-width="2.5" transform="rotate(-12 114 {top+34})"/>\n'
    body += arrow(114, top + 48, 114, top + 60)
    # balance bubble
    bx, bw = 168, 196
    body += R(bx, top + 30, bw, 40, PAPER, RED, 2, 8)
    body += T(bx + bw / 2 + 12, top + 57, d['bal'], 17, INK, True, 'middle')
    body += f'<line x1="134" y1="{top+72}" x2="{bx}" y2="{top+56}" stroke="{RED}" stroke-width="2"/>\n'
    # walk-through arrow
    body += arrow(200, base - 6, 200, top + 146)
    body += num(46, top + 40, 1) + num(bx + 20, top + 50, 2) + num(232, base - 26, 3)
    y = top + H + 12
    s, y = items_list(y, d['items']); body += s
    s, y = foot(y + 4, d['foot']); body += s
    write(lang, 'seoul-subway-4', d['title'], body, y + 16)

# ---------------------------------------------------------------- subway-5: top-up machine
SUB5 = {
 'en': dict(title='The top-up machine', items=['Put your card on the machine', 'Choose the amount', 'Pay in cash (notes)', 'Check the new balance'], foot='T-money top-ups: cash only'),
 'ko': dict(title='충전기', items=['카드를 충전기에 올려요', '금액을 골라요', '현금(지폐)으로 내요', '새 잔액을 확인해요'], foot='티머니 충전은 현금만 돼요'),
 'ja': dict(title='チャージ機', items=['カードを機械に置く', '金額を選ぶ', '現金(紙幣)で払う', '新しい残高を確認'], foot='T-moneyのチャージは現金のみ'),
 'zh-tw': dict(title='儲值機', items=['把卡放在機器上', '選金額', '投現金(紙鈔)', '確認新餘額'], foot='T-money儲值只收現金'),
}
def b_sub5(lang, d):
    body, y = title_block(d['title'])
    top = y; H = 200
    body += R(PAD, top, W - 2 * PAD, H, WHITE, RULE, 2)
    mx, mw = 140, 120
    body += R(mx, top + 14, mw, H - 28, SOFT, INK, 2.5, 10)
    body += R(mx + 14, top + 30, mw - 28, 66, WHITE, INK, 2, 6)           # screen
    body += R(mx + 14, top + 114, 40, 30, RED, None, 5)                   # card spot
    body += R(mx + 66, top + 124, 40, 8, INK, None, 3)                    # note slot
    body += R(mx + 70, top + 140, 32, 18, WHITE, MUTED, 2, 3)             # banknote
    body += num(108, top + 129, 1) + num(108, top + 63, 2) + num(292, top + 128, 3) + num(292, top + 63, 4)
    body += f'<line x1="123" y1="{top+129}" x2="{mx+14}" y2="{top+129}" stroke="{RED}" stroke-width="2"/>'
    body += f'<line x1="123" y1="{top+63}" x2="{mx+14}" y2="{top+63}" stroke="{RED}" stroke-width="2"/>'
    body += f'<line x1="277" y1="{top+128}" x2="{mx+106}" y2="{top+128}" stroke="{RED}" stroke-width="2"/>'
    body += f'<line x1="277" y1="{top+63}" x2="{mx+mw-14}" y2="{top+63}" stroke="{RED}" stroke-width="2"/>\n'
    y = top + H + 12
    s, y = items_list(y, d['items']); body += s
    s, y = foot(y + 4, d['foot'], True); body += s
    write(lang, 'seoul-subway-5', d['title'], body, y + 16)

# ---------------------------------------------------------------- subway-6: signs
SUB6 = {
 'en': dict(title='Three signs to read', dir='→ (end station)', exit='Exit 8',
            items=['Line number\tFind your line by number', 'Direction\tThe end station you are heading towards', 'Exit number\tFrom your map app, e.g. Myeongdong Station, Exit 8'],
            foot='Drawn simply: real signs look different'),
 'ko': dict(title='볼 표지판 세 가지', dir='→ (종착역)', exit='8번 출구',
            items=['노선 번호\t번호로 노선을 찾아요', '방향\t가는 쪽의 종착역', '출구 번호\t지도 앱에서 확인, 예: 명동역 8번 출구'],
            foot='단순하게 그린 그림이에요. 실제 표지판과 모양이 달라요'),
 'ja': dict(title='見る標識は3つ', dir='→ (終着駅)', exit='8番出口',
            items=['路線番号\t番号で路線を探す', '方向\t行きたい方向の終着駅', '出口番号\t地図アプリで確認。例:明洞駅8番出口'],
            foot='簡略化した図です。実際の標識とは見た目が違います'),
 'zh-tw': dict(title='要看的三種標示', dir='→ (終點站)', exit='8號出口',
            items=['路線號碼\t用號碼找路線', '方向\t你要去那一頭的終點站', '出口號碼\t用地圖App查,例:明洞站8號出口'],
            foot='簡化示意圖,實際標示外觀不同'),
}
def b_sub6(lang, d):
    body, y = title_block(d['title'])
    top = y
    body += R(PAD, top, W - 2 * PAD, 60, INK, None, 8)
    body += f'<circle cx="62" cy="{top+30}" r="20" fill="{WHITE}"/>\n' + T(62, top + 38, '4', 22, INK, True, 'middle')
    body += T(100, top + 37, d['dir'], 19, WHITE, True)
    body += num(62, top + 84, 1) + num(200, top + 84, 2)
    top2 = top + 112
    body += R(PAD, top2, W - 2 * PAD, 60, SOFT, INK, 2.5, 8)
    body += T(W / 2, top2 + 39, d['exit'] + '  ↑', 22, INK, True, 'middle')
    body += num(W / 2, top2 + 84, 3)
    y = top2 + 112
    s, y = items_list(y, d['items']); body += s
    s, y = foot(y + 4, d['foot']); body += s
    write(lang, 'seoul-subway-6', d['title'], body, y + 16)

# ---------------------------------------------------------------- subway-7: seats
SUB7 = {
 'en': dict(title='Seats to leave free', end='Car end', items=['Priority seats\tBoth ends of the car: older, disabled and injured passengers, pregnant women', 'Pink seats\nTwo per car\tFor pregnant women. Leave them empty.'], foot='Early pregnancy doesn\'t show: some women wear a pink badge'),
 'ko': dict(title='비워 둘 자리', end='칸 끝', items=['노약자석\t칸 양 끝: 어르신, 장애인, 다친 사람, 임산부', '분홍색 좌석\n한 칸에 두 자리\t임산부 배려석. 비워 둬요.'], foot='초기 임산부는 티가 안 나서 분홍색 배지를 달기도 해요'),
 'ja': dict(title='空けておく席', end='車両の端', items=['優先席\t車両の両端:高齢の方、体の不自由な方、けがをした方、妊婦さん', 'ピンクの座席\n1両に2席\t妊婦さんのための席。空けておきます。'], foot='妊娠初期は外見でわからないため、ピンクのバッジをつける方もいます'),
 'zh-tw': dict(title='請空著的座位', end='車廂端', items=['博愛座\t車廂兩端:長者、身障者、受傷的人、孕婦', '粉紅色座位\n每節2個\t孕婦優先座,請空著。'], foot='懷孕初期看不出來,有些孕婦會別粉紅色徽章'),
}
def b_sub7(lang, d):
    body, y = title_block(d['title'])
    top = y; H = 120
    body += R(PAD, top, W - 2 * PAD, H, WHITE, INK, 2.5, 18)
    # middle seats (neutral)
    for x in range(102, 300, 28):
        body += R(x, top + 10, 24, 22, SOFT, RULE, 1.5, 4) + R(x, top + H - 32, 24, 22, SOFT, RULE, 1.5, 4)
    # end blocks
    for x0 in (28, 302):
        body += R(x0, top + 10, 70, 22, WHITE, RED, 2.5, 4) + R(x0, top + H - 32, 70, 22, WHITE, RED, 2.5, 4)
    body += num(63, top + H / 2, 1) + num(337, top + H / 2, 1)
    y = top + H + 12
    s, y = items_list(y, d['items'], [RED, PINK]); body += s
    s, y = foot(y + 4, d['foot']); body += s
    write(lang, 'seoul-subway-7', d['title'], body, y + 16)

# ---------------------------------------------------------------- subway-8: AREX
SUB8 = {
 'en': dict(title='Same line, two trains', a='All-stop', e='Express', st=['Seoul Station', 'Gongdeok', 'Hongik Univ.', '…', 'Incheon Airport'],
            ab='All-stop\tEvery station · tap your card · transfers apply', eb='Express\tNon-stop · reserved seat · separate ticket'),
 'ko': dict(title='같은 노선, 다른 열차', a='일반열차', e='직통열차', st=['서울역', '공덕', '홍대입구', '…', '인천공항'],
            ab='일반열차\t모든 역 정차 · 교통카드 태그 · 환승 할인', eb='직통열차\t무정차 · 지정 좌석 · 승차권 따로 구매'),
 'ja': dict(title='同じ路線に2種類', a='一般列車', e='直通列車', st=['ソウル駅', '孔徳', '弘大入口', '…', '仁川空港'],
            ab='一般列車\t全駅に停車・交通カードでタッチ・乗り換え割引あり', eb='直通列車\tノンストップ・座席指定・乗車券を別に購入'),
 'zh-tw': dict(title='同一條路線兩種車', a='普通車', e='直達車', st=['首爾站', '孔德', '弘大入口', '…', '仁川機場'],
            ab='普通車\t每站都停・嗶交通卡・可享轉乘優惠', eb='直達車\t中途不停・對號座・另外買票'),
}
def b_sub8(lang, d):
    body, y = title_block(d['title'])
    top = y; XA, XE = 252, 340; RH = 42
    body += T(XA, top + 18, d['a'], 17, INK, True, 'middle') + T(XE, top + 18, d['e'], 17, RED, True, 'middle')
    y0 = top + 46
    yl = y0 + RH * (len(d['st']) - 1)
    body += f'<line x1="{XA}" y1="{y0}" x2="{XA}" y2="{yl}" stroke="{INK}" stroke-width="5"/>\n'
    body += f'<line x1="{XE}" y1="{y0}" x2="{XE}" y2="{yl}" stroke="{RED}" stroke-width="5"/>\n'
    for i, s in enumerate(d['st']):
        cy = y0 + RH * i
        if s == '…':
            body += T(PAD + 8, cy + 6, s, 17, MUTED)
            continue
        body += T(PAD + 8, cy + 6, s, 17, INK, True)
        body += f'<circle cx="{XA}" cy="{cy}" r="9" fill="{INK}"/>\n'
        end = i in (0, len(d['st']) - 1)
        body += f'<circle cx="{XE}" cy="{cy}" r="9" fill="{RED if end else WHITE}" stroke="{RED}" stroke-width="2.5"/>\n'
    y = yl + 24
    s, y = items_list(y, [d['ab'], d['eb']], [INK, RED]); body += s
    write(lang, 'seoul-subway-8', d['title'], body, y + 10)

# ---------------------------------------------------------------- bus-4: the bus, side view
BUS4 = {
 'en': dict(title='One bus ride', items=['Route number on the front', 'Front door: get on and tap the reader', 'Stop next? Press the bell by the window', 'Rear door: tap the reader, then get off'], foot='Skip the tap at the rear door and the transfer chain breaks'),
 'ko': dict(title='버스 한 번 타기', items=['버스 앞의 노선 번호', '앞문: 타면서 단말기에 태그', '다음이 내릴 곳? 창가 하차벨', '뒷문: 단말기에 태그하고 내리기'], foot='뒷문에서 안 찍으면 환승이 거기서 끊겨요'),
 'ja': dict(title='バスに1回乗る', items=['正面に路線番号', '前のドア:乗って読み取り機にタッチ', '次で降りる?窓際の降車ボタン', '後ろのドア:読み取り機にタッチして降りる'], foot='後ろのドアでタッチしないと、そこで乗り換えが切れます'),
 'zh-tw': dict(title='搭一次公車', items=['車頭的路線號碼', '前門:上車刷卡', '下一站要下?按窗邊下車鈴', '後門:刷卡後下車'], foot='後門沒刷卡,轉乘就在這裡斷掉'),
}
def b_bus4(lang, d):
    body, y = title_block(d['title'])
    top = y; H = 210
    body += R(PAD, top, W - 2 * PAD, H, WHITE, RULE, 2)
    bt = top + 48
    body += f'<path d="M30,{bt} H350 Q372,{bt} 372,{bt+22} V{bt+122} H30 Z" fill="{SOFT}" stroke="{INK}" stroke-width="2.5"/>\n'
    body += R(312, bt + 8, 52, 20, INK, None, 4)                      # route display
    for xx in (322, 334, 346):
        body += R(xx, bt + 15, 8, 6, WHITE, None, 1)
    # windows (skip doors)
    for x0, x1 in ((40, 160), (214, 304)):
        x = x0
        while x + 30 <= x1:
            body += R(x, bt + 36, 32, 34, WHITE, MUTED, 1.5, 4); x += 38
    body += R(166, bt + 30, 40, 92, WHITE, INK, 2.5, 3)              # rear door
    body += R(318, bt + 34, 42, 88, WHITE, INK, 2.5, 3)              # front door
    body += R(210, bt + 76, 9, 16, RED, None, 2) + R(305, bt + 76, 9, 16, RED, None, 2)   # readers
    body += f'<circle cx="112" cy="{bt+82}" r="7" fill="{RED}"/>\n'   # bell
    body += f'<circle cx="92" cy="{bt+124}" r="15" fill="{INK}"/><circle cx="270" cy="{bt+124}" r="15" fill="{INK}"/>\n'
    body += num(338, top + 24, 1) + num(339, bt + 150, 2) + num(112, top + 24, 3) + num(186, bt + 150, 4)
    body += f'<line x1="112" y1="{top+39}" x2="112" y2="{bt+75}" stroke="{RED}" stroke-width="2"/>\n'
    y = top + H + 12
    s, y = items_list(y, d['items']); body += s
    s, y = foot(y + 4, d['foot'], True); body += s
    write(lang, 'seoul-bus-4', d['title'], body, y + 16)

# ---------------------------------------------------------------- bus-5: two kinds of N
BUS5 = {
 'en': dict(title='Two kinds of N bus', a_h='City night bus', a_n='N + route number', a_l=['14 routes', '11 p.m.–6 a.m.', '₩2,500 by card: just tap'],
            b_h='Airport late-night bus', b_n='N6000 · N6002 · N6701 · N6703', b_l=['₩17,000–18,000', 'Buy a ticket'], foot='Same letter, about seven times the fare'),
 'ko': dict(title='N버스 두 종류', a_h='시내 심야버스', a_n='N + 노선 번호', a_l=['14개 노선', '밤 11시~새벽 6시', '교통카드 2,500원, 태그만'],
            b_h='심야 공항버스', b_n='N6000 · N6002 · N6701 · N6703', b_l=['17,000~18,000원', '표를 사서 타요'], foot='같은 N이지만 요금은 약 7배 차이'),
 'ja': dict(title='2種類のNバス', a_h='市内の深夜バス', a_n='N+路線番号', a_l=['14路線', '23時〜翌6時', '交通カードで2,500ウォン、タッチだけ'],
            b_h='深夜の空港バス', b_n='N6000 · N6002 · N6701 · N6703', b_l=['17,000〜18,000ウォン', '乗車券を買って乗る'], foot='同じNでも運賃は約7倍違います'),
 'zh-tw': dict(title='兩種N字頭公車', a_h='市區深夜公車', a_n='N+路線號碼', a_l=['14條路線', '晚上11點~早上6點', '交通卡2,500韓元,嗶卡就好'],
            b_h='深夜機場巴士', b_n='N6000 · N6002 · N6701 · N6703', b_l=['17,000~18,000韓元', '要買票搭乘'], foot='同樣是N,票價差約7倍'),
}
def card(y, head, numtxt, lines, stroke):
    TW_ = W - 2 * PAD - 32
    hl = wrap(head, 17, TW_, True); nl = wrap(numtxt, 19, TW_, True)
    ll = []
    for t in lines:
        ll += wrap(t, 17, TW_)
    h = len(hl) * lh(17) + len(nl) * lh(19) + len(ll) * lh(17) + 34
    body = R(PAD, y, W - 2 * PAD, h, WHITE, stroke, 3)
    ty = y + 14
    s, hh = block(PAD + 16, ty, nl, 19, stroke, True); body += s; ty += hh
    s, hh = block(PAD + 16, ty, hl, 17, INK, True); body += s; ty += hh + 6
    s, hh = block(PAD + 16, ty, ll, 17, INK); body += s
    return body, y + h

def b_bus5(lang, d):
    body, y = title_block(d['title'])
    s, y = card(y, d['a_h'], d['a_n'], d['a_l'], INK); body += s
    body += T(W / 2, y + 26, '≠', 22, RED, True, 'middle'); y += 38
    s, y = card(y, d['b_h'], d['b_n'], d['b_l'], RED); body += s
    s, y = foot(y + 12, d['foot']); body += s
    write(lang, 'seoul-bus-5', d['title'], body, y + 16)

# ---------------------------------------------------------------- subway-1 wording fix (overseas cards)
NB = {'en': 'Single ticket at a new machine (overseas card):', 'ko': '새 무인기(해외 신용·체크카드)에서 1회용 승차권:',
      'ja': '新しい券売機(海外発行カード)で1回用乗車券:', 'zh-tw': '在新售票機(海外發行卡)買單程票:'}

if __name__ == '__main__':
    for lang in LANGS:
        b_sub4(lang, SUB4[lang]); b_sub5(lang, SUB5[lang]); b_sub6(lang, SUB6[lang]); b_sub7(lang, SUB7[lang]); b_sub8(lang, SUB8[lang])
        b_bus4(lang, BUS4[lang]); b_bus5(lang, BUS5[lang])
        d = dict(g.SUB1[lang]); d['nb'] = NB[lang]
        g.b_sub1(lang, d)
    print('ok', g.OUT)
