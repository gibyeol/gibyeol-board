# Phone-first redesign of 12 figures x 4 languages. Output: figs-phone/out/<lang>/<slug>-<n>.svg
import os, sys, re, unicodedata
from xml.sax.saxutils import escape as E

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
FONT = 'system-ui, -apple-system, &quot;Noto Sans KR&quot;, &quot;Noto Sans JP&quot;, &quot;Noto Sans TC&quot;, sans-serif'
INK, RED, PAPER, MUTED, RULE, WHITE, SOFT = '#16151a', '#b8392f', '#f4f0e6', '#5f5b55', '#c9c1b2', '#ffffff', '#e9e2d3'
W = 400
PAD = 16
MINFS = 16

# ---------------------------------------------------------------- text metrics
def cw(ch):
    if ch == ' ':
        return 0.30
    ea = unicodedata.east_asian_width(ch)
    if ea in ('W', 'F'):
        return 1.0
    if ch in '.,:;·\'’|!il()[]':
        return 0.32
    if ch in '“”"‘':
        return 0.40
    if ch in '—–~〜→↔×':
        return 0.75 if ch not in '—' else 0.9
    if ch == '₩':
        return 0.75
    if ch.isdigit():
        return 0.60
    if ch.isupper():
        return 0.68
    return 0.56

def tw(s, size, bold=False):
    return sum(cw(c) for c in s) * size * (1.07 if bold else 1.0)

NOSTART = set('、。,,.・)」』!?:;ー〜~%)』】:')
NOEND = set('(「『【(')

def wrap(s, size, width, bold=False):
    """Explicit '\n' breaks first; then wrap by spaces (if the text has spaces) or by characters."""
    out = []
    for para in s.split('\n'):
        if tw(para, size, bold) <= width:
            out.append(para)
            continue
        if ' ' in para and not re.search(r'[\u3040-\u30ff\u3400-\u9fff]', para):
            words = para.split(' ')
            cur = ''
            for wd in words:
                cand = wd if not cur else cur + ' ' + wd
                if tw(cand, size, bold) <= width or not cur:
                    cur = cand
                else:
                    out.append(cur)
                    cur = wd
            if cur:
                out.append(cur)
            # any word still too long -> char wrap
            fixed = []
            for ln in out[len(out) - 0:]:
                fixed.append(ln)
        else:
            # tokens: runs of latin letters/digits stay together; CJK chars break anywhere
            toks = re.findall(r'[A-Za-z0-9₩,.\-+/]+|.', para)
            cur = ''
            for tk in toks:
                cand = cur + tk
                if tw(cand, size, bold) <= width or not cur:
                    cur = cand
                else:
                    if tk[0] in NOSTART and len(cur) > 1:
                        out.append(cur[:-1])
                        cur = cur[-1] + tk
                    elif cur[-1] in NOEND and len(cur) > 1:
                        out.append(cur[:-1])
                        cur = cur[-1] + tk
                    else:
                        out.append(cur)
                        cur = tk
            if cur:
                out.append(cur)
    return out

def lh(size):
    return round(size * 1.38)

def T(x, y, s, size=16, fill=INK, bold=False, anchor='start'):
    assert size >= MINFS, (s, size)
    w = ' font-weight="bold"' if bold else ''
    return f'<text x="{x:g}" y="{y:g}" font-size="{size}" fill="{fill}"{w} text-anchor="{anchor}">{E(s)}</text>\n'

def block(x, top, lines, size=16, fill=INK, bold=False, anchor='start'):
    """lines already wrapped; returns (svg, height). Baseline at top + size."""
    out = ''
    y = top
    for ln in lines:
        out += T(x, round(y + size * 1.0), ln, size, fill, bold, anchor)
        y += lh(size)
    return out, y - top

def R(x, y, w, h, fill=WHITE, stroke=RULE, sw=2, rx=12):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" fill="{fill}"{st}/>\n'

def arrow(x1, y1, x2, y2, color=INK):
    return f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{color}" stroke-width="2.5" marker-end="url(#ah)"/>\n'

def num(cx, cy, n, fill=RED):
    return f'<circle cx="{cx}" cy="{cy}" r="15" fill="{fill}"/>\n' + T(cx, cy + 6, str(n), 17, WHITE, True, 'middle')

DEFS = f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>\n'

def doc(title, body, h):
    h = round(h)
    title = title.replace('\n', ' ')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" role="img" aria-label="{E(title)}" font-family="{FONT}">\n'
            f'<title>{E(title)}</title>\n<rect width="{W}" height="{h}" rx="16" fill="{PAPER}"/>\n{DEFS}{body}</svg>\n')

def title_block(title, sub=None):
    s, h = block(PAD + 4, 18, wrap(title, 21, W - 2 * PAD - 8, True), 21, INK, True)
    y = 18 + h
    if sub:
        s2, h2 = block(PAD + 4, y + 2, wrap(sub, 16, W - 2 * PAD - 8), 16, MUTED)
        s += s2
        y += h2 + 2
    return s, y + 14

def write(lang, name, title, body, h):
    d = os.path.join(OUT, lang)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(doc(title, body, h))

# ---------------------------------------------------------------- generic: decision tree (vertical spine)
def tree(title, nodes, spine_label, spine_color, footer=None):
    """nodes: list of dicts:
       {'q': text, 'ex': optional note under the box}
       {'branch': answer text, 'label': text, 'style': 'pick'|'soft', 'sub': optional red note}
       {'end': text, 'style': 'pick'|'redfill'}
    Between a question and the next question/end the spine carries spine_label."""
    body, y = title_block(title)
    SX = 40               # spine x
    BX = 124              # branch box x
    BW = W - PAD - BX     # branch box width
    for i, n in enumerate(nodes):
        if 'q' in n:
            lines = wrap(n['q'], 17, W - 2 * PAD - 28, True)
            h = len(lines) * lh(17) + 26
            body += R(PAD, y, W - 2 * PAD, h, SOFT, RULE, 2)
            s, _ = block(W / 2, y + 13, lines, 17, INK, True, 'middle')
            body += s
            qbottom = y + h
            y += h
            if n.get('ex'):
                s, hh = block(SX + 16, y + 8, wrap(n['ex'], 16, W - SX - 16 - PAD), 16, MUTED)
                body += s
                y += hh + 8
            spine_top = qbottom
        elif 'branch' in n:
            st = n.get('style', 'pick')
            lines = wrap(n['branch'], 17, BW - 24, st == 'pick')
            h = len(lines) * lh(17) + 24
            top = y + 14
            if st == 'pick':
                body += R(BX, top, BW, h, WHITE, RED, 3)
            else:
                body += R(BX, top, BW, h, SOFT, RULE, 2)
            s, _ = block(BX + BW / 2, top + 12, lines, 17, INK, st == 'pick', 'middle')
            body += s
            mid = top + h / 2
            body += f'<line x1="{SX}" y1="{spine_top}" x2="{SX}" y2="{mid:g}" stroke="{INK}" stroke-width="2.5"/>\n'
            body += arrow(SX, mid, BX - 2, mid)
            body += T((SX + BX) / 2 + 4, mid - 9, n['label'], 16, n.get('label_color', RED), True, 'middle')
            y = top + h
            if n.get('sub'):
                s, hh = block(BX + BW / 2, y + 6, wrap(n['sub'], 16, BW), 16, RED, False, 'middle')
                body += s
                y += hh + 6
            spine_top = mid
        elif 'end' in n:
            st = n.get('style', 'pick')
            gap = 52
            top = y + gap
            body += arrow(SX, spine_top, SX, top - 2)
            body += T(SX + 12, top - gap / 2 + 6, spine_label, 16, spine_color, True)
            lines = wrap(n['end'], 18, W - 2 * PAD - 24, True)
            h = len(lines) * lh(18) + 26
            if st == 'redfill':
                body += R(PAD, top, W - 2 * PAD, h, RED, None)
                s, _ = block(W / 2, top + 13, lines, 18, WHITE, True, 'middle')
            else:
                body += R(PAD, top, W - 2 * PAD, h, WHITE, RED, 3)
                s, _ = block(W / 2, top + 13, lines, 18, INK, True, 'middle')
            body += s
            y = top + h
            if n.get('sub'):
                s, hh = block(W / 2, y + 8, wrap(n['sub'], 16, W - 2 * PAD - 16), 16, MUTED, False, 'middle')
                body += s
                y += hh + 8
        # connector into the next question
        if i + 1 < len(nodes) and 'q' in nodes[i + 1] and 'q' not in n:
            gap = 52
            body += arrow(SX, spine_top, SX, y + gap - 2)
            body += T(SX + 12, y + gap / 2 + 6, spine_label, 16, spine_color, True)
            y += gap
    if footer:
        y += 18
        kind, payload = footer
        if kind == 'box':
            lines = wrap(payload, 16, W - 2 * PAD - 24)
            h = len(lines) * lh(16) + 22
            body += R(PAD, y, W - 2 * PAD, h, SOFT, None)
            s, _ = block(W / 2, y + 11, lines, 16, INK, False, 'middle')
            body += s
            y += h
        else:  # 'note': (head, body, bullets)
            head, txt, bullets = payload
            body += f'<line x1="{PAD}" y1="{y}" x2="{W-PAD}" y2="{y}" stroke="{RULE}" stroke-width="2" stroke-dasharray="6 6"/>\n'
            y += 12
            s, hh = block(PAD + 4, y, wrap(head, 17, W - 2 * PAD - 8, True), 17, INK, True)
            body += s; y += hh + 2
            s, hh = block(PAD + 4, y, wrap(txt, 16, W - 2 * PAD - 8), 16, MUTED)
            body += s; y += hh + 4
            for b in bullets:
                body += f'<circle cx="{PAD+10}" cy="{y+11}" r="3.5" fill="{RED}"/>\n'
                s, hh = block(PAD + 22, y, wrap(b, 16, W - 2 * PAD - 30), 16, INK)
                body += s; y += hh
    return body, y + 18

# ---------------------------------------------------------------- generic: step list
def steps(title, items, icon_fn=None, footer_boxes=(), warn=None, group=None):
    """items: dicts {t, sub(list of str), hl(bool), red_num(bool), icon}
       group: (start_index, label) - adds a red label above that step and a bracket to the end."""
    body, y = title_block(title)
    TX = 72 if not icon_fn else 138
    TWID = W - PAD - 14 - TX
    gy0 = None
    for i, it in enumerate(items):
        if i > 0:
            body += arrow(42, y + 1, 42, y + 17)
            y += 20
        if group and i == group[0]:
            s, hh = block(PAD + 2, y, wrap(group[1], 16, W - 2 * PAD), 16, RED, True)
            body += s
            y += hh + 4
            gy0 = y
        tl = wrap(it['t'], 18, TWID, True)
        sl = []
        for sb in it.get('sub', []):
            sl += wrap(sb, 16, TWID)
        th = len(tl) * lh(18) + len(sl) * lh(16)
        h = max(th + 26, 60 if not icon_fn else 84)
        hl = it.get('hl')
        body += R(PAD, y, W - 2 * PAD, h, WHITE, RED if hl else RULE, 3 if hl else 2)
        body += num(42, round(y + h / 2), i + 1, RED if it.get('red_num', True) else INK)
        if icon_fn:
            body += icon_fn(it.get('icon'), 100, y + h / 2)
        ty = y + (h - th) / 2
        s, hh = block(TX, ty, tl, 18, INK, True)
        body += s
        s, _ = block(TX, ty + hh, sl, 16, MUTED)
        body += s
        y += h
    if group and gy0 is not None:
        body += f'<line x1="{W-PAD+0}" y1="{gy0}" x2="{W-PAD}" y2="{y}" stroke="{RED}" stroke-width="0"/>\n' if False else ''
    for head, txt in footer_boxes:
        y += 16
        hl_ = wrap(head, 17, W - 2 * PAD - 28, True)
        bl_ = wrap(txt, 16, W - 2 * PAD - 28)
        h = len(hl_) * lh(17) + len(bl_) * lh(16) + 26
        body += R(PAD, y, W - 2 * PAD, h, SOFT, RULE, 2)
        s, hh = block(PAD + 14, y + 13, hl_, 17, INK, True)
        body += s
        s, _ = block(PAD + 14, y + 13 + hh, bl_, 16, INK)
        body += s
        y += h
    if warn:
        y += 16
        lines = wrap(warn, 17, W - 2 * PAD - 28, True)
        h = len(lines) * lh(17) + 24
        body += R(PAD, y, W - 2 * PAD, h, WHITE, RED, 2)
        s, _ = block(W / 2, y + 12, lines, 17, RED, True, 'middle')
        body += s
        y += h
    return body, y + 18

# ---------------------------------------------------------------- icons for subway-2
def subway_icon(kind, cx, cy):
    cx = round(cx); cy = round(cy)
    if kind == 'gate':
        return (f'<rect x="{cx-19}" y="{cy-14}" width="12" height="36" rx="3" fill="{INK}"/>'
                f'<rect x="{cx+7}" y="{cy-14}" width="12" height="36" rx="3" fill="{INK}"/>'
                f'<rect x="{cx-8}" y="{cy-22}" width="16" height="12" rx="3" fill="{RED}"/>\n')
    if kind == 'line4':
        return f'<circle cx="{cx}" cy="{cy}" r="22" fill="{INK}"/>\n' + T(cx, cy + 8, '4', 22, WHITE, True, 'middle')
    if kind == 'l25':
        return (f'<circle cx="{cx-14}" cy="{cy}" r="15" fill="{INK}"/><circle cx="{cx+16}" cy="{cy}" r="15" fill="{MUTED}"/>\n'
                + T(cx - 14, cy + 6, '2', 17, WHITE, True, 'middle') + T(cx + 16, cy + 6, '5', 17, WHITE, True, 'middle'))
    return ''

# ================================================================ DATA
SUB1 = {
 'ko': dict(title='서울 지하철 결제 수단 고르기', yes='예', no='아니요',
   q1='서울 안에서만 하루 3번 이상,\n3일 이상 다니나요?', a1='기후동행카드\n단기권',
   a3='티머니, 또는\n와우패스(티머니 기능 포함)', a3s='와우패스의 티머니 잔액은 따로 충전',
   nh='카드도 현금도 아직 없다면?', nb='새 무인기(Visa·Mastercard)에서 1회용 승차권:',
   nl=['한 번에 +100원', '보증금 500원', '버스 환승 안 됨']),
 'en': dict(title='How to pay for the Seoul subway', yes='Yes', no='No',
   q1='3+ rides a day for 3+ days,\nall inside Seoul?', a1='Climate Card\nshort-term pass',
   a3='T-money, or\nWOWPASS (T-money inside)', a3s='WOWPASS: its T-money balance\nis topped up separately',
   nh='No card and no cash yet?', nb='Single ticket at a new machine (Visa/Mastercard):',
   nl=['+₩100 a ride', '₩500 deposit', 'No bus transfer']),
 'ja': dict(title='ソウル地下鉄の支払い方法', yes='はい', no='いいえ',
   q1='ソウル市内だけで1日3回以上、\n3日以上乗る?', a1='Climate Card\n短期券',
   a3='T-money、または\nWOWPASS(T-money機能付き)', a3s='WOWPASSのT-money残高は別にチャージ',
   nh='カードも現金もまだない?', nb='新しい券売機(Visa・Mastercard)で1回用乗車券:',
   nl=['1回+100ウォン', '保証金500ウォン', 'バス乗り換え不可']),
 'zh-tw': dict(title='首爾地鐵付款方式怎麼選', yes='是', no='否',
   q1='只在首爾市內,一天3趟以上,\n連續3天以上?', a1='氣候同行卡\n短期券',
   a3='T-money,或\nWOWPASS(內建T-money)', a3s='WOWPASS的T-money餘額要分開儲值',
   nh='還沒有卡也沒現金?', nb='在新售票機(Visa・Mastercard)買單程票:',
   nl=['每趟+100韓元', '押金500韓元', '不能轉乘公車']),
}

SUB2 = {
 'ko': dict(title='한 번 탈 때 순서', steps=[('탈 때 태그', '단말기에 잔액 표시'), ('노선 번호', '그다음 방향 확인'), ('역 안 환승', '개찰구 다시 안 나가요'), ('내릴 때 태그', '요금은 거리로 계산')],
   n1=('버스로 갈아탈 땐', '같은 카드로 30분 안에\n(밤 9시~아침 7시는 1시간) 승차'), n2=('1회용 승차권이라면', '나와서 보증금 환급기에 넣으면 500원 환급')),
 'en': dict(title='One trip, step by step', steps=[('Tap in', 'Balance shows on the reader'), ('Line number', 'Then check the direction'), ('Change inside', 'No extra gate'), ('Tap out', 'Fare is set by distance')],
   n1=('Bus next?', 'Board within 30 min (60 min, 9 p.m.–7 a.m.) with the same card'), n2=('Single ticket?', 'Put it in the Deposit Refund machine: ₩500 back')),
 'ja': dict(title='1回の乗車の流れ', steps=[('乗るときタッチ', '画面に残高表示'), ('路線番号', '次に方向を確認'), ('駅の中で乗換', '改札は出ません'), ('降りるときタッチ', '運賃は距離で計算')],
   n1=('バスに乗り継ぐなら', '同じカードで30分以内\n(夜9時〜朝7時は60分)に乗車'), n2=('1回用乗車券なら', '改札を出て保証金払い戻し機へ。\n500ウォン返金')),
 'zh-tw': dict(title='搭一趟的步驟', steps=[('進站嗶卡', '感應機顯示餘額'), ('看路線號碼', '再確認方向'), ('站內轉乘', '不用再出閘門'), ('出站嗶卡', '票價依距離計算')],
   n1=('要接公車的話', '用同一張卡30分鐘內\n(晚上9點~早上7點為60分鐘)上車'), n2=('用單程票的話', '出站後放進押金退還機,退回500韓元')),
}

SUB3 = {
 'ko': dict(title='교통카드 vs 1회용 승차권(어른)', cols=('티머니·와우패스', '1회용 승차권'), rows=[
   ('기본요금(10km)', '1,550원', '1,650원', None), ('보증금', '—', '500원,\n나가서 환급', None),
   ('버스 환승 할인', '돼요\n(30분 안)', '안 돼요', None), ('쓸 수 있는 곳', '지하철·버스', '수도권\n도시철도만', None),
   ('충전', '역 충전기에서\n현금', '탈 때마다\n새로 구매', '(와우패스는 앱도 가능)')]),
 'en': dict(title='Card vs single ticket (adult)', cols=('T-money / WOWPASS', 'Single ticket'), rows=[
   ('Base fare (10 km)', '₩1,550', '₩1,650', None), ('Deposit', '—', '₩500, refunded\nat the exit', None),
   ('Bus transfer discount', 'Yes, within\n30 min', 'No', None), ('Where it works', 'Subway\nand buses', 'Seoul-area\nrail only', None),
   ('Top-up', 'Cash at\nstation machines', 'Buy a new\none each ride', '(WOWPASS:\nalso in app)')]),
 'ja': dict(title='交通カードと1回用乗車券(大人)', cols=('T-money・\nWOWPASS', '1回用乗車券'), rows=[
   ('基本運賃(10km)', '1,550ウォン', '1,650ウォン', None), ('保証金', '—', '500ウォン、\n出口で返金', None),
   ('バス乗り換え割引', 'あり\n(30分以内)', 'なし', None), ('使える範囲', '地下鉄・バス', '首都圏の\n鉄道のみ', None),
   ('チャージ', '駅のチャージ機で\n現金', '毎回\n買い直し', '(WOWPASSは\nアプリも可)')]),
 'zh-tw': dict(title='交通卡 vs 單程票(成人)', cols=('T-money・\nWOWPASS', '單程票'), rows=[
   ('基本票價(10公里)', '1,550韓元', '1,650韓元', None), ('押金', '—', '500韓元,\n出站退還', None),
   ('公車轉乘優惠', '有\n(30分鐘內)', '沒有', None), ('可搭乘範圍', '地鐵、公車', '只限首都圈\n鐵路', None),
   ('儲值', '車站儲值機\n付現金', '每趟\n重新購買', '(WOWPASS\n也可用App)')]),
}

BLUE, GREEN, YELLOW = '#2f5d9e', '#3d7a4a', '#d9a521'
BUS1 = {
 'ko': dict(title='서울 버스 색깔 한눈에', foot='어른, 교통카드 요금', rows=[
   ('파랑', BLUE, WHITE, '간선', '외곽과 도심을 길게', '1,500원'),
   ('초록', GREEN, WHITE, '지선·마을', '동네와 간선버스·지하철을 이어요', '1,500원(마을 1,200원)'),
   ('노랑', YELLOW, INK, '순환', '도심 안을 돌아요', '1,400원'),
   ('빨강', RED, WHITE, '광역', '수도권과 도심 연결', '3,000원'),
   ('N…', INK, WHITE, '심야버스', '지하철이 끊긴 밤에', '2,500원')]),
 'en': dict(title='Seoul bus colours at a glance', foot='Adult fares with a transport card', rows=[
   ('Blue', BLUE, WHITE, 'Trunk', 'Long routes across the city', '₩1,500'),
   ('Green', GREEN, WHITE, 'Branch / village', 'Links neighbourhoods to trunk buses and the subway', '₩1,500 (village ₩1,200)'),
   ('Yellow', YELLOW, INK, 'Circular', 'Loops in the centre', '₩1,400'),
   ('Red', RED, WHITE, 'Wide-area', 'Seoul ↔ wider metro area', '₩3,000'),
   ('N…', INK, WHITE, 'Night bus', 'Late night, after the subway', '₩2,500')]),
 'ja': dict(title='ソウルのバス、色で見分ける', foot='大人・交通カード運賃', rows=[
   ('青', BLUE, WHITE, '幹線', '市内を長く結ぶ', '1,500ウォン'),
   ('緑', GREEN, WHITE, '支線・マウル', '地域と幹線バス・地下鉄をつなぐ', '1,500ウォン(マウル1,200)'),
   ('黄', YELLOW, INK, '循環', '中心部を回る', '1,400ウォン'),
   ('赤', RED, WHITE, '広域', '首都圏と中心部', '3,000ウォン'),
   ('N…', INK, WHITE, '深夜バス', '地下鉄が終わった後', '2,500ウォン')]),
 'zh-tw': dict(title='首爾公車,看顏色就懂', foot='成人、交通卡票價', rows=[
   ('藍', BLUE, WHITE, '幹線', '長距離穿越市區', '1,500韓元'),
   ('綠', GREEN, WHITE, '支線・社區', '連接社區與幹線公車、地鐵', '1,500韓元(社區1,200)'),
   ('黃', YELLOW, INK, '循環', '在市中心繞行', '1,400韓元'),
   ('紅', RED, WHITE, '廣域', '連接首都圈與市區', '3,000韓元'),
   ('N…', INK, WHITE, '深夜公車', '地鐵收班後', '2,500韓元')]),
}

BUS2 = {
 'ko': dict(title='탈 때 한 번, 내릴 때 한 번', steps=[('탑승', ''), ('카드 태그', '단말기에'), ('이동', '지도로 확인'), ('다시 태그', '내리기 전에'), ('하차', '')], warn='내릴 때 안 찍으면 환승 할인이 사라져요'),
 'en': dict(title='Every ride: tap in, tap out', steps=[('Board', ''), ('Tap card', 'on the reader'), ('Ride', 'follow the map'), ('Tap again', 'as you get off'), ('Get off', '')], warn='Skip the second tap and your transfer discount is gone'),
 'ja': dict(title='乗るときと降りるとき、2回タッチ', steps=[('乗車', ''), ('カードをタッチ', '読み取り機に'), ('移動', '地図で確認'), ('もう一度タッチ', '降りる前に'), ('降車', '')], warn='降車タッチを忘れると\n乗り換え割引が消えます'),
 'zh-tw': dict(title='上車刷一次,下車再刷一次', steps=[('上車', ''), ('刷卡', '刷卡機'), ('搭乘', '看地圖'), ('再刷一次', '下車前'), ('下車', '')], warn='下車沒刷卡,轉乘優惠就沒了'),
}

BUS3 = {
 'ko': dict(title='내린 뒤 환승 인정 시간', rows=[('아침 7시~밤 9시', '30분', 0.5), ('밤 9시~아침 7시', '1시간', 1.0)], off='하차 태그',
   main='이 안에 다음 버스·지하철을 타면 환승', notes=['최대 4번 환승', '같은 노선 재탑승은 환승 아님']),
 'en': dict(title='Transfer window\nafter you get off', rows=[('7 a.m.–9 p.m.', '30 min', 0.5), ('9 p.m.–7 a.m.', '60 min', 1.0)], off='Tap off',
   main='Next bus or subway\ncounts as a transfer', notes=['Up to 4 transfers', 'Same route again does not count']),
 'ja': dict(title='降りてから乗り換えできる時間', rows=[('7時〜21時', '30分', 0.5), ('21時〜翌7時', '60分', 1.0)], off='降車タッチ',
   main='この間に次のバス・地下鉄に乗れば\n乗り換え', notes=['乗り換えは4回まで', '同じ路線の再乗車は対象外']),
 'zh-tw': dict(title='下車後的轉乘時限', rows=[('07:00~21:00', '30分鐘', 0.5), ('21:00~隔天07:00', '60分鐘', 1.0)], off='下車刷卡',
   main='時限內搭下一班公車或地鐵算轉乘', notes=['最多轉乘4次', '同一路線再上車不算轉乘']),
}

DA1 = {
 'ko': dict(title='한국 다이소 가격 6가지:\n₩500~₩5,000', sub='최저가와 최고가',
   pts=[('₩500', '최저가'), ('₩5,000', '최고가')],
   f1='가격은 모두 6가지\n(아성다이소, 2026년 11월).', f2='가격표를 확인하세요.'),
 'en': dict(title='Daiso Korea: six prices,\n₩500 to ₩5,000', sub='Lowest and highest price',
   pts=[('₩500', 'Lowest price'), ('₩5,000', 'Top price')],
   f1='Six price points in all\n(Asung Daiso, Nov 2026).', f2='Check the tag.'),
 'ja': dict(title='韓国ダイソーの6つの価格:\n500〜5,000ウォン', sub='最低価格と最高価格(単位:ウォン)',
   pts=[('500', '最低価格'), ('5,000', '最高価格')],
   f1='価格は全部で6つ\n(アソン・ダイソー、2026年11月)。', f2='値札を確認。'),
 'zh-tw': dict(title='韓國大創 6 種價格:\n500 至 5,000 韓元', sub='最低價與最高價(單位:韓元)',
   pts=[('500', '最低價'), ('5,000', '最高價')],
   f1='價格共 6 種\n(亞城大創,2026 年 11 月)。', f2='請看標價。'),
}
PRICES = [500, 1000, 2000, 5000]

DA2 = {
 'ko': dict(title='명동역점 다이소, 4단계', group='택스리펀드를 받으려면', steps=[
   ('층별 안내', ['영·일·중 안내', '2~3개 층 고르기']), ('뷰티는 2층', ['화제 상품은 품절되기도']),
   ('한 번에 계산', ['영수증마다 ₩15,000 이상']), ('여권', ['결제할 때 보여 주기'])]),
 'en': dict(title='Myeongdong Station Daiso:\n4 steps', group='For a tax refund', steps=[
   ('Floor guide', ['EN · JA · ZH', 'pick 2–3 floors']), ('Beauty: 2F', ['viral items can sell out']),
   ('One purchase', ['each receipt ₩15,000+']), ('Passport', ['show it when you pay'])]),
 'ja': dict(title='明洞駅店ダイソーを4ステップで', group='免税を受けるなら', steps=[
   ('フロアガイド', ['英・日・中あり', '2〜3階に絞る']), ('コスメは2階', ['話題の商品は売り切れも']),
   ('会計は1回に', ['レシート1枚ごとに15,000ウォン以上']), ('パスポート', ['支払いのときに提示'])]),
 'zh-tw': dict(title='明洞站店大創,4 步驟逛完', group='要退稅的話', steps=[
   ('樓層指南', ['有英日中文', '縮到 2~3 層']), ('美妝在 2 樓', ['爆紅商品可能賣完']),
   ('一次結帳', ['每張收據滿 15,000 韓元']), ('護照', ['付款時出示正本'])]),
}

DA3 = {
 'ko': dict(title='다이소에서 택스리펀드?', yes='예', no='아니요',
   q1='이 매장에 “Tax Free”나 “Tax Refund” 표시가 있나요?', n1='그냥 결제',
   q2='영수증 한 장이 ₩15,000 이상인가요?', ex='₩5,000 × 3 = ₩15,000', n2='더 담거나\n그냥 결제', n2s='영수증마다 따로 계산',
   end='결제할 때\n실물 여권 제시', foot='규정·한도: 택스리펀드 페이지'),
 'en': dict(title='Tax refund at Daiso?', yes='Yes', no='No',
   q1='“Tax Free” or “Tax Refund” sign at this branch?', n1='Pay normally',
   q2='One receipt ₩15,000 or more?', ex='₩5,000 × 3 = ₩15,000', n2='Add items, or\npay normally', n2s='Each receipt counts alone',
   end='Show your passport\nwhen you pay', foot='Rules and limits: our tax refund page'),
 'ja': dict(title='ダイソーで免税できる?', yes='はい', no='いいえ',
   q1='この店に「Tax Free」か\n「Tax Refund」の表示がある?', n1='通常どおり支払い',
   q2='レシート1枚で15,000ウォン以上?', ex='5,000ウォン × 3 = 15,000ウォン', n2='買い足すか\n通常どおり支払い', n2s='レシートは1枚ずつ判定',
   end='支払いのときに\nパスポート原本を提示', foot='ルール・上限:免税のページ'),
 'zh-tw': dict(title='在大創可以退稅嗎?', yes='是', no='否',
   q1='這家店有「Tax Free」或\n「Tax Refund」標示嗎?', n1='照常付款',
   q2='同一張收據滿 15,000 韓元?', ex='5,000 韓元 × 3 = 15,000 韓元', n2='再加購,\n或照常付款', n2s='每張收據分開計算',
   end='付款時\n出示護照正本', foot='規定與上限:見退稅頁面'),
}

MARKS = [[2, 1, 0, 0], [1, 2, 0, 2], [1, 2, 2, 0], [0, 2, 0, 0]]  # 2 best, 1 also good, 0 none
SH1 = {
 'ko': dict(title='어디서 무엇을, 언제', cats=['뷰티', '패션', 'K-팝 굿즈', '팝업'],
   areas=[('명동', '이른 시간'), ('성수', '평일'), ('홍대', '늦은 오후~저녁'), ('동대문', '저녁~자정')], best='가장 잘 맞음', good='이것도 괜찮음', time='가기 좋은 시간'),
 'en': dict(title='What to buy where, and when', cats=['Beauty', 'Fashion', 'K-pop goods', 'Pop-ups'],
   areas=[('Myeongdong', 'Earlier in the day'), ('Seongsu', 'Weekday'), ('Hongdae', 'Late afternoon–evening'), ('Dongdaemun', 'Evening–midnight')], best='Best for', good='Also good', time='Best time'),
 'ja': dict(title='どこで何を、いつ買う?', cats=['コスメ', '服', 'K-POP', 'ポップアップ'],
   areas=[('明洞', '早めの時間'), ('聖水', '平日'), ('弘大', '夕方〜夜'), ('東大門', '夕方〜深夜0時')], best='いちばん向いている', good='これも向いている', time='いい時間帯'),
 'zh-tw': dict(title='哪裡買什麼、什麼時候去', cats=['美妝', '服飾', 'K-POP周邊', '快閃店'],
   areas=[('明洞', '早點去'), ('聖水', '平日'), ('弘大', '傍晚到晚上'), ('東大門', '傍晚到午夜')], best='最適合', good='也不錯', time='最佳時段'),
}

SH2 = {
 'ko': dict(title='2호선 위의 네 쇼핑 지역', sub='개념도, 축척 아님', river='한강', line='2호선(순환선)',
   st={'md': ('명동', '뷰티'), 'ss': ('성수', '새 브랜드·팝업'), 'hd': ('홍대', '젊은 패션'), 'dd': ('동대문', '밤 옷 쇼핑')}),
 'en': dict(title='Four shopping areas on Line 2', sub='Schematic, not to scale', river='Han River', line='Line 2 (loop)',
   st={'md': ('Myeongdong', 'Beauty'), 'ss': ('Seongsu', 'New brands, pop-ups'), 'hd': ('Hongdae', 'Young fashion'), 'dd': ('Dongdaemun', 'Clothes at night')}),
 'ja': dict(title='2号線沿いの4つの買い物エリア', sub='イメージ図・縮尺は不正確', river='漢江', line='2号線(環状線)',
   st={'md': ('明洞', 'コスメ'), 'ss': ('聖水', '新ブランド・\nポップアップ'), 'hd': ('弘大', '若いファッション'), 'dd': ('東大門', '夜の服探し')}),
 'zh-tw': dict(title='2號線上的四個逛街區', sub='示意圖,非實際比例', river='漢江', line='2號線(環狀線)',
   st={'md': ('明洞', '美妝'), 'ss': ('聖水', '新品牌、快閃店'), 'hd': ('弘大', '年輕服飾'), 'dd': ('東大門', '晚上買衣服')}),
}

SH3 = {
 'ko': dict(title='2호선 한나절 동선', foot='뷰티가 먼저라면 성수 대신 명동\n(을지로입구역, 2호선).', steps=[
   ('성수', '이른 오후', ['4번(또는 3번) 출구', '연무장길로']), ('2호선', '타고 이동', ['동대문역사문화공원역까지']),
   ('동대문', '저녁', ['1번 출구 → DDP', '두타몰은 자정까지']), ('영수증', '여권과 함께', ['한 장 100만 원 초과 → 즉시 환급 안 됨'])]),
 'en': dict(title='Half-day route on Line 2', foot='Beauty first? Swap Seongsu for Myeongdong (Euljiro 1-ga, Line 2).', steps=[
   ('Seongsu', 'Early afternoon', ['Exit 4 (or 3)', 'Yeonmujang-gil']), ('Line 2', 'Ride to', ['Dongdaemun History & Culture Park']),
   ('Dongdaemun', 'Evening', ['Exit 1 → DDP', 'Doota until midnight']), ('Receipts', 'Keep with passport', ['Over ₩1,000,000 per receipt\n→ no instant refund'])]),
 'ja': dict(title='2号線で半日コース', foot='コスメ優先なら聖水を明洞に\n(乙支路入口駅も2号線)。', steps=[
   ('聖水', '午後早め', ['4番(または3番)出口', '演武場キルへ']), ('2号線', '乗って移動', ['東大門歴史文化公園駅まで']),
   ('東大門', '夜', ['1番出口 → DDP', 'DOOTAは0時まで']), ('レシート', 'パスポートと一緒に', ['1枚100万ウォン超 →\nその場の還付は不可'])]),
 'zh-tw': dict(title='2號線半日路線', foot='美妝優先?把聖水換成明洞\n(乙支路入口站也在2號線)。', steps=[
   ('聖水', '午後', ['4號(或3號)出口', '走到演武場街']), ('2號線', '搭乘', ['到東大門歷史文化公園站']),
   ('東大門', '晚上', ['1號出口 → DDP', 'DOOTA開到午夜']), ('收據', '和護照放一起', ['單張超過100萬韓元 → 不能現場退稅'])]),
}

# ================================================================ BUILDERS
def b_sub1(lang, d):
    nodes = [{'q': d['q1']}, {'branch': d['a1'], 'label': d['yes']},
             {'end': d['a3'], 'style': 'pick', 'sub': d['a3s']}]
    body, h = tree(d['title'], nodes, d['no'], MUTED, ('note', (d['nh'], d['nb'], d['nl'])))
    write(lang, 'seoul-subway-1', d['title'], body, h)

def b_sub2(lang, d):
    icons = ['gate', 'line4', 'l25', 'gate']
    items = [{'t': t, 'sub': [s], 'hl': i in (0, 3), 'icon': icons[i]} for i, (t, s) in enumerate(d['steps'])]
    body, h = steps(d['title'], items, subway_icon, footer_boxes=[d['n1'], d['n2']])
    write(lang, 'seoul-subway-2', d['title'], body, h)

def b_sub3(lang, d):
    body, y = title_block(d['title'])
    X0, X1 = PAD, W - PAD
    C1, C2 = (PAD + 4, 196), (204, W - PAD - 4)   # column spans
    top = y
    # header
    hl1 = wrap(d['cols'][0], 17, 170, True); hl2 = wrap(d['cols'][1], 17, 170, True)
    hh = max(len(hl1), len(hl2)) * lh(17) + 22
    rows_svg = ''
    yy = top + hh
    rows_svg += f'<line x1="{X0}" y1="{yy}" x2="{X1}" y2="{yy}" stroke="{RULE}" stroke-width="2"/>\n'
    for i, (lab, a, b, extra) in enumerate(d['rows']):
        bold = i == 0
        yy += 10
        s, h1 = block(PAD + 12, yy, wrap(lab, 16, W - 2 * PAD - 24, True), 16, MUTED, True)
        rows_svg += s
        yy += h1 + 4
        la = wrap(a, 17 if bold else 16, 160, bold); lb = wrap(b, 17 if bold else 16, 160, bold)
        fs = 17 if bold else 16
        ha = len(la) * lh(fs)
        if extra:
            le = wrap(extra, 16, 166)
            ha_e = ha + len(le) * lh(16)
        else:
            le = []; ha_e = ha
        hb = len(lb) * lh(fs)
        s, _ = block((C1[0] + C1[1]) / 2, yy, la, fs, INK, bold, 'middle'); rows_svg += s
        if le:
            s, _ = block((C1[0] + C1[1]) / 2, yy + ha, le, 16, MUTED, False, 'middle'); rows_svg += s
        s, _ = block((C2[0] + C2[1]) / 2, yy, lb, fs, INK, bold, 'middle'); rows_svg += s
        yy += max(ha_e, hb) + 12
        if i < len(d['rows']) - 1:
            rows_svg += f'<line x1="{X0}" y1="{yy}" x2="{X1}" y2="{yy}" stroke="{RULE}" stroke-width="2"/>\n'
    total_h = yy - top
    body += R(X0, top, X1 - X0, total_h, WHITE, RULE, 2)
    body += f'<rect x="{C1[0]-4}" y="{top+1}" width="{C1[1]-C1[0]+8}" height="{total_h-2}" fill="{SOFT}"/>\n'
    s, _ = block((C1[0] + C1[1]) / 2, top + 11, hl1, 17, RED, True, 'middle'); body += s
    s, _ = block((C2[0] + C2[1]) / 2, top + 11, hl2, 17, MUTED, True, 'middle'); body += s
    # Row labels sit across both columns; draw a white strip behind them? keep simple: labels over the tint.
    body += rows_svg
    body += R(X0, top, X1 - X0, total_h, 'none', RULE, 2)
    write(lang, 'seoul-subway-3', d['title'], body, yy + 18)

def b_bus1(lang, d):
    body, y = title_block(d['title'])
    TX = PAD + 92
    TWID = W - PAD - 12 - TX
    for (chip, cf, ct, typ, desc, fare) in d['rows']:
        tl = wrap(typ, 18, TWID, True); dl = wrap(desc, 16, TWID); fl = wrap(fare, 17, TWID, True)
        th = len(tl) * lh(18) + len(dl) * lh(16) + len(fl) * lh(17)
        h = th + 22
        body += R(PAD, y, W - 2 * PAD, h, WHITE, RULE, 1.5)
        body += R(PAD + 12, y + h / 2 - 18, 68, 36, cf, None, 8)
        body += T(PAD + 46, round(y + h / 2 + 6), chip, 17, ct, True, 'middle')
        ty = y + 11
        s, hh = block(TX, ty, tl, 18, INK, True); body += s; ty += hh
        s, hh = block(TX, ty, dl, 16, MUTED); body += s; ty += hh
        s, hh = block(TX, ty, fl, 17, INK, True); body += s
        y += h + 10
    s, hh = block(PAD + 4, y + 2, wrap(d['foot'], 16, W - 2 * PAD), 16, MUTED)
    body += s
    write(lang, 'seoul-bus-1', d['title'], body, y + hh + 20)

def b_bus2(lang, d):
    items = [{'t': t, 'sub': [s] if s else [], 'hl': i in (1, 3), 'red_num': i in (1, 3)} for i, (t, s) in enumerate(d['steps'])]
    body, h = steps(d['title'], items, None, warn=d['warn'])
    write(lang, 'seoul-bus-2', d['title'], body, h)

def b_bus3(lang, d):
    body, y = title_block(d['title'])
    BX0, BX1 = PAD + 22, W - PAD - 4
    # tap-off label above the dot column
    body += T(BX0 - 6, y + 16, d['off'], 16, RED, True, 'start')
    y += 30
    for lab, val, frac in d['rows']:
        s, hh = block(PAD + 4, y, wrap(lab, 17, W - 2 * PAD, True), 17, INK, True)
        body += s
        y += hh + 6
        full = BX1 - BX0
        body += R(BX0, y, full, 44, WHITE, RULE, 1.5, 10)
        body += R(BX0, y, full * frac, 44, SOFT, INK, 1.5, 10)
        body += T(BX0 + full * frac / 2, y + 28, val, 18, INK, True, 'middle')
        body += f'<circle cx="{BX0}" cy="{y+22}" r="9" fill="{RED}"/>\n'
        y += 44 + 20
    s, hh = block(PAD + 4, y, wrap(d['main'], 17, W - 2 * PAD - 8, True), 17, INK, True)
    body += s; y += hh + 4
    for n in d['notes']:
        body += f'<circle cx="{PAD+10}" cy="{y+11}" r="3.5" fill="{MUTED}"/>\n'
        s, hh = block(PAD + 22, y, wrap(n, 16, W - 2 * PAD - 30), 16, MUTED)
        body += s; y += hh
    write(lang, 'seoul-bus-3', d['title'], body, y + 20)

def b_da1(lang, d):
    body, y = title_block(d['title'], d['sub'])
    y += 30
    X0, X1 = PAD + 40, W - PAD - 40
    body += f'<line x1="{X0}" y1="{y}" x2="{X1}" y2="{y}" stroke="{SOFT}" stroke-width="16" stroke-linecap="round"/>\n'
    body += f'<line x1="{X0}" y1="{y}" x2="{X1}" y2="{y}" stroke="{RULE}" stroke-width="2" stroke-dasharray="2 8"/>\n'
    (p0, l0), (p1, l1_) = d['pts']
    body += f'<circle cx="{X0}" cy="{y}" r="11" fill="{INK}"/>\n<circle cx="{X1}" cy="{y}" r="11" fill="{RED}"/>\n'
    body += T(X0, y + 46, p0, 24, INK, True, 'middle') + T(X0, y + 72, l0, 17, MUTED, False, 'middle')
    body += T(X1, y + 46, p1, 24, RED, True, 'middle') + T(X1, y + 72, l1_, 17, RED, True, 'middle')
    y += 104
    l1 = wrap(d['f1'], 17, W - 2 * PAD - 24, True); l2 = wrap(d['f2'], 16, W - 2 * PAD - 24)
    h = len(l1) * lh(17) + len(l2) * lh(16) + 26
    body += R(PAD, y, W - 2 * PAD, h, SOFT, None, 10)
    s_, hh = block(PAD + 12, y + 13, l1, 17, INK, True); body += s_
    s_, _ = block(PAD + 12, y + 13 + hh, l2, 16, MUTED); body += s_
    write(lang, 'daiso-1', d['title'], body, y + h + 18)

def b_da2(lang, d):
    items = [{'t': t, 'sub': subs, 'hl': False, 'red_num': i == 3} for i, (t, subs) in enumerate(d['steps'])]
    body, h = steps(d['title'], items, None, group=(2, d['group']))
    write(lang, 'daiso-2', d['title'], body, h)

def b_da3(lang, d):
    nodes = [{'q': d['q1']}, {'branch': d['n1'], 'label': d['no'], 'style': 'soft', 'label_color': MUTED},
             {'q': d['q2'], 'ex': d['ex']}, {'branch': d['n2'], 'label': d['no'], 'style': 'soft', 'label_color': MUTED, 'sub': d['n2s']},
             {'end': d['end'], 'style': 'redfill'}]
    body, h = tree(d['title'], nodes, d['yes'], RED, ('box', d['foot']))
    write(lang, 'daiso-3', d['title'], body, h)

def mark(kind, cx, cy):
    if kind == 2:
        return f'<circle cx="{cx}" cy="{cy}" r="8" fill="{RED}"/>\n'
    if kind == 1:
        return f'<circle cx="{cx}" cy="{cy}" r="7" fill="none" stroke="{INK}" stroke-width="2.5"/>\n'
    return f'<line x1="{cx-6}" y1="{cy}" x2="{cx+6}" y2="{cy}" stroke="{RULE}" stroke-width="2.5"/>\n'

def clock(cx, cy, color=MUTED):
    return (f'<circle cx="{cx}" cy="{cy}" r="8" fill="none" stroke="{color}" stroke-width="2"/>'
            f'<path d="M{cx},{cy-5} L{cx},{cy} L{cx+4},{cy+2}" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round"/>\n')

def b_sh1(lang, d):
    body, y = title_block(d['title'])
    for (area, when), mk in zip(d['areas'], MARKS):
        h = 34 + 2 * 30 + 14
        body += R(PAD, y, W - 2 * PAD, h, WHITE, RULE, 1.5)
        body += T(PAD + 14, y + 28, area, 19, INK, True)
        # time, right aligned with clock icon
        tws = tw(when, 16)
        body += clock(round(W - PAD - 14 - tws - 14), y + 22)
        body += T(W - PAD - 14, y + 28, when, 16, INK, False, 'end')
        for k, (cat, m) in enumerate(zip(d['cats'], mk)):
            cx = PAD + 24 + (k % 2) * 176
            cy = y + 34 + 18 + (k // 2) * 30
            body += mark(m, cx, cy)
            body += T(cx + 16, cy + 6, cat, 16, INK if m else MUTED, m == 2)
        y += h + 10
    # legend
    y += 2
    for k, (m, lab) in enumerate([(2, d['best']), (1, d['good'])]):
        cx = PAD + 14 + k * 0
        body += mark(m, cx, y + 11)
        body += T(cx + 16, y + 17, lab, 16, INK)
        y += 26
    body += clock(PAD + 14, y + 11)
    body += T(PAD + 30, y + 17, d['time'], 16, INK)
    y += 26
    write(lang, 'shopping-streets-1', d['title'], body, y + 14)

def b_sh2(lang, d):
    body, y = title_block(d['title'], d['sub'])
    top = y + 60
    cx, cy, rx, ry = 200, top + 130, 158, 120
    import math
    river_y = cy + 84
    # river band
    body += (f'<path d="M0,{river_y} C80,{river_y-22} 160,{river_y+18} 240,{river_y} S360,{river_y-16} 400,{river_y-4} '
             f'L400,{river_y+40} C320,{river_y+26} 260,{river_y+58} 180,{river_y+42} S60,{river_y+30} 0,{river_y+46} Z" fill="{SOFT}" stroke="{RULE}" stroke-width="1.5"/>\n')
    body += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="9 7"/>\n'
    def pt(deg):
        a = math.radians(deg)
        return round(cx + rx * math.cos(a)), round(cy - ry * math.sin(a))
    st = d['st']
    pos = {'hd': pt(180), 'md': pt(97), 'dd': pt(55), 'ss': pt(-12)}
    for k, (x, yy) in pos.items():
        body += f'<circle cx="{x}" cy="{yy}" r="10" fill="{RED}" stroke="{WHITE}" stroke-width="3"/>\n'
    # labels
    def lab(key, x, yy, anchor):
        name, sub = st[key]
        s = T(x, yy, name, 18, INK, True, anchor)
        sl = sub.split('\n')
        for i, ln in enumerate(sl):
            s += T(x, yy + 22 + i * 21, ln, 16, MUTED, False, anchor)
        return s
    x, yy = pos['hd']; body += lab('hd', x + 18, yy - 6, 'start')
    x, yy = pos['md']; body += lab('md', x, yy - 50, 'middle')
    x, yy = pos['dd']; body += lab('dd', min(x + 14, W - PAD - 60), yy - 50, 'middle') if False else lab('dd', x + 4, yy - 50, 'middle')
    x, yy = pos['ss']; body += lab('ss', x - 18, yy - 6 - (21 if '\n' in st['ss'][1] else 0), 'end')
    body += T(70, river_y + 34, d['river'], 16, MUTED, False, 'middle')
    bottom = cy + ry
    body += T(W - PAD - 4, bottom + 34, d['line'], 16, INK, True, 'end')
    write(lang, 'shopping-streets-2', d['title'], body, bottom + 52)

def b_sh3(lang, d):
    body, y = title_block(d['title'])
    TX = 72
    TWID = W - PAD - 14 - TX
    for i, (place, when, det) in enumerate(d['steps']):
        if i > 0:
            body += arrow(42, y + 1, 42, y + 17)
            y += 20
        pl = wrap(place, 19, TWID, True); wl = wrap(when, 17, TWID)
        dl = []
        for x_ in det:
            dl += wrap(x_, 16, TWID)
        th = len(pl) * lh(19) + len(wl) * lh(17) + len(dl) * lh(16)
        h = th + 24
        red = i in (0, 2)
        body += R(PAD, y, W - 2 * PAD, h, WHITE, RED if red else RULE, 2.5 if red else 2)
        body += num(42, round(y + h / 2), i + 1, RED if red else INK)
        ty = y + 12
        s, hh = block(TX, ty, pl, 19, INK, True); body += s; ty += hh
        s, hh = block(TX, ty, wl, 17, INK); body += s; ty += hh
        s, hh = block(TX, ty, dl, 16, MUTED); body += s
        y += h
    y += 16
    fl = wrap(d['foot'], 16, W - 2 * PAD - 28)
    h = len(fl) * lh(16) + 22
    body += R(PAD, y, W - 2 * PAD, h, SOFT, None, 10)
    s, _ = block(PAD + 14, y + 11, fl, 16, INK); body += s
    write(lang, 'shopping-streets-3', d['title'], body, y + h + 18)

if __name__ == '__main__':
    for lang in ['en', 'ko', 'ja', 'zh-tw']:
        b_sub1(lang, SUB1[lang]); b_sub2(lang, SUB2[lang]); b_sub3(lang, SUB3[lang])
        b_bus1(lang, BUS1[lang]); b_bus2(lang, BUS2[lang]); b_bus3(lang, BUS3[lang])
        b_da1(lang, DA1[lang]); b_da2(lang, DA2[lang]); b_da3(lang, DA3[lang])
        b_sh1(lang, SH1[lang]); b_sh2(lang, SH2[lang]); b_sh3(lang, SH3[lang])
    print('ok', OUT)
