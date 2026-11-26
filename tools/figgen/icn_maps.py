# Schematic wayfinding maps for Incheon Airport T1 (1F -> B1 transportation center) and T2 (1F -> B1).
# Facts only, redrawn by Nadri. Fact sources (opened 2026-11-26): airport.kr ap_en/1512 (AREX guide floor plans
# train-map2/3), ap_ko/986 (taxi stands), ap_ko/1008 (facility list: info desks, bus desks, roaming centres).
# usage: python3 tools/figgen/icn_maps.py  -> static/fig/<lang>/airport-to-seoul-t1map.svg, -t2map.svg
import math, os, html
L = {
 'ko': dict(f1='1층 입국장', b1='지하 1층 교통센터', here='여기서 나와요', go='가운데로 걸어가 지하 1층으로', reg='일반열차', exp='직통열차',
            info='안내데스크 24시간', bus='공항버스 안내', roam='로밍센터', taxi='인터내셔널택시 4C', e='동', w='서',
            t1='1터미널', t2='2터미널', ex='출입구', busw='버스 대기실', gl='지방 01~10', gs='서울 11~35', gg='경기 36~45', down='입국장에서 지하 1층으로 내려가요', gates='회색 칸 = 버스 타는 곳 번호'),
 'en': dict(f1='1F arrival halls', b1='B1 Transportation Center', here='You come out here', go='Walk to the middle, go down to B1', reg='Regular train', exp='Express train',
            info='Info desk 24h', bus='Airport bus desk', roam='Roaming centre', taxi='International Taxi 4C', e='E', w='W',
            t1='Terminal 1', t2='Terminal 2', ex='Exit', busw='Bus waiting room', gl='Local 01–10', gs='Seoul 11–35', gg='Gyeonggi 36–45', down='Go down to B1', gates='Grey = bus stop numbers'),
 'ja': dict(f1='1階 到着ロビー', b1='地下1階 交通センター', here='ここから出てきます', go='真ん中へ歩いて地下1階へ', reg='一般列車', exp='直通列車',
            info='案内デスク 24時間', bus='空港バス案内', roam='ローミング', taxi='国際タクシー 4C', e='東', w='西',
            t1='第1ターミナル', t2='第2ターミナル', ex='出入口', busw='バス待合室', gl='地方 01〜10', gs='ソウル 11〜35', gg='京畿 36〜45', down='到着ロビーから地下1階へ下ります', gates='灰色 = バス乗り場の番号'),
 'zh-tw': dict(f1='1樓 入境大廳', b1='地下1樓 交通中心', here='你從這裡出來', go='走到中間,下到地下1樓', reg='普通列車', exp='直達車',
            info='服務台 24小時', bus='機場巴士服務台', roam='漫遊中心', taxi='International Taxi 4C', e='東', w='西',
            t1='第1航廈', t2='第2航廈', ex='出入口', busw='巴士候車室', gl='地方 01〜10', gs='首爾 11〜35', gg='京畿 36〜45', down='從入境大廳下到地下1樓', gates='灰色 = 巴士乘車處編號'),
}
FONT = "font-family='Pretendard,Noto Sans KR,Noto Sans JP,Noto Sans TC,system-ui,sans-serif'"
NAVY, TEAL, RED, INK, GREY = '#1d2b53', '#2f8f8a', '#d64545', '#1f2328', '#6b7280'
def esc(s): return html.escape(s)
def T(x, y, s, size=13, fill=INK, w='500', anchor='middle'):
    return f"<text x='{x:.0f}' y='{y:.0f}' font-size='{size}' font-weight='{w}' fill='{fill}' text-anchor='{anchor}' {FONT}>{esc(s)}</text>"

def arcpt(r, x, cy=-560):
    th = math.asin((x - 390) / r); return x, cy + r * math.cos(th)

def badge(x, y, s, fill='#16a3b8', w=34, fs=20):
    return f"<rect x='{x-w/2:.0f}' y='{y-w/2:.0f}' width='{w}' height='{w}' rx='7' fill='{fill}'/>" + T(x, y + fs * 0.36, s, fs, '#fff', '700')

def t1(lab):
    W, H = 780, 640; o = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' aria-label='{esc(lab['t1'])}: {esc(lab['f1'])} → {esc(lab['b1'])}'>",
         f"<rect width='{W}' height='{H}' rx='18' fill='#f7f7f5'/>", T(28, 46, lab['t1'], 30, INK, '700', 'start')]
    o.append("<rect x='200' y='62' width='380' height='150' rx='16' fill='#fff' stroke='#c9ccd1' stroke-width='2'/>")
    o.append(T(390, 100, lab['b1'], 26, INK, '700'))
    o.append(f"<rect x='216' y='120' width='170' height='50' rx='10' fill='{NAVY}'/>" + T(301, 153, lab['reg'], 24, '#fff', '700'))
    o.append(f"<rect x='394' y='120' width='170' height='50' rx='10' fill='{TEAL}'/>" + T(479, 153, lab['exp'], 24, '#fff', '700'))
    o.append(T(390, 200, '◀ ' + lab['e'] + '  ·  ' + lab['w'] + ' ▶', 20, GREY, '600'))
    pts_o = [arcpt(1060, x) for x in range(16, 765, 10)]; pts_i = [arcpt(920, x) for x in range(46, 735, 10)]
    d = 'M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts_o) + ' L' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in reversed(pts_i)) + 'Z'
    o.append(f"<path d='{d}' fill='#e3e6eb'/>")
    o.append(T(30, arcpt(920, 50)[1] - 30, lab['f1'], 22, GREY, '700', 'start'))
    ex = {}
    for i in range(14):
        x = 58 + i * (664 / 13); _, y = arcpt(950, x); ex[i + 1] = (x, y); o.append(badge(x, y, str(i + 1)))
    halls = {}
    for i, c in enumerate('ABCDEF'):
        x = 90 + i * (600 / 5); _, y = arcpt(1025, x); halls[c] = (x, y)
        o.append(f"<circle cx='{x:.0f}' cy='{y:.0f}' r='24' fill='#2563eb'/>" + T(x, y + 9, c, 26, '#fff', '700'))
    o.append(T(28, H - 20, lab['e'], 26, INK, '700', 'start') + T(W - 28, H - 20, lab['w'], 26, INK, '700', 'end'))
    mx, my = arcpt(950, 390)
    o.append(f"<path d='M{halls['B'][0]:.0f},{halls['B'][1]-30:.0f} Q{mx-80:.0f},{my+20:.0f} {mx:.0f},{my-26:.0f} M{halls['E'][0]:.0f},{halls['E'][1]-30:.0f} Q{mx+80:.0f},{my+20:.0f} {mx:.0f},{my-26:.0f} M{mx:.0f},{my-28:.0f} L390,226' fill='none' stroke='{RED}' stroke-width='6' stroke-dasharray='12 8' stroke-linecap='round'/>")
    o.append(f"<path d='M378,236 L390,214 L402,236Z' fill='{RED}'/>")
    hy = halls['C'][1]
    o.append(T(390, hy + 58, '▲ ' + lab['here'] + ' (A–F)', 24, RED, '700'))
    o.append(T(390, hy + 92, '→ ' + lab['go'], 24, RED, '700'))
    def tag(n, s, col, dy, anchor='middle'):
        x, y = ex[n]; y -= 18
        return f"<line x1='{x:.0f}' y1='{y:.0f}' x2='{x:.0f}' y2='{y+dy:.0f}' stroke='{col}' stroke-width='2.5'/>" + T(x - 4 if anchor == 'start' else x, y + dy - 6, s, 20, col, '700', anchor)
    o.append(tag(5, 'ⓘ ' + lab['info'], '#7c3aed', -78))
    o.append(tag(9, lab['bus'], '#b45309', -40, 'start'))
    o.append(tag(10, 'ⓘ ' + lab['info'], '#7c3aed', -78))
    o.append(tag(11, lab['bus'], '#b45309', -116))
    for c in 'AF': o.append(T(halls[c][0], halls[c][1] + 50, lab['roam'], 20, GREY, '700'))
    o.append('</svg>'); return ''.join(o)

def t2(lab):
    W, H = 780, 640; o = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' role='img' aria-label='{esc(lab['t2'])}: {esc(lab['f1'])} → {esc(lab['b1'])}'>",
         f"<rect width='{W}' height='{H}' rx='18' fill='#f7f7f5'/>", T(28, 46, lab['t2'], 30, INK, '700', 'start')]
    o.append("<rect x='28' y='84' width='724' height='86' rx='43' fill='#e3e6eb'/>")
    o.append(T(390, 146, lab['f1'], 24, GREY, '700'))
    for i, n in enumerate(range(10, 0, -1)):
        x = 66 + i * (648 / 9); o.append(badge(x, 84, str(n)))
    o.append(f"<path d='M390,178 L390,222' stroke='{RED}' stroke-width='6' stroke-dasharray='12 8'/><path d='M378,218 L390,240 L402,218Z' fill='{RED}'/>")
    o.append(T(410, 214, lab['down'], 22, RED, '700', 'start'))
    o.append("<rect x='110' y='250' width='560' height='330' rx='16' fill='#fff' stroke='#c9ccd1' stroke-width='2'/>")
    o.append(T(390, 286, lab['b1'], 26, INK, '700'))
    o.append(f"<rect x='200' y='302' width='380' height='46' rx='10' fill='{TEAL}'/>" + T(390, 334, lab['exp'], 24, '#fff', '700'))
    o.append(f"<rect x='200' y='356' width='380' height='46' rx='10' fill='{NAVY}'/>" + T(390, 388, lab['reg'], 24, '#fff', '700'))
    o.append("<rect x='220' y='414' width='340' height='48' rx='12' fill='#4b5563'/>" + T(390, 446, lab['busw'], 24, '#fff', '700'))
    o.append("<rect x='126' y='302' width='62' height='262' rx='10' fill='#9ca3af'/><rect x='592' y='302' width='62' height='262' rx='10' fill='#9ca3af'/>")
    o.append("<rect x='200' y='474' width='380' height='90' rx='10' fill='#9ca3af'/>")
    o.append(T(390, 528, lab['gs'], 24, '#fff', '700'))
    o.append(T(157, 606, lab['gg'], 20, INK, '700') + T(623, 606, lab['gl'], 20, INK, '700'))
    o.append(T(28, H - 10, lab['e'], 26, INK, '700', 'start') + T(W - 28, H - 10, lab['w'], 26, INK, '700', 'end'))
    o.append(T(390, 632, lab['gates'], 20, GREY, '700'))
    o.append('</svg>'); return ''.join(o)

if __name__ == '__main__':
    root = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'fig')
    for lang, lab in L.items():
        os.makedirs(os.path.join(root, lang), exist_ok=True)
        open(os.path.join(root, lang, 'airport-to-seoul-t1map.svg'), 'w').write(t1(lab))
        open(os.path.join(root, lang, 'airport-to-seoul-t2map.svg'), 'w').write(t2(lab))
    print('ok')
