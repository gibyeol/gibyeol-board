# Wayfinding to the Klook T-money pickup points at Incheon Airport, redrawn by Nadri (facts only).
# Fact sources (opened 2026-11-28):
#  - airport.kr ap_ko/1004 (general shops) T1: 경인문고(K BOOKS) "제1여객터미널 1층 일반지역 중앙 밀레니엄홀 부근" 07:00~21:00,
#    FLOPORT 꽃집 "1층 일반지역 8번 출입구 부근"; T2 (srchTerminalId=P03): 트래블메이트 & 북스토어 "제2여객터미널 3층 일반지역 F 체크인카운터 맞은편"
#  - airport.kr ap_ko/1008 (facilities) T1: 메디컬코리아 의료관광 안내센터 "1층 7번 출입구 부근"; T2: 안내데스크 24H "1층 4번 출입구 부근",
#    "1층 9번 출입구 부근", "3층 D 체크인카운터 부근"; 내국세환급(키오스크) "3층 F 체크인카운터 부근"
#  - airport.kr ap_ko/6652 T2 3F plan image (img_bg_traffic_t2.jpg): counters A..N, gap in the middle between F and G
#  - Klook T-money product page (원두 screens 2026-11-28): T1 "Book Store, 1st Floor, Exit 7, 07:00-21:00";
#    T2 "Travel Mate & Book Store, 3rd Floor, Counter F, 06:30-21:30"
# usage: python3 tools/figgen/tmoney_pickup_maps.py -> static/fig/<lang>/airport-tmoney-t1.svg, airport-tmoney-t2.svg
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from icn_maps import T, arcpt, badge, esc, RED, INK, GREY

L = {
 'ko': dict(t1='1터미널 1층', t2='2터미널 3층 (출국장)', here='입국장(A~F)에서 나와요', go='출입구 번호 7 쪽(가운데)으로', shop1='서점 K BOOKS = 티머니 받는 곳',
            hall='밀레니엄홀', med='의료관광 안내센터', flower='꽃집 FLOPORT', shop2='트래블메이트 & 북스토어 = 티머니 받는 곳', opp='F 카운터 맞은편',
            up='1층 입국장에서 3층으로 올라와요 (올라오는 자리는 확인 못 함)', mid='가운데', info='안내데스크 24시간', kiosk='택스리펀드 키오스크', gates='출국장', counters='체크인 카운터 A~N',
            note='가게 자리는 공식 안내 "F 체크인카운터 맞은편" 기준이에요'),
 'en': dict(t1='Terminal 1, 1F', t2='Terminal 2, 3F (departures)', here='You come out of arrival exit A–F', go='Walk towards door 7 (the middle)', shop1='K BOOKS bookstore = T-money pickup',
            hall='Millennium Hall', med='Medical Korea info', flower='FLOPORT florist', shop2='Travel Mate & Book Store = T-money pickup', opp='Opposite counter F',
            up='Come up from 1F arrivals (where exactly: not confirmed)', mid='Middle', info='Info desk 24h', kiosk='Tax refund kiosk', gates='Departure entrances', counters='Check-in counters A–N',
            note='Shop position follows the official "opposite check-in counter F"'),
 'ja': dict(t1='第1ターミナル 1階', t2='第2ターミナル 3階(出国)', here='到着出口(A〜F)から出てきます', go='出入口番号7(真ん中)の方へ', shop1='書店 K BOOKS = T-money受け取り',
            hall='ミレニアムホール(Millennium Hall)', med='Medical Korea 案内センター', flower='花屋 FLOPORT', shop2='Travel Mate & Book Store = T-money受け取り', opp='Fカウンターの向かい',
            up='1階の到着ロビーから3階へ(上がる場所は未確認)', mid='真ん中', info='案内デスク 24時間', kiosk='税金還付キオスク', gates='出国場', counters='チェックインカウンター A〜N',
            note='店の位置は公式案内「Fチェックインカウンターの向かい」に基づきます'),
 'zh-tw': dict(t1='第1航廈 1樓', t2='第2航廈 3樓(出境)', here='從入境出口(A〜F)出來', go='往出入口7號(中間)走', shop1='書店 K BOOKS = 領T-money處',
            hall='Millennium Hall', med='Medical Korea 服務中心', flower='花店 FLOPORT', shop2='Travel Mate & Book Store = 領T-money處', opp='F櫃台對面',
            up='從1樓入境大廳上到3樓(上來的位置未確認)', mid='中間', info='服務台 24小時', kiosk='退稅機', gates='出境口', counters='報到櫃台 A〜N',
            note='店的位置依官方說明「F報到櫃台對面」'),
}
STAR = '#f59e0b'

def star(x, y, r=20):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5; rr = r if i % 2 == 0 else r * 0.45
        pts.append(f'{x + rr * math.cos(a):.0f},{y + rr * math.sin(a):.0f}')
    return f"<polygon points='{' '.join(pts)}' fill='{STAR}' stroke='#92400e' stroke-width='2'/>"

def t1(lab):
    W, H = 780, 450
    o = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' aria-label='{esc(lab['t1'])}: {esc(lab['shop1'])}'>",
         f"<rect width='{W}' height='{H}' rx='18' fill='#f7f7f5'/>", T(28, 46, lab['t1'], 30, INK, '700', 'start')]
    cy = -750
    pts_o = [arcpt(1060, x, cy) for x in range(16, 765, 10)]; pts_i = [arcpt(920, x, cy) for x in range(46, 735, 10)]
    d = 'M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts_o) + ' L' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in reversed(pts_i)) + 'Z'
    o.append(f"<path d='{d}' fill='#e3e6eb'/>")
    ex = {}
    for i in range(14):
        x = 58 + i * (664 / 13); _, y = arcpt(950, x, cy); ex[i + 1] = (x, y)
    halls = {}
    for i, c in enumerate('ABCDEF'):
        x = 90 + i * (600 / 5); _, y = arcpt(1025, x, cy); halls[c] = (x, y)
    x7, y7 = ex[7]
    sx, sy = 390, (y7 + halls['C'][1]) / 2 + 6  # Millennium Hall: the middle of the 1F hall, between the exits and arrival exits C/D
    for c in 'AF':
        hx, hy = halls[c]
        o.append(f"<path d='M{hx:.0f},{hy-26:.0f} Q{(hx+sx)/2:.0f},{sy+4:.0f} {sx + (30 if c=='F' else -30):.0f},{sy:.0f}' fill='none' stroke='{RED}' stroke-width='6' stroke-dasharray='12 8' stroke-linecap='round'/>")
    for n, (x, y) in ex.items():
        o.append(badge(x, y, str(n), '#f59e0b' if n == 7 else '#16a3b8'))
    for c, (x, y) in halls.items():
        o.append(f"<circle cx='{x:.0f}' cy='{y:.0f}' r='24' fill='#2563eb'/>" + T(x, y + 9, c, 26, '#fff', '700'))
    o.append(star(sx, sy, 24))
    x8, y8 = ex[8]
    o.append(f"<line x1='{x8:.0f}' y1='{y8-18:.0f}' x2='{x8+40:.0f}' y2='{y8-60:.0f}' stroke='#be185d' stroke-width='2.5'/>" + T(x8 + 44, y8 - 64, lab['flower'] + ' (8)', 18, '#be185d', '700', 'start'))
    o.append(f"<line x1='{x7:.0f}' y1='{y7-18:.0f}' x2='{x7-40:.0f}' y2='{y7-60:.0f}' stroke='#7c3aed' stroke-width='2.5'/>" + T(x7 - 44, y7 - 64, lab['med'] + ' (7)', 18, '#7c3aed', '700', 'end'))
    hy = halls['C'][1]
    o.append(T(390, hy + 62, '★ ' + lab['shop1'], 24, '#92400e', '800'))
    o.append(T(390, hy + 90, lab['hall'] + ' · 07:00–21:00', 20, GREY, '700'))
    o.append(T(390, hy + 130, '▲ ' + lab['here'], 22, RED, '700'))
    o.append(T(390, hy + 160, '→ ' + lab['go'], 22, RED, '700'))
    o.append('</svg>'); return ''.join(o)

def t2(lab):
    W, H = 780, 520
    o = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' aria-label='{esc(lab['t2'])}: {esc(lab['shop2'])}'>",
         f"<rect width='{W}' height='{H}' rx='18' fill='#f7f7f5'/>", T(28, 46, lab['t2'], 30, INK, '700', 'start')]
    # x positions taken from the official plan image (img_bg_traffic_t2.jpg, 1480 px wide), mapped to 40..740
    X = lambda ox: 40 + (ox - 260) * 700 / 920
    Y = lambda x: 190 + 64 * ((x - 390) / 350) ** 2   # the row bows up in the middle, as on the official plan
    band_t = ' L'.join(f'{x},{Y(x) - 70:.0f}' for x in range(20, 761, 20)); band_b = ' L'.join(f'{x},{Y(x) + 70:.0f}' for x in range(760, 19, -20))
    o.append(f"<path d='M{band_t} L{band_b}Z' fill='#e3e6eb'/>")
    off = {'N': 287, 'M': 328, 'L': 395, 'K': 466, 'J': 545, 'H': 621, 'G': 689, 'F': 789, 'E': 853, 'D': 932, 'C': 1008, 'B': 1083, 'A': 1149}
    pos = {c: X(v) for c, v in off.items()}
    lx = dict(pos); lx['N'] -= 8; lx['M'] += 6
    for c, x in pos.items():
        y = Y(x); hl = c == 'F'
        o.append(f"<rect x='{x-13:.0f}' y='{y-42:.0f}' width='26' height='58' rx='5' fill='{'#f59e0b' if hl else '#9ca3af'}'/>")
        o.append(f"<circle cx='{lx[c]:.0f}' cy='{y+34:.0f}' r='15' fill='{'#b45309' if hl else '#6b7280'}'/>" + T(lx[c], y + 41, c, 19, '#fff', '700'))
    xm = (pos['G'] + pos['F']) / 2
    o.append(T(xm, Y(xm) - 60, lab['mid'], 20, GREY, '700') + f"<path d='M{xm:.0f},{Y(xm)-52:.0f} L{xm:.0f},{Y(xm)+30:.0f}' stroke='{GREY}' stroke-width='2' stroke-dasharray='4 5'/>")
    gates = {'2D': 400, '2C': 463, '2B': 527, '2A': 589, '1D': 885, '1C': 948, '1B': 1010, '1A': 1073}
    for nm, ox in gates.items():
        x = X(ox); y = Y(x) - 104
        o.append(f"<rect x='{x-17:.0f}' y='{y:.0f}' width='34' height='52' rx='4' fill='#3b2f80'/>" + T(x, y + 32, nm, 15, '#fde047', '700'))
    o.append(T(X(980), Y(X(980)) - 116, lab['gates'], 18, GREY, '700'))
    xf = pos['F']; yf = Y(xf)
    o.append(f"<line x1='{xf:.0f}' y1='{yf+52:.0f}' x2='{xf:.0f}' y2='{yf+108:.0f}' stroke='#92400e' stroke-width='3'/>")
    o.append(star(xf, yf + 128, 26))
    o.append(T(xf, yf + 176, lab['shop2'], 22, '#92400e', '800'))
    o.append(T(xf, yf + 204, '(' + lab['opp'] + ')', 20, '#92400e', '700'))
    xd = pos['D']; yd = Y(xd)
    o.append(f"<line x1='{xd:.0f}' y1='{yd+50:.0f}' x2='{xd+60:.0f}' y2='{yd+84:.0f}' stroke='#7c3aed' stroke-width='2.5'/>" + T(W - 18, yd + 104, 'ⓘ ' + lab['info'] + ' (D)', 18, '#7c3aed', '700', 'end'))
    o.append(T(390, H - 86, lab['up'], 22, INK, '700'))
    o.append(T(390, H - 54, lab['kiosk'] + ': F · ' + lab['counters'], 19, GREY, '700'))
    o.append(T(390, H - 24, lab['note'], 17, GREY, '600'))
    o.append('</svg>'); return ''.join(o)

if __name__ == '__main__':
    root = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'fig')
    for lang, lab in L.items():
        os.makedirs(os.path.join(root, lang), exist_ok=True)
        open(os.path.join(root, lang, 'airport-tmoney-t1.svg'), 'w').write(t1(lab))
        open(os.path.join(root, lang, 'airport-tmoney-t2.svg'), 'w').write(t2(lab))
    print('ok')
