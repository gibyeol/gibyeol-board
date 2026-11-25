#!/usr/bin/env python3
"""Figures for jeju, ktx-busan, winter, everyday (2026-11-26).
Owner of: jeju-1..3, ktx-busan-1..4, winter-1..2, everyday-1..2.
(everyday also shows emergency-1 and seoul-subway-7, owned by other generators.)
Phone-first: viewBox width 400, min font-size 16. Text must match the page facts.
Helpers copied from gen-guides1.py (not imported, so that file is never run).
Usage: python3 gen-guides3.py [outdir]   (default: static/fig)"""
import os, re, sys
from xml.sax.saxutils import escape as _e

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'fig')
FONT = 'system-ui, -apple-system, &quot;Noto Sans KR&quot;, &quot;Noto Sans JP&quot;, &quot;Noto Sans TC&quot;, sans-serif'
INK, RED, PAPER, MUTED, RULE, WHITE, SOFT = '#16151a', '#b8392f', '#f4f0e6', '#5f5b55', '#c9c1b2', '#ffffff', '#e9e2d3'
W = 400
LANGS = ['en', 'ko', 'ja', 'zh-tw']


def e(s):
    return _e(s, {'"': '&quot;'})


def cw(ch):
    o = ord(ch)
    if o >= 0x1100 and not (0x2000 <= o <= 0x206f):
        return 1.0
    if ch == ' ':
        return 0.30
    if ch in 'il.,:;|!\'’()[]':
        return 0.32
    if ch in 'mwMW₩@%':
        return 0.90
    if ch.isupper() or ch.isdigit():
        return 0.66
    return 0.56


def tw(s, size, bold=False):
    return sum(cw(c) for c in s) * size * (1.07 if bold else 1.0)


def wrap(s, width, size, bold=False, lang='en'):
    out = []
    for para in s.split('\n'):
        if lang in ('ja', 'zh-tw'):
            toks = re.findall(r"[A-Za-z0-9₩,.:+%\-–/()~'’]+|\s|.", para)
        else:
            toks = re.findall(r'\S+|\s+', para)
        line = ''
        for t in toks:
            cand = line + t
            if line and tw(cand.rstrip(), size, bold) > width:
                out.append(line.rstrip())
                line = t.lstrip()
            else:
                line = cand
        if line.strip():
            out.append(line.rstrip())
    # no line may start with closing punctuation
    for i in range(1, len(out)):
        while out[i] and out[i][0] in '、。,，)）」:：' and len(out[i - 1]) > 1:
            out[i] = out[i - 1][-1] + out[i]
            out[i - 1] = out[i - 1][:-1]
    out = [l for l in out if l]
    if lang in ('ja', 'zh-tw') and len(out) >= 2 and len(out[-1]) <= 2 and len(out[-2]) > 4:
        out[-1] = out[-2][-2:] + out[-1]
        out[-2] = out[-2][:-2]
    return out


def T(x, y, s, size=16, w='400', fill=INK, anchor='start'):
    assert size >= 16
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{e(s)}</text>\n'


def R(x, y, w, h, fill=WHITE, stroke=None, sw=1.5, rx=10):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}/>\n'


class Fig:
    def __init__(self, lang, title):
        self.lang, self.b = lang, ''
        self.tl = wrap(title, 360, 20, True, lang)
        self.title = title
        self.y = 16 + 26 * len(self.tl) + 14

    def add(self, s):
        self.b += s

    def lines(self, x, text, width, size=16, bold=False, fill=INK, lh=None):
        lh = lh or round(size * 1.38)
        ls = wrap(text, width, size, bold, self.lang)
        for l in ls:
            self.y += lh
            self.add(T(x, self.y - 6, l, size, '700' if bold else '400', fill))
        return len(ls)

    def card(self, head='', sub='', badge=None, accent=False, fill=SOFT, badge_round=False, inner=None):
        """Card with optional left badge (number/label), bold head, muted sub, optional inner white box."""
        x0, y0 = 16, self.y
        bw = 0
        if badge is not None:
            bw = max(36, tw(badge, 18, True) + 20)
        tx = 30 + (bw + 12 if bw else 0)
        width = 384 - tx - 12
        self.y += 8
        if head:
            self.lines(tx, head, width, 17, True, RED if accent else INK)
        if sub:
            self.lines(tx, sub, width, 16, False, MUTED if not accent else INK)
        if inner:
            self.y += 8
            iy = self.y
            ib = tw(inner[0], 16, True) + 24
            itx = 36 + ib + 10
            iw = 374 - itx - 8
            body = ''
            save_b, self.b = self.b, ''
            self.y += 6
            self.lines(itx, inner[1], iw, 16, True)
            if len(inner) > 2 and inner[2]:
                self.lines(itx, inner[2], iw, 16, False, MUTED)
            self.y += 10
            body, self.b = self.b, save_b
            self.add(R(26, iy, 348, self.y - iy, WHITE, rx=8))
            self.add(R(36, iy + 10, ib, 26, RED, rx=13))
            self.add(T(36 + ib / 2, iy + 28, inner[0], 16, '700', WHITE, 'middle'))
            self.add(body)
        self.y += 14
        h = self.y - y0
        rect = R(x0, y0, 368, h, WHITE if accent else fill, RED if accent else None, 2)
        bad = ''
        if badge is not None:
            if badge_round:
                bad = (f'<circle cx="{30 + 18}" cy="{y0 + 26}" r="17" fill="{RED}"/>\n'
                       + T(48, y0 + 32, badge, 18, '700', WHITE, 'middle'))
            else:
                bad = R(30, y0 + 10, bw, 32, RED, rx=8) + T(30 + bw / 2, y0 + 32, badge, 18, '700', WHITE, 'middle')
        self.b = self.b[:self._mark] + rect + bad + self.b[self._mark:] if hasattr(self, '_mark') else self.b
        return h

    def begin(self):
        self._mark = len(self.b)

    def C(self, *a, **k):
        self.begin()
        self.card(*a, **k)
        del self._mark
        self.y += 10

    def arrow(self, label=None):
        y = self.y - 8
        self.add(f'<path d="M44 {y} V{y + 22}" stroke="{MUTED}" stroke-width="2"/>\n'
                 f'<path d="M38 {y + 16} L44 {y + 24} L50 {y + 16}" fill="none" stroke="{MUTED}" stroke-width="2"/>\n')
        if label:
            self.add(T(60, y + 18, label, 16, '700', MUTED))
        self.y += 22

    def header(self, text):
        self.y += 4
        self.add(R(16, self.y, 368, 34, INK, rx=8))
        self.add(T(30, self.y + 23, text, 17, '700', WHITE))
        self.y += 44

    def check(self, head, sub=''):
        """Checklist row: square box + bold head + muted sub."""
        y0 = self.y
        self.y += 2
        self.lines(52, head, 320, 17, True)
        if sub:
            self.lines(52, sub, 320, 16, False, MUTED)
        self.add(R(22, y0 + 8, 20, 20, WHITE, INK, 2, rx=4))
        self.y += 10
        self.add(f'<path d="M22 {self.y - 4} H378" stroke="{RULE}" stroke-width="1"/>\n')
        self.y += 4

    def foot(self, text, fill=MUTED, size=16):
        self.y += 2
        self.lines(20, text, 360, size, False, fill)

    def svg(self, pad=16):
        h = int(self.y + pad)
        t = ''.join(T(20, 16 + 26 * (i + 1), s, 20, '700') for i, s in enumerate(self.tl))
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" role="img" aria-label="{e(self.title)}" '
                f'font-family="{FONT}">\n<title>{e(self.title)}</title>\n'
                f'<rect width="{W}" height="{h}" fill="{PAPER}"/>\n{t}{self.b}</svg>\n')


def write(lang, name, svg):
    p = os.path.join(OUT, lang, name + '.svg')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(svg)


# ---------------------------------------------------------------- figure builders
def checklist(lang, d):
    f = Fig(lang, d['title'])
    for grp, items in d['groups']:
        f.header(grp)
        for it in items:
            f.check(*it)
    if d.get('foot'):
        f.foot(d['foot'])
    return f.svg()


def decision(lang, d):
    f = Fig(lang, d['title'])
    for i, (q, yes, ans, sub) in enumerate(d['qs']):
        f.C(q, inner=(yes, ans, sub))
        f.arrow(d['no'])
    end = d['end']
    f.C(end[0], end[1], accent=True)
    return f.svg()


def cards(lang, d, badge_round=False, arrows=False):
    f = Fig(lang, d['title'])
    for i, c in enumerate(d['cards']):
        badge, head, sub = c[0], c[1], c[2] if len(c) > 2 else ''
        acc = len(c) > 3 and c[3]
        f.C(head, sub, badge=badge, badge_round=badge_round, accent=acc)
        if arrows and i < len(d['cards']) - 1 and not (len(d['cards'][i + 1]) > 3 and d['cards'][i + 1][3]):
            f.y -= 6
            f.arrow()
            f.y -= 2
    if d.get('foot'):
        f.foot(d['foot'])
    return f.svg()



# ---------------------------------------------------------------- builders for this set
def bar(f, text, fill=INK):
    f.y += 4
    f.add(R(16, f.y, 368, 34, fill, rx=8))
    f.add(T(30, f.y + 23, text, 17, '700', WHITE))
    f.y += 44


def routes(lang, d):
    """Each route: coloured header bar, stops on a vertical line ('…' = stops not shown), a note."""
    f = Fig(lang, d['title'])
    for r in d['routes']:
        col = RED if r.get('red') else INK
        bar(f, r['name'], col)
        pts, dots = [], []
        for name, sub in r['stops']:
            if name == '…':
                for k in range(3):
                    dots.append(f.y + 4 + k * 9)
                f.y += 30
                continue
            y0 = f.y
            f.lines(70, name, 300, 17, True)
            if sub:
                f.lines(70, sub, 300, 16, False, MUTED)
            pts.append(y0 + 11)
            f.y += 8
        f.add(f'<line x1="44" y1="{pts[0]}" x2="44" y2="{pts[-1]}" stroke="{col}" stroke-width="5"/>\n')
        for cy in dots:
            f.add(f'<circle cx="44" cy="{cy}" r="3.5" fill="{PAPER}" stroke="{col}" stroke-width="1.5"/>\n')
        for cy in pts:
            f.add(f'<circle cx="44" cy="{cy}" r="8" fill="{WHITE}" stroke="{col}" stroke-width="2.5"/>\n')
        if r.get('note'):
            f.lines(20, r['note'], 360, 16, True, col)
        f.y += 12
    if d.get('foot'):
        f.foot(d['foot'])
    return f.svg()


def bars(lang, d):
    f = Fig(lang, d['title'])
    mx = max(v for _, v, _, _ in d['bars'])
    for label, v, shown, acc in d['bars']:
        f.y += 4
        y0 = f.y
        f.lines(20, label, 250, 17, True, RED if acc else INK)
        f.add(T(380, y0 + 17, shown, 17, '700', RED if acc else INK, 'end'))
        f.y += 4
        f.add(R(20, f.y, max(8, 360 * v / mx), 26, RED if acc else MUTED, rx=6))
        f.y += 36
    if d.get('foot'):
        f.y += 4
        f.foot(d['foot'])
    return f.svg()


def qrpole(lang, d):
    f = Fig(lang, d['title'])
    top = f.y + 6
    f.add(R(36, top, 14, 170, MUTED, rx=4))
    f.add(R(58, top + 24, 96, 96, WHITE, INK, 2, rx=6))
    import random
    rnd = random.Random(7)
    cells = ''
    for i in range(9):
        for j in range(9):
            corner = (i < 3 and j < 3) or (i < 3 and j > 5) or (i > 5 and j < 3)
            if corner:
                continue
            if rnd.random() < 0.45:
                cells += f'<rect x="{66 + j * 9}" y="{top + 32 + i * 9}" width="8" height="8" fill="{INK}"/>\n'
    for (cx, cy) in [(66, top + 32), (66 + 6 * 9, top + 32), (66, top + 32 + 6 * 9)]:
        cells += (f'<rect x="{cx}" y="{cy}" width="25" height="25" fill="{INK}"/>\n'
                  f'<rect x="{cx + 5}" y="{cy + 5}" width="15" height="15" fill="{WHITE}"/>\n'
                  f'<rect x="{cx + 9}" y="{cy + 9}" width="7" height="7" fill="{INK}"/>\n')
    f.add(cells)
    f.y = top + 18
    f.lines(172, d['qr'][0], 208, 17, True, RED)
    f.lines(172, d['qr'][1], 208, 16, False, MUTED)
    f.y = max(f.y, top + 170) + 16
    for c in d['cards']:
        f.C(c[1], c[2], badge=c[0], accent=len(c) > 3 and c[3])
    if d.get('foot'):
        f.foot(d['foot'])
    return f.svg()


def calendar(lang, d):
    f = Fig(lang, d['title'])
    cw_, x0 = 72, 20
    f.y += 4
    # holiday band over the first four days
    f.add(R(x0 + 2, f.y, cw_ * 4 - 4, 30, RED, rx=8))
    f.add(T(x0 + cw_ * 2, f.y + 21, d['band'], 16, '700', WHITE, 'middle'))
    f.y += 38
    for i, (dn, dd) in enumerate(d['days']):
        cx = x0 + cw_ * i + cw_ / 2
        f.add(R(x0 + cw_ * i + 2, f.y, cw_ - 4, 54, SOFT if i < 4 else WHITE, RULE, 1, rx=8))
        f.add(T(cx, f.y + 22, dn, 16, '400', MUTED, 'middle'))
        f.add(T(cx, f.y + 45, dd, 18, '700', INK, 'middle'))
    f.y += 66
    for label, cells in d['rows']:
        f.lines(20, label, 360, 17, True)
        f.y += 4
        for i, c in enumerate(cells):
            x = x0 + cw_ * i + 2
            closed = c == 'X'
            f.add(R(x, f.y, cw_ - 4, 34, RED if closed else WHITE, None if closed else INK, 1.5, rx=6))
            f.add(T(x + (cw_ - 4) / 2, f.y + 23, d['closed'] if closed else d['open'], 16, '700',
                    WHITE if closed else INK, 'middle'))
        f.y += 46
    if d.get('foot'):
        f.foot(d['foot'])
    return f.svg()


def badge(x, y, n):
    return (f'<circle cx="{x}" cy="{y}" r="13" fill="{RED}"/>\n' + T(x, y + 6, n, 16, '700', WHITE, 'middle'))


def restaurant(lang, d):
    f = Fig(lang, d['title'])
    y = f.y + 6
    f.add(R(24, y, 352, 176, SOFT, RULE, 1.5, rx=18))
    # 1 call button
    f.add(f'<circle cx="80" cy="{y + 52}" r="20" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>\n'
          f'<circle cx="80" cy="{y + 52}" r="9" fill="{RED}"/>\n')
    f.add(badge(108, y + 26, '1'))
    # 2 tablet
    f.add(R(140, y + 22, 100, 66, INK, rx=8) + R(147, y + 29, 86, 52, WHITE, rx=4))
    f.add(badge(250, y + 20, '2'))
    # 3 water cup
    f.add(f'<path d="M286 {y + 34} L320 {y + 34} L314 {y + 84} L292 {y + 84} Z" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>\n'
          f'<path d="M289 {y + 50} L317 {y + 50}" stroke="{RULE}" stroke-width="2"/>\n')
    f.add(badge(338, y + 30, '3'))
    # 4 sign
    f.add(R(110, y + 114, 170, 42, WHITE, INK, 2, rx=6))
    f.add(T(195, y + 142, '2인분 이상', 18, '700', INK, 'middle'))
    f.add(badge(298, y + 114, '4'))
    f.y = y + 192
    for n, head, sub in d['items']:
        f.C(head, sub, badge=n, badge_round=True)
    if d.get('foot'):
        f.C(d['foot'][0], d['foot'][1], accent=True)
    return f.svg()


def plug(lang, d):
    f = Fig(lang, d['title'])
    y = f.y + 8
    # Korean socket
    f.add(f'<circle cx="100" cy="{y + 58}" r="52" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>\n'
          f'<circle cx="80" cy="{y + 58}" r="9" fill="{INK}"/>\n<circle cx="120" cy="{y + 58}" r="9" fill="{INK}"/>\n')
    # flat-pin plug
    f.add(R(276, y + 14, 9, 30, INK, rx=2) + R(305, y + 14, 9, 30, INK, rx=2))
    f.add(R(256, y + 42, 78, 66, SOFT, INK, 2, rx=12))
    f.add(T(200, y + 68, '≠', 22, '700', RED, 'middle'))
    ly = y + 140
    for i, l in enumerate(d['kr']):
        f.add(T(100, ly + 22 * i, l, 17 if i == 0 else 16, '700' if i == 0 else '400', INK if i == 0 else MUTED, 'middle'))
    for i, l in enumerate(d['home']):
        f.add(T(295, ly + 22 * i, l, 17 if i == 0 else 16, '700' if i == 0 else '400', INK if i == 0 else MUTED, 'middle'))
    f.y = ly + 22 * max(len(d['kr']), len(d['home'])) + 6
    f.lines(20, d['need'], 360, 17, True, RED)
    f.y += 10
    for b, head, sub, acc in d['cards']:
        f.C(head, sub, badge=b, accent=acc)
    if d.get('foot'):
        f.foot(d['foot'])
    return f.svg()


# ---------------------------------------------------------------- data (facts as on the pages, 26 Nov 2026)
D = {}

D['jeju-1'] = (cards, {
    'en': {'title': 'Incheon to Jeju: two ways', 'cards': [
        ('A', 'Through Gimpo, any day', 'AREX train from Incheon to Gimpo, then a domestic flight'),
        ('B', 'Direct, three days a week', 'Jeju Air Incheon–Jeju: Mon, Wed, Fri, through 27 March 2027'),
        ('!', 'Book early', 'Gimpo–Jeju is the world’s busiest route, but seats fell in 2026', True)],
        'foot': 'Domestic flight: bring your passport. Korean Air closes check-in 30 min before departure.'},
    'ko': {'title': '인천에서 제주로: 두 가지 길', 'cards': [
        ('A', '김포를 거쳐서, 매일', '인천에서 공항철도로 김포, 그다음 국내선'),
        ('B', '직항, 주 3회', '제주항공 인천–제주: 월·수·금, 2027년 3월 27일까지'),
        ('!', '일찍 예매', '김포–제주는 세계에서 가장 붐비는 노선인데, 2026년 좌석이 줄었어요', True)],
        'foot': '국내선: 외국인은 여권. 대한항공 체크인은 출발 30분 전 마감.'},
    'ja': {'title': '仁川から済州へ:2つの行き方', 'cards': [
        ('A', '金浦経由なら毎日', '仁川からAREXで金浦へ、そこから国内線'),
        ('B', '直行は週3便', 'チェジュ航空 仁川–済州:月・水・金、2027年3月27日まで'),
        ('!', '早めに予約', '金浦–済州は世界一の混雑路線。2026年は座席が減っています', True)],
        'foot': '国内線もパスポートを。大韓航空のチェックインは出発30分前まで。'},
    'zh-tw': {'title': '仁川到濟州:兩種走法', 'cards': [
        ('A', '經金浦,每天都有', '從仁川搭機場鐵路到金浦,再搭國內線'),
        ('B', '直飛,一週3班', '濟州航空仁川–濟州:週一、三、五,到2027年3月27日'),
        ('!', '提早訂', '金浦–濟州是全球最繁忙航線,2026年座位卻變少', True)],
        'foot': '國內線也要帶護照。大韓航空報到在起飛前30分鐘截止。'},
}, '')

D['jeju-2'] = (routes, {
    'en': {'title': 'Two buses for the east coast', 'routes': [
        {'name': 'Express 101', 'red': True, 'stops': [
            ('Jeju Airport', 'Platform 2, in front of Gate 2, 1F'), ('…', ''),
            ('Hamdeok Beach', 'about 40 min, 10 stops'), ('…', ''), ('Namwon (Seogwipo)', '')],
         'note': 'From ₩2,000 by card · few stops'},
        {'name': 'Bus 201', 'stops': [
            ('Jeju City Bus Terminal', 'not the airport'), ('…', ''), ('Hamdeok Beach', ''), ('…', ''),
            ('Seongsan Ilchulbong', ''), ('…', ''), ('Seogwipo', '')],
         'note': '₩1,150 by card · every 30–80 min'}],
        'foot': 'Change from 101 to 201 at Hamdeok Beach. Only some stops shown.'},
    'ko': {'title': '동쪽 해안의 버스 두 노선', 'routes': [
        {'name': '급행 101번', 'red': True, 'stops': [
            ('제주공항', '1층 2번 게이트 앞 2번 승차장'), ('…', ''),
            ('함덕해수욕장', '약 40분, 정류장 10개'), ('…', ''), ('서귀포 남원', '')],
         'note': '카드 2,000원부터 · 정류장 적음'},
        {'name': '201번', 'stops': [
            ('제주시외버스터미널', '공항 아님'), ('…', ''), ('함덕해수욕장', ''), ('…', ''),
            ('성산일출봉', ''), ('…', ''), ('서귀포', '')],
         'note': '카드 1,150원 · 30~80분 간격'}],
        'foot': '함덕해수욕장에서 101번 → 201번 환승. 정류장은 일부만 표시.'},
    'ja': {'title': '東海岸を走る2つのバス', 'routes': [
        {'name': '急行101番', 'red': True, 'stops': [
            ('済州空港', '1階2番ゲート前の2番乗り場'), ('…', ''),
            ('咸徳ビーチ', '約40分、停留所10個'), ('…', ''), ('西帰浦・南元', '')],
         'note': 'カードで2,000ウォンから・停留所少なめ'},
        {'name': '201番', 'stops': [
            ('済州市外バスターミナル', '空港には行かない'), ('…', ''), ('咸徳ビーチ', ''), ('…', ''),
            ('城山日出峰', ''), ('…', ''), ('西帰浦', '')],
         'note': 'カードで1,150ウォン・30〜80分間隔'}],
        'foot': '咸徳ビーチで101番から201番へ。停留所は一部のみ表示。'},
    'zh-tw': {'title': '跑東海岸的兩條公車', 'routes': [
        {'name': '急行101路', 'red': True, 'stops': [
            ('濟州機場', '1樓2號門前的2號站牌'), ('…', ''),
            ('咸德海水浴場', '約40分鐘,10站'), ('…', ''), ('西歸浦南元', '')],
         'note': '刷卡2,000韓元起・停靠站少'},
        {'name': '201路', 'stops': [
            ('濟州市外巴士總站', '不到機場'), ('…', ''), ('咸德海水浴場', ''), ('…', ''),
            ('城山日出峰', ''), ('…', ''), ('西歸浦', '')],
         'note': '刷卡1,150韓元・30〜80分鐘一班'}],
        'foot': '在咸德海水浴場從101路換201路。只標出部分站。'},
})

D['jeju-3'] = (qrpole, {
    'en': {'title': 'Paying on a Jeju bus', 'qr': ('QR code on the pole by the driver', 'Instructions in several languages'),
           'cards': [('1', 'Card', 'A loaded Korean transport card'),
                     ('2', 'Or scan the QR', 'With a payment app that supports it'),
                     ('3', 'QR: enter the fare', '₩1,150 regular, ₩2,000 express 101'),
                     ('!', 'No cash', 'Not accepted since 1 October 2024', True)]},
    'ko': {'title': '제주 버스 요금 내기', 'qr': ('기사 옆 기둥의 QR 코드', '여러 언어 안내가 옆에'),
           'cards': [('1', '카드', '충전한 교통카드'),
                     ('2', '또는 QR 찍기', 'QR 결제가 되는 결제 앱으로'),
                     ('3', 'QR: 요금 입력', '일반 1,150원, 급행 101번 2,000원'),
                     ('!', '현금 안 돼요', '2024년 10월 1일부터', True)]},
    'ja': {'title': '済州のバスの払い方', 'qr': ('運転席横のポールにQRコード', '横に多言語の案内'),
           'cards': [('1', 'カード', 'チャージした韓国の交通カード'),
                     ('2', 'またはQRを読み取る', '対応する決済アプリで'),
                     ('3', 'QR:運賃を入力', '一般1,150ウォン、急行101番2,000ウォン'),
                     ('!', '現金は不可', '2024年10月1日から', True)]},
    'zh-tw': {'title': '濟州公車怎麼付', 'qr': ('司機旁柱子上的QR碼', '旁邊有多語說明'),
           'cards': [('1', '刷卡', '儲值過的韓國交通卡'),
                     ('2', '或掃QR', '用有支援的支付App'),
                     ('3', 'QR:輸入票價', '一般1,150韓元,急行101路2,000韓元'),
                     ('!', '不收現金', '2024年10月1日起', True)]},
})

D['ktx-busan-1'] = (cards, {
    'en': {'title': 'Booking a KTX', 'cards': [
        ('1', 'Two months before', 'Sales open (since 1 October 2026)'),
        ('2', 'Where to buy', 'Korail+ app, letskorail.com, Klook, or a station machine that takes overseas cards'),
        ('3', 'Pick a seat direction', 'Depending on the train, seats face forward or backward'),
        ('!', 'Holiday trains: separate sale', 'Seollal 2027 holiday: 6–9 February', True)]},
    'ko': {'title': 'KTX 예매', 'cards': [
        ('1', '출발 2개월 전', '예매 시작(2026년 10월 1일부터)'),
        ('2', '어디서 사나', '코레일+ 앱, letskorail.com, 클룩, 해외 카드 되는 역 발권기'),
        ('3', '좌석 방향 고르기', '열차에 따라 순방향·역방향 좌석'),
        ('!', '명절 열차는 따로 예매', '2027년 설 연휴: 2월 6~9일', True)]},
    'ja': {'title': 'KTXの予約', 'cards': [
        ('1', '出発の2か月前', '発売開始(2026年10月1日から)'),
        ('2', 'どこで買う', 'Korail+アプリ、letskorail.com、Klook、海外カード対応の駅の券売機'),
        ('3', '席の向きを選ぶ', '列車によって進行方向向き・逆向きがあります'),
        ('!', '連休の列車は別枠で発売', '2027年ソル連休:2月6〜9日', True)]},
    'zh-tw': {'title': '訂KTX', 'cards': [
        ('1', '出發前2個月', '開賣(2026年10月1日起)'),
        ('2', '在哪裡買', 'Korail+ App、letskorail.com、Klook,或可刷海外卡的車站售票機'),
        ('3', '選座位方向', '依車種分順向和逆向座位'),
        ('!', '連假列車另外開賣', '2027春節連假:2月6〜9日', True)]},
}, 'arrows')

D['ktx-busan-2'] = (routes, {
    'en': {'title': 'Three Seoul stations to Busan', 'routes': [
        {'name': 'KTX from Seoul Station or Yongsan', 'red': True, 'stops': [
            ('Seoul Station or Yongsan', 'Korail Pass: yes'), ('…', ''), ('Busan Station', '2 h 17 min to 2 h 41 min')]},
        {'name': 'SRT from Suseo', 'stops': [
            ('Suseo', 'Southeast Seoul: Gangnam, Jamsil'), ('…', ''), ('Busan Station', '')],
         'note': 'Korail Pass: not as of August 2026'},
        {'name': 'KTX-Eum from Cheongnyangni', 'stops': [
            ('Cheongnyangni', 'Eastern Seoul'), ('…', ''), ('Sinhaeundae', ''), ('Centum', ''),
            ('…', ''), ('Bujeon', 'about 3 h 38 min')],
         'note': 'For hotels in Haeundae'}],
        'foot': 'All three are booked in the Korail+ app.'},
    'ko': {'title': '부산행 열차가 서는 서울의 세 역', 'routes': [
        {'name': '서울역·용산역 KTX', 'red': True, 'stops': [
            ('서울역 또는 용산역', '코레일패스: 됨'), ('…', ''), ('부산역', '2시간 17분~2시간 41분')]},
        {'name': '수서 SRT', 'stops': [
            ('수서', '서울 남동쪽: 강남, 잠실'), ('…', ''), ('부산역', '')],
         'note': '코레일패스: 2026년 8월 기준 안 됨'},
        {'name': '청량리 KTX-이음', 'stops': [
            ('청량리', '서울 동쪽'), ('…', ''), ('신해운대', ''), ('센텀', ''),
            ('…', ''), ('부전', '약 3시간 38분')],
         'note': '숙소가 해운대라면'}],
        'foot': '세 가지 모두 코레일+ 앱에서 예매해요.'},
    'ja': {'title': '釜山行きが出るソウルの3駅', 'routes': [
        {'name': 'ソウル駅・龍山駅のKTX', 'red': True, 'stops': [
            ('ソウル駅か龍山駅', 'KORAIL PASS:使える'), ('…', ''), ('釜山駅', '2時間17分〜2時間41分')]},
        {'name': '水西のSRT', 'stops': [
            ('水西', 'ソウル南東:江南、蚕室'), ('…', ''), ('釜山駅', '')],
         'note': 'KORAIL PASS:2026年8月時点で不可'},
        {'name': '清凉里のKTX-イウム', 'stops': [
            ('清凉里', 'ソウル東部'), ('…', ''), ('新海雲台', ''), ('センタム', ''),
            ('…', ''), ('釜田', '約3時間38分')],
         'note': '海雲台に泊まるなら'}],
        'foot': '3つともKorail+アプリで予約できます。'},
    'zh-tw': {'title': '首爾有車到釜山的三個車站', 'routes': [
        {'name': '首爾站・龍山站 KTX', 'red': True, 'stops': [
            ('首爾站或龍山站', 'KORAIL PASS:可用'), ('…', ''), ('釜山站', '2小時17分〜2小時41分')]},
        {'name': '水西 SRT', 'stops': [
            ('水西', '首爾東南:江南、蠶室'), ('…', ''), ('釜山站', '')],
         'note': 'KORAIL PASS:2026年8月時不能用'},
        {'name': '清涼里 KTX-Eum', 'stops': [
            ('清涼里', '首爾東邊'), ('…', ''), ('新海雲台', ''), ('Centum', ''),
            ('…', ''), ('釜田', '約3小時38分')],
         'note': '住海雲台的話'}],
        'foot': '三種都在Korail+ App訂。'},
})

D['ktx-busan-3'] = (bars, {
    'en': {'title': 'Round trip or Korail Pass? (adult)', 'bars': [
        ('Seoul–Busan round trip, 2 × ₩54,400', 108800, '₩108,800', True),
        ('2-day Korail Pass', 131000, '₩131,000', False),
        ('3-day Korail Pass', 186000, '₩186,000', False)],
        'foot': 'Fare since 1 September 2026; pass prices as reported in December 2025.'},
    'ko': {'title': '왕복 승차권이냐 코레일패스냐(성인)', 'bars': [
        ('서울-부산 왕복, 54,400원 × 2', 108800, '108,800원', True),
        ('코레일패스 2일권', 131000, '131,000원', False),
        ('코레일패스 3일권', 186000, '186,000원', False)],
        'foot': '운임은 2026년 9월 1일 기준, 패스 가격은 2025년 12월 보도 기준.'},
    'ja': {'title': '往復乗車券かKORAIL PASSか(大人)', 'bars': [
        ('ソウル〜釜山往復、54,400ウォン×2', 108800, '108,800ウォン', True),
        ('KORAIL PASS 2日用', 131000, '131,000ウォン', False),
        ('KORAIL PASS 3日用', 186000, '186,000ウォン', False)],
        'foot': '運賃は2026年9月1日から、パスの値段は2025年12月の報道より。'},
    'zh-tw': {'title': '來回車票還是KORAIL PASS?(成人)', 'bars': [
        ('首爾–釜山來回,54,400韓元×2', 108800, '108,800韓元', True),
        ('KORAIL PASS 2日券', 131000, '131,000韓元', False),
        ('KORAIL PASS 3日券', 186000, '186,000韓元', False)],
        'foot': '票價為2026年9月1日起;通票價格依2025年12月報導。'},
})

D['ktx-busan-4'] = (cards, {
    'en': {'title': 'Gimhae Airport into Busan', 'cards': [
        ('1', 'Light rail', 'Cheapest and fastest. Change at Sasang (Line 2) or Daejeo (Line 3)'),
        ('2', 'Limousine 2', 'Seomyeon, Bujeon · ₩6,000 · about 50 min · every 60–80 min'),
        ('3', 'Limousine 1', 'Haeundae · ₩9,500'),
        ('!', 'Limousines take no cash', 'Machine on 1F by Gate 4, or tap a card on board', True)],
        'foot': 'Two bags up to 30 kg in total ride free.'},
    'ko': {'title': '김해공항에서 부산 시내로', 'cards': [
        ('1', '경전철', '가장 싸고 빨라요. 사상(2호선)이나 대저(3호선)에서 환승'),
        ('2', '공항리무진 2번', '서면·부전 · 6,000원 · 약 50분 · 60~80분 간격'),
        ('3', '공항리무진 1번', '해운대 · 9,500원'),
        ('!', '리무진은 현금 안 돼요', '1층 4번 게이트 옆 발권기, 또는 버스에서 카드', True)],
        'foot': '짐은 두 개, 합쳐서 30kg까지 무료.'},
    'ja': {'title': '金海空港から釜山市内へ', 'cards': [
        ('1', '軽電鉄', 'いちばん安くて速い。沙上(2号線)か大渚(3号線)で乗り換え'),
        ('2', '空港リムジン2番', '西面・釜田・6,000ウォン・約50分・60〜80分おき'),
        ('3', '空港リムジン1番', '海雲台・9,500ウォン'),
        ('!', 'リムジンは現金不可', '1階4番ゲート横の券売機か、車内でカード', True)],
        'foot': '荷物は2個・合計30kgまで無料。'},
    'zh-tw': {'title': '從金海機場進釜山市區', 'cards': [
        ('1', '輕軌', '最便宜也最快。在沙上(2號線)或大渚(3號線)轉車'),
        ('2', '機場巴士2號', '西面、釜田・6,000韓元・約50分鐘・每60〜80分鐘'),
        ('3', '機場巴士1號', '海雲台・9,500韓元'),
        ('!', '機場巴士不收現金', '1樓4號門旁售票機,或上車刷卡', True)],
        'foot': '行李2件、合計30公斤內免費。'},
}, '')

D['winter-1'] = (cards, {
    'en': {'title': 'January in Seoul: average low −5.5°C', 'cards': [
        ('1', 'Long down coat or parka', 'One that covers your hips'),
        ('2', 'Thermal base layer', 'Warm outside, not too hot inside'),
        ('3', 'Hat, gloves, scarf', 'Touchscreen gloves for maps'),
        ('+', 'Buy there: hot packs (핫팩)', 'CU, GS25, 7-Eleven, all winter', True)],
        'foot': 'Indoors is heated: open the coat, take off the scarf.'},
    'ko': {'title': '1월 서울: 평균 최저 −5.5°C', 'cards': [
        ('1', '긴 패딩이나 파카', '엉덩이를 덮는 길이'),
        ('2', '발열 내의', '밖은 따뜻하게, 안은 덥지 않게'),
        ('3', '모자, 장갑, 목도리', '지도 볼 땐 터치 장갑'),
        ('+', '가서 사기: 핫팩', 'CU, GS25, 세븐일레븐, 겨울 내내', True)],
        'foot': '실내는 난방: 패딩 열고, 목도리 풀기.'},
    'ja': {'title': '1月のソウル:平均最低−5.5°C', 'cards': [
        ('1', 'ロングダウンか厚手のコート', 'お尻まで隠れる丈'),
        ('2', 'インナー', '外は暖かく、室内は暑すぎず'),
        ('3', '帽子、手袋、マフラー', '地図アプリ用にスマホ対応の手袋'),
        ('+', '現地で買う:カイロ(핫팩)', 'CU、GS25、セブンイレブンで冬じゅう', True)],
        'foot': '室内は暖房:ダウンの前を開けて、マフラーを外す。'},
    'zh-tw': {'title': '1月首爾:平均最低 −5.5°C', 'cards': [
        ('1', '長版羽絨外套或厚大衣', '蓋過臀部'),
        ('2', '發熱衣', '外面保暖,室內不會太熱'),
        ('3', '毛帽、手套、圍巾', '看地圖用觸控手套'),
        ('+', '到了再買:暖暖包(핫팩)', 'CU、GS25、7-Eleven,整個冬天都有', True)],
        'foot': '室內有暖氣:外套拉開,圍巾拿下。'},
}, '')

D['winter-2'] = (calendar, {
    'en': {'title': 'Seollal 2027, day by day (February)', 'band': 'Holiday 6–9 Feb',
           'days': [('Sat', '6'), ('Sun', '7'), ('Mon', '8'), ('Tue', '9'), ('Wed', '10')],
           'open': 'Open', 'closed': 'Shut',
           'rows': [('Palaces and Jongmyo (by the rules)', 'OOOOX'), ('National Museum of Korea', 'OXOOO')],
           'foot': '2027 notices are not out yet. Department stores: check each store’s notice.'},
    'ko': {'title': '2027년 설 연휴, 날짜별로 (2월)', 'band': '연휴 2월 6~9일',
           'days': [('토', '6'), ('일', '7'), ('월', '8'), ('화', '9'), ('수', '10')],
           'open': '개방', 'closed': '휴무',
           'rows': [('궁궐·종묘 (규정 기준)', 'OOOOX'), ('국립중앙박물관', 'OXOOO')],
           'foot': '2027년 공지는 아직이에요. 백화점은 매장별 공지를 확인하세요.'},
    'ja': {'title': '2027年ソル連休、日ごとに(2月)', 'band': '連休 2月6〜9日',
           'days': [('土', '6'), ('日', '7'), ('月', '8'), ('火', '9'), ('水', '10')],
           'open': '開館', 'closed': '休み',
           'rows': [('王宮・宗廟(規定どおりなら)', 'OOOOX'), ('国立中央博物館', 'OXOOO')],
           'foot': '2027年のお知らせはまだです。百貨店は各店のお知らせを確認。'},
    'zh-tw': {'title': '2027春節連假,逐日看(2月)', 'band': '連假 2/6〜2/9',
           'days': [('六', '6'), ('日', '7'), ('一', '8'), ('二', '9'), ('三', '10')],
           'open': '開放', 'closed': '休息',
           'rows': [('古宮・宗廟(依規定)', 'OOOOX'), ('國立中央博物館', 'OXOOO')],
           'foot': '2027年公告還沒出。百貨公司請看各店公告。'},
})

D['everyday-1'] = (restaurant, {
    'en': {'title': 'At a Korean restaurant table', 'items': [
        ('1', 'Call button', 'Press it and staff come. It can be loud'),
        ('2', 'Tablet or kiosk', 'Many places take your order and payment here'),
        ('3', 'Water', 'Free, often self-serve by the wall'),
        ('4', '“2인분 이상”', 'Two servings or more: ask before you sit')],
        'foot': ('No tip', 'Menu prices include tax and service')},
    'ko': {'title': '한국 식당 테이블에서', 'items': [
        ('1', '호출벨', '누르면 직원이 와요. 소리가 클 수 있어요'),
        ('2', '태블릿이나 키오스크', '여기서 주문하고 결제하는 곳이 많아요'),
        ('3', '물', '무료, 벽 쪽에서 직접 떠 오는 곳이 많아요'),
        ('4', '“2인분 이상”', '혼자라면 앉기 전에 물어보기')],
        'foot': ('팁 없음', '메뉴 가격에 세금·봉사료 포함')},
    'ja': {'title': '韓国の食堂のテーブルで', 'items': [
        ('1', '呼び出しボタン', '押すと店員さんが来ます。音は大きめ'),
        ('2', 'タブレットかキオスク', 'ここで注文と支払いをする店が多い'),
        ('3', '水', '無料。壁際でセルフの店が多い'),
        ('4', '「2인분 이상」', '2人前以上。ひとりなら座る前に確認')],
        'foot': ('チップ不要', 'メニュー価格は税・サービス料込み')},
    'zh-tw': {'title': '韓國餐廳的桌上', 'items': [
        ('1', '服務鈴', '按了店員就會來,鈴聲可能很大'),
        ('2', '平板或kiosk', '很多店在這裡點餐付款'),
        ('3', '水', '免費,很多是牆邊自取'),
        ('4', '「2인분 이상」', '2人份以上:一個人先問再坐')],
        'foot': ('不用小費', '菜單價格已含稅與服務費')},
})

D['everyday-2'] = (plug, {
    'en': {'title': 'Will your plug fit?', 'kr': ['Korea', '220V, 60Hz', 'two round pins'],
           'home': ['US', '120V', 'flat pins'], 'need': 'You need an adapter. Then read the label:',
           'cards': [('100–240V', 'Adapter is enough', 'Most phone and laptop chargers', False),
                     ('120V only', 'Needs a converter', 'Hair dryer, straightener: or leave it at home', True)],
           'foot': 'Hotel desks can often lend adapters; Incheon Airport convenience stores sell them.'},
    'ko': {'title': '플러그가 맞을까?', 'kr': ['한국', '220V, 60Hz', '둥근 핀 두 개'],
           'home': ['미국·일본·대만', '120V·100V·110V', '납작한 핀'], 'need': '어댑터가 필요해요. 그다음 표시를 보세요:',
           'cards': [('100–240V', '어댑터만 있으면 돼요', '휴대폰·노트북 충전기 대부분', False),
                     ('자국 전압 전용', '변압기가 필요해요', '드라이기, 고데기', True)],
           'foot': '호텔 프런트에서 빌려주기도 하고, 인천공항 편의점·면세점에서 팔아요.'},
    'ja': {'title': 'プラグは挿さる?', 'kr': ['韓国', '220V・60Hz', '丸ピン2本'],
           'home': ['日本', '100V', '平たいピン'], 'need': '変換プラグが必要です。次に表示を確認:',
           'cards': [('100–240V', '変換プラグだけでOK', 'スマホやPCの充電器の多く', False),
                     ('100V専用', '変圧器が必要', 'ドライヤー、ヘアアイロンは持って行かないほうが無難', True)],
           'foot': 'ホテルのフロントで借りられることも。仁川空港のコンビニや免税店でも販売。'},
    'zh-tw': {'title': '插頭插得進去嗎?', 'kr': ['韓國', '220V、60Hz', '圓形雙腳'],
           'home': ['台灣', '110V', '扁腳'], 'need': '一定要帶轉接頭。再看標示:',
           'cards': [('100–240V', '轉接頭就夠', '大部分手機、筆電充電器', False),
                     ('只支援110V', '需要變壓器', '吹風機、離子夾,建議別帶', True)],
           'foot': '飯店櫃檯常可借轉接頭,仁川機場便利商店和免稅店也買得到。'},
})


def main():
    for name, spec in D.items():
        fn, data = spec[0], spec[1]
        mode = spec[2] if len(spec) > 2 else ''
        for lang in LANGS:
            if fn is cards:
                svg = cards(lang, data[lang], badge_round='round' in mode, arrows='arrows' in mode)
            else:
                svg = fn(lang, data[lang])
            write(lang, name, svg)
    print('wrote', len(D) * 4, 'files to', os.path.abspath(OUT))


if __name__ == '__main__':
    main()
