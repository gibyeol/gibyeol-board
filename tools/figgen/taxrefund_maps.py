# Schematic wayfinding maps: Incheon T1 / T2 departures, customs check (kiosk) -> refund counter / machine.
# Facts only, redrawn by Nadri (not to scale, counter letters in order only). Fact sources opened 2026-11-26:
#  airport.kr ap_ko/1008 facility list (T1 3F landside 내국세환급 kiosks 24h near check-in B, E, J, L; T1 3F airside
#  staffed counter near gate 28; concourse 3F centre 부가세환급; T2 3F landside kiosks near check-in F, G; T2 3F airside
#  staffed counters near gate 249 and east near gate 270, 07:00-21:30),
#  airport.kr ap_ko/898 내국세환급 procedure (kiosk first; customs desk if flagged; T1 counter near gate 28 07:00-22:00;
#  machines 24h near gate 28 and concourse 3F centre next to the pharmacy; T2 counter/machines opposite gate 250, near 253),
#  VISITKOREA Comprehensive Tax Refund Guide (customs T1 near E and J counters 3F; T2 near F and G counters 3F).
# usage: python3 tools/figgen/taxrefund_maps.py -> static/fig/<lang>/tax-refund-t1map.svg, tax-refund-t2map.svg
import os, html
L = {
 'ko': dict(t1='1터미널: 세관 확인 → 환급', a='① 3층 출국장(보안검색 전)', look='체크인 카운터 위 알파벳을 봐요',
            kiosk='내국세환급 키오스크 24시간', customs='세관(E·J 근처)', down='출국장 → 보안검색 → 출국심사',
            b='② 3층 면세구역', g28='28번 게이트 근처', g28d='환급 창구 07:00~22:00|무인 환급기 24시간',
            conc='탑승동(101~132번)이면: 3층 중앙 약국 옆 무인 환급기 24시간',
            note='개략도(축척 아님). 알파벳 순서만 맞아요. 인천공항 시설 안내·내국세환급 안내, 비짓코리아 기준',
            t2='2터미널: 세관 확인 → 환급', t2look='체크인 카운터 F·G 근처', t2customs='세관(F·G 근처)',
            t2g1='번 게이트 근처', t2g2='번 게이트 근처(동편)', t2gd='환급 창구 07:00~21:30',
            t2alt='공항 안내 페이지에는 250번 맞은편·253번 근처로 적혀 있어요. 무인 환급기는 24시간'),
 'en': dict(t1='T1: customs check, then refund', a='1 · 3F departures (before security)', look='Read the letter above each check-in row',
            kiosk='Tax refund kiosk, 24h', customs='Customs (near E and J)', down='Departure hall → security → passport control',
            b='2 · 3F duty-free area', g28='Near gate 28', g28d='Refund counter 07:00–22:00|Refund machines 24h',
            conc='Gates 101–132 (Concourse): refund machine next to the pharmacy, 3F centre, 24h',
            note='Schematic, not to scale; letters in order only. From airport.kr facility and refund pages and VISITKOREA',
            t2='T2: customs check, then refund', t2look='Near check-in rows F and G', t2customs='Customs (near F and G)',
            t2g1='Near this gate', t2g2='Near this gate (east)', t2gd='Refund counter 07:00–21:30',
            t2alt='The airport refund page gives opposite gate 250 and near 253 instead. Refund machines 24h'),
 'ja': dict(t1='第1ターミナル: 税関確認 → 還付', a='① 3階 出国フロア(保安検査の前)', look='チェックインカウンター上のアルファベットを見ます',
            kiosk='内国税還付キオスク 24時間', customs='税関(E・J付近)', down='出国場 → 保安検査 → 出国審査',
            b='② 3階 免税エリア', g28='28番ゲート付近', g28d='還付窓口 07:00〜22:00|無人還付機 24時間',
            conc='搭乗棟(101〜132番)なら: 3階中央 薬局横の無人還付機 24時間',
            note='略図(縮尺なし)。アルファベットの順番のみ正確。仁川空港の施設案内・内国税還付案内、VISITKOREAより',
            t2='第2ターミナル: 税関確認 → 還付', t2look='チェックインカウンターF・G付近', t2customs='税関(F・G付近)',
            t2g1='番ゲート付近', t2g2='番ゲート付近(東側)', t2gd='還付窓口 07:00〜21:30',
            t2alt='空港の還付案内ページでは250番の向かい・253番付近。無人還付機は24時間'),
 'zh-tw': dict(t1='第1航廈: 海關確認 → 退稅', a='① 3樓 出境大廳(安檢前)', look='看報到櫃台上方的英文字母',
            kiosk='退稅自助機 24小時', customs='海關(E・J附近)', down='出境口 → 安檢 → 出境審查',
            b='② 3樓 免稅區', g28='28號登機門附近', g28d='退稅櫃台 07:00〜22:00|無人退稅機 24小時',
            conc='在搭乘棟(101〜132號): 3樓中央 藥局旁無人退稅機 24小時',
            note='示意圖(非比例),只有字母順序正確。依仁川機場設施資料・退稅說明、VISITKOREA',
            t2='第2航廈: 海關確認 → 退稅', t2look='報到櫃台 F・G 附近', t2customs='海關(F・G附近)',
            t2g1='號登機門附近', t2g2='號登機門附近(東側)', t2gd='退稅櫃台 07:00〜21:30',
            t2alt='機場退稅頁寫的是 250號對面・253號附近。無人退稅機 24小時'),
}
FONT = "font-family='Pretendard,Noto Sans KR,Noto Sans JP,Noto Sans TC,system-ui,sans-serif'"
INK, GREY, RED, NAVY, PURP = '#1f2328', '#5b6470', '#c0392b', '#1d2b53', '#6d28d9'
LANG = ['ko']
def esc(s): return html.escape(s)
def T(x, y, s, size=16, fill=INK, w='600', anchor='middle'):
    return f"<text x='{x:.0f}' y='{y:.0f}' font-size='{size}' font-weight='{w}' fill='{fill}' text-anchor='{anchor}' {FONT}>{esc(s)}</text>"
def wrap(s, n):
    if '|' in s: return s.split('|')
    if LANG[0] in ('ja', 'zh-tw', 'ko'):
        if ' ' in s and LANG[0] == 'ko':
            pass
        else:
            n = max(6, int(n * 0.8))
            return [s[i:i+n] for i in range(0, len(s), n)]
    out, cur = [], ''
    for w in s.split(' '):
        if len(cur) + len(w) + 1 > n and cur: out.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    out.append(cur); return out
def lines(x, y, s, n, size=15, fill=INK, w='600', anchor='middle', lh=20):
    ls = wrap(s, n)
    return ''.join(T(x, y + i*lh, t, size, fill, w, anchor) for i, t in enumerate(ls)), len(ls)

def counters(o, y, letters, kiosks, customs, lang):
    # row of check-in rows; '…' = rows left out
    n = len(letters); x0, x1 = 26, 374; step = (x1 - x0) / n
    for i, c in enumerate(letters):
        cx = x0 + step * (i + .5)
        if c == '…':
            o.append(T(cx, y + 22, '…', 18, GREY, '700')); continue
        col = RED if c in kiosks else NAVY
        o.append(f"<rect x='{cx-16:.0f}' y='{y}' width='32' height='30' rx='6' fill='{col}'/>" + T(cx, y + 22, c, 17, '#fff', '700'))
        if c in customs:
            o.append(f"<rect x='{cx-16:.0f}' y='{y+36}' width='32' height='8' rx='4' fill='{PURP}'/>")

def landside(o, l, lang, y, letters, kiosks, customs, look, cust):
    n = 40 if lang == 'en' else 22
    top = y
    body = []
    yy = y + 26; body.append(T(28, yy, l['a'], 17, INK, '700', 'start'))
    s, k = lines(200, yy + 26, look, n, 16, GREY, '600'); body.append(s); yy += 26 + 20 * k
    counters(body, yy, letters, kiosks, customs, lang); yy += 58
    body.append(f"<rect x='30' y='{yy-14}' width='22' height='18' rx='4' fill='{RED}'/>")
    s, k = lines(60, yy, l['kiosk'], 34 if lang == 'en' else 18, 16, RED, '700', 'start'); body.append(s); yy += 20 * k + 8
    body.append(f"<rect x='30' y='{yy-10}' width='22' height='8' rx='4' fill='{PURP}'/>")
    s, k = lines(60, yy, cust, 34 if lang == 'en' else 18, 16, PURP, '700', 'start'); body.append(s); yy += 20 * (k - 1) + 16
    o.append(f"<rect x='16' y='{top}' width='368' height='{yy-top}' rx='10' fill='#fff' stroke='#c9ccd1'/>"); o.extend(body)
    yy += 8
    s, k = lines(200, yy + 24, l['down'], 40 if lang == 'en' else 22, 16, NAVY, '700')
    o.append(f"<rect x='16' y='{yy}' width='368' height='{16 + 20*k}' rx='10' fill='#eef2f7'/>"); o.append(s)
    return yy + 16 + 20 * k + 8

def t1(l, lang):
    W = 400
    o = [T(16, 32, l['t1'], 18, INK, '700', 'start')]
    y = landside(o, l, lang, 46, ['A', '…', 'B', '…', 'E', '…', 'J', '…', 'L', '…', 'N'], {'B', 'E', 'J', 'L'}, {'E', 'J'}, l['look'], l['customs'])
    y0 = y; body = []
    body.append(T(28, y0 + 26, l['b'], 17, INK, '700', 'start'))
    body.append(f"<path d='M44,{y0+96} Q200,{y0+46} 356,{y0+96}' fill='none' stroke='#d5d9df' stroke-width='22' stroke-linecap='round'/>")
    for gno, x in [(50, 64), (28, 200), (2, 336)]:
        yy = y0 + 96 - 50 * (1 - ((x - 200) / 156) ** 2) * 0.98
        col = RED if gno == 28 else NAVY
        body.append(f"<rect x='{x-16:.0f}' y='{yy-14:.0f}' width='32' height='26' rx='5' fill='{col}'/>" + T(x, yy + 6, str(gno), 16, '#fff', '700'))
    yy = y0 + 104
    body.append(T(200, yy, l['g28'], 18, RED, '700'))
    s, k = lines(200, yy + 24, l['g28d'], 40, 16, INK, '600'); body.append(s); yy += 24 + 20 * k
    s, k = lines(200, yy + 6, l['conc'], 40 if lang == 'en' else 22, 16, GREY, '600'); body.append(s); yy += 6 + 20 * k
    o.append(f"<rect x='16' y='{y0}' width='368' height='{yy-y0}' rx='10' fill='#fff' stroke='#c9ccd1'/>"); o.extend(body)
    s, k = lines(200, yy + 24, l['note'], 44 if lang == 'en' else 24, 16, GREY, '500'); o.append(s); H = yy + 24 + 20 * k
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H:.0f}' role='img' aria-label='{esc(l['t1'])}'>"
            f"<rect width='{W}' height='{H:.0f}' rx='14' fill='#f7f7f5'/>" + ''.join(o) + '</svg>')

def t2(l, lang):
    W = 400
    o = [T(16, 32, l['t2'], 18, INK, '700', 'start')]
    y = landside(o, l, lang, 46, ['…', 'F', 'G', '…'], {'F', 'G'}, {'F', 'G'}, l['t2look'], l['t2customs'])
    y0 = y; body = []
    body.append(T(28, y0 + 26, l['b'], 17, INK, '700', 'start'))
    yy = y0 + 42; hmax = 0
    for i, (gno, lab) in enumerate([('249', l['t2g1']), ('270', l['t2g2'])]):
        x = 28 + i * 180
        body.append(f"<rect x='{x}' y='{yy}' width='50' height='28' rx='6' fill='{RED}'/>" + T(x + 25, yy + 20, gno, 16, '#fff', '700'))
        s, k = lines(x + 58, yy + 20, lab, 14 if lang == 'en' else 7, 16, RED, '700', 'start'); body.append(s); hmax = max(hmax, k)
    yy += 20 * hmax + 22
    s, k = lines(200, yy, l['t2gd'], 40, 16, INK, '600'); body.append(s); yy += 20 * k
    s, k = lines(200, yy + 4, l['t2alt'], 40 if lang == 'en' else 22, 16, GREY, '600'); body.append(s); yy += 4 + 20 * k
    o.append(f"<rect x='16' y='{y0}' width='368' height='{yy-y0}' rx='10' fill='#fff' stroke='#c9ccd1'/>"); o.extend(body)
    s, k = lines(200, yy + 24, l['note'], 44 if lang == 'en' else 24, 16, GREY, '500'); o.append(s); H = yy + 24 + 20 * k
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H:.0f}' role='img' aria-label='{esc(l['t2'])}'>"
            f"<rect width='{W}' height='{H:.0f}' rx='14' fill='#f7f7f5'/>" + ''.join(o) + '</svg>')

if __name__ == '__main__':
    root = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'fig')
    out = os.environ.get('OUT') or root
    for lang, l in L.items():
        LANG[0] = lang
        os.makedirs(os.path.join(out, lang), exist_ok=True)
        open(os.path.join(out, lang, 'tax-refund-t1map.svg'), 'w').write(t1(l, lang))
        open(os.path.join(out, lang, 'tax-refund-t2map.svg'), 'w').write(t2(l, lang))
        print(lang, 'ok')
