# Shopping figures (daiso, shopping-streets, kbeauty-how-to-choose), 2026-11-26 principles pass.
# Reuses the helpers in gen-4pages.py. Usage: python3 gen-shopping.py <outdir>  -> <outdir>/<lang>/<name>.svg
# Writes only: shopping-streets-1..7, daiso-2, daiso-4, kbeauty-how-to-choose-4.
import os, sys, math, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('g4', os.path.join(HERE, 'gen-4pages.py'))
G = importlib.util.module_from_spec(spec); spec.loader.exec_module(G)
G.OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out-shopping')
INK, RED, PAPER, MUTED, RULE, WHITE, SOFT = G.INK, G.RED, G.PAPER, G.MUTED, G.RULE, G.WHITE, G.SOFT
W, PAD, T, R, block, wrap, lh, arrow, num, tw = G.W, G.PAD, G.T, G.R, G.block, G.wrap, G.lh, G.arrow, G.num, G.tw
LANGS = ['en', 'ko', 'ja', 'zh-tw']

# ------------------------------------------------------------------ shopping-streets-1/2/3 (three areas, no Dongdaemun)
SH1 = {
 'en': dict(title='What to buy where, and when', cats=['Beauty', 'Fashion', 'K-pop goods', 'Pop-ups'],
   areas=[('Myeongdong', 'Earlier in the day'), ('Seongsu', 'Weekday'), ('Hongdae', 'Late afternoon–evening')], best='Best for', good='Also good', time='Best time (our call)'),
 'ko': dict(title='어디서 무엇을, 언제', cats=['뷰티', '패션', 'K-팝 굿즈', '팝업'],
   areas=[('명동', '이른 시간'), ('성수', '평일'), ('홍대', '늦은 오후~저녁')], best='가장 잘 맞음', good='이것도 괜찮음', time='가기 좋은 시간(저희 판단)'),
 'ja': dict(title='どこで何を、いつ買う?', cats=['コスメ', '服', 'K-POP', 'ポップアップ'],
   areas=[('明洞', '早めの時間'), ('聖水', '平日'), ('弘大', '夕方〜夜')], best='いちばん向いている', good='これも向いている', time='いい時間帯(私たちの判断)'),
 'zh-tw': dict(title='哪裡買什麼、什麼時候去', cats=['美妝', '服飾', 'K-POP周邊', '快閃店'],
   areas=[('明洞', '早點去'), ('聖水', '平日'), ('弘大', '傍晚到晚上')], best='最適合', good='也不錯', time='最佳時段(我們的判斷)'),
}
G.MARKS = [[2, 1, 0, 0], [1, 2, 0, 2], [1, 2, 2, 0]]

SH2 = {
 'en': dict(title='Three shopping areas on Line 2', sub='Schematic, not to scale', river='Han River', line='Line 2 (loop)',
   st={'hd': ('Hongdae', 'Young fashion', 'Hongik Univ. · Exit 9'), 'md': ('Myeongdong', 'Beauty', 'Euljiro 1-ga · Exit 5'), 'ss': ('Seongsu', 'New brands, pop-ups', 'Seongsu · Exit 4')}),
 'ko': dict(title='2호선 위의 세 쇼핑 지역', sub='개념도, 축척 아님', river='한강', line='2호선(순환선)',
   st={'hd': ('홍대', '젊은 패션', '홍대입구역 9번 출구'), 'md': ('명동', '뷰티', '을지로입구역 5번 출구'), 'ss': ('성수', '새 브랜드·팝업', '성수역 4번 출구')}),
 'ja': dict(title='2号線沿いの3つの買い物エリア', sub='イメージ図・縮尺は不正確', river='漢江', line='2号線(環状線)',
   st={'hd': ('弘大', '若いファッション', '弘大入口駅 9番出口'), 'md': ('明洞', 'コスメ', '乙支路入口駅 5番出口'), 'ss': ('聖水', '新ブランド・ポップアップ', '聖水駅 4番出口')}),
 'zh-tw': dict(title='2號線上的三個逛街區', sub='示意圖,非實際比例', river='漢江', line='2號線(環狀線)',
   st={'hd': ('弘大', '年輕服飾', '弘大入口站 9號出口'), 'md': ('明洞', '美妝', '乙支路入口站 5號出口'), 'ss': ('聖水', '新品牌、快閃店', '聖水站 4號出口')}),
}

SH3 = {
 'en': dict(title='Half-day route on Line 2', foot='Beauty first? Swap Seongsu for Myeongdong (Euljiro 1-ga, Line 2).', steps=[
   ('Seongsu', 'Early afternoon', ['Exit 4 (or 3)', 'Yeonmujang-gil']), ('Line 2', 'Ride to', ['Hongik Univ.']),
   ('Hongdae', 'Late afternoon–evening', ['Exit 9 → R3, 350 m', 'Covernat until 21:00']), ('Receipts', 'Keep with passport', ['Over ₩1,000,000 per receipt\n→ no instant refund'])]),
 'ko': dict(title='2호선 한나절 동선', foot='뷰티가 먼저라면 성수 대신 명동\n(을지로입구역, 2호선).', steps=[
   ('성수', '이른 오후', ['4번(또는 3번) 출구', '연무장길로']), ('2호선', '타고 이동', ['홍대입구역까지']),
   ('홍대', '늦은 오후~저녁', ['9번 출구 → R3, 350m', '커버낫 21:00까지']), ('영수증', '여권과 함께', ['한 장 100만 원 초과 → 즉시 환급 안 됨'])]),
 'ja': dict(title='2号線で半日コース', foot='コスメ優先なら聖水を明洞に\n(乙支路入口駅も2号線)。', steps=[
   ('聖水', '午後早め', ['4番(または3番)出口', '演武場キルへ']), ('2号線', '乗って移動', ['弘大入口駅まで']),
   ('弘大', '夕方〜夜', ['9番出口 → R3、350m', 'COVERNATは21:00まで']), ('レシート', 'パスポートと一緒に', ['1枚100万ウォン超 →\nその場の還付は不可'])]),
 'zh-tw': dict(title='2號線半日路線', foot='美妝優先?把聖水換成明洞\n(乙支路入口站也在2號線)。', steps=[
   ('聖水', '午後', ['4號(或3號)出口', '走到演武場街']), ('2號線', '搭乘', ['到弘大入口站']),
   ('弘大', '傍晚到晚上', ['9號出口 → R3,350公尺', 'COVERNAT 到21:00']), ('收據', '和護照放一起', ['單張超過100萬韓元 → 不能現場退稅'])]),
}

def b_sh2(lang, d):
    body, y = G.title_block(d['title'], d['sub'])
    top = y + 96
    cx, cy, rx, ry = 200, top + 120, 150, 112
    river_y = cy + ry - 24
    body += (f'<path d="M0,{river_y} C80,{river_y-22} 160,{river_y+18} 240,{river_y} S360,{river_y-16} 400,{river_y-4} '
             f'L400,{river_y+40} C320,{river_y+26} 260,{river_y+58} 180,{river_y+42} S60,{river_y+30} 0,{river_y+46} Z" fill="{SOFT}" stroke="{RULE}" stroke-width="1.5"/>\n')
    body += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="9 7"/>\n'
    def pt(deg):
        a = math.radians(deg)
        return round(cx + rx * math.cos(a)), round(cy - ry * math.sin(a))
    pos = {'hd': pt(180), 'md': pt(97), 'ss': pt(-8)}
    for k, (x, yy) in pos.items():
        body += f'<circle cx="{x}" cy="{yy}" r="10" fill="{RED}" stroke="{WHITE}" stroke-width="3"/>\n'
    def lab(key, x, yy, anchor):
        name, what, stn = d['st'][key]
        # paper-coloured halo so labels stay readable where they cross the loop
        return (f'<g stroke="{PAPER}" stroke-width="6" stroke-linejoin="round" paint-order="stroke">\n'
                + T(x, yy, name, 18, INK, True, anchor) + T(x, yy + 22, what, 16, MUTED, False, anchor)
                + T(x, yy + 44, stn, 16, RED, True, anchor) + '</g>\n')
    x, yy = pos['md']; body += lab('md', x, yy - 72, 'middle')
    x, yy = pos['hd']; body += lab('hd', x + 24, yy + 14, 'start')
    x, yy = pos['ss']; body += lab('ss', x - 20, yy - 84, 'end')
    body += T(60, river_y + 34, d['river'], 16, MUTED, False, 'middle')
    bottom = cy + ry
    body += T(W - PAD - 4, bottom + 34, d['line'], 16, INK, True, 'end')
    G.write(lang, 'shopping-streets-2', d['title'], body, bottom + 52)

# ------------------------------------------------------------------ exits figures (shopping-streets-4/5/6)
EXITLAB = {'en': 'Exit', 'ko': '출구', 'ja': '出口', 'zh-tw': '出口'}
SH4 = {
 'en': dict(title='Myeongdong: which exit', groups=[('Myeongdong', 'Line 4', [('Exit 8', 'Olive Young Myeongdong Global Store', ['Opens 10:00'])]),
            ('Euljiro 1-ga', 'Line 2', [('Exit 5', 'Olive Young Myeongdong Global Store', ['Same store, from Line 2'])])],
            foot='Also by Myeong-dong Station: Daiso, 12 floors'),
 'ko': dict(title='명동: 어느 출구로', groups=[('명동역', '4호선', [('8번 출구', '올리브영 명동 글로벌 매장', ['10:00 개점'])]),
            ('을지로입구역', '2호선', [('5번 출구', '올리브영 명동 글로벌 매장', ['같은 매장, 2호선에서'])])],
            foot='명동역 옆: 12층짜리 다이소'),
 'ja': dict(title='明洞:どの出口から', groups=[('明洞駅', '4号線', [('8番出口', 'オリーブヤング明洞グローバル店', ['10:00開店'])]),
            ('乙支路入口駅', '2号線', [('5番出口', 'オリーブヤング明洞グローバル店', ['同じ店、2号線から'])])],
            foot='明洞駅のそば:12階建てのダイソー'),
 'zh-tw': dict(title='明洞:走哪個出口', groups=[('明洞站', '4號線', [('8號出口', 'Olive Young 明洞 Global 門市', ['10:00開門'])]),
            ('乙支路入口站', '2號線', [('5號出口', 'Olive Young 明洞 Global 門市', ['同一家店,從2號線'])])],
            foot='明洞站旁:12層樓的大創'),
}
SH5 = {
 'en': dict(title='Seongsu Station: Exit 4 or 3', groups=[('Seongsu', 'Line 2', [
            ('Exit 4', 'Yeonmujang-gil starts here', ['Olive Young N Seongsu: about a minute’s walk']),
            ('Exit 3', 'Musinsa Megastore', ['475 m · 11:00–22:00'])])],
            foot='Weekends: crowded at Musinsa Megastore, waits at some shops (Korea Herald)'),
 'ko': dict(title='성수역: 4번 또는 3번 출구', groups=[('성수역', '2호선', [
            ('4번 출구', '연무장길이 시작되는 곳', ['올리브영 N 성수: 걸어서 1분']),
            ('3번 출구', '무신사 메가스토어', ['475m · 11:00~22:00'])])],
            foot='주말엔 무신사 메가스토어가 붐비고 일부 매장은 대기(코리아헤럴드)'),
 'ja': dict(title='聖水駅:4番出口か3番出口か', groups=[('聖水駅', '2号線', [
            ('4番出口', '演武場キルの起点', ['オリーブヤング N 聖水:徒歩1分']),
            ('3番出口', 'ムシンサ・メガストア', ['475m・11:00〜22:00'])])],
            foot='週末はムシンサ・メガストアが混雑、待ち時間が出る店も(コリア・ヘラルド)'),
 'zh-tw': dict(title='聖水站:4號還是3號出口', groups=[('聖水站', '2號線', [
            ('4號出口', '演武場街從這裡開始', ['Olive Young N 聖水:步行約1分鐘']),
            ('3號出口', 'MUSINSA Megastore', ['475公尺・11:00–22:00'])])],
            foot='週末 MUSINSA Megastore 人多,有些店要排隊(韓國先驅報)'),
}
SH6 = {
 'en': dict(title='Hongik Univ. Station: Exit 9 or 1', groups=[('Hongik Univ.', 'Line 2 · AREX · Gyeongui–Jungang', [
            ('Exit 9', 'R3 fashion street', ['350 m · clothing and cosmetics shops']),
            ('Exit 1', 'K-Pop Square', ['Former LINE Friends flagship'])])],
            foot='Covernat flagship: 12:00–21:00, tax refund at the counter (Visit Seoul)'),
 'ko': dict(title='홍대입구역: 9번 또는 1번 출구', groups=[('홍대입구역', '2호선 · 공항철도 · 경의·중앙선', [
            ('9번 출구', 'R3 패션 거리', ['350m · 옷 가게와 화장품 가게']),
            ('1번 출구', 'K-Pop Square', ['옛 라인프렌즈 플래그십'])])],
            foot='커버낫 플래그십: 12:00~21:00, 계산대에서 택스 리펀드(비짓서울)'),
 'ja': dict(title='弘大入口駅:9番出口か1番出口か', groups=[('弘大入口駅', '2号線・空港鉄道・京義・中央線', [
            ('9番出口', 'R3ファッション通り', ['350m・服とコスメの店']),
            ('1番出口', 'K-Pop Square', ['元LINE FRIENDS旗艦店'])])],
            foot='COVERNAT旗艦店:12:00〜21:00、レジでタックスリファンド(Visit Seoul)'),
 'zh-tw': dict(title='弘大入口站:9號還是1號出口', groups=[('弘大入口站', '2號線・機場鐵路・京義中央線', [
            ('9號出口', 'R3 服飾街', ['350公尺・服飾店和美妝店']),
            ('1號出口', 'K-Pop Square', ['原 LINE FRIENDS 旗艦店'])])],
            foot='COVERNAT 旗艦店:12:00–21:00,櫃台可退稅(Visit Seoul)'),
}

def exits(name, d):
    body, y = G.title_block(d['title'])
    BX, BW = PAD, 96            # exit badge
    CX = PAD + BW + 26          # card x
    CW = W - PAD - CX
    for gi, (stn, line, rows) in enumerate(d['groups']):
        if gi:
            y += 14
        # station sign
        sl = wrap(line, 16, W - 2 * PAD - 28)
        h = lh(19) + len(sl) * lh(16) + 20
        body += R(PAD, y, W - 2 * PAD, h, INK, None, 10)
        s, hh = block(PAD + 14, y + 10, [stn], 19, WHITE, True); body += s
        s, _ = block(PAD + 14, y + 10 + hh, sl, 16, SOFT); body += s
        y += h
        for ex, dest, det in rows:
            y += 12
            dl = wrap(dest, 17, CW - 24, True)
            tl = []
            for t_ in det:
                tl += wrap(t_, 16, CW - 24)
            h = len(dl) * lh(17) + len(tl) * lh(16) + 22
            body += f'<line x1="{PAD + 20}" y1="{y - 12}" x2="{PAD + 20}" y2="{y + h / 2:g}" stroke="{RULE}" stroke-width="3"/>\n'
            body += R(BX + 8, y + h / 2 - 18, BW - 8, 36, RED, None, 18)
            body += T(BX + 8 + (BW - 8) / 2, y + h / 2 + 6, ex, 17, WHITE, True, 'middle')
            body += arrow(BX + BW + 2, y + h / 2, CX - 4, y + h / 2)
            body += R(CX, y, CW, h, WHITE, RULE, 2)
            s, hh = block(CX + 12, y + 11, dl, 17, INK, True); body += s
            s, _ = block(CX + 12, y + 11 + hh, tl, 16, MUTED); body += s
            y += h
    y += 16
    fl = wrap(d['foot'], 16, W - 2 * PAD - 28)
    h = len(fl) * lh(16) + 22
    body += R(PAD, y, W - 2 * PAD, h, SOFT, None, 10)
    s, _ = block(PAD + 14, y + 11, fl, 16, INK); body += s
    return body, y + h + 18

# ------------------------------------------------------------------ shopping-streets-7: receipt range
SH7 = {
 'en': dict(title='Tax-free at the till, per receipt', a=('₩15,000 – ₩1,000,000', 'The refund is given in the store'),
   b=('Over ₩1,000,000', 'No instant refund at the till: see our tax refund page'), pp='Physical passport, shown when you pay',
   foot='Olive Young Myeongdong Global Store FAQ. Other stores: ask before you pay.'),
 'ko': dict(title='계산대 택스프리, 영수증 한 장 기준', a=('1만 5천 원 ~ 100만 원', '환급은 매장에서 받아요'),
   b=('100만 원 초과', '계산대 즉시 환급 안 됨: 택스 리펀드 페이지로'), pp='실물 여권, 계산할 때 보여 주기',
   foot='올리브영 명동 글로벌 매장 FAQ 기준. 다른 매장은 계산 전에 물어보기.'),
 'ja': dict(title='レジでの免税、レシート1枚ごと', a=('1万5千〜100万ウォン', '還付は店内で受けられる'),
   b=('100万ウォン超', 'レジでの即時還付は不可:タックスリファンドのページへ'), pp='パスポートの実物を会計のときに提示',
   foot='オリーブヤング明洞グローバル店のFAQより。ほかの店は会計前に確認。'),
 'zh-tw': dict(title='結帳現場退稅,以單張收據計', a=('1萬5千~100萬韓元', '退稅在店內辦好'),
   b=('超過100萬韓元', '不能結帳時現場退稅:見退稅頁面'), pp='帶護照正本,結帳時出示',
   foot='依 Olive Young 明洞 Global 門市 FAQ。其他店請結帳前先問。'),
}

def receipt_icon(x, y):
    s = f'<path d="M{x},{y} h44 v62 l-7,-5 l-7,5 l-8,-5 l-7,5 l-8,-5 l-7,5 z" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>\n'
    for i in range(4):
        s += f'<line x1="{x+8}" y1="{y+12+i*11}" x2="{x+36 - (12 if i == 3 else 0)}" y2="{y+12+i*11}" stroke="{RULE}" stroke-width="3"/>\n'
    return s

def passport_icon(x, y):
    return (f'<rect x="{x}" y="{y}" width="40" height="54" rx="5" fill="{RED}"/>'
            f'<circle cx="{x+20}" cy="{y+22}" r="9" fill="none" stroke="{WHITE}" stroke-width="2"/>'
            f'<line x1="{x+10}" y1="{y+42}" x2="{x+30}" y2="{y+42}" stroke="{WHITE}" stroke-width="2"/>\n')

def b_sh7(lang, d):
    body, y = G.title_block(d['title'])
    TX = PAD + 76
    TWD = W - PAD - 14 - TX
    for (head, sub), hl in ((d['a'], True), (d['b'], False)):
        hl_ = wrap(head, 19 if hl else 18, TWD, True); sl = wrap(sub, 16, TWD)
        h = max(len(hl_) * lh(19 if hl else 18) + len(sl) * lh(16) + 26, 86)
        body += R(PAD, y, W - 2 * PAD, h, WHITE if hl else SOFT, RED if hl else None, 3 if hl else 0)
        body += receipt_icon(PAD + 16, y + h / 2 - 32)
        if hl:
            body += f'<circle cx="{PAD + 58}" cy="{y + h / 2 + 22:g}" r="11" fill="{RED}"/><path d="M{PAD+52},{y + h / 2 + 22:g} l4,5 l8,-9" fill="none" stroke="{WHITE}" stroke-width="2.5"/>\n'
        else:
            body += f'<circle cx="{PAD + 58}" cy="{y + h / 2 + 22:g}" r="11" fill="{MUTED}"/><path d="M{PAD+53},{y + h / 2 + 17:g} l10,10 M{PAD+63},{y + h / 2 + 17:g} l-10,10" stroke="{WHITE}" stroke-width="2.5"/>\n'
        ty = y + (h - len(hl_) * lh(19 if hl else 18) - len(sl) * lh(16)) / 2
        s, hh = block(TX, ty, hl_, 19 if hl else 18, RED if hl else INK, True); body += s
        s, _ = block(TX, ty + hh, sl, 16, INK if hl else MUTED); body += s
        y += h + 12
    pl = wrap(d['pp'], 17, TWD, True)
    h = max(len(pl) * lh(17) + 24, 76)
    body += R(PAD, y, W - 2 * PAD, h, WHITE, RULE, 2)
    body += passport_icon(PAD + 18, y + h / 2 - 27)
    s, _ = block(TX, y + (h - len(pl) * lh(17)) / 2, pl, 17, INK, True); body += s
    y += h + 12
    fl = wrap(d['foot'], 16, W - 2 * PAD - 8)
    s, hh = block(PAD + 4, y, fl, 16, MUTED); body += s
    G.write(lang, 'shopping-streets-7', d['title'], body, y + hh + 16)

# ------------------------------------------------------------------ cards with drawn icons (daiso-4, kbeauty-4)
def icon(kind, cx, cy):
    cx, cy = round(cx), round(cy)
    if kind == 'tube':
        return (f'<rect x="{cx-14}" y="{cy-22}" width="28" height="40" rx="6" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
                f'<rect x="{cx-8}" y="{cy-32}" width="16" height="11" rx="2" fill="{RED}"/>'
                f'<line x1="{cx-7}" y1="{cy-4}" x2="{cx+7}" y2="{cy-4}" stroke="{RULE}" stroke-width="3"/>\n')
    if kind == 'snack':
        return (f'<path d="M{cx-20},{cy-24} l5,-5 l5,5 l5,-5 l5,5 l5,-5 l5,5 l5,-5 l5,5 v46 h-40 z" fill="{SOFT}" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>'
                f'<circle cx="{cx}" cy="{cy+2}" r="9" fill="{RED}"/>\n')
    if kind == 'plug':
        return (f'<rect x="{cx-18}" y="{cy-14}" width="36" height="30" rx="6" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
                f'<line x1="{cx-7}" y1="{cy-14}" x2="{cx-7}" y2="{cy-26}" stroke="{INK}" stroke-width="4"/>'
                f'<line x1="{cx+7}" y1="{cy-14}" x2="{cx+7}" y2="{cy-26}" stroke="{INK}" stroke-width="4"/>'
                f'<path d="M{cx},{cy+16} q0,12 12,14" fill="none" stroke="{RED}" stroke-width="3"/>\n')
    if kind == 'zipbag':
        s = (f'<rect x="{cx-26}" y="{cy-24}" width="52" height="50" rx="5" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
             f'<line x1="{cx-26}" y1="{cy-15}" x2="{cx+26}" y2="{cy-15}" stroke="{RED}" stroke-width="3"/>')
        for i, hgt in enumerate([24, 30, 20]):
            x = cx - 18 + i * 13
            s += f'<rect x="{x}" y="{cy+22-hgt}" width="10" height="{hgt}" rx="3" fill="{SOFT}" stroke="{INK}" stroke-width="1.5"/>'
        return s + '\n'
    if kind == 'suitcase':
        return (f'<rect x="{cx-26}" y="{cy-18}" width="52" height="42" rx="7" fill="{SOFT}" stroke="{INK}" stroke-width="2.5"/>'
                f'<path d="M{cx-10},{cy-18} v-9 h20 v9" fill="none" stroke="{INK}" stroke-width="2.5"/>'
                f'<line x1="{cx-12}" y1="{cy-18}" x2="{cx-12}" y2="{cy+24}" stroke="{INK}" stroke-width="2"/>'
                f'<line x1="{cx+12}" y1="{cy-18}" x2="{cx+12}" y2="{cy+24}" stroke="{INK}" stroke-width="2"/>\n')
    if kind == 'sealed':
        return (f'<rect x="{cx-22}" y="{cy-24}" width="44" height="50" rx="5" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>'
                f'<rect x="{cx-22}" y="{cy-24}" width="44" height="10" fill="{RED}"/>'
                f'<rect x="{cx-9}" y="{cy}" width="18" height="20" rx="3" fill="{SOFT}" stroke="{INK}" stroke-width="1.5"/>\n')
    return ''

def cards(name, title, items, forlab, foot):
    body, y = G.title_block(title)
    TX = PAD + 84
    TWD = W - PAD - 12 - TX
    for it in items:
        tl = wrap(it['t'], 18, TWD, True)
        ll = []
        for t_ in it['lines']:
            ll += wrap(t_, 16, TWD)
        fl = wrap(forlab + it['for'], 16, TWD, True) if it.get('for') else []
        th = len(tl) * lh(18) + len(ll) * lh(16) + (len(fl) * lh(16) + 4 if fl else 0)
        h = max(th + 24, 88)
        body += R(PAD, y, W - 2 * PAD, h, WHITE, RULE, 2)
        body += icon(it['icon'], PAD + 42, y + h / 2)
        ty = y + (h - th) / 2
        s, hh = block(TX, ty, tl, 18, INK, True); body += s; ty += hh
        s, hh = block(TX, ty, ll, 16, MUTED); body += s; ty += hh
        if fl:
            s, _ = block(TX, ty + 4, fl, 16, RED, True); body += s
        y += h + 12
    fl = wrap(foot, 16, W - 2 * PAD - 28)
    h = len(fl) * lh(16) + 22
    body += R(PAD, y, W - 2 * PAD, h, SOFT, None, 10)
    s, _ = block(PAD + 14, y + 11, fl, 16, INK); body += s
    return body, y + h + 18

DA4 = {
 'en': dict(title='What visitors buy at Daiso, and who it is for', forlab='For: ', foot='Who it is for: our call. Prices: check the tag.', items=[
   dict(icon='tube', t='Budget skincare', lines=['About 170 beauty brands (2026)', 'Often smaller sizes or Daiso-only lines'], **{'for': 'yourself'}),
   dict(icon='snack', t='Snacks and small souvenirs', lines=['Most snacks about ₩1,000–₩2,000', 'Character goods, photocard accessories'], **{'for': 'sharing; a K-pop fan'}),
   dict(icon='plug', t='Trip fixes', lines=['Multi-adaptors, luggage scales, phone chargers'], **{'for': 'the trip itself'})]),
 'ko': dict(title='다이소에서 사는 것, 누구를 위해', forlab='누구에게: ', foot='누구에게 맞는지는 저희 판단. 가격은 가격표로 확인.', items=[
   dict(icon='tube', t='저가 화장품', lines=['뷰티 브랜드 약 170개(2026년)', '작은 용량·다이소 전용 라인이 많음'], **{'for': '나'}),
   dict(icon='snack', t='과자와 작은 기념품', lines=['과자는 대체로 ₩1,000~₩2,000', '캐릭터 상품, 포토카드 용품'], **{'for': '나눠 줄 사람들, K-팝 팬'}),
   dict(icon='plug', t='여행 중 필요한 물건', lines=['멀티 어댑터, 수하물 저울, 휴대폰 충전기'], **{'for': '여행 중의 나'})]),
 'ja': dict(title='ダイソーで買われているもの、誰のために', forlab='誰に:', foot='誰に向くかは私たちの判断。価格は値札で確認。', items=[
   dict(icon='tube', t='プチプラコスメ', lines=['コスメブランド約170(2026年)', '小容量やダイソー専用ラインが多い'], **{'for': '自分'}),
   dict(icon='snack', t='お菓子と小さなお土産', lines=['お菓子はだいたい1,000〜2,000ウォン', 'キャラクター商品、トレカ用品'], **{'for': '配る用、K-POPファン'}),
   dict(icon='plug', t='旅行中に必要な物', lines=['マルチ変換プラグ、荷物はかり、スマホの充電器'], **{'for': '旅行中の自分'})]),
 'zh-tw': dict(title='旅客在大創買什麼、買給誰', forlab='買給:', foot='買給誰是我們的判斷。價格請看標價。', items=[
   dict(icon='tube', t='平價保養品', lines=['美妝品牌約 170 個(2026 年)', '常是小容量或大創專用系列'], **{'for': '自己'}),
   dict(icon='snack', t='零食和小伴手禮', lines=['零食大多 1,000 至 2,000 韓元', '角色商品、小卡周邊'], **{'for': '分送親友、K-POP 粉絲'}),
   dict(icon='plug', t='旅途用品', lines=['萬用轉接頭、行李秤、手機充電器'], **{'for': '旅途中的自己'})]),
}

KB4 = {
 'en': dict(title='Packing K-beauty for the flight', foot='Incheon Airport, international flights. Check your airline too.', items=[
   dict(icon='zipbag', t='Cabin bag', lines=['Each liquid, gel or spray: 100 mL or less', 'All in one clear 1 L zip bag per person']),
   dict(icon='suitcase', t='Checked baggage', lines=['Bigger bottles', 'Personal sprays such as hairspray: 500 mL each, 2 L in total']),
   dict(icon='sealed', t='Duty-free liquids', lines=['Keep the sealed bag closed until you board the flight to your final destination'])]),
 'ko': dict(title='화장품 짐 싸기', foot='인천공항 국제선 기준. 이용 항공사 기준도 확인하세요.', items=[
   dict(icon='zipbag', t='기내 반입', lines=['액체·젤·스프레이: 용기당 100mL 이하', '1인당 1L 투명 지퍼백 1개']),
   dict(icon='suitcase', t='위탁 수하물', lines=['큰 용량', '헤어스프레이 같은 개인 위생용 스프레이: 용기당 500mL, 총 2L']),
   dict(icon='sealed', t='면세 액체류', lines=['최종 목적지행 비행기에 탈 때까지 밀봉 봉투 그대로'])]),
 'ja': dict(title='コスメの荷造り', foot='仁川空港の国際線の基準。航空会社の基準も確認を。', items=[
   dict(icon='zipbag', t='機内持ち込み', lines=['液体・ジェル・スプレー:1容器100mL以下', '1人1枚の1L透明ジッパー袋に']),
   dict(icon='suitcase', t='預け入れ荷物', lines=['大きいボトル', 'ヘアスプレーなど身だしなみ用スプレー:1容器500mL・合計2Lまで']),
   dict(icon='sealed', t='免税店の液体物', lines=['最終目的地行きの便に乗るまで、密封袋を開けない'])]),
 'zh-tw': dict(title='保養品怎麼打包', foot='仁川機場國際線規定。也請確認你搭乘航空公司的規定。', items=[
   dict(icon='zipbag', t='手提行李', lines=['液體、凝膠、噴霧:每瓶 100mL 以下', '每人一個 1L 透明夾鏈袋']),
   dict(icon='suitcase', t='託運行李', lines=['大瓶的', '髮膠等個人衛生噴霧:每瓶 500mL、總共 2L']),
   dict(icon='sealed', t='免稅店液體', lines=['搭上前往最終目的地的班機前,專用袋保持密封'])]),
}

# ------------------------------------------------------------------ daiso-2: 12-floor tower + 4 steps
DA2 = {
 'en': dict(title='Myeongdong Station Daiso:\n12 floors, 4 steps', beauty='2F Beauty', where='On the road between Myeong-dong Station Exits 1 and 4',
   note='Beauty on 2F: Daiso’s 2023 floor plan, still reported in Sept 2026', group='For a tax refund', sc=('Self-checkout', 'Scan the QR code on the product, not the barcode.'), steps=[
   ('Floor guide', ['EN · JA · ZH', 'pick 2–3 floors']), ('Beauty: 2F', ['viral items can sell out']),
   ('One purchase', ['each receipt ₩15,000+']), ('Passport', ['show it when you pay'])]),
 'ko': dict(title='명동역점 다이소:\n12개 층, 4단계', beauty='2F 뷰티', where='명동역 1번과 4번 출구 사이 길가',
   note='2층 뷰티: 다이소 2023년 층 구성, 2026년 9월 보도도 2층', group='택스리펀드를 받으려면', sc=('셀프 계산대', '바코드가 아니라 상품의 QR코드를 찍어요.'), steps=[
   ('층별 안내', ['영·일·중 안내', '2~3개 층 고르기']), ('뷰티는 2층', ['화제 상품은 품절되기도']),
   ('한 번에 계산', ['영수증마다 ₩15,000 이상']), ('여권', ['결제할 때 보여 주기'])]),
 'ja': dict(title='明洞駅店ダイソー:\n12フロア、4ステップ', beauty='2F コスメ', where='明洞駅1番出口と4番出口の間の通り沿い',
   note='コスメは2階:2023年のフロア構成、2026年9月の報道でも2階', group='免税を受けるなら', sc=('セルフレジ', 'バーコードではなく、商品のQRコードを読み取る。'), steps=[
   ('フロアガイド', ['英・日・中あり', '2〜3階に絞る']), ('コスメは2階', ['話題の商品は売り切れも']),
   ('会計は1回に', ['レシート1枚ごとに15,000ウォン以上']), ('パスポート', ['支払いのときに提示'])]),
 'zh-tw': dict(title='明洞站店大創:\n12 層樓、4 步驟', beauty='2F 美妝', where='明洞站 1 號和 4 號出口之間的路邊',
   note='美妝在 2 樓:大創 2023 年樓層配置,2026 年 9 月報導仍在 2 樓', group='要退稅的話', sc=('自助結帳', '掃商品上的 QR code,不是條碼。'), steps=[
   ('樓層指南', ['有英日中文', '縮到 2~3 層']), ('美妝在 2 樓', ['爆紅商品可能賣完']),
   ('一次結帳', ['每張收據滿 15,000 韓元']), ('護照', ['付款時出示正本'])]),
}

def b_da2(lang, d):
    body, y = G.title_block(d['title'])
    wl = wrap(d['where'], 16, W - 2 * PAD - 8)
    s, hh = block(PAD + 4, y - 6, wl, 16, MUTED); body += s
    y += hh + 6
    top = y
    TWX, TWW, FH = PAD, 100, 27
    # tower
    for i in range(12):
        f = 12 - i
        fy = top + i * FH
        fill = RED if f == 2 else (SOFT if f % 2 else WHITE)
        body += f'<rect x="{TWX}" y="{fy}" width="{TWW}" height="{FH}" fill="{fill}" stroke="{RULE}" stroke-width="1.5"/>\n'
        lab = d['beauty'] if f == 2 else f'{f}F'
        body += T(TWX + TWW / 2, fy + 20, lab, 16, WHITE if f == 2 else INK, f == 2, 'middle')
    body += f'<rect x="{TWX}" y="{top}" width="{TWW}" height="{12 * FH}" fill="none" stroke="{INK}" stroke-width="2.5"/>\n'
    tower_bottom = top + 12 * FH
    # steps on the right
    SX = TWX + TWW + 14
    SW = W - PAD - SX
    TX = SX + 40
    TWD = SW - 48
    y = top
    for i, (t, subs) in enumerate(d['steps']):
        if i == 2:
            s, hh = block(SX + 2, y, wrap(d['group'], 16, SW), 16, RED, True); body += s
            y += hh + 2
        tl = wrap(t, 17, TWD, True); sl = []
        for sb in subs:
            sl += wrap(sb, 16, TWD)
        th = len(tl) * lh(17) + len(sl) * lh(16)
        h = th + 18
        hl = i == 1
        body += R(SX, y, SW, h, WHITE, RED if hl else RULE, 2.5 if hl else 2, 10)
        body += f'<circle cx="{SX + 20}" cy="{y + h / 2:g}" r="13" fill="{RED if i in (1, 3) else INK}"/>\n' + T(SX + 20, y + h / 2 + 6, str(i + 1), 16, WHITE, True, 'middle')
        s, hh = block(TX, y + 9, tl, 17, INK, True); body += s
        s, _ = block(TX, y + 9 + hh, sl, 16, MUTED); body += s
        y += h + 10
    y = max(y, tower_bottom) + 10
    nl = wrap(d['note'], 16, W - 2 * PAD - 8)
    s, hh = block(PAD + 4, y, nl, 16, MUTED); body += s
    y += hh + 10
    head, txt = d['sc']
    hl_ = wrap(head, 17, W - 2 * PAD - 28, True); bl_ = wrap(txt, 16, W - 2 * PAD - 28)
    h = len(hl_) * lh(17) + len(bl_) * lh(16) + 24
    body += R(PAD, y, W - 2 * PAD, h, SOFT, None, 10)
    s, hh = block(PAD + 14, y + 12, hl_, 17, INK, True); body += s
    s, _ = block(PAD + 14, y + 12 + hh, bl_, 16, INK); body += s
    G.write(lang, 'daiso-2', d['title'], body, y + h + 18)

if __name__ == '__main__':
    for lang in LANGS:
        G.b_sh1(lang, SH1[lang]); b_sh2(lang, SH2[lang]); G.b_sh3(lang, SH3[lang])
        for n, D in ((4, SH4), (5, SH5), (6, SH6)):
            body, h = exits(f'shopping-streets-{n}', D[lang]); G.write(lang, f'shopping-streets-{n}', D[lang]['title'], body, h)
        b_sh7(lang, SH7[lang])
        b_da2(lang, DA2[lang])
        d = DA4[lang]; body, h = cards('daiso-4', d['title'], d['items'], d['forlab'], d['foot']); G.write(lang, 'daiso-4', d['title'], body, h)
        d = KB4[lang]; body, h = cards('kbeauty-how-to-choose-4', d['title'], d['items'], '', d['foot']); G.write(lang, 'kbeauty-how-to-choose-4', d['title'], body, h)
    print('ok', G.OUT)
