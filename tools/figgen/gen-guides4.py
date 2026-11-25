"""Figures for health, skin-clinic, concert-trip (2026-11-26 revision).

Phone-first: viewBox width 400, min font-size 16. Text matches the page facts (no new facts).
usage: python3 gen-guides4.py <outdir>      (writes <outdir>/<lang>/<name>.svg)
Owner of: health-1..5, skin-clinic-1..3, concert-trip-1..3.
"""
import os
import re
import sys
from xml.sax.saxutils import escape as _e

FONT = 'system-ui, -apple-system, &quot;Noto Sans KR&quot;, &quot;Noto Sans JP&quot;, &quot;Noto Sans TC&quot;, sans-serif'
INK, RED, PAPER, MUTED, RULE, WHITE, SOFT = '#16151a', '#b8392f', '#f4f0e6', '#5f5b55', '#c9c1b2', '#ffffff', '#e9e2d3'
W = 400
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
LANGS = ['en', 'ko', 'ja', 'zh-tw']


def e(s):
    return _e(s, {'"': '&quot;'})


def cw(ch, size, bold):
    o = ord(ch)
    if o >= 0x1100 and not (0x2000 <= o <= 0x206f):
        w = 1.0
    elif ch == ' ':
        w = 0.3
    elif ch in 'il.,:;|!\'()[]':
        w = 0.32
    elif ch.isupper() or ch in 'mwMW₩%@':
        w = 0.7
    else:
        w = 0.56
    return w * size * (1.06 if bold else 1.0)


def tw(s, size=16, bold=False):
    return sum(cw(c, size, bold) for c in s)


def wrap(s, maxw, size=16, bold=False):
    toks = re.findall(r'[A-Za-z0-9₩$%.,:;/()\'+\-–~&@?!*\uac00-\ud7a3·~]+[ ]?|[ ]|.', s)  # Hangul wraps at spaces, Han/Kana per character
    lines, cur = [], ''
    for t in toks:
        if tw((cur + t).rstrip(), size, bold) <= maxw or not cur.strip():
            cur += t
        else:
            if t in '、。,):」』,.' and len(t) == 1:  # keep closing punctuation on the line
                cur += t
                continue
            lines.append(cur.rstrip())
            cur = t.lstrip()
    if cur.strip():
        lines.append(cur.rstrip())
    return lines


def T(x, y, s, size=16, w='400', fill=INK, anchor='start'):
    assert size >= 16, (s, size)
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{e(s)}</text>\n'


def R(x, y, w, h, fill=WHITE, stroke=RULE, sw=1.5, rx=10, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>\n'


def L(x1, y1, x2, y2, c=RULE, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}"{d}/>\n'


def C(cx, cy, r, fill=WHITE, stroke=INK, sw=2):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>\n'


def arrow_down(x, y1, y2, c=INK):
    return L(x, y1, x, y2 - 8, c, 2.5) + f'<path d="M{x - 7},{y2 - 10} L{x},{y2} L{x + 7},{y2 - 10} z" fill="{c}"/>\n'


def check(x, y, c=INK):
    return f'<path d="M{x + 3},{y + 11} L{x + 8},{y + 16} L{x + 18},{y + 4}" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>\n'


def cross(x, y, c=RED):
    return (f'<path d="M{x + 4},{y + 4} L{x + 16},{y + 16} M{x + 16},{y + 4} L{x + 4},{y + 16}" '
            f'stroke="{c}" stroke-width="3" stroke-linecap="round"/>\n')


class Fig:
    def __init__(self, title):
        self.title = title
        self.tl = wrap(title, 360, 20, True)
        self.body = ''
        self.y = 34 + 26 * (len(self.tl) - 1) + 14

    def add(self, s):
        self.body += s

    def svg(self, pad=18):
        h = self.y + pad
        t = ''.join(T(20, 34 + 26 * i, s, 20, '700') for i, s in enumerate(self.tl))
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" role="img" aria-label="{e(self.title)}" '
                f'font-family="{FONT}">\n<title>{e(self.title)}</title>\n'
                f'<rect width="{W}" height="{h}" fill="{PAPER}"/>\n{t}{self.body}</svg>\n')

    # numbered / badged cards: items = [(badge, head, sub)] ; badge '' -> no badge
    def cards(self, items, gap=10, red_first=True, x=16, w=368, arrows=False):
        for i, (badge, head, sub) in enumerate(items):
            bw = max(40, tw(badge, 16, True) + 18) if badge else 0
            top = bw > 60  # long badge (phone number): own line above the text
            tx = x + 14 if (top or not badge) else x + 24 + bw
            mw = w - (tx - x) - 20
            hl = wrap(head, mw, 17, True)
            sl = wrap(sub, mw, 16) if sub else []
            h = 16 + 22 * len(hl) + 22 * len(sl) + 12 + (44 if top else 0)
            h = max(h, 60)
            y0 = self.y + gap
            self.add(R(x, y0, w, h, WHITE, RULE, 1.5))
            if badge:
                self.add(R(x + 12, y0 + 12, bw, 36, RED if (red_first or i) else INK, 'none', 0, 8))
                self.add(T(x + 12 + bw / 2, y0 + 36, badge, 16, '700', WHITE, 'middle'))
            yy = y0 + 12 + (44 if top else 0)
            for s in hl:
                yy += 22
                self.add(T(tx, yy, s, 17, '700'))
            for s in sl:
                yy += 22
                self.add(T(tx, yy, s, 16, '400', MUTED))
            self.y = y0 + h
            if arrows and i < len(items) - 1:
                self.add(arrow_down(x + 32 if badge else W // 2, self.y + 1, self.y + gap + 9))
                self.y += 10

    def note(self, text, red=True):
        ls = wrap(text, 340, 16, True)
        h = 16 + 22 * len(ls)
        y0 = self.y + 12
        self.add(R(16, y0, 368, h, SOFT, RED if red else RULE, 2 if red else 1.5))
        yy = y0 + 8
        for s in ls:
            yy += 22
            self.add(T(30, yy - 4, s, 16, '700', RED if red else INK))
        self.y = y0 + h

    def text(self, s, size=16, w='400', fill=MUTED, x=20, mw=360):
        for ln in wrap(s, mw, size, w == '700'):
            self.y += 22
            self.add(T(x, self.y, ln, size, w, fill))


def write(lang, name, svg):
    p = os.path.join(OUT, lang, f'{name}.svg')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(svg)


# ---------------------------------------------------------------- health
H1 = {  # numbers to save
    'en': ('Save these three numbers', [
        ('119', 'Ambulance and fire', '24 hours. Chest pain, trouble breathing, fainting, heavy bleeding, a bad injury'),
        ('1339', 'KDCA health call center', '24 hours, every day. Free from a Korean number. From abroad +82-2-2633-1339'),
        ('1330', 'Three-way call when language is the problem', 'Hours and languages: Everyday Korea page')],
        'Not sure which one? Call 1339.'),
    'ko': ('저장해 둘 번호 세 개', [
        ('119', '구급·소방', '24시간. 심한 가슴 통증, 호흡 곤란, 의식 잃음, 큰 출혈, 큰 부상'),
        ('1339', '질병관리청 콜센터', '365일 24시간. 국내 번호로 걸면 무료. 해외에서는 +82-2-2633-1339'),
        ('1330', '말이 안 통할 때 3자 통화', '운영 시간과 언어: 생활 정보 페이지')],
        '어디로 가야 할지 모르겠다면 1339'),
    'ja': ('保存しておく3つの番号', [
        ('119', '救急・消防', '24時間。激しい胸の痛み、息苦しさ、意識がない、大量出血、大けが'),
        ('1339', '疾病管理庁コールセンター', '365日24時間。韓国の番号からは無料。海外から+82-2-2633-1339'),
        ('1330', '言葉が通じないときの三者通話', '日本語対応と受付時間:暮らしのルールのページ')],
        '迷ったら1339へ'),
    'zh-tw': ('先存好這 3 個電話', [
        ('119', '救護車與消防', '24 小時。劇烈胸痛、呼吸困難、昏倒、大量出血、重傷'),
        ('1339', '疾病管理廳專線', '365 天 24 小時,韓國號碼撥打免費。國外撥 +82-2-2633-1339'),
        ('1330', '語言不通時的三方通話', '中文服務時間:韓國生活小規則頁')],
        '不知道該去哪?打 1339'),
}

H2 = {  # convenience-store shelf
    'en': dict(t='The medicine shelf at a 24-hour convenience store',
               bins=['Fever & pain', 'Cold', 'Digestion', 'Pain patches'],
               n='11 products in practice (13 designated, 2 no longer made)',
               rules=[('ok', 'Only registered stores open 24 hours, all year'), ('ok', 'One pack per product per purchase'),
                      ('no', 'No pharmacist to ask'), ('no', 'Not on the list: diarrhea medicine, burn cream')],
               tip='Symptoms continue? See a clinic.'),
    'ko': dict(t='24시간 편의점의 상비약 선반',
               bins=['해열진통제', '감기약', '소화제', '파스'],
               n='실제로는 11개 품목(지정 13개 중 2개 생산 중단)',
               rules=[('ok', '등록한 연중무휴 24시간 점포만'), ('ok', '같은 약은 한 번에 한 통만'),
                      ('no', '약사 상담 없음'), ('no', '목록에 없는 것: 지사제, 화상 연고')],
               tip='증상이 이어지면 의원으로'),
    'ja': dict(t='24時間コンビニの常備薬の棚',
               bins=['解熱鎮痛薬', '風邪薬', '消化薬', '湿布'],
               n='実際は11品目(指定13品目のうち2品目は生産中止)',
               rules=[('ok', '登録した年中無休・24時間の店だけ'), ('ok', '同じ薬は1回に1箱まで'),
                      ('no', '薬剤師はいない'), ('no', '下痢止め・やけどの軟膏はない')],
               tip='症状が続くならクリニックへ'),
    'zh-tw': dict(t='24 小時便利商店的常備藥架',
                  bins=['退燒止痛', '感冒藥', '消化藥', '貼布'],
                  n='實際 11 項(指定 13 項,2 項已停產)',
                  rules=[('ok', '只有登記、全年無休 24 小時的店'), ('ok', '同一種藥一次只能買 1 盒'),
                         ('no', '沒有藥師'), ('no', '沒有止瀉藥、燙傷藥膏')],
                  tip='症狀持續就去診所'),
}

H3 = {  # pharmacy sign + finding open ones
    'en': dict(t='Find the sign, then find one that is open', sign='= medicine (pharmacy)',
               items=[('1', 'E-Gen (e-gen.or.kr)', 'Area → pharmacy → date or holiday'),
                      ('2', 'Late-night pharmacies', 'Designated by local governments: often 10 p.m. to midnight or later'),
                      ('3', 'Holiday pharmacies', 'Weekend and holiday hours on pharm114.or.kr')],
               tip='Korean-only at midnight? Call 1339 or ask your hotel front desk.'),
    'ko': dict(t='간판을 찾고, 문 연 곳을 찾기', sign='= 약국',
               items=[('1', '이젠(e-gen.or.kr)', '지역 → 약국 → 날짜나 연휴'),
                      ('2', '공공심야약국', '지자체 지정, 보통 밤 10시부터 자정이나 새벽까지'),
                      ('3', '휴일지킴이 약국', 'pharm114.or.kr에서 주말·휴일 영업시간')],
               tip='외국인 친구에게 어렵다면 대신 찾아 주거나 1339'),
    'ja': dict(t='看板を見つけ、開いている薬局へ', sign='= 薬(薬局)',
               items=[('1', 'E-Gen(e-gen.or.kr)', '地域 → 薬局 → 日付や連休'),
                      ('2', '深夜薬局', '自治体の指定。たいてい夜10時から深夜0時か明け方まで'),
                      ('3', '休日当番薬局', '週末・休日の営業時間はpharm114.or.kr')],
               tip='韓国語のサイトがつらければ1339かホテルのフロントへ'),
    'zh-tw': dict(t='先認招牌,再找有開的', sign='= 藥(藥局)',
                  items=[('1', 'E-Gen(e-gen.or.kr)', '選地區 → 藥局 → 日期或連假'),
                         ('2', '深夜藥局', '地方政府指定,通常晚上 10 點開到午夜或清晨'),
                         ('3', '假日值班藥局', '週末和假日營業時間查 pharm114.or.kr')],
                  tip='看不懂韓文網站?打 1339 或請飯店櫃台幫忙'),
}

H4 = {  # clinic visit
    'en': dict(t='A clinic visit without Korean insurance',
               items=[('1', 'Pick a small clinic (uiwon)', 'Colds, skin trouble, an upset stomach. Hospitals are for scans, admission, surgery'),
                      ('2', 'Bring your passport', ''),
                      ('3', 'Pay the full price yourself', 'Typical clinic visit: about ₩30,000–60,000 without insurance (Naeil Shinmun)'),
                      ('4', 'Ask for an itemized receipt in English', 'Keep every receipt for your insurance claim')]),
    'ko': dict(t='국내 건강보험 없이 의원에 갈 때',
               items=[('1', '동네 의원을 고르기', '감기, 피부 트러블, 배탈. 검사·입원·수술은 병원으로'),
                      ('2', '여권 챙기기', ''),
                      ('3', '진료비는 전액 본인 부담', '의원 진료비: 보험 없으면 약 30,000~60,000원(내일신문)'),
                      ('4', '영수증과 진료비 세부내역서 받기', '보험 청구용으로 모두 보관')]),
    'ja': dict(t='韓国の保険なしでクリニックへ',
               items=[('1', '街の医院(クリニック)を選ぶ', '風邪、肌荒れ、おなかの不調。精密検査・入院・手術は病院へ'),
                      ('2', 'パスポートを持って行く', ''),
                      ('3', '診療費は全額自己負担', '医院の受診:保険なしで約30,000〜60,000ウォン(内日新聞)'),
                      ('4', '領収書と明細をもらう', '海外旅行保険の請求に使います')]),
    'zh-tw': dict(t='沒有韓國健保去診所',
                  items=[('1', '選巷口診所(의원)', '感冒、皮膚問題、拉肚子。檢查、住院、手術才去醫院'),
                         ('2', '帶護照', ''),
                         ('3', '全額自費', '診所看一次:沒保險約 30,000~60,000 韓元(內日新聞)'),
                         ('4', '拿收據和費用明細', '回台灣申請保險理賠用')]),
}

H5 = {  # bringing medicine
    'en': dict(t='Can I bring my medicine into Korea?',
               q='Does it contain a narcotic or psychotropic ingredient?', qs='Check ingredients, not brand names (e.g. dextromethorphan)',
               yes='Yes', no='No',
               ya='Get MFDS approval before you fly', ys='Apply on Drug Safety Korea. Allow up to 10 business days',
               na='Up to 6 bottles', ns='More than that: up to 3 months\' supply by the label',
               foot='The six-bottle rule applies from 12 November 2026. The medicine must be prescribed or bought legally.'),
    'ko': dict(t='가져오는 약, 반입될까?',
               q='마약류·향정신성 성분이 들었나요?', qs='상품명이 아니라 성분 확인(예: 덱스트로메토르판)',
               yes='예', no='아니요',
               ya='입국 전에 식약처 승인', ys='의약품안전나라에서 신청, 최대 10영업일',
               na='6병까지', ns='그보다 많으면 용법 기준 3개월분 이내',
               foot='6병 기준은 2026년 11월 12일부터. 정상적으로 처방받거나 산 약이어야 해요.'),
    'ja': dict(t='日本から持っていく薬、入れられる?',
               q='麻薬・向精神薬の成分を含む?', qs='商品名ではなく成分で確認(例:デキストロメトルファン)',
               yes='はい', no='いいえ',
               ya='入国前にMFDSの承認', ys='医薬品安全ナラで申請。最大10営業日',
               na='6本(瓶)まで', ns='超える場合は用法に沿って3か月分以内',
               foot='6本(瓶)の基準は2026年11月12日から。正規に処方・購入した薬が条件です。'),
    'zh-tw': dict(t='自己的藥,能帶進韓國嗎?',
                  q='含麻醉或精神藥物成分嗎?', qs='看成分,不要只看品名(例:右美沙芬)',
                  yes='是', no='否',
                  ya='入境前取得 MFDS 核准', ys='在醫藥品安全 Nara 申請,預留最多 10 個工作天',
                  na='6 瓶以內', ns='超過的話依用法 3 個月份以內',
                  foot='6 瓶的規定自 2026 年 11 月 12 日起。須為合法處方或購買的藥。'),
}

# ---------------------------------------------------------------- skin-clinic
S1 = {
    'en': dict(t='Check the clinic before you book',
               items=[('1', 'Copy the clinic\'s Korean name', 'The registry site is in Korean'),
                      ('2', 'Search the Medical Korea registry', 'medicalkorea.or.kr: by name, type and region'),
                      ('3', 'Is it registered and active?', 'Check the agency or booking app the same way')],
               cert='Registration certificate', certs='Must be posted where anyone can see it',
               tip='Registration is not a quality rating.'),
    'ko': dict(t='예약 전에 의료기관 조회',
               items=[('1', '의료기관의 한글 이름 복사', ''),
                      ('2', '메디컬코리아 등록 명단에서 검색', 'medicalkorea.or.kr: 이름·종류·지역'),
                      ('3', '등록돼 있고 유효한가?', '유치업자(에이전시·앱)도 같은 방법으로')],
               cert='외국인환자 유치 등록증', certs='누구나 볼 수 있게 게시해야 해요',
               tip='등록은 품질 평가가 아니에요'),
    'ja': dict(t='予約前にクリニックを確認',
               items=[('1', 'クリニックのハングル名をコピー', '登録システムは韓国語のサイトです'),
                      ('2', 'Medical Korea の登録名簿で検索', 'medicalkorea.or.kr:名前・種類・地域'),
                      ('3', '登録済みで有効?', '代理店や予約アプリも同じように確認')],
               cert='外国人患者誘致の登録証', certs='誰でも見える場所に掲示する決まり',
               tip='登録は品質の評価ではありません'),
    'zh-tw': dict(t='預約前先查診所',
                  items=[('1', '複製診所的韓文名稱', '查詢網站是韓文'),
                         ('2', '到 Medical Korea 登錄名單查詢', 'medicalkorea.or.kr:名稱、類型、地區'),
                         ('3', '有登錄、狀態有效嗎?', '仲介或預約 App 也用同樣方法查')],
                  cert='外國患者招攬登錄證', certs='依法要貼在任何人都看得到的地方',
                  tip='登錄不等於品質評等'),
}

S2 = {
    'en': dict(t='What a registered clinic must give you in writing',
               rows=['Diagnosis', 'Treatment method', 'Possible side effects', 'Treatment contract and estimated cost', 'Dispute procedure if something goes wrong'],
               foot='In a language you can read, before you sign',
               ask='Ask the doctor: who does it, follow-up, when you can fly'),
    'ko': dict(t='등록 의료기관이 따로 알려 줘야 하는 것',
               rows=['진단명', '치료 방법', '생길 수 있는 부작용', '진료계약서와 예상 진료비', '의료사고 때 분쟁 해결 절차'],
               foot='서명 전에, 읽을 수 있는 언어로',
               ask='의사에게: 누가 시술하는지, 사후 관리, 비행기 타도 되는 날'),
    'ja': dict(t='登録医療機関が書面で示すこと',
               rows=['診断名', '治療方法', '起こりうる副作用', '診療契約書と費用の見積もり', '医療事故のときの紛争解決手続き'],
               foot='署名する前に、読める言語で',
               ask='医師に:誰が施術するか、経過観察、飛行機に乗れる日'),
    'zh-tw': dict(t='登錄機構必須另外給你的說明',
                  rows=['診斷', '治療方法', '可能的副作用', '診療契約書與預估費用', '醫療事故的爭議處理程序'],
                  foot='簽名前,用你看得懂的語言',
                  ask='問醫師:誰執行、回診安排、何時可以搭機'),
}

S3 = {
    'en': ('Who to call, in your language', [
        ('1577-7129', 'Medical Korea information center', '24 hours. Korean, English, Japanese, Chinese, Russian, Arabic. Complaints and disputes'),
        ('HiKR', 'Korea Medical Tourism Business Center', '40 Cheonggyecheon-ro, Seoul. English, Chinese, Japanese, Russian. Weekdays 9:00–18:00'),
        ('1670-2545', 'Medical dispute counseling (K-Medi)', 'Free. Weekdays 9:00–12:00 and 13:00–18:00')]),
    'ko': ('외국어로 도움받을 곳', [
        ('1577-7129', '메디컬코리아 상담센터', '24시간. 한국어·영어·일본어·중국어·러시아어·아랍어. 민원·분쟁 접수'),
        ('HiKR', '의료관광 비즈니스센터', '서울 청계천로 40. 영어·중국어·일본어·러시아어. 평일 9:00~18:00'),
        ('1670-2545', '한국의료분쟁조정중재원 상담', '무료. 평일 9:00~12:00, 13:00~18:00')]),
    'ja': ('日本語で相談できる窓口', [
        ('1577-7129', 'メディカルコリア情報センター', '24時間。日本語あり(韓・英・中・露・アラビア語も)。苦情・紛争の受付'),
        ('HiKR', '医療観光ビジネスセンター', 'ソウル・清渓川路40。英・中・日・露語。平日9:00〜18:00'),
        ('1670-2545', '韓国医療紛争調停仲裁院', '無料相談。平日9:00〜12:00、13:00〜18:00')]),
    'zh-tw': ('可以用中文求助的地方', [
        ('1577-7129', 'Medical Korea 資訊中心', '24 小時。有中文(另有韓、英、日、俄、阿拉伯語)。受理申訴與糾紛'),
        ('HiKR', '醫療觀光商務中心', '首爾清溪川路 40 號。英、中、日、俄語。平日 9:00–18:00'),
        ('1670-2545', '韓國醫療糾紛調解仲裁院', '免費諮詢。平日 9:00–12:00、13:00–18:00')]),
}

# ---------------------------------------------------------------- concert-trip
K1 = {
    'en': dict(t='Buying a K-pop ticket from abroad',
               items=[('1', 'Read the agency\'s notice', 'It names the one site that sells the show'),
                      ('2', 'Make an account on the global site', 'Often NOL World (world.nol.com). Separate from a Korean account'),
                      ('3', 'Verify your passport', '"Verified Member Only" listings need this first'),
                      ('4', 'Book in your passport name', 'Exact romanized spelling. Limits differ by show'),
                      ('5', 'Pick up on site', 'Physical ID + booking confirmation. The booker only')],
               tip='Resale ticket offered? Walk away.'),
    'ko': dict(t='해외에서 K팝 티켓 사기',
               items=[('1', '소속사 공지 확인', '그 공연을 파는 사이트가 한 곳 나와 있어요'),
                      ('2', '글로벌 사이트에 가입', '흔히 NOL World(world.nol.com). 한국 계정과 별도'),
                      ('3', '여권 인증', '"Verified Member Only" 공연은 먼저 인증'),
                      ('4', '여권 이름으로 예매', '로마자 철자 그대로. 매수 제한은 공연마다 달라요'),
                      ('5', '현장 수령', '실물 신분증 + 예매 확인. 예매자 본인만')],
               tip='되팔이 표는 받지 마세요'),
    'ja': dict(t='K-POPチケットを海外から買う流れ',
               items=[('1', '事務所の公式告知を見る', 'その公演を売るサイトが1か所書いてあります'),
                      ('2', 'グローバル版に登録', '多くはNOL World(world.nol.com)。韓国のアカウントとは別'),
                      ('3', 'パスポート認証', '「Verified Member Only」の公演は先に認証'),
                      ('4', 'パスポートの名前で予約', 'ローマ字のつづりどおり。枚数制限は公演ごと'),
                      ('5', '会場で受け取り', '身分証の実物+予約確認。予約した本人だけ')],
               tip='転売チケットには手を出さない'),
    'zh-tw': dict(t='從國外買韓團演唱會門票',
                  items=[('1', '看經紀公司公告', '會寫明唯一販售的網站'),
                         ('2', '註冊國際版網站', '常見是 NOL World(world.nol.com),和韓國帳號分開'),
                         ('3', '護照認證', '「Verified Member Only」的場次要先認證'),
                         ('4', '用護照姓名訂票', '英文拼法一字不差。張數限制每場不同'),
                         ('5', '現場取票', '實體證件+訂票確認,限訂票本人')],
                  tip='有人轉賣票給你?別買'),
}

K2 = {
    'en': dict(t='Four venues and how to reach them', river='Han River', w='West', e='East', air='Incheon Airport', nts='Schematic, not to scale',
               v=[('KSPO Dome', 'Olympic Park Stn, Lines 5 and 9, Exit 4, about 7 min walk', 'About 15,000 seats. Stay: Gangnam or Jamsil'),
                  ('Gocheok Sky Dome', 'Guil Stn, Line 1', 'About 20,000. Stay: an easy ride on Line 1'),
                  ('Seoul World Cup Stadium', 'World Cup Stadium Stn, Line 6', '66,000+. Stay: Hongdae is nearest'),
                  ('Inspire Arena', 'About 15 min by car from the airport', 'About 15,000. Taxi to central Seoul: 1 to 1.5 hours')],
               lab=['KSPO', 'Gocheok', 'World Cup', 'Inspire']),
    'ko': dict(t='공연장 네 곳, 가는 길', river='한강', w='서', e='동', air='인천공항', nts='개략도, 실제 축척 아님',
               v=[('KSPO돔', '5·9호선 올림픽공원역 4번 출구, 걸어서 약 7분', '약 1만 5천 석. 숙소: 강남·잠실'),
                  ('고척스카이돔', '1호선 구일역', '약 2만 명. 숙소: 1호선 타기 쉬운 곳'),
                  ('서울월드컵경기장', '6호선 월드컵경기장역', '6만 6천 석 이상. 숙소: 홍대가 가장 가까워요'),
                  ('인스파이어 아레나', '인천공항에서 차로 약 15분', '약 1만 5천 석. 서울 도심까지 택시 1~1.5시간')],
               lab=['KSPO돔', '고척', '월드컵', '인스파이어']),
    'ja': dict(t='4つの会場と行き方', river='漢江', w='西', e='東', air='仁川空港', nts='略図(縮尺なし)',
               v=[('KSPO DOME', '5・9号線オリンピック公園駅4番出口、徒歩約7分', '約1万5千席。宿:江南か蚕室'),
                  ('高尺スカイドーム', '1号線九一(クイル)駅', '約2万人。宿:1号線に乗りやすい所'),
                  ('ソウルワールドカップ競技場', '6号線ワールドカップ競技場駅', '6万6千席以上。宿:弘大がいちばん近い'),
                  ('インスパイア・アリーナ', '仁川空港から車で約15分', '約1万5千席。ソウル中心部までタクシー1〜1.5時間')],
               lab=['KSPO', '高尺', 'W杯', 'インスパイア']),
    'zh-tw': dict(t='4 個場館怎麼去', river='漢江', w='西', e='東', air='仁川機場', nts='示意圖,非實際比例',
                  v=[('KSPO DOME', '5、9 號線奧林匹克公園站 4 號出口,步行約 7 分鐘', '約 15,000 席。住:江南或蠶室'),
                     ('高尺巨蛋', '1 號線九一站', '約 20,000 人。住:搭 1 號線方便的地方'),
                     ('首爾世界盃競技場', '6 號線世界盃競技場站', '超過 66,000 席。住:弘大最近'),
                     ('Inspire Arena', '離仁川機場車程約 15 分鐘', '約 15,000 席。搭計程車回首爾市中心 1~1.5 小時')],
                  lab=['KSPO', '高尺', '世界盃', 'Inspire']),
}

K3 = {
    'en': dict(t='After the encore: plan the ride home first',
               items=[('1', 'Before the show', 'Check your last train in Naver Map. Know your backup'),
                      ('2', 'KSPO Dome: skip the crowd', 'Walk to Hanseong Baekje (Line 9, about 20 min) or Mongchontoseong (Line 8, about 23 min)'),
                      ('3', 'Missed the last train?', 'Night buses (N routes) or a taxi app')],
               tip='Taxis cost most from 11 p.m. to 2 a.m. (surcharge up to 40%).'),
    'ko': dict(t='앙코르 뒤: 돌아갈 길부터 정하기',
               items=[('1', '공연 전에', '네이버 지도로 막차 확인, 대안 정해 두기'),
                      ('2', 'KSPO돔: 붐비는 역 피하기', '한성백제역(9호선, 걸어서 약 20분)이나 몽촌토성역(8호선, 약 23분)'),
                      ('3', '막차를 놓쳤다면', '심야버스(N번)나 택시 앱')],
               tip='택시는 밤 11시~새벽 2시가 가장 비싸요(최대 40% 할증)'),
    'ja': dict(t='終演後:帰り道を先に決めておく',
               items=[('1', '開演前に', 'NAVERマップで終電を確認、代わりの手段も'),
                      ('2', 'KSPO DOME:混雑を避ける', '漢城百済駅(9号線、徒歩約20分)か夢村土城駅(8号線、約23分)へ'),
                      ('3', '終電を逃したら', '深夜バス(N番)かタクシーアプリ')],
               tip='タクシーは夜11時〜深夜2時がいちばん高い(割増は最大40%)'),
    'zh-tw': dict(t='安可之後:先想好怎麼回去',
                  items=[('1', '開演前', '用 NAVER 地圖查末班車,想好備案'),
                         ('2', 'KSPO DOME:避開人潮', '走到漢城百濟站(9 號線,約 20 分鐘)或夢村土城站(8 號線,約 23 分鐘)'),
                         ('3', '錯過末班車', '深夜公車(N 字頭)或叫車 App')],
                  tip='計程車晚上 11 點到凌晨 2 點最貴(最多加成 40%)'),
}


def numbers_card(d):
    t, items, tip = d
    f = Fig(t)
    f.cards(items)
    f.note(tip)
    return f.svg()


def h2(d):
    f = Fig(d['t'])
    y0 = f.y + 10
    # shelf unit
    f.add(R(16, y0, 368, 210, SOFT, RULE, 1.5, 8))
    for i, b in enumerate(d['bins']):
        col, row = i % 2, i // 2
        x, y = 28 + col * 178, y0 + 14 + row * 98
        f.add(R(x, y, 166, 84, WHITE, RULE, 1.5, 8))
        for k in range(3):  # little boxes
            f.add(R(x + 14 + k * 34, y + 12, 26, 30, SOFT if k else RED, RULE if k else 'none', 1, 4))
        f.add(T(x + 14, y + 68, b, 16, '700'))
    f.y = y0 + 210
    f.text(d['n'], 16, '700', INK)
    f.y += 4
    for kind, s in d['rules']:
        ls = wrap(s, 320, 16)
        f.y += 10
        (f.add(check(20, f.y + 2)) if kind == 'ok' else f.add(cross(20, f.y + 2)))
        for ln in ls:
            f.y += 22
            f.add(T(52, f.y, ln, 16, '400', INK))
    f.note(d['tip'])
    return f.svg()


def h3(d):
    f = Fig(d['t'])
    y0 = f.y + 10
    f.add(R(16, y0, 368, 96, WHITE, RULE, 1.5, 10))
    f.add(R(32, y0 + 14, 92, 68, RED, 'none', 0, 6))
    f.add(T(78, y0 + 62, '약', 40, '700', WHITE, 'middle'))
    ls = wrap(d['sign'], 230, 18, True)
    yy = y0 + 48 - 11 * (len(ls) - 1)
    for ln in ls:
        f.add(T(140, yy + 6, ln, 18, '700'))
        yy += 24
    f.y = y0 + 96
    f.cards(d['items'], red_first=False)
    f.note(d['tip'], red=False)
    return f.svg()


def steps(d, arrows=False):
    f = Fig(d['t'])
    f.cards(d['items'], arrows=arrows)
    if d.get('tip'):
        f.note(d['tip'])
    return f.svg()


def h5(d):
    f = Fig(d['t'])
    f.cards([('?', d['q'], d['qs'])], red_first=False)
    y = f.y
    # two branches
    f.add(L(110, y, 110, y + 30, INK, 2.5) + L(290, y, 290, y + 30, INK, 2.5))
    f.add(R(80, y + 8, 60, 28, RED, 'none', 0, 14) + T(110, y + 28, d['yes'], 16, '700', WHITE, 'middle'))
    f.add(R(260, y + 8, 60, 28, INK, 'none', 0, 14) + T(290, y + 28, d['no'], 16, '700', WHITE, 'middle'))
    y += 44
    hs = []
    for x, head, sub, col in [(16, d['ya'], d['ys'], RED), (204, d['na'], d['ns'], INK)]:
        hl = wrap(head, 156, 17, True)
        sl = wrap(sub, 156, 16)
        hs.append((x, hl, sl, col))
    h = max(16 + 22 * (len(a[1]) + len(a[2])) + 12 for a in hs)
    for x, hl, sl, col in hs:
        f.add(R(x, y, 180, h, WHITE, col, 2, 10))
        yy = y + 12
        for s in hl:
            yy += 22
            f.add(T(x + 12, yy, s, 17, '700', col))
        for s in sl:
            yy += 22
            f.add(T(x + 12, yy, s, 16, '400', MUTED))
    f.y = y + h + 6
    f.text(d['foot'], 16, '400', MUTED)
    return f.svg()


def s1(d):
    f = Fig(d['t'])
    f.cards(d['items'])
    y0 = f.y + 14
    # certificate on a wall
    f.add(R(16, y0, 368, 120, SOFT, RULE, 1.5, 10))
    f.add(R(32, y0 + 16, 88, 88, WHITE, INK, 2, 2))
    for k in range(4):
        f.add(L(46, y0 + 40 + k * 14, 106, y0 + 40 + k * 14, RULE, 3))
    f.add(C(96, y0 + 90, 8, RED, RED, 1))
    hl = wrap(d['cert'], 236, 17, True)
    sl = wrap(d['certs'], 236, 16)
    yy = y0 + 30
    for s in hl:
        f.add(T(134, yy, s, 17, '700'))
        yy += 22
    for s in sl:
        f.add(T(134, yy, s, 16, '400', MUTED))
        yy += 22
    f.y = y0 + 120
    f.note(d['tip'], red=False)
    return f.svg()


def s2(d):
    f = Fig(d['t'])
    y0 = f.y + 10
    rows = [wrap(r, 290, 16) for r in d['rows']]
    h = 24 + sum(14 + 22 * len(r) for r in rows) + 12
    f.add(R(16, y0, 368, h, WHITE, RULE, 1.5, 4))
    f.add(L(16, y0 + 8, 384, y0 + 8, RED, 4))
    yy = y0 + 20
    for r in rows:
        f.add(R(30, yy + 6, 22, 22, WHITE, INK, 2, 3) + check(31, yy + 7, RED))
        for k, ln in enumerate(r):
            f.add(T(66, yy + 23 + 22 * k, ln, 16, '700', INK))
        yy += 14 + 22 * len(r)
        f.add(L(30, yy + 4, 370, yy + 4, SOFT, 1.5))
    f.y = y0 + h
    f.note(d['foot'])
    f.y += 4
    f.text(d['ask'], 16, '400', MUTED)
    return f.svg()


def k2(d):
    f = Fig(d['t'])
    y0 = f.y + 10
    H = 222
    f.add(R(16, y0, 368, H, WHITE, RULE, 1.5, 10))
    # river band
    f.add(f'<path d="M16,{y0 + 92} C90,{y0 + 70} 150,{y0 + 118} 230,{y0 + 96} S340,{y0 + 70} 384,{y0 + 88}" fill="none" stroke="#e9e2d3" stroke-width="16"/>\n')
    f.add(T(250, y0 + 128, d['river'], 16, '400', MUTED))
    f.add(T(28, y0 + 24, d['w'], 16, '700', MUTED) + T(372, y0 + 24, d['e'], 16, '700', MUTED, 'end'))
    pts = [(310, y0 + 140, 0), (150, y0 + 150, 1), (180, y0 + 50, 2), (50, y0 + 140, 3)]
    for x, y, i in pts:
        f.add(C(x, y, 9, RED if i == 0 else INK, WHITE, 2))
        lab = d['lab'][i]
        anchor = 'start' if i == 3 else 'middle'
        f.add(T(x - 18 if i == 3 else x, y + 30 if i != 2 else y - 16, lab, 16, '700', INK, anchor))
    f.add(T(28, y0 + 60, d['air'], 16, '400', MUTED))
    f.add(L(50, y0 + 70, 50, y0 + 128, RULE, 2, '4 4'))
    f.y = y0 + H
    f.add(T(372, y0 + H - 12, d["nts"], 16, '400', MUTED, 'end'))
    f.cards([(str(i + 1), n, a + '. ' + b) for i, (n, a, b) in enumerate(d['v'])])
    return f.svg()


BUILD = {
    'health-1': lambda l: numbers_card(H1[l]),
    'health-2': lambda l: h2(H2[l]),
    'health-3': lambda l: h3(H3[l]),
    'health-4': lambda l: steps(H4[l]),
    'health-5': lambda l: h5(H5[l]),
    'skin-clinic-1': lambda l: s1(S1[l]),
    'skin-clinic-2': lambda l: s2(S2[l]),
    'skin-clinic-3': lambda l: numbers_card(S3[l] + ('',)) if False else steps(dict(t=S3[l][0], items=S3[l][1])),
    'concert-trip-1': lambda l: steps(K1[l], arrows=True),
    'concert-trip-2': lambda l: k2(K2[l]),
    'concert-trip-3': lambda l: steps(K3[l]),
}

if __name__ == '__main__':
    only = sys.argv[2:] or list(BUILD)
    for name in only:
        for lang in LANGS:
            write(lang, name, BUILD[name](lang))
    print('wrote', len(only) * len(LANGS), 'files to', OUT)
