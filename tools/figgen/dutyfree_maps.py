# Schematic wayfinding maps: Incheon T1 / T2, departure immigration -> duty-free pickup counter.
# Facts only, redrawn by Nadri (not to scale). Fact sources opened 2026-11-26:
#  Hyundai Duty Free bcaInfo.do + en shoppingGuide.do (counter positions: T1 west 4F opposite gate 43; concourse near
#  gate 119 4F after shuttle train; T2 west: escalator opposite Korean Traditional Culture Center (West) near gate 225
#  down to 2F; T2 east: towards gate 274, opposite KTCC (East), escalator down to 2F),
#  Shilla Duty Free deliverypointinfo (same; concourse: escalator next to gate 119),
#  airport.kr ap_ko/1008 facility list (T1 3F airside info desks 24h near gates 25 and 29; centre = gate 28;
#  KTCC West near gate 29; Matina Lounge (West) 4F near gate 43).
# usage: python3 tools/figgen/dutyfree_maps.py -> static/fig/<lang>/duty-free-t1map.svg, duty-free-t2map.svg
import os, html
L = {
 'ko': dict(t1='1터미널 출국: 인도장 찾아가기', here='출국심사를 지나면|3층 면세구역.|게이트 번호|표지판을 봐요', walk='게이트 번호가 커지는 쪽(서편)으로',
            g='번', info='안내데스크|24시간(3층)', ktcc='한국전통문화센터 서관', up='43번 맞은편 위층(4층)', pick='인도장',
            lounge='4층 마티나|라운지(서편) 근처', conc='탑승동(101~132번 게이트)이라면:|셔틀트레인 → 119번 옆 에스컬레이터 → 4층',
            w='서', e='동', note='개략도(축척 아님). 현대·신라면세점 인도장 안내, 인천공항 시설 안내 기준',
            t2='2터미널 출국: 인도장 찾아가기', t2here='출국심사를 지나면 3층 면세구역', t2w='서편 인도장', t2e='동편 인도장',
            t2wd='225번 게이트 근처|한국전통문화센터|(서관) 맞은편|에스컬레이터로|2층', t2ed='274번 게이트 쪽|한국전통문화센터|(동관) 맞은편|에스컬레이터로|2층',
            t2note='어느 쪽인지는 교환권에 적혀 있어요'),
 'en': dict(t1='T1 departures: to the pickup counter', here='After passport control: 3F duty-free area. Look for gate-number signs', walk='Walk where gate numbers go up (west)',
            g='', info='Info desk 24h (3F)', ktcc='Korean Traditional Culture Center (West)', up='Upper floor (4F), opposite 43', pick='Pickup counter',
            lounge='Near Matina Lounge (West), 4F', conc='Gates 101–132 (Concourse): shuttle train → escalator next to gate 119 → 4F counter',
            w='W', e='E', note='Schematic, not to scale. From Hyundai/Shilla pickup guides and airport.kr',
            t2='T2 departures: to the pickup counter', t2here='After passport control: 3F duty-free area', t2w='West counter', t2e='East counter',
            t2wd='Near gate 225: escalator opposite the Korean Traditional Culture Center (West), down to 2F', t2ed='Towards gate 274: escalator opposite the Korean Traditional Culture Center (East), down to 2F',
            t2note='Your voucher says which counter'),
 'ja': dict(t1='第1ターミナル出国: 引き渡し場へ', here='出国審査を通ると|3階 免税エリア。|ゲート番号の|表示を見ます', walk='ゲート番号が大きい方(西側)へ',
            g='番', info='案内デスク|24時間(3階)', ktcc='韓国伝統文化|センター 西館', up='43番の向かい、上の階(4階)', pick='引き渡し場',
            lounge='4階|マティナラウンジ|(西側)の近く', conc='搭乗棟(101〜132番)なら: シャトル|トレイン → 119番横のエスカレーター → 4階',
            w='西', e='東', note='略図(縮尺なし)。現代・新羅免税店の引き渡し案内、|仁川空港の施設案内より',
            t2='第2ターミナル出国: 引き渡し場へ', t2here='出国審査を通ると3階 免税エリア', t2w='西側の引き渡し場', t2e='東側の引き渡し場',
            t2wd='225番ゲート近く|韓国伝統文化|センター(西館)|向かいの|エスカレーターで|2階へ', t2ed='274番ゲート方面|韓国伝統文化|センター(東館)|向かいの|エスカレーターで|2階へ',
            t2note='どちらかは引換券に書いてあります'),
 'zh-tw': dict(t1='第1航廈出境: 走到提貨處', here='過了出境審查|是3樓免稅區,|看登機門|號碼指標', walk='往登機門號碼變大的方向(西側)',
            g='號', info='服務台|24小時(3樓)', ktcc='韓國傳統文化|中心 西館', up='43號對面的樓上(4樓)', pick='提貨處',
            lounge='4樓|Matina 貴賓室|(西側)附近', conc='在 101〜132 號登機門(搭乘棟):|接駁列車 → 119號旁電扶梯 → 4樓',
            w='西', e='東', note='示意圖(非比例)。|依現代・新羅免稅店提貨說明、仁川機場設施資料',
            t2='第2航廈出境: 走到提貨處', t2here='過了出境審查是3樓免稅區', t2w='西側提貨處', t2e='東側提貨處',
            t2wd='225號登機門附近|韓國傳統文化|中心(西館)|對面的電扶梯|下到2樓', t2ed='往274號登機門方向|韓國傳統文化|中心(東館)|對面的電扶梯|下到2樓',
            t2note='哪一個寫在兌換券上'),
}
FONT = "font-family='Pretendard,Noto Sans KR,Noto Sans JP,Noto Sans TC,system-ui,sans-serif'"
INK, GREY, RED, NAVY, TEAL, PURP = '#1f2328', '#5b6470', '#c0392b', '#1d2b53', '#2f8f8a', '#6d28d9'
def esc(s): return html.escape(s)
def T(x, y, s, size=16, fill=INK, w='600', anchor='middle'):
    return f"<text x='{x:.0f}' y='{y:.0f}' font-size='{size}' font-weight='{w}' fill='{fill}' text-anchor='{anchor}' {FONT}>{esc(s)}</text>"
LANG = ['ko']
def wrap(s, n):
    if '|' in s: return s.split('|')
    if LANG[0] in ('ja', 'zh-tw'): n = max(6, int(n * 0.8))
    # naive wrap for CJK/latin: split on spaces if latin, else by char count
    if ' ' in s and len(s) > n and LANG[0] not in ('ja', 'zh-tw'):
        out, cur = [], ''
        for w in s.split(' '):
            if len(cur) + len(w) + 1 > n and cur: out.append(cur); cur = w
            else: cur = (cur + ' ' + w).strip()
        out.append(cur); return out
    return [s[i:i+n] for i in range(0, len(s), n)]
def lines(x, y, s, n, size=15, fill=INK, w='600', anchor='middle', lh=20):
    return ''.join(T(x, y + i*lh, t, size, fill, w, anchor) for i, t in enumerate(wrap(s, n)))

def t1(l, lang):
    W, H = 400, 610; n = 34 if lang in ('en',) else 20
    o = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' aria-label='{esc(l['t1'])}'>",
         f"<rect width='{W}' height='{H}' rx='14' fill='#f7f7f5'/>", T(16, 32, l['t1'], 18, INK, '700', 'start')]
    # concourse note (top)
    o.append(f"<rect x='16' y='46' width='368' height='70' rx='10' fill='#eef2f7' stroke='#c9ccd1'/>")
    o.append(lines(200, 76, l['conc'], 44 if lang == 'en' else 27, 15 if lang != 'ko' else 16, NAVY, '700', lh=24))
    # 4F band (upper) and 3F arc (gates)
    o.append(f"<rect x='16' y='122' width='368' height='92' rx='10' fill='#fff' stroke='#c9ccd1'/>")
    o.append(T(28, 142, '4F', 15, GREY, '700', 'start'))
    o.append(f"<rect x='34' y='150' width='150' height='56' rx='10' fill='{RED}'/>")
    o.append(T(109, 174, l['pick'], 17, '#fff', '700'))
    o.append(lines(109, 196, l['up'], 22 if lang == 'en' else 13, 12, '#fff', '600', lh=14) if False else T(109, 196, '↑ 43', 15, '#fff', '700'))
    o.append(lines(286, 160, '← ' + l['lounge'], 18 if lang == 'en' else 10, 15, GREY, '700', lh=19))
    # 3F airside
    o.append(f"<rect x='16' y='226' width='368' height='244' rx='10' fill='#fff' stroke='#c9ccd1'/>")
    o.append(T(28, 246, '3F', 15, GREY, '700', 'start'))
    o.append(f"<path d='M300,318 Q200,316 132,300 L132,212' fill='none' stroke='{RED}' stroke-width='5' stroke-dasharray='10 7' stroke-linecap='round'/>")
    o.append(f"<path d='M122,218 L132,200 L142,218Z' fill='{RED}'/>")
    o.append(f"<rect x='232' y='310' width='128' height='16' rx='8' fill='{RED}' opacity='0.85'/>")
    o.append(lines(296, 350, l['here'], 19 if lang == 'en' else 11, 15, RED, '700', lh=19))
    gates = [(50, 60), (43, 104), (29, 178), (28, 214), (25, 250), (11, 312), (2, 356)]
    o.append("<path d='M44,300 Q200,250 360,300' fill='none' stroke='#d5d9df' stroke-width='22' stroke-linecap='round'/>")
    for gno, x in gates:
        y = 300 - 50 * (1 - ((x - 200) / 160) ** 2) * 0.98
        col = RED if gno == 43 else NAVY
        o.append(f"<rect x='{x-15:.0f}' y='{y-13:.0f}' width='30' height='24' rx='5' fill='{col}'/>" + T(x, y + 5, str(gno), 14, '#fff', '700'))
    o.append(T(30, 268, l['w'], 18, INK, '700', 'start') + T(370, 268, l['e'], 18, INK, '700', 'end'))
    # landmarks at 29
    o.append(f"<line x1='178' y1='272' x2='178' y2='376' stroke='{PURP}' stroke-width='2'/>")
    o.append(lines(140, 394, l['info'], 18 if lang == 'en' else 9, 15, PURP, '700', lh=19))
    ni = len(wrap(l['info'], 18 if lang == 'en' else 9))
    o.append(lines(140, 394 + 19 * ni + 2, l['ktcc'], 22 if lang == 'en' else 11, 14, GREY, '600', lh=17))

    o.append(f"<rect x='16' y='482' width='368' height='{60 if lang == 'en' else 44}' rx='10' fill='#fdecea'/>")
    o.append(lines(200, 510, '← ' + l['walk'], 36 if lang == 'en' else 22, 17, RED, '700', lh=22))
    o.append(lines(200, 566, l['note'], 46 if lang == 'en' else 27, 13, GREY, '500', lh=16))
    o.append('</svg>'); return ''.join(o)

def t2(l, lang):
    W, H = 400, 420; n = 40 if lang == 'en' else 22
    o = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' aria-label='{esc(l['t2'])}'>",
         f"<rect width='{W}' height='{H}' rx='14' fill='#f7f7f5'/>", T(16, 32, l['t2'], 18, INK, '700', 'start')]
    o.append(f"<rect x='16' y='48' width='368' height='40' rx='10' fill='#fff' stroke='#c9ccd1'/>" + T(200, 74, '3F · ' + l['t2here'], 16, NAVY, '700'))
    for i, (tt, dd, gno) in enumerate([(l['t2w'], l['t2wd'], '225'), (l['t2e'], l['t2ed'], '274')]):
        x = 16 + i * 188
        o.append(f"<rect x='{x}' y='100' width='180' height='250' rx='10' fill='#fff' stroke='#c9ccd1'/>")
        o.append(f"<rect x='{x+12}' y='112' width='54' height='28' rx='6' fill='{NAVY}'/>" + T(x + 39, 132, gno, 16, '#fff', '700'))
        o.append(T(x + 76, 132, '↓ 2F', 16, RED, '700', 'start'))
        o.append(lines(x + 90, 166, tt, 16, 17, RED, '700'))
        o.append(lines(x + 90, 194, dd, 19 if lang == 'en' else 10, 15, INK, '600', lh=19))
    o.append(T(200, 374, l['t2note'], 16, GREY, '700'))
    o.append(lines(200, 398, l['note'], 46 if lang == 'en' else 27, 13, GREY, '500', lh=16))
    o.append('</svg>'); return ''.join(o)

if __name__ == '__main__':
    root = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'fig')
    for lang, l in L.items():
        LANG[0] = lang
        os.makedirs(os.path.join(root, lang), exist_ok=True)
        open(os.path.join(root, lang, 'duty-free-t1map.svg'), 'w').write(t1(l, lang))
        open(os.path.join(root, lang, 'duty-free-t2map.svg'), 'w').write(t2(l, lang))
        print(lang, 'ok')
