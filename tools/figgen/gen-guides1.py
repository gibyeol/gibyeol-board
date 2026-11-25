#!/usr/bin/env python3
"""Figures for essentials, first-trip, emergency, convenience-store (2026-11-26).
Owner of: essentials-1..5, first-trip-1..3, emergency-1..4, convenience-store-1..3.
Phone-first: viewBox width 400, min font-size 16. Text must match the page facts.
Usage: python3 gen-guides1.py [outdir]   (default: static/fig)"""
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


def phone_apps(lang, d):
    f = Fig(lang, d['title'])
    y0 = f.y
    f.y += 26
    rows = d['apps']
    body = ''
    save, f.b = f.b, ''
    for name, job in rows:
        ry = f.y
        f.add(R(44, ry, 312, 64, SOFT, rx=12))
        f.add(R(56, ry + 12, 40, 40, WHITE, RULE, 1.5, rx=10))
        f.add(T(76, ry + 39, name[0], 18, '700', RED, 'middle'))
        f.add(T(108, ry + 27, name, 17, '700'))
        f.add(T(108, ry + 50, job, 16, '400', MUTED))
        f.y += 74
    f.y += 14
    body, f.b = f.b, save
    f.add(R(28, y0, 344, f.y - y0, WHITE, INK, 3, rx=26))
    f.add(R(170, y0 + 10, 60, 6, RULE, rx=3))
    f.add(body)
    f.y += 4
    if d.get('foot'):
        f.foot(d['foot'])
    return f.svg()


def week(lang, d):
    f = Fig(lang, d['title'])
    cw_ = 368 / 7
    for name, closed in d['palaces']:
        f.y += 4
        f.add(T(20, f.y + 18, name, 17, '700'))
        f.y += 28
        for i, day in enumerate(d['days']):
            x = 16 + i * cw_
            isc = i == closed
            f.add(R(round(x + 2, 1), f.y, round(cw_ - 4, 1), 48, RED if isc else WHITE, None if isc else RULE, 1.5, rx=8))
            f.add(T(round(x + cw_ / 2, 1), f.y + 21, day, 16, '700', WHITE if isc else INK, 'middle'))
            f.add(T(round(x + cw_ / 2, 1), f.y + 41, d['closed'] if isc else d['open'], 16, '400', WHITE if isc else MUTED, 'middle'))
        f.y += 60
    f.y += 4
    for head, sub in d['facts']:
        f.C(head, sub, fill=SOFT)
        f.y -= 4
    return f.svg()


def phrases(lang, d):
    f = Fig(lang, d['title'])
    rects = ''
    for num, ko, tr in d['cards']:
        y0 = f.y
        f.y += 10
        f.lines(100, ko, 272, 20, True, INK, 30)
        f.lines(100, tr, 272, 16, False, MUTED)
        f.y += 14
        rects += R(16, y0, 368, f.y - y0, WHITE, INK, 2)
        rects += R(26, y0 + 14, 64, 34, RED, rx=8) + T(58, y0 + 37, num, 18, '700', WHITE, 'middle')
        f.y += 10
    f.b = rects + f.b
    if d.get('foot'):
        f.foot(d['foot'])
    return f.svg()


def tags(lang, d):
    f = Fig(lang, d['title'])
    for big, line in d['tags']:
        y0 = f.y
        f.add(R(16, y0, 368, 70, WHITE, INK, 2, rx=6))
        f.add(R(16, y0, 110, 70, RED, rx=6))
        f.add(T(71, y0 + 45, big, 28, '700', WHITE, 'middle'))
        ls = wrap(line, 230, 17, True, lang)
        yy = y0 + (42 if len(ls) == 1 else 30)
        for i, l in enumerate(ls):
            f.add(T(140, yy + 24 * i, l, 17, '700'))
        f.y += 80
    f.y += 4
    f.C(d['calc'][0], d['calc'][1], accent=True)
    if d.get('foot'):
        f.y -= 6
        f.foot(d['foot'])
    return f.svg()


# ---------------------------------------------------------------- content
D = {}

D['essentials-1'] = (checklist, {
    'en': {'title': 'Your day-one checklist', 'groups': [
        ('Before you fly', [('e-Arrival Card', 'Within 3 days before landing. Free'), ('K-ETA', 'Only if your passport is not exempt'),
                            ('Data', 'eSIM installed, or a SIM to pick up'), ('Apps, on wifi', 'Naver Map, Kakao T, Papago'),
                            ('Passport photo page', 'A photo of it on your phone')]),
        ('At the airport', [('Turn data on', ''), ('Transport card', 'T-money, WOWPASS or the AREX card'), ('Some won cash', 'T-money top-ups, market food')])]},
    'ko': {'title': '첫날 체크리스트', 'groups': [
        ('출발 전', [('전자입국신고서', '도착 3일 전부터. 무료'), ('K-ETA', '면제 대상이 아닐 때만'),
                   ('데이터', 'eSIM 설치, 또는 공항 수령 유심'), ('앱 설치(와이파이에서)', '네이버 지도, 카카오 T, 파파고'),
                   ('여권 사진면', '휴대폰에 사진 한 장')]),
        ('공항에서', [('데이터 켜기', ''), ('교통카드', '티머니, WOWPASS, 공항철도 카드'), ('현금 조금', '티머니 충전, 시장 음식')])]},
    'ja': {'title': '初日のチェックリスト', 'groups': [
        ('出発前', [('電子入国申告', '到着3日前から。無料'), ('K-ETA', '免除対象でない場合だけ'),
                  ('データ', 'eSIMを設定、または空港受取のSIM'), ('アプリ(Wi-Fiで)', 'NAVERマップ、Kakao T、Papago'),
                  ('パスポート顔写真ページ', 'スマホに写真を1枚')]),
        ('空港で', [('データをオン', ''), ('交通カード', 'T-money、WOWPASS、空港鉄道カード'), ('少しのウォン現金', 'T-moneyのチャージ、市場の食べ物')])]},
    'zh-tw': {'title': '第一天檢查清單', 'groups': [
        ('出發前', [('電子入境卡', '抵達前3天內。免費'), ('K-ETA', '護照不在免除名單才需要'),
                  ('網路', '先裝好eSIM,或機場取SIM卡'), ('App(用Wi-Fi下載)', 'NAVER 地圖、Kakao T、Papago'),
                  ('護照照片頁', '手機裡存一張照片')]),
        ('在機場', [('打開行動網路', ''), ('交通卡', 'T-money、WOWPASS或機場快線卡'), ('一點韓元現金', 'T-money儲值、市場小吃')])]},
})

D['essentials-2'] = (decision, {
    'en': {'title': 'Arrival card or K-ETA?', 'no': 'No', 'qs': [
        ('Do you hold a valid K-ETA?', 'Yes', 'No arrival card needed', ''),
        ('Is your passport exempt from K-ETA? (to 31 Dec 2027)', 'Yes', 'File the e-Arrival Card', 'Free, within 3 days before landing')],
        'end': ('Apply for a K-ETA first', '₩10,000, before you book')},
    'ko': {'title': '입국신고서인가, K-ETA인가?', 'no': '아니요', 'qs': [
        ('유효한 K-ETA가 있나요?', '예', '입국신고서 필요 없음', ''),
        ('K-ETA 면제 대상 여권인가요? (2027년 12월 31일까지)', '예', '전자입국신고서 제출', '무료, 도착 3일 전부터')],
        'end': ('먼저 K-ETA 신청', '1만 원, 예약 전에')},
    'ja': {'title': '入国申告?それともK-ETA?', 'no': 'いいえ', 'qs': [
        ('有効なK-ETAを持っている?', 'はい', '入国申告は不要', ''),
        ('K-ETA免除の対象?(2027年12月31日まで)', 'はい', '電子入国申告を提出', '無料、到着3日前から')],
        'end': ('先にK-ETAを申請', '1万ウォン、予約の前に')},
    'zh-tw': {'title': '填入境卡,還是K-ETA?', 'no': '否', 'qs': [
        ('有有效的K-ETA嗎?', '是', '不用填入境卡', ''),
        ('護照在K-ETA免除名單內嗎?(至2027年12月31日)', '是', '填電子入境卡', '免費,抵達前3天內')],
        'end': ('先申請K-ETA', '1萬韓元,訂機票前')},
})

D['essentials-3'] = (cards, {
    'en': {'title': 'Three ways to stay online', 'cards': [
        ('1', 'eSIM', 'Install before you fly, works when you land. Phone must support eSIM and be unlocked'),
        ('2', 'Physical SIM', 'Pick up at the airport. For phones without eSIM'),
        ('3', 'Pocket wifi', 'One connection for a group. One more thing to charge and return'),
        ('!', 'Need calls and texts?', 'Choose a plan that includes them', True)]},
    'ko': {'title': '데이터, 세 가지 방법', 'cards': [
        ('1', 'eSIM', '출발 전에 설치, 도착하면 바로 연결. eSIM 지원·언락 폰만'),
        ('2', '유심', '공항에서 수령. eSIM이 안 되는 폰'),
        ('3', '포켓 와이파이', '여럿이 한 회선. 충전하고 반납할 물건이 하나 더'),
        ('!', '통화·문자도 필요하다면', '통화·문자가 포함된 요금제로', True)]},
    'ja': {'title': 'ネットにつなぐ3つの方法', 'cards': [
        ('1', 'eSIM', '出発前に設定、着いたらすぐ使える。eSIM対応・SIMフリーの端末のみ'),
        ('2', 'SIMカード', '空港で受け取り。eSIM非対応の端末に'),
        ('3', 'ポケットWi-Fi', 'グループで1回線。充電と返却が1つ増える'),
        ('!', '通話・SMSも必要なら', '通話・SMS付きのプランを', True)]},
    'zh-tw': {'title': '上網的三種方式', 'cards': [
        ('1', 'eSIM', '出發前安裝,落地就能用。手機需支援eSIM且未鎖卡'),
        ('2', '實體SIM卡', '在機場領取。適合不支援eSIM的手機'),
        ('3', 'Wi-Fi分享器', '多人共用一條線路。多一樣要充電、要歸還的東西'),
        ('!', '需要打電話、收簡訊?', '選含通話與簡訊的方案', True)]},
})

D['essentials-4'] = (cards, {
    'en': {'title': 'Four cards, and how you pay for them', 'cards': [
        ('T', 'T-money', 'Convenience stores and station machines. Top-ups usually need won cash'),
        ('A', 'AREX T-money card', '₩15,000 at the airport railroad stations. Foreign credit cards OK'),
        ('W', 'WOWPASS', 'Load it at machines in major stations, in your home currency'),
        ('C', 'Climate Card (short-term)', 'Seoul only. New machines at 273 stations take Visa and Mastercard')]},
    'ko': {'title': '카드 네 가지, 결제 방법', 'cards': [
        ('T', '티머니', '편의점·역 기계. 충전은 대개 현금'),
        ('A', '공항철도 티머니 카드', '공항철도역에서 1만 5천 원. 해외 신용카드 가능'),
        ('W', 'WOWPASS', '주요 역 기계에서 자국 통화로 충전'),
        ('C', '기후동행카드 단기권', '서울 전용. 273개 역 새 기계가 비자·마스터 결제')]},
    'ja': {'title': '4つのカードと支払い方', 'cards': [
        ('T', 'T-money', 'コンビニ・駅の機械で。チャージは基本ウォン現金'),
        ('A', '空港鉄道のT-moneyカード', '空港鉄道の駅で1万5千ウォン。海外クレジットカード可'),
        ('W', 'WOWPASS', '主要駅の機械で、自国通貨でチャージ'),
        ('C', '気候同行カード短期券', 'ソウル限定。273駅の新しい券売機でVisa・Mastercard可')]},
    'zh-tw': {'title': '四種卡,怎麼付錢', 'cards': [
        ('T', 'T-money', '超商、車站機器。儲值通常要韓元現金'),
        ('A', '機場快線T-money卡', '機場快線車站1萬5千韓元。可刷海外信用卡'),
        ('W', 'WOWPASS', '主要車站機器,用本國貨幣儲值'),
        ('C', '氣候同行卡短期券', '僅限首爾。273站新售票機收Visa、Mastercard')]},
})

D['essentials-5'] = (phone_apps, {
    'en': {'title': 'Your phone on day one', 'apps': [('Naver Map', 'Walking, subway, bus'), ('Kakao Map', 'A second opinion'), ('Kakao T', 'Taxis'),
                                                       ('Papago', 'Point the camera at a menu'), ('Subway Korea', 'Routes, works offline'), ('Korail+', 'KTX tickets')]},
    'ko': {'title': '첫날 휴대폰 첫 화면', 'apps': [('네이버 지도', '도보·지하철·버스 길찾기'), ('카카오맵', '두 번째 의견'), ('카카오 T', '택시'),
                                              ('파파고', '메뉴판에 카메라를'), ('Subway Korea', '노선, 오프라인 가능'), ('코레일+', 'KTX 예매')]},
    'ja': {'title': '初日のスマホのホーム画面', 'apps': [('NAVERマップ', '徒歩・地下鉄・バス'), ('Kakao Map', 'セカンドオピニオン'), ('Kakao T', 'タクシー'),
                                                 ('Papago', 'メニューにカメラを向ける'), ('Subway Korea', '路線、オフライン可'), ('Korail+', 'KTXの予約')]},
    'zh-tw': {'title': '第一天的手機首頁', 'apps': [('NAVER 地圖', '步行、地鐵、公車'), ('Kakao Map', '第二意見'), ('Kakao T', '計程車'),
                                              ('Papago', '相機對準菜單'), ('Subway Korea', '路線,可離線'), ('Korail+', 'KTX訂票')]},
})

D['first-trip-1'] = (cards, {
    'en': {'title': 'Four days, one area a day', 'cards': [
        ('1', 'Arrival', 'Hotel, eat nearby, sleep'), ('2', 'Palace and Bukchon', 'One palace in the morning, the lanes after'),
        ('3', 'One neighborhood', 'Myeongdong, Hongdae or Seongsu'), ('4', 'Slow morning, airport', 'At Incheon 3 hours before departure')]},
    'ko': {'title': '나흘, 하루에 한 지역', 'cards': [
        ('1', '도착', '숙소, 근처에서 식사, 잠'), ('2', '궁궐과 북촌', '오전에 궁 하나, 그다음 골목'),
        ('3', '동네 하나', '명동, 홍대, 성수 중 하나'), ('4', '느긋한 아침, 공항', '출발 3시간 전 인천공항')]},
    'ja': {'title': '4日間、1日1エリア', 'cards': [
        ('1', '到着', 'ホテル、近くで食事、寝る'), ('2', '王宮と北村', '午前に王宮を1つ、そのあと路地へ'),
        ('3', '街を1つ', '明洞、弘大、聖水のどれか'), ('4', 'ゆっくりの朝、空港へ', '出発3時間前に仁川空港')]},
    'zh-tw': {'title': '四天,一天一區', 'cards': [
        ('1', '抵達', '回飯店、附近吃飯、睡覺'), ('2', '宮殿與北村', '上午一座宮殿,之後逛巷弄'),
        ('3', '一個街區', '明洞、弘大或聖水擇一'), ('4', '慢慢的早晨、去機場', '起飛前3小時到仁川機場')]},
}, 'round')

D['first-trip-2'] = (cards, {
    'en': {'title': 'Day one, in order', 'cards': [
        ('1', 'Before you fly', 'File the e-Arrival Card'), ('2', 'At the airport', 'Transport card and data'),
        ('3', 'The ride that suits your hotel', 'Train or bus, by where you sleep'), ('4', 'Drop your bags', 'Walk your block, eat close by'),
        ('✓', 'Nothing booked tonight', 'A late flight costs you nothing', True)]},
    'ko': {'title': '첫날, 순서대로', 'cards': [
        ('1', '출발 전', '전자입국신고서 제출'), ('2', '공항에서', '교통카드와 데이터'),
        ('3', '숙소에 맞는 교통편', '자는 곳 기준으로 열차나 버스'), ('4', '짐 내려놓기', '동네 한 바퀴, 가까운 곳에서 식사'),
        ('✓', '오늘 밤 예약 없음', '비행기가 늦어도 잃을 게 없어요', True)]},
    'ja': {'title': '初日、この順番で', 'cards': [
        ('1', '出発前', '電子入国申告を提出'), ('2', '空港で', '交通カードとデータ'),
        ('3', 'ホテルに合う交通手段', '泊まる場所で電車かバスを選ぶ'), ('4', '荷物を置く', '近所を歩いて、近くで食事'),
        ('✓', '今夜は予約なし', '便が遅れても失うものがない', True)]},
    'zh-tw': {'title': '第一天,照這個順序', 'cards': [
        ('1', '出發前', '填好電子入境卡'), ('2', '在機場', '交通卡和網路'),
        ('3', '適合飯店的交通方式', '依住處選電車或巴士'), ('4', '放下行李', '在附近走走、就近吃飯'),
        ('✓', '今晚什麼都不預約', '航班延誤也不會白白浪費', True)]},
}, 'round_arrows')

D['first-trip-3'] = (week, {
    'en': {'title': 'Which palace on which day', 'days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 'open': 'open', 'closed': 'shut',
           'palaces': [('Gyeongbokgung', 1), ('Changdeokgung', 0)],
           'facts': [('Gyeongbokgung, November', '09:00–17:00'), ('Changdeokgung, Nov–Jan', '09:00–17:30, last entry 16:30'),
                     ('Adults ₩3,000', 'Free in hanbok'), ('Bukchon red zones', 'Visitors 10:00–17:00 only')]},
    'ko': {'title': '무슨 요일에 어느 궁?', 'days': ['월', '화', '수', '목', '금', '토', '일'], 'open': '개방', 'closed': '휴궁',
           'palaces': [('경복궁', 1), ('창덕궁', 0)],
           'facts': [('경복궁, 11월', '09:00~17:00'), ('창덕궁, 11~1월', '09:00~17:30, 입장 마감 16:30'),
                     ('어른 3,000원', '한복 착용 시 무료'), ('북촌 레드존', '관광객 방문 10:00~17:00만')]},
    'ja': {'title': '何曜日にどの王宮?', 'days': ['月', '火', '水', '木', '金', '土', '日'], 'open': '開', 'closed': '休',
           'palaces': [('景福宮', 1), ('昌徳宮', 0)],
           'facts': [('景福宮、11月', '09:00~17:00'), ('昌徳宮、11~1月', '09:00~17:30、入場は16:30まで'),
                     ('大人3,000ウォン', '韓服なら無料'), ('北村のレッドゾーン', '観光客の訪問は10:00~17:00だけ')]},
    'zh-tw': {'title': '星期幾去哪座宮?', 'days': ['一', '二', '三', '四', '五', '六', '日'], 'open': '開', 'closed': '休',
              'palaces': [('景福宮', 1), ('昌德宮', 0)],
              'facts': [('景福宮,11月', '09:00–17:00'), ('昌德宮,11–1月', '09:00–17:30,16:30停止入場'),
                        ('成人3,000韓元', '穿韓服免費'), ('北村紅區', '遊客僅限10:00–17:00')]},
})

D['emergency-1'] = (cards, {
    'en': {'title': 'Which number?', 'cards': [
        ('119', 'Ambulance and fire', 'Someone hurt, a fire, can’t breathe'), ('112', 'Police', 'Crime, threat, you feel unsafe'),
        ('1330', 'Travel hotline', 'Interpretation, tourist complaints'), ('1339', 'Health questions', 'Not an emergency'),
        ('1345', 'Immigration', 'Visa and stay')], 'foot': '1330 from abroad: +82-2-1330'},
    'ko': {'title': '어느 번호로?', 'cards': [
        ('119', '구급·화재', '다쳤을 때, 불, 숨쉬기 힘들 때'), ('112', '경찰', '범죄, 위협, 불안할 때'),
        ('1330', '관광통역안내', '통역, 관광 불편 신고'), ('1339', '건강 상담', '응급이 아닐 때'),
        ('1345', '출입국', '비자와 체류')], 'foot': '해외에서 1330: +82-2-1330'},
    'ja': {'title': 'どの番号に?', 'cards': [
        ('119', '救急・消防', 'けが、火事、息が苦しい'), ('112', '警察', '犯罪、脅し、身の危険を感じる'),
        ('1330', '観光案内電話', '通訳、観光の苦情'), ('1339', '健康の相談', '緊急でないとき'),
        ('1345', '出入国', 'ビザと滞在')], 'foot': '海外から1330: +82-2-1330'},
    'zh-tw': {'title': '打哪個號碼?', 'cards': [
        ('119', '救護、火災', '有人受傷、失火、呼吸困難'), ('112', '警察', '犯罪、威脅、覺得不安全'),
        ('1330', '旅遊諮詢熱線', '口譯、觀光申訴'), ('1339', '健康諮詢', '不是急症時'),
        ('1345', '出入境', '簽證與停留')], 'foot': '從國外撥1330: +82-2-1330'},
})

D['emergency-2'] = (cards, {
    'en': {'title': 'Left something in a taxi? Start from how you paid', 'cards': [
        ('A', 'Booked with an app', 'Call or message the driver from the trip record'),
        ('B', 'Paid by transport card', 'T-money 1644-1188, Cashbee 1644-1472. Have the card number ready'),
        ('C', 'Paid cash, no app', 'Note the plate, places and time. Ask 1330 for help')],
        'foot': 'Taxi companies keep items about a week, then hand them to the police.'},
    'ko': {'title': '택시에 두고 내렸다면: 어떻게 냈는지부터', 'cards': [
        ('A', '앱으로 호출', '이용 기록에서 기사에게 전화·메시지'),
        ('B', '교통카드로 결제', '티머니 1644-1188, 캐시비 1644-1472. 카드 번호 준비'),
        ('C', '현금, 앱 없음', '차량 번호, 장소, 시간을 적고 1330에 도움 요청')],
        'foot': '택시 회사는 유실물을 1주일쯤 보관하고 경찰로 넘겨요.'},
    'ja': {'title': 'タクシーに忘れ物?払い方から考える', 'cards': [
        ('A', 'アプリで呼んだ', '利用履歴から運転手に電話・メッセージ'),
        ('B', '交通カードで払った', 'T-money 1644-1188、Cashbee 1644-1472。カード番号を手元に'),
        ('C', '現金、アプリなし', 'ナンバー、場所、時間をメモして1330に相談')],
        'foot': 'タクシー会社は約1週間保管し、その後警察へ渡します。'},
    'zh-tw': {'title': '東西忘在計程車上?先看你怎麼付錢', 'cards': [
        ('A', '用App叫車', '從行程紀錄打電話或傳訊息給司機'),
        ('B', '用交通卡付款', 'T-money 1644-1188、Cashbee 1644-1472。準備好卡號'),
        ('C', '付現金、沒用App', '記下車牌、地點、時間,請1330協助')],
        'foot': '計程車公司約保管一週,之後交給警察。'},
})

D['emergency-3'] = (cards, {
    'en': {'title': 'Lost passport: three stops', 'cards': [
        ('1', 'Police box: 지구대 or 파출소', 'Ask for a loss report confirmation: 분실신고 확인서'),
        ('2', 'Your embassy', 'Passport photos, the police report, your flight details'),
        ('3', 'Questions about your stay?', 'Call 1345')]},
    'ko': {'title': '여권 분실: 세 곳만', 'cards': [
        ('1', '지구대·파출소', '분실신고 확인서 받기'),
        ('2', '자국 대사관', '여권 사진, 경찰 확인서, 항공편 정보'),
        ('3', '체류 관련 문의', '1345에 전화')]},
    'ja': {'title': 'パスポート紛失:3か所', 'cards': [
        ('1', '交番:지구대・파출소', '紛失届の確認書(분실신고 확인서)をもらう'),
        ('2', '日本大使館・総領事館', 'パスポート用写真、警察の確認書、航空便の情報'),
        ('3', '滞在について質問', '1345に電話')]},
    'zh-tw': {'title': '護照遺失:三個地方', 'cards': [
        ('1', '派出所:지구대或파출소', '申請遺失報案確認書(분실신고 확인서)'),
        ('2', '駐韓代表處', '護照照片、警方確認書、航班資訊'),
        ('3', '停留相關問題', '撥1345')]},
}, 'round_arrows')

D['emergency-4'] = (phrases, {
    'en': {'title': 'Save this image. Show it to someone nearby', 'cards': [
        ('112', '도와주세요. 112(경찰)에 신고해 주시겠어요?', 'Please call the police (112) for me.'),
        ('119', '구급차를 불러 주세요. 119에 전화해 주세요.', 'Please call an ambulance (119).'),
        ('1330', '한국어를 못 해요. 1330에 전화해 주실 수 있나요?', 'I don’t speak Korean. Please call 1330.')]},
    'ko': {'title': '이 이미지를 저장해 두고 옆 사람에게 보여 주세요', 'cards': [
        ('112', '도와주세요. 112(경찰)에 신고해 주시겠어요?', 'Please call the police (112) for me.'),
        ('119', '구급차를 불러 주세요. 119에 전화해 주세요.', 'Please call an ambulance (119).'),
        ('1330', '한국어를 못 해요. 1330에 전화해 주실 수 있나요?', 'I don’t speak Korean. Please call 1330.')]},
    'ja': {'title': 'この画像を保存して、近くの人に見せる', 'cards': [
        ('112', '도와주세요. 112(경찰)에 신고해 주시겠어요?', '警察(112)に通報してもらえますか?'),
        ('119', '구급차를 불러 주세요. 119에 전화해 주세요.', '救急車(119)を呼んでください。'),
        ('1330', '한국어를 못 해요. 1330에 전화해 주실 수 있나요?', '韓国語が話せません。1330に電話してもらえますか?')]},
    'zh-tw': {'title': '存下這張圖,給旁邊的人看', 'cards': [
        ('112', '도와주세요. 112(경찰)에 신고해 주시겠어요?', '可以幫我報警(112)嗎?'),
        ('119', '구급차를 불러 주세요. 119에 전화해 주세요.', '請幫我叫救護車(119)。'),
        ('1330', '한국어를 못 해요. 1330에 전화해 주실 수 있나요?', '我不會說韓語。可以幫我打1330嗎?')]},
})

D['convenience-store-1'] = (cards, {
    'en': {'title': 'Loading T-money at the counter', 'cards': [
        ('1', 'Hand over the card and won cash', ''), ('2', 'Say how much', 'Or say “충전해 주세요” (please top it up)'),
        ('3', 'Staff load it', 'Keep the card; the gate shows your balance'),
        ('!', 'No won cash?', 'iPhone: MobileTmoney with Mastercard, Amex or UnionPay (not Visa). Airport: the AREX T-money card, ₩15,000, foreign cards OK', True)]},
    'ko': {'title': '계산대에서 티머니 충전하기', 'cards': [
        ('1', '카드와 현금을 건네기', ''), ('2', '금액 말하기', '“만 원 충전해 주세요”처럼'),
        ('3', '직원이 충전', '카드는 그대로, 개찰구에 잔액이 떠요'),
        ('!', '현금이 없다면?', '아이폰: 모바일티머니에 마스터·아멕스·유니온페이(비자 불가). 공항: 공항철도 티머니 카드 1만 5천 원, 해외 카드 가능', True)]},
    'ja': {'title': 'レジでT-moneyをチャージ', 'cards': [
        ('1', 'カードとウォン現金を渡す', ''), ('2', '金額を伝える', '「충전해 주세요(チャージしてください)」'),
        ('3', '店員がチャージ', '改札で残高が表示されます'),
        ('!', 'ウォン現金がない?', 'iPhone:モバイルT-moneyにMastercard・Amex・銀聯(Visa不可)。空港:空港鉄道のT-moneyカード1万5千ウォン、海外カード可', True)]},
    'zh-tw': {'title': '在櫃台儲值T-money', 'cards': [
        ('1', '交出卡片和韓元現金', ''), ('2', '說要儲多少', '或說「충전해 주세요」(請幫我儲值)'),
        ('3', '店員儲值', '過閘門時會顯示餘額'),
        ('!', '沒有韓元現金?', 'iPhone:Mobile T-money綁Mastercard、Amex、銀聯(不收Visa)。機場:機場快線T-money卡1萬5千韓元,可刷海外卡', True)]},
}, 'round_arrows')

D['convenience-store-2'] = (tags, {
    'en': {'title': 'Reading the deal tag', 'tags': [('1+1', 'Buy one, get a second free'), ('2+1', 'Buy two, get a third free')],
           'calc': ('Worth it?', 'Price ÷ items you get = price per item. Compare with a supermarket'),
           'foot': 'Deals change monthly; some items sell out early.'},
    'ko': {'title': '행사 가격표 읽기', 'tags': [('1+1', '하나 사면 하나 더'), ('2+1', '두 개 사면 하나 더')],
           'calc': ('이득일까?', '가격 ÷ 받는 개수 = 개당 가격. 대형마트와 비교'),
           'foot': '행사는 달마다 바뀌고, 일찍 품절되는 상품도 있어요.'},
    'ja': {'title': 'セール札の読み方', 'tags': [('1+1', '1つ買うと、もう1つ無料'), ('2+1', '2つ買うと、3つ目が無料')],
           'calc': ('本当にお得?', '価格 ÷ もらえる個数 = 1個の値段。スーパーと比べる'),
           'foot': 'セールは月ごとに変わり、早く売り切れる商品もあります。'},
    'zh-tw': {'title': '看懂優惠標籤', 'tags': [('1+1', '買一送一'), ('2+1', '買二送一')],
              'calc': ('划算嗎?', '價格 ÷ 拿到的件數 = 單件價格。和大型超市比'),
              'foot': '優惠每月更換,有些商品會提早賣完。'},
})

D['convenience-store-3'] = (cards, {
    'en': {'title': 'The ramyeon machine (some CU stores)', 'cards': [
        ('1', 'Buy a packet of ramyeon', ''), ('2', 'Pay the machine charge', '₩900 when the Korea Herald reported it'),
        ('3', 'The machine cooks it', 'In a disposable bowl'),
        ('!', 'No machine?', 'Cup ramyeon works at any store', True)]},
    'ko': {'title': '라면 조리기 (일부 CU 매장)', 'cards': [
        ('1', '봉지 라면 사기', ''), ('2', '조리기 이용료 내기', '코리아헤럴드 보도 당시 900원'),
        ('3', '기계가 끓여 줌', '일회용 용기에'),
        ('!', '조리기가 없다면?', '컵라면은 어느 매장에서나', True)]},
    'ja': {'title': 'ラーメン調理機(一部のCU)', 'cards': [
        ('1', '袋ラーメンを買う', ''), ('2', '調理機の料金を払う', 'コリア・ヘラルド報道時は900ウォン'),
        ('3', '機械が調理', '使い捨て容器で'),
        ('!', '調理機がない?', 'カップ麺ならどの店でも', True)]},
    'zh-tw': {'title': '泡麵調理機(部分CU門市)', 'cards': [
        ('1', '買一包袋裝泡麵', ''), ('2', '付調理機費用', '《韓國先驅報》報導時為900韓元'),
        ('3', '機器幫你煮', '裝在一次性碗裡'),
        ('!', '沒有調理機?', '杯麵哪家店都有', True)]},
}, 'round_arrows')


def main():
    only = set(a for a in sys.argv[2:])
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
