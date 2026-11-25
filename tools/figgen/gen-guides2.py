"""Figures for palaces, seoul-areas, food, departure-day (2026-11-26 revision).

Phone-first: viewBox width 400, min font-size 16. Text matches the page facts.
usage: python3 gen-guides2.py <outdir>      (writes <outdir>/<lang>/<name>.svg)
Owner of: palaces-1..7, seoul-areas-1..2, food-1..4, departure-day-1..5.
"""
import os
import sys
from xml.sax.saxutils import escape as _e

FONT = 'system-ui, -apple-system, &quot;Noto Sans KR&quot;, &quot;Noto Sans JP&quot;, &quot;Noto Sans TC&quot;, sans-serif'
INK, RED, PAPER, MUTED, RULE, WHITE, SOFT = '#16151a', '#b8392f', '#f4f0e6', '#5f5b55', '#c9c1b2', '#ffffff', '#e9e2d3'
W = 400
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'


def e(s):
    return _e(s, {'"': '&quot;'})


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


def check(x, y, c=INK):  # 20x20 box at x,y
    return f'<path d="M{x + 3},{y + 11} L{x + 8},{y + 16} L{x + 18},{y + 4}" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>\n'


def cross(x, y, c=RED):
    return (f'<path d="M{x + 4},{y + 4} L{x + 16},{y + 16} M{x + 16},{y + 4} L{x + 4},{y + 16}" '
            f'stroke="{c}" stroke-width="3" stroke-linecap="round"/>\n')


class Fig:
    def __init__(self, title_lines):
        self.title = title_lines
        self.body = ''
        self.y = 30 + 26 * (len(title_lines) - 1) + 24

    def add(self, s):
        self.body += s

    def svg(self, pad=18):
        h = self.y + pad
        t = ''.join(T(20, 34 + 26 * i, s, 20, '700') for i, s in enumerate(self.title))
        label = ' '.join(self.title)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" role="img" aria-label="{e(label)}" '
                f'font-family="{FONT}">\n<title>{e(label)}</title>\n'
                f'<rect width="{W}" height="{h}" fill="{PAPER}"/>\n{t}{self.body}</svg>\n')

    def lines(self, rows, x=20, size=16, fill=MUTED, gap=8, w='400'):
        self.y += gap
        for s in rows:
            self.y += 22
            self.add(T(x, self.y, s, size, w, fill))


def write(lang, name, svg):
    p = os.path.join(OUT, lang, f'{name}.svg')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(svg)


LANGS = ['en', 'ko', 'ja', 'zh-tw']

# ---------------------------------------------------------------- text
S = {
 'en': dict(
  p1t=['Gyeongbokgung: walk north'], north='North',
  p1=[('Geunjeongjeon', ['The throne hall']), ('Geunjeongmun', ['The third gate']),
      ('Heungnyemun', ['Torn down 1914,', 'rebuilt 1997–2001']),
      ('Gwanghwamun', ['Guard ceremony 10:00, 14:00', 'Free, no ticket needed'])],
  p1f=['Schematic, not to scale'],
  p2t=['Which day is each site open?'], days=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  sites=['Gyeongbokgung', 'Changdeokgung', 'Changgyeonggung', 'Deoksugung', 'Jongmyo'], guide='Guide',
  p2f=['× closed', 'Guide: Jongmyo by guided tour only;', 'free walking on weekends', 'Closing day on a public holiday:', 'closed the next working day instead'],
  p3t=['Winter last entry', '(November to January)'],
  p3=[('Gyeongbokgung', '16:00'), ('Changdeokgung', '16:30'), ('Jongmyo', '16:30'), ('Deoksugung', '20:00'), ('Changgyeonggung', '20:00')],
  p3f=['Last entry: one hour before closing.', 'Gyeongbokgung keeps 16:00 in February.'],
  p4t=['Integrated ticket'], p4price='₩6,000', p4sub=['One visit to each site,', 'valid 6 months'],
  p4tear='Staff tear off one part per site',
  p4sep='Bought separately: ₩9,000', p4no=['Not included: Secret Garden,', 'the art museum in Deoksugung'],
  p5t=['What counts as hanbok', 'for free entry'], top='Top (jeogori)', bottom='Skirt or trousers',
  p5ok=['Ties and buttons done up', 'Legs covered', 'Modern-style hanbok'],
  p5no=['Jeogori with jeans', 'T-shirt-style "hanbok"', 'One-piece robes (cheollik)', 'have been refused'],
  p6t=['Secret Garden: 100 places', 'per session'], online='Online 50', onsite='On site 50',
  p6ex='Example: you visit on the 12th',
  p6=[('6th, 10:00', 'Online booking opens'), ('11th', 'Online booking closes'), ('12th', '50 places sold on site')],
  p6f=['First come, first served.', 'Buy a palace ticket too.'],
  p7t=["Bukchon's red zone, hour by hour"], ok='Open to visitors', no='No tourist visits',
  p7f=['Bukchon-ro 11-gil, about 34,000 m²', 'Fine: ₩100,000', 'Residents and shop visitors exempt'],
  a1t=['Where the seven areas sit'], river='Han River',
  areas=dict(jongno='Jongno', hongdae='Hongdae', myeong='Myeongdong', ddm='Dongdaemun', stn='Seoul Station', seong='Seongsu', gang='Gangnam'),
  palaces='palaces', a1f=['Schematic, not to scale'],
  a2t=['From Incheon Airport', 'to each area'], arex='AREX', t1='Incheon Airport',
  a2=[('Hongik Univ.', 'Hongdae · all-stop, ~1 hr, ₩4,650'), ('Gongdeok', ''), ('Seoul Station', 'Express nonstop, 43 min, ₩13,000')],
  l2='Line 2 → Seongsu', l4='Line 4 → Myeongdong',
  busT='No train? Limousine bus',
  bus=[('6001', 'Myeongdong, Dongdaemun'), ('6002', 'Hongdae, Jongno'), ('6011', 'Gyeongbokgung, Changdeokgung'),
       ('6701', 'Gwanghwamun, City Hall, Euljiro'), ('6702', 'Namsan, Dongdaemun'), ('6013', 'Seongsu-dong'), ('6020', 'Gangnam')],
  a2f=['Times as of June 2026 (Visit Seoul)'],
  f1t=['At a Korean restaurant table'],
  f1=['Call button: press for staff (it can be loud)', 'Drawer: spoons, chopsticks, napkins', 'Grill built into the table (BBQ places)',
      'Storage chair: lift the lid for your coat', 'Tablet: order here, often pay too'],
  f2t=['Three ways to order and pay'],
  f2=[('Tablet at the table', ['Order on the screen', 'Usually pay as you order']),
      ('Kiosk at the door', ['Order and often pay first']),
      ('Staff', ['Press the call button', 'Pay at the counter on the way out'])],
  f2f=['Water and side dishes: free refills'],
  f3t=['Booking in Naver Map', 'as a visitor'],
  f3=[('Verify your passport', ['On your phone. No Korean number,', 'no call to support']),
      ('Book, order or pay', ['Inside Naver Map']),
      ('Check the restaurant', ['Each one decides whether it takes', 'overseas-card bookings'])],
  f4t=['Ordering on Baemin', 'from your hotel'],
  f4=[('Language', ['English, Chinese, Japanese:', "follows your phone's setting"]),
      ('Pay', ['Foreign cards, Apple Pay,', 'WeChat Pay, Alipay+']),
      ('Verify', ['A text to your overseas number,', 'no Korean phone needed']),
      ('Before you order', ["Copy the hotel's Korean address;", 'ask where riders hand over food'])],
  d1t=['Departure at Incheon, in order'],
  d1a=[('Arrive on 3F', '3 hours before departure'), ('Check in, drop bags', 'Tell the agent about refund goods'),
       ('Tax refund kiosk', 'Only if you have a refund slip')],
  d1wall='No way back after this',
  d1b=[('Security', ''), ('Passport control', '')],
  d1c=[('Pickup and refunds', 'Duty-free counter on your voucher'), ('Your gate', '30–40 min before boarding')],
  d1f=['Checked in at Seoul Station?', 'Use the 3F dedicated entrance.'],
  d2t=['Which terminal?'], d2line='AREX from Seoul', d2first='Terminal 1: first stop', d2last='Terminal 2: last stop',
  d2T1=['Jeju Air, Trinity Airways,', 'Eastar Jet, Air Premia, Parata Air,', 'Peach, ZIPAIR, EVA Air,', 'Tigerair Taiwan and most', 'other foreign airlines'],
  d2T2=['Korean Air, Asiana, Jin Air,', 'Air Busan, Air Seoul, Delta,', 'Air France, KLM, China Airlines'],
  d2f=['Codeshare? Check your e-ticket', 'or search your flight on airport.kr'],
  d3t=['Seoul Station check-in'], d3where='B2, Seoul Station',
  d3=[('Check-in, bag drop', '05:20–19:00'), ('Immigration', '05:30–19:00')],
  d3dl='Deadline before departure', d3T1=('Terminal 1', '3 h'), d3T2=('Terminal 2', '3 h 20 min'),
  d3f=['AREX Express ticket only', 'Same-day flights from Incheon,', 'only some airlines'],
  d4t=['After passport control'], ref='Refund', pick='Pickup',
  d4=[('Terminal 1 · gates 1–50', [('ref', 'Near gate 28'), ('sub', 'Desk 07:00–22:00, kiosks 24 h'), ('pick', 'Across from gate 43, 4F')]),
      ('Concourse · gates 101–132', [('ref', 'Kiosk by gate 115'), ('pick', 'Near gate 119, 4F')]),
      ('Terminal 2 · gates 208–290', [('ref', 'Near gate 253'), ('sub', 'Desk 07:00–21:30, kiosks 24 h'), ('pick', 'Near 225 · towards 274, 2F')])],
  d4f=['Concourse: shuttle train, no return'],
  d5t=['What goes in which bag'], carry='Carry-on', checked='Checked bag',
  d5c=['Power banks: up to 2, each', '160 Wh or less', 'Liquids: 100 ml or less each,', 'in one 1-litre clear bag', 'Duty-free liquids: sealed bag'],
  d5k=['Liquids over 100 ml', 'Sprays: non-flammable, 500 ml', 'each, 2 litres in total'],
  d5n=['Power banks never go in', 'the checked bag. No charging', 'in flight, not in the overhead bin.'],
 ),
 'ko': dict(
  p1t=['경복궁: 북쪽으로 걸어요'], north='북',
  p1=[('근정전', ['정전(왕의 자리)']), ('근정문', ['세 번째 문']),
      ('흥례문', ['1914년 헐림,', '1997~2001년 다시 지음']),
      ('광화문', ['수문장 교대의식 10:00, 14:00', '무료, 관람권 필요 없음'])],
  p1f=['개략도, 축척 아님'],
  p2t=['요일별로 열린 곳'], days=['월', '화', '수', '목', '금', '토', '일'],
  sites=['경복궁', '창덕궁', '창경궁', '덕수궁', '종묘'], guide='해설',
  p2f=['× 휴궁', '해설: 종묘는 해설사 동행 관람만,', '주말은 자유관람', '휴궁일이 공휴일이면', '다음 평일에 쉬어요'],
  p3t=['겨울 입장 마감', '(11~1월)'],
  p3=[('경복궁', '16:00'), ('창덕궁', '16:30'), ('종묘', '16:30'), ('덕수궁', '20:00'), ('창경궁', '20:00')],
  p3f=['입장 마감은 닫기 1시간 전', '경복궁은 2월에도 16:00'],
  p4t=['통합관람권'], p4price='6,000원', p4sub=['다섯 곳을 한 번씩,', '6개월 동안'],
  p4tear='입장할 때 그 궁 부분을 떼어 가요',
  p4sep='따로 사면 9,000원', p4no=['포함 안 됨: 창덕궁 후원,', '덕수궁 안 미술관'],
  p5t=['무료 입장이 되는 한복'], top='저고리', bottom='치마 또는 바지',
  p5ok=['고름과 단추를 채우기', '다리를 가리기', '생활한복도 돼요'],
  p5no=['저고리에 청바지', '티셔츠형 "한복"', '철릭 같은 위아래 붙은 옷은', '거절된 사례가 있어요'],
  p6t=['창덕궁 후원: 회차당 100명'], online='온라인 50', onsite='현장 50',
  p6ex='예: 12일에 간다면',
  p6=[('6일 10:00', '온라인 예약 시작'), ('11일', '온라인 예약 마감'), ('12일', '현장에서 50명 판매')],
  p6f=['선착순이에요.', '창덕궁 관람권도 사야 해요.'],
  p7t=['북촌 레드존, 시간대별로'], ok='방문 가능', no='관광객 방문 제한',
  p7f=['북촌로11길 일대, 약 34,000㎡', '과태료 10만 원', '주민과 가게 손님은 예외'],
  a1t=['일곱 동네의 위치'], river='한강',
  areas=dict(jongno='종로', hongdae='홍대', myeong='명동', ddm='동대문', stn='서울역', seong='성수', gang='강남'),
  palaces='궁', a1f=['개략도, 축척 아님'],
  a2t=['인천공항에서 동네까지'], arex='공항철도', t1='인천공항',
  a2=[('홍대입구', '홍대 · 일반열차 약 1시간, 4,650원'), ('공덕', ''), ('서울역', '직통열차 무정차 43분, 13,000원')],
  l2='2호선 → 성수', l4='4호선 → 명동',
  busT='기차가 없으면 공항버스',
  bus=[('6001', '명동, 동대문'), ('6002', '홍대, 종로'), ('6011', '경복궁, 창덕궁'),
       ('6701', '광화문, 시청, 을지로'), ('6702', '남산, 동대문'), ('6013', '성수동'), ('6020', '강남')],
  a2f=['2026년 6월 기준 시간(Visit Seoul)'],
  f1t=['한국 식당 테이블에 있는 것'],
  f1=['호출벨: 직원 부르기(소리가 클 수 있어요)', '서랍: 수저와 냅킨', '테이블에 박힌 그릴(고깃집)',
      '수납 의자: 뚜껑을 열고 겉옷 넣기', '태블릿: 여기서 주문, 결제도 자주'],
  f2t=['주문과 결제, 세 가지 방식'],
  f2=[('테이블 태블릿', ['화면에서 주문', '보통 주문할 때 결제']),
      ('입구 키오스크', ['주문하고 먼저 결제하는 곳이 많아요']),
      ('직원 주문', ['호출벨 누르기', '나가면서 계산대에서 결제'])],
  f2f=['물과 반찬 리필은 무료'],
  f3t=['외국인이 네이버 지도로', '예약하는 순서'],
  f3=[('여권 인증', ['휴대폰에서. 한국 번호도,', '고객센터 연락도 필요 없어요']),
      ('예약·주문·결제', ['네이버 지도 안에서']),
      ('식당 확인', ['해외 카드 예약을 받을지는', '식당마다 정해요'])],
  f4t=['숙소에서 배민으로 주문하기'],
  f4=[('언어', ['영어, 중국어, 일본어:', '휴대폰 언어 설정을 따라가요']),
      ('결제', ['해외 카드, 애플페이,', '위챗페이, 알리페이플러스']),
      ('인증', ['해외 번호로 받은 문자,', '한국 휴대폰 필요 없음']),
      ('주문 전에', ['숙소 한국어 주소 복사,', '음식 받는 곳은 프런트에 확인'])],
  d1t=['인천공항 출국, 순서대로'],
  d1a=[('3층 도착', '출발 3시간 전'), ('탑승수속, 짐 부치기', '환급할 물건은 직원에게 말하기'),
       ('환급 키오스크', '환급 전표가 있을 때만')],
  d1wall='여기부터는 되돌아올 수 없어요',
  d1b=[('보안검색', ''), ('출국심사', '')],
  d1c=[('인도장과 환급', '교환권에 적힌 면세품 인도장'), ('탑승구', '탑승 30~40분 전')],
  d1f=['서울역에서 수속했다면', '3층 전용 출국통로로'],
  d2t=['어느 터미널?'], d2line='서울역에서 공항철도', d2first='제1터미널: 먼저 서요', d2last='제2터미널: 종점',
  d2T1=['제주항공, 트리니티항공,', '이스타항공, 에어프레미아,', '파라타항공, 피치, ZIPAIR,', '에바항공, 타이거에어 타이완 등', '대부분의 외국 항공사'],
  d2T2=['대한항공, 아시아나, 진에어,', '에어부산, 에어서울, 델타,', '에어프랑스, KLM, 중화항공'],
  d2f=['공동운항이라면 전자항공권이나', 'airport.kr에서 편명 검색'],
  d3t=['서울역 탑승수속'], d3where='서울역 지하 2층',
  d3=[('탑승수속, 짐 부치기', '05:20~19:00'), ('출국심사', '05:30~19:00')],
  d3dl='출발 기준 수속 마감', d3T1=('제1터미널', '3시간 전'), d3T2=('제2터미널', '3시간 20분 전'),
  d3f=['공항철도 직통열차 승차권만', '당일 인천 출발 국제선,', '일부 항공사만'],
  d4t=['출국심사 뒤'], ref='환급', pick='인도장',
  d4=[('제1터미널 · 1~50번 게이트', [('ref', '28번 근처'), ('sub', '데스크 07:00~22:00, 키오스크 24시간'), ('pick', '43번 맞은편, 4층')]),
      ('탑승동 · 101~132번 게이트', [('ref', '115번 옆 키오스크'), ('pick', '119번 근처, 4층')]),
      ('제2터미널 · 208~290번 게이트', [('ref', '253번 근처'), ('sub', '데스크 07:00~21:30, 키오스크 24시간'), ('pick', '225번 근처 · 274번 방향, 2층')])],
  d4f=['탑승동: 셔틀트레인, 되돌아올 수 없어요'],
  d5t=['어느 가방에 넣을까'], carry='기내 가방', checked='부치는 짐',
  d5c=['보조배터리: 2개까지,', '각 160Wh 이하', '액체류: 용기당 100ml 이하,', '1L 투명 지퍼백 하나', '면세 액체류: 봉인 봉투'],
  d5k=['100ml 넘는 액체류', '스프레이: 비인화성, 개당', '500ml, 합계 2L'],
  d5n=['보조배터리는 부치는 짐에', '절대 안 돼요. 기내 충전 금지,', '선반 보관도 안 돼요.'],
 ),
 'ja': dict(
  p1t=['景福宮:北へ歩く'], north='北',
  p1=[('勤政殿', ['正殿(王の御座所)']), ('勤政門', ['3つめの門']),
      ('興礼門', ['1914年に取り壊し、', '1997〜2001年に再建']),
      ('光化門', ['守門将交代儀式 10:00、14:00', '無料、入場券なしで見られる'])],
  p1f=['概略図・縮尺なし'],
  p2t=['曜日ごとに開いている場所'], days=['月', '火', '水', '木', '金', '土', '日'],
  sites=['景福宮', '昌徳宮', '昌慶宮', '徳寿宮', '宗廟'], guide='解説',
  p2f=['× 休み', '解説:宗廟は解説員つきの観覧のみ、', '週末は自由観覧', '休宮日が祝日なら', '翌平日に休み'],
  p3t=['冬の入場締切', '(11〜1月)'],
  p3=[('景福宮', '16:00'), ('昌徳宮', '16:30'), ('宗廟', '16:30'), ('徳寿宮', '20:00'), ('昌慶宮', '20:00')],
  p3f=['入場締切は閉門の1時間前', '景福宮は2月も16:00'],
  p4t=['統合観覧券'], p4price='6,000ウォン', p4sub=['5か所に1回ずつ、', '6か月有効'],
  p4tear='入場ごとにその場所の部分を切り取り',
  p4sep='別々に買うと9,000ウォン', p4no=['含まれない:昌徳宮の後苑、', '徳寿宮内の美術館'],
  p5t=['無料入場になる韓服'], top='チョゴリ(上衣)', bottom='スカートかズボン',
  p5ok=['結びひもとボタンを留める', '脚が隠れている', 'モダン韓服もOK'],
  p5no=['チョゴリにジーンズ', 'Tシャツ風の「韓服」', 'チョルリクなど上下一体の服は', '断られた例あり'],
  p6t=['昌徳宮の後苑:1回100人'], online='オンライン50', onsite='当日50',
  p6ex='例:12日に行くなら',
  p6=[('6日 10:00', 'オンライン予約開始'), ('11日', 'オンライン予約締切'), ('12日', '当日券50人分を販売')],
  p6f=['先着順です。', '昌徳宮の入場券も必要。'],
  p7t=['北村レッドゾーン、時間帯ごと'], ok='訪問できる', no='観光客は立ち入り制限',
  p7f=['北村路11ギル一帯、約34,000㎡', '過料10万ウォン', '住民とお店の利用者は対象外'],
  a1t=['7つのエリアの位置'], river='漢江',
  areas=dict(jongno='鍾路', hongdae='弘大', myeong='明洞', ddm='東大門', stn='ソウル駅', seong='聖水', gang='江南'),
  palaces='王宮', a1f=['概略図・縮尺なし'],
  a2t=['仁川空港から各エリアへ'], arex='AREX', t1='仁川空港',
  a2=[('弘大入口', '弘大・一般列車 約1時間、4,650ウォン'), ('孔徳', ''), ('ソウル駅', '直通列車 ノンストップ43分、13,000ウォン')],
  l2='2号線 → 聖水', l4='4号線 → 明洞',
  busT='電車がなければ空港バス',
  bus=[('6001', '明洞、東大門'), ('6002', '弘大、鍾路'), ('6011', '景福宮、昌徳宮'),
       ('6701', '光化門、市庁、乙支路'), ('6702', '南山、東大門'), ('6013', '聖水洞'), ('6020', '江南')],
  a2f=['2026年6月時点の所要時間(Visit Seoul)'],
  f1t=['韓国の飲食店のテーブルにあるもの'],
  f1=['呼び出しボタン:店員を呼ぶ(音が大きめ)', '引き出し:スプーン、箸、ナプキン', 'テーブルに埋め込んだグリル(焼肉店)',
      '収納椅子:ふたを開けて上着を入れる', 'タブレット:ここで注文、支払いも多い'],
  f2t=['注文と支払い、3つのパターン'],
  f2=[('テーブルのタブレット', ['画面で注文', 'たいてい注文時に支払い']),
      ('入口のキオスク', ['注文して先に支払う店が多い']),
      ('店員に注文', ['呼び出しボタンを押す', '帰りにレジで支払い'])],
  f2f=['水とおかずのおかわりは無料'],
  f3t=['旅行者がNAVERマップで', '予約する流れ'],
  f3=[('パスポート認証', ['スマホで。韓国の番号も、', 'サポートへの連絡も不要']),
      ('予約・注文・支払い', ['NAVERマップの中で']),
      ('店を確認', ['海外カードの予約を受けるかは', '店ごとに決めます'])],
  f4t=['ホテルから배민で注文する'],
  f4=[('言語', ['日本語、英語、中国語:', 'スマホの言語設定に合わせる']),
      ('支払い', ['海外カード、Apple Pay、', 'WeChat Pay、Alipay+']),
      ('認証', ['日本の携帯番号に届くSMS、', '韓国の電話は不要']),
      ('注文の前に', ['ホテルの韓国語住所をコピー、', '受け取り場所をフロントで確認'])],
  d1t=['仁川空港の出国、順番どおりに'],
  d1a=[('3階に到着', '出発の3時間前'), ('搭乗手続き、荷物預け', '還付する品物は係員に伝える'),
       ('還付キオスク', '還付の伝票があるときだけ')],
  d1wall='ここから先は戻れません',
  d1b=[('保安検査', ''), ('出国審査', '')],
  d1c=[('受け取りと還付', '引換券にある免税品カウンター'), ('搭乗口', '搭乗の30〜40分前')],
  d1f=['ソウル駅で手続きしたなら', '3階の専用出国通路へ'],
  d2t=['どのターミナル?'], d2line='ソウル駅からAREX', d2first='第1ターミナル:先に停車', d2last='第2ターミナル:終点',
  d2T1=['チェジュ航空、トリニティ航空、', 'イースター航空、エアプレミア、', 'パラタ航空、ピーチ、ZIPAIR、', 'エアージャパン、エバー航空など', '多くの外国航空会社'],
  d2T2=['大韓航空、アシアナ、ジンエアー、', 'エアプサン、エアソウル、デルタ、', 'エールフランス、KLM、', 'チャイナエアライン'],
  d2f=['共同運航便はeチケットか', 'airport.krで便名を検索'],
  d3t=['ソウル駅での搭乗手続き'], d3where='ソウル駅 地下2階',
  d3=[('搭乗手続き、荷物預け', '05:20〜19:00'), ('出国審査', '05:30〜19:00')],
  d3dl='出発時刻からの締切', d3T1=('第1ターミナル', '3時間前'), d3T2=('第2ターミナル', '3時間20分前'),
  d3f=['AREX直通列車の乗車券が必要', '当日の仁川発国際線、', '一部の航空会社のみ'],
  d4t=['出国審査の後'], ref='還付', pick='受け取り',
  d4=[('第1ターミナル・1〜50番ゲート', [('ref', '28番付近'), ('sub', 'デスク07:00〜22:00、キオスク24時間'), ('pick', '43番の向かい、4階')]),
      ('コンコース・101〜132番ゲート', [('ref', '115番横のキオスク'), ('pick', '119番付近、4階')]),
      ('第2ターミナル・208〜290番ゲート', [('ref', '253番付近'), ('sub', 'デスク07:00〜21:30、キオスク24時間'), ('pick', '225番付近・274番方面、2階')])],
  d4f=['コンコース:シャトルトレイン、戻れません'],
  d5t=['どのかばんに入れる?'], carry='機内持ち込み', checked='預ける荷物',
  d5c=['モバイルバッテリー:2個まで、', '各160Wh以下', '液体:1容器100ml以下、', '1Lの透明な袋ひとつ', '免税の液体:封印袋のまま'],
  d5k=['100mlを超える液体', 'スプレー:不燃性、1本500ml、', '合計2Lまで'],
  d5n=['モバイルバッテリーは預け入れ', '不可。機内での充電禁止、', '頭上の棚にも入れない。'],
 ),
 'zh-tw': dict(
  p1t=['景福宮:往北走'], north='北',
  p1=[('勤政殿', ['正殿(國王的寶座)']), ('勤政門', ['第三道門']),
      ('興禮門', ['1914 年拆除,', '1997~2001 年重建']),
      ('光化門', ['守門將交接儀式 10:00、14:00', '免費,不用門票'])],
  p1f=['示意圖,非比例'],
  p2t=['星期幾哪裡開'], days=['一', '二', '三', '四', '五', '六', '日'],
  sites=['景福宮', '昌德宮', '昌慶宮', '德壽宮', '宗廟'], guide='導覽',
  p2f=['× 休館', '導覽:宗廟只能跟導覽員參觀,', '週末可自由參觀', '休館日遇國定假日:', '改在下一個平日休'],
  p3t=['冬季最後入場', '(11~1 月)'],
  p3=[('景福宮', '16:00'), ('昌德宮', '16:30'), ('宗廟', '16:30'), ('德壽宮', '20:00'), ('昌慶宮', '20:00')],
  p3f=['關門前 1 小時停止入場', '景福宮 2 月也是 16:00'],
  p4t=['整合參觀券'], p4price='6,000 韓元', p4sub=['五個地方各一次,', '6 個月內有效'],
  p4tear='每次入場撕下該處票根',
  p4sep='分開買要 9,000 韓元', p4no=['不含:昌德宮後苑、', '德壽宮裡的美術館'],
  p5t=['哪種韓服能免費入場'], top='上衣(赤古里)', bottom='裙子或褲子',
  p5ok=['繫帶和扣子要扣好', '腿要遮住', '改良式韓服也可以'],
  p5no=['赤古里配牛仔褲', 'T 恤式「韓服」', '帖裡等上下連身的衣服', '曾被拒絕'],
  p6t=['昌德宮後苑:每梯 100 人'], online='網路 50', onsite='現場 50',
  p6ex='例:12 號去的話',
  p6=[('6 號 10:00', '網路預約開放'), ('11 號', '網路預約截止'), ('12 號', '現場賣 50 個名額')],
  p6f=['先搶先贏。', '也要買昌德宮門票。'],
  p7t=['北村紅區,各時段限制'], ok='可以參觀', no='限制觀光客進入',
  p7f=['北村路 11 街一帶,約 34,000㎡', '罰鍰 10 萬韓元', '居民和店家顧客不在此限'],
  a1t=['七個區域的相對位置'], river='漢江',
  areas=dict(jongno='鍾路', hongdae='弘大', myeong='明洞', ddm='東大門', stn='首爾站', seong='聖水', gang='江南'),
  palaces='古宮', a1f=['示意圖,非比例'],
  a2t=['從仁川機場到各區'], arex='機場鐵路', t1='仁川機場',
  a2=[('弘大入口', '弘大・普通車約 1 小時、4,650 韓元'), ('孔德', ''), ('首爾站', '直達車不停站 43 分、13,000 韓元')],
  l2='2 號線 → 聖水', l4='4 號線 → 明洞',
  busT='沒有鐵路就搭機場巴士',
  bus=[('6001', '明洞、東大門'), ('6002', '弘大、鍾路'), ('6011', '景福宮、昌德宮'),
       ('6701', '光化門、市廳、乙支路'), ('6702', '南山、東大門'), ('6013', '聖水洞'), ('6020', '江南')],
  a2f=['2026 年 6 月的時間(Visit Seoul)'],
  f1t=['韓國餐廳桌上有什麼'],
  f1=['服務鈴:叫店員(鈴聲可能很大)', '抽屜:湯匙、筷子、紙巾', '嵌在桌上的烤爐(烤肉店)',
      '收納椅:掀開蓋子放外套', '平板:在這裡點餐,常常也付款'],
  f2t=['點餐付款的三種方式'],
  f2=[('桌上平板', ['在螢幕點餐', '通常點餐時付款']),
      ('門口 kiosk', ['很多店是點完先付款']),
      ('跟店員點', ['按服務鈴', '離開時到櫃檯結帳'])],
  f2f=['水和小菜續加免費'],
  f3t=['外國旅客用 NAVER 地圖', '訂位的步驟'],
  f3=[('護照認證', ['在手機上完成。不用韓國門號,', '也不用打客服']),
      ('訂位、點餐、付款', ['都在 NAVER 地圖裡']),
      ('確認店家', ['是否接受海外卡訂位,', '由各店自己決定'])],
  f4t=['在飯店用 배민 點外送'],
  f4=[('語言', ['中文、英文、日文:', '跟著手機語言設定']),
      ('付款', ['外國信用卡、Apple Pay、', '微信支付、Alipay+']),
      ('驗證', ['用台灣手機號碼收簡訊,', '不用韓國門號']),
      ('下單前', ['複製飯店韓文地址,', '問櫃檯在哪裡取餐'])],
  d1t=['仁川機場出境,依順序'],
  d1a=[('到 3 樓', '起飛前 3 小時'), ('報到、託運行李', '要退稅的商品先告訴櫃檯'),
       ('退稅機', '有退稅單才需要')],
  d1wall='過了這裡就回不來',
  d1b=[('安檢', ''), ('出境審查', '')],
  d1c=[('提貨與退稅', '兌換券上的免稅品提貨處'), ('登機門', '登機前 30~40 分鐘')],
  d1f=['在首爾站辦好報到的話,', '走 3 樓專用出境通道'],
  d2t=['哪個航廈?'], d2line='從首爾站搭機場鐵路', d2first='第1航廈:先到', d2last='第2航廈:終點站',
  d2T1=['濟州航空、Trinity Airways、', '易斯達航空、Air Premia、', 'Parata Air、長榮航空、', '台灣虎航等多數外籍航空'],
  d2T2=['大韓航空、韓亞航空、真航空、', '釜山航空、首爾航空、達美、', '法航、荷航、中華航空'],
  d2f=['共用班號請看電子機票,', '或在 airport.kr 查班機'],
  d3t=['首爾站預辦登機'], d3where='首爾站地下 2 樓',
  d3=[('報到、託運', '05:20~19:00'), ('出境審查', '05:30~19:00')],
  d3dl='起飛前的截止時間', d3T1=('第1航廈', '3 小時'), d3T2=('第2航廈', '3 小時 20 分'),
  d3f=['限機場鐵路直達車車票', '當天仁川出發的國際線,', '只限部分航空公司'],
  d4t=['出境審查之後'], ref='退稅', pick='提貨',
  d4=[('第1航廈・1~50 號登機門', [('ref', '28 號附近'), ('sub', '櫃檯 07:00~22:00,退稅機 24 小時'), ('pick', '43 號對面,4 樓')]),
      ('登機區・101~132 號登機門', [('ref', '115 號旁的退稅機'), ('pick', '119 號附近,4 樓')]),
      ('第2航廈・208~290 號登機門', [('ref', '253 號附近'), ('sub', '櫃檯 07:00~21:30,退稅機 24 小時'), ('pick', '225 號附近・往 274 號,2 樓')])],
  d4f=['登機區:搭接駁列車,不能折返'],
  d5t=['什麼放哪個包'], carry='隨身行李', checked='託運行李',
  d5c=['行動電源:最多 2 個,', '每個 160Wh 以下', '液體:每瓶 100ml 以下,', '裝進一個 1 公升透明袋', '免稅液體:保持密封'],
  d5k=['超過 100ml 的液體', '噴霧:不易燃,每瓶 500ml,', '總共 2 公升以內'],
  d5n=['行動電源絕對不能託運。', '機上不能充電,', '也不能放頭頂置物櫃。'],
 ),
}


# ---------------------------------------------------------------- figures
def palaces_1(d):
    f = Fig(d['p1t'])
    top = f.y + 10
    xs = 60  # axis x
    gap = 96
    n = len(d['p1'])
    f.add(L(xs, top + 24, xs, top + gap * (n - 1) + 30, RULE, 4))
    # north arrow
    f.add(f'<path d="M{xs - 8},{top + 8} L{xs},{top - 6} L{xs + 8},{top + 8} z" fill="{INK}"/>\n')
    f.add(T(xs + 16, top + 6, d['north'], 16, '700', MUTED))
    for i, (name, notes) in enumerate(d['p1']):
        y = top + 30 + gap * i
        hot = i == n - 1
        if i == 0:  # hall: wide roof + body
            f.add(f'<path d="M{xs - 34},{y - 4} L{xs - 24},{y - 18} L{xs + 24},{y - 18} L{xs + 34},{y - 4} z" fill="{INK}"/>\n')
            f.add(R(xs - 24, y - 4, 48, 26, SOFT, INK, 1.5, 2))
        else:  # gate: roof + opening
            f.add(f'<path d="M{xs - 26},{y - 2} L{xs - 18},{y - 14} L{xs + 18},{y - 14} L{xs + 26},{y - 2} z" fill="{RED if hot else INK}"/>\n')
            f.add(R(xs - 18, y - 2, 36, 20, WHITE, RED if hot else INK, 1.5, 2))
            f.add(R(xs - 6, y + 4, 12, 14, PAPER, 'none', 0, 6))
        f.add(T(112, y + 2, name, 18, '700', RED if hot else INK))
        for k, s in enumerate(notes):
            f.add(T(112, y + 26 + 22 * k, s, 16, '400', MUTED))
    f.y = top + 30 + gap * (n - 1) + 52
    f.lines(d['p1f'], gap=0)
    return f


def palaces_2(d):
    f = Fig(d['p2t'])
    x0, cw = 20, 51.4
    y = f.y + 6
    for j, dn in enumerate(d['days']):
        f.add(T(x0 + cw * j + cw / 2, y + 16, dn, 16, '700', MUTED, 'middle'))
    y += 28
    closed = {0: [1], 1: [0], 2: [0], 3: [0], 4: [1]}
    for i, site in enumerate(d['sites']):
        f.add(T(x0, y + 18, site, 17, '700'))
        y += 28
        for j in range(7):
            x = x0 + cw * j
            if j in closed[i]:
                f.add(R(x + 2, y, cw - 4, 34, RED, RED, 1, 6))
                f.add(T(x + cw / 2, y + 24, '×', 22, '700', WHITE, 'middle'))
            elif i == 4 and j in (0, 2, 3, 4):
                f.add(R(x + 2, y, cw - 4, 34, SOFT, RULE, 1, 6))
                f.add(T(x + cw / 2, y + 23, d['guide'], 16, '400', INK, 'middle'))
            else:
                f.add(R(x + 2, y, cw - 4, 34, WHITE, RULE, 1, 6))
        y += 44
    f.y = y - 6
    f.lines(d['p2f'], gap=4)
    return f


def palaces_3(d):
    f = Fig(d['p3t'])
    y = f.y + 8
    x0, x1 = 20, 380  # 9:00 .. 21:00
    span = 12.0

    def X(h):
        return x0 + (x1 - x0) * (h - 9) / span
    for name, tm in d['p3']:
        hh, mm = map(int, tm.split(':'))
        h = hh + mm / 60
        hot = tm == '16:00'
        f.add(T(x0, y + 16, name, 17, '700', RED if hot else INK))
        y += 26
        f.add(R(x0, y, X(h) - x0, 22, RED if hot else SOFT, RED if hot else RULE, 1, 4))
        tx = X(h) + 8
        anchor = 'start'
        if tx > 330:
            tx, anchor = X(h) - 8, 'end'
        f.add(T(tx, y + 18, tm, 17, '700', RED if hot else INK, anchor))
        y += 34
    # axis
    f.add(L(x0, y, x1, y, MUTED, 1.5))
    for h in (9, 13, 17, 21):
        f.add(L(X(h), y - 4, X(h), y + 4, MUTED, 1.5))
        f.add(T(X(h), y + 24, f'{h}:00', 16, '400', MUTED, 'middle' if 9 < h < 21 else ('start' if h == 9 else 'end')))
    f.y = y + 26
    f.lines(d['p3f'], gap=6)
    return f


def palaces_4(d):
    f = Fig(d['p4t'])
    y = f.y + 4
    head = 100
    stub = 40
    n = len(d['sites'])
    h = head + stub * n
    f.add(R(20, y, 360, h, WHITE, INK, 2, 12))
    f.add(R(20, y, 360, head, SOFT, 'none', 0, 12))
    f.add(L(20, y + head, 380, y + head, INK, 2))
    f.add(T(36, y + 38, d['p4price'], 26, '700', RED))
    for k, s in enumerate(d['p4sub']):
        f.add(T(36, y + 64 + 22 * k, s, 16, '400', INK))
    for i, site in enumerate(d['sites']):
        yy = y + head + stub * i
        if i:
            f.add(L(20, yy, 380, yy, MUTED, 1.5, '6 5'))
        f.add(T(44, yy + 26, site, 17, '700'))
        f.add(f'<path d="M346,{yy + 12} l10,8 l-10,8" fill="none" stroke="{RULE}" stroke-width="2"/>\n')
    y += h + 10
    f.add(T(20, y + 16, d['p4tear'], 16, '700', INK))
    y += 32
    f.add(T(20, y + 16, d['p4sep'], 16, '400', MUTED))
    y += 6
    f.y = y + 16
    f.lines(d['p4no'], fill=RED, gap=4, w='700')
    return f


def palaces_5(d):
    f = Fig(d['p5t'])
    y = f.y + 8
    # jeogori (left) + skirt (right)
    cx1, cx2 = 105, 295
    f.add(f'<path d="M{cx1 - 30},{y + 10} L{cx1 - 70},{y + 40} L{cx1 - 60},{y + 54} L{cx1 - 30},{y + 34} L{cx1 - 30},{y + 78} '
          f'L{cx1 + 30},{y + 78} L{cx1 + 30},{y + 34} L{cx1 + 60},{y + 54} L{cx1 + 70},{y + 40} L{cx1 + 30},{y + 10} z" '
          f'fill="{SOFT}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>\n')
    f.add(f'<path d="M{cx1 - 10},{y + 10} L{cx1 + 8},{y + 40} M{cx1 + 8},{y + 40} L{cx1 + 2},{y + 70} M{cx1 + 8},{y + 40} L{cx1 + 16},{y + 70}" '
          f'stroke="{RED}" stroke-width="3" fill="none" stroke-linecap="round"/>\n')
    f.add(T(200, y + 52, '+', 28, '700', MUTED, 'middle'))
    f.add(f'<path d="M{cx2 - 34},{y + 10} L{cx2 + 34},{y + 10} L{cx2 + 58},{y + 78} L{cx2 - 58},{y + 78} z" '
          f'fill="{SOFT}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>\n')
    f.add(T(cx1, y + 104, d['top'], 16, '700', INK, 'middle'))
    f.add(T(cx2, y + 104, d['bottom'], 16, '700', INK, 'middle'))
    y += 124
    for s in d['p5ok']:
        f.add(check(20, y))
        f.add(T(50, y + 17, s, 16))
        y += 30
    y += 4
    f.add(L(20, y, 380, y, RULE, 1.5))
    y += 12
    for i, s in enumerate(d['p5no']):
        cont = i == len(d['p5no']) - 1
        if not cont:
            f.add(cross(20, y))
        f.add(T(50, y + 17, s, 16, '400', RED if not cont else MUTED))
        y += 30 if not (i == len(d['p5no']) - 2) else 24
    f.y = y
    return f


def palaces_6(d):
    f = Fig(d['p6t'])
    y = f.y + 6
    f.add(R(20, y, 180, 44, INK, INK, 1, 8))
    f.add(T(110, y + 28, d['online'], 17, '700', WHITE, 'middle'))
    f.add(R(200, y, 180, 44, SOFT, RULE, 1, 8))
    f.add(T(290, y + 28, d['onsite'], 17, '700', INK, 'middle'))
    y += 70
    f.add(T(20, y, d['p6ex'], 17, '700', RED))
    y += 18
    step = 58
    n = len(d['p6'])
    f.add(L(36, y + 14, 36, y + 14 + step * (n - 1), RULE, 4))
    for i, (when, what) in enumerate(d['p6']):
        yy = y + step * i
        f.add(C(36, yy + 14, 9, RED if i == 0 else WHITE, RED if i == 0 else INK))
        f.add(T(58, yy + 12, when, 17, '700', RED if i == 0 else INK))
        f.add(T(58, yy + 34, what, 16))
    f.y = y + step * (n - 1) + 40
    f.lines(d['p6f'], gap=4)
    return f


def palaces_7(d):
    f = Fig(d['p7t'])
    y = f.y + 10
    x0, x1 = 20, 380

    def X(h):
        return x0 + (x1 - x0) * h / 24
    f.add(R(X(0), y, X(10) - X(0), 46, RED, RED, 1, 0))
    f.add(R(X(10), y, X(17) - X(10), 46, WHITE, INK, 2, 0))
    f.add(R(X(17), y, X(24) - X(17), 46, RED, RED, 1, 0))
    for h in (0, 10, 17, 24):
        f.add(L(X(h), y + 46, X(h), y + 54, INK, 1.5))
        lab = f'{h:02d}:00' if h < 24 else '24:00'
        anchor = 'start' if h == 0 else ('end' if h == 24 else 'middle')
        f.add(T(X(h), y + 76, lab, 16, '700' if h in (10, 17) else '400', INK if h in (10, 17) else MUTED, anchor))
    y += 100
    f.add(R(20, y, 22, 22, WHITE, INK, 2, 3))
    f.add(T(52, y + 17, d['ok'], 16, '700'))
    y += 32
    f.add(R(20, y, 22, 22, RED, RED, 1, 3))
    f.add(T(52, y + 17, d['no'], 16, '700', RED))
    f.y = y + 26
    f.lines(d['p7f'], gap=8)
    return f


def areas_1(d):
    f = Fig(d['a1t'])
    y0 = f.y + 4
    a = d['areas']

    def box(cx, cy, s, hot=False, note=None):
        wdt = max(len(s) * (17 if ord(s[0]) > 0x2E80 else 9.6) + 26, 64)
        f.add(R(cx - wdt / 2, cy - 18, wdt, 34, WHITE if not hot else INK, INK, 1.5, 17))
        f.add(T(cx, cy + 5, s, 16, '700', WHITE if hot else INK, 'middle'))
        if note:
            f.add(T(cx, cy + 36, note, 16, '400', MUTED, 'middle'))
    # river
    ry = y0 + 236
    f.add(f'<path d="M0,{ry} C80,{ry - 18} 150,{ry + 22} 220,{ry + 4} S340,{ry - 20} 400,{ry - 4} L400,{ry + 26} '
          f'C340,{ry + 10} 280,{ry + 34} 220,{ry + 32} S80,{ry + 10} 0,{ry + 28} z" fill="#c9d6dc" stroke="none"/>\n')
    f.add(T(28, ry + 52, d['river'], 16, '700', MUTED))
    # north arrow
    f.add(f'<path d="M372,{y0 + 18} L380,{y0 + 2} L388,{y0 + 18} z" fill="{INK}"/>\n')
    f.add(T(392, y0 + 40, d['north'], 16, '700', MUTED, 'end'))
    box(200, y0 + 30, a['jongno'], note=d['palaces'])
    box(72, y0 + 100, a['hongdae'], hot=True)
    box(206, y0 + 120, a['myeong'], hot=True)
    box(322, y0 + 62, a['ddm'])
    box(160, y0 + 176, a['stn'], hot=True)
    box(330, y0 + 176, a['seong'])
    box(270, y0 + 316, a['gang'])
    f.y = y0 + 346
    f.lines(d['a1f'], gap=0)
    return f


def areas_2(d):
    f = Fig(d['a2t'])
    y = f.y + 8
    x = 36
    f.add(R(20, y, 360, 36, INK, INK, 1, 8))
    f.add(T(36, y + 24, d['t1'], 17, '700', WHITE))
    f.add(T(364, y + 24, d['arex'], 16, '700', WHITE, 'end'))
    y += 36
    step = 76
    f.add(L(x, y, x, y + 24 + step * 2, RED, 5))
    for i, (stn, note) in enumerate(d['a2']):
        yy = y + 24 + step * i
        f.add(C(x, yy, 9, WHITE, RED, 3))
        f.add(T(58, yy + 6, stn, 17, '700'))
        if note:
            f.add(T(58, yy + 30, note, 16, '400', MUTED))
        if i == 0:
            f.add(T(58, yy + 52, d['l2'], 16, '700', RED))
        if i == 2:
            f.add(T(58, yy + 52, d['l4'], 16, '700', RED))
    y += 24 + step * 2 + 98
    f.add(T(20, y, d['busT'], 17, '700'))
    y += 12
    rh = 30
    f.add(R(20, y, 360, rh * len(d['bus']) + 12, WHITE, RULE, 1.5, 10))
    for i, (no, where) in enumerate(d['bus']):
        yy = y + 28 + rh * i
        f.add(T(36, yy, no, 16, '700', RED))
        f.add(T(92, yy, where, 16))
    f.y = y + rh * len(d['bus']) + 12
    f.lines(d['a2f'], gap=0)
    return f


def food_1(d):
    f = Fig(d['f1t'])
    y = f.y + 8
    # chair (left), table, items with numbers
    f.add(R(20, y + 50, 56, 110, SOFT, INK, 1.5, 8))  # storage chair
    f.add(L(20, y + 70, 76, y + 70, INK, 1.5))
    f.add(R(92, y, 288, 210, WHITE, INK, 2, 14))  # table
    f.add(C(236, y + 105, 44, '#3a3532', INK, 2))  # grill
    f.add(C(236, y + 105, 30, 'none', '#8a817a', 2))
    f.add(R(300, y + 16, 64, 44, INK, INK, 1, 6))  # tablet
    f.add(R(306, y + 22, 52, 32, '#d8e0e6', 'none', 0, 3))
    f.add(C(330, y + 170, 13, RED, RED, 1))  # call button
    f.add(R(130, y + 198, 110, 24, SOFT, INK, 1.5, 4))  # drawer
    f.add(L(170, y + 210, 200, y + 210, INK, 2.5))
    marks = [(330, y + 140), (185, y + 240), (236, y + 168), (48, y + 186), (332, y + 80)]
    for i, (mx, my) in enumerate(marks):
        f.add(C(mx, my, 13, WHITE, RED, 2))
        f.add(T(mx, my + 6, str(i + 1), 16, '700', RED, 'middle'))
    y += 270
    for i, s in enumerate(d['f1']):
        f.add(C(32, y + 10, 12, WHITE, RED, 2))
        f.add(T(32, y + 16, str(i + 1), 16, '700', RED, 'middle'))
        f.add(T(54, y + 16, s, 16))
        y += 32
    f.y = y - 6
    return f


def cards(f, items, num=True, hot_first=False):
    y = f.y + 6
    for i, (head, rows) in enumerate(items):
        h = 44 + 22 * len(rows)
        f.add(R(20, y, 360, h, WHITE, RED if (hot_first and i == 0) else RULE, 2 if (hot_first and i == 0) else 1.5, 10))
        x = 36
        if num:
            f.add(C(42, y + 24, 13, RED, RED, 1))
            f.add(T(42, y + 30, str(i + 1), 16, '700', WHITE, 'middle'))
            x = 66
        f.add(T(x, y + 30, head, 17, '700'))
        for k, s in enumerate(rows):
            f.add(T(x, y + 54 + 22 * k, s, 16, '400', MUTED))
        y += h + 10
    f.y = y - 10


def food_2(d):
    f = Fig(d['f2t'])
    cards(f, d['f2'], num=False)
    f.lines(d['f2f'], gap=4, fill=INK, w='700')
    return f


def food_3(d):
    f = Fig(d['f3t'])
    cards(f, d['f3'])
    return f


def food_4(d):
    f = Fig(d['f4t'])
    cards(f, d['f4'], num=False)
    return f


def dep_1(d):
    f = Fig(d['d1t'])
    y = f.y + 6
    n = 0

    def step(y, head, sub, hot=False):
        nonlocal n
        n += 1
        h = 62 if sub else 42
        f.add(R(20, y, 360, h, WHITE, RED if hot else RULE, 2 if hot else 1.5, 10))
        f.add(C(44, y + 21, 13, RED if hot else INK, RED if hot else INK, 1))
        f.add(T(44, y + 27, str(n), 16, '700', WHITE, 'middle'))
        f.add(T(68, y + 27, head, 17, '700'))
        if sub:
            f.add(T(68, y + 50, sub, 16, '400', MUTED))
        return y + h + 8
    for head, sub in d['d1a']:
        y = step(y, head, sub)
    f.add(L(20, y + 6, 380, y + 6, RED, 2.5, '8 6'))
    f.add(T(200, y + 30, d['d1wall'], 16, '700', RED, 'middle'))
    y += 44
    for head, sub in d['d1b']:
        y = step(y, head, sub)
    for i, (head, sub) in enumerate(d['d1c']):
        y = step(y, head, sub, hot=(i == 1))
    f.y = y - 8
    f.lines(d['d1f'], gap=4)
    return f


def dep_2(d):
    f = Fig(d['d2t'])
    y = f.y + 6
    f.add(T(20, y + 14, d['d2line'], 16, '700', MUTED))
    y += 30
    x = 36
    h1 = 50 + 22 * len(d['d2T1'])
    h2 = 50 + 22 * len(d['d2T2'])
    f.add(L(x, y - 6, x, y + h1 + 30, RED, 5))
    for k, (lab, lst) in enumerate([(d['d2first'], d['d2T1']), (d['d2last'], d['d2T2'])]):
        h = 50 + 22 * len(lst)
        f.add(C(x, y + 22, 10, WHITE if k == 0 else RED, RED, 3))
        f.add(R(60, y, 320, h, WHITE, RULE, 1.5, 10))
        f.add(T(76, y + 28, lab, 17, '700', RED if k else INK))
        for i, s in enumerate(lst):
            f.add(T(76, y + 52 + 22 * i, s, 16, '400', INK))
        y += h + 14
    f.y = y - 14
    f.lines(d['d2f'], gap=6)
    return f


def dep_3(d):
    f = Fig(d['d3t'])
    y = f.y + 6
    f.add(R(20, y, 360, 40, INK, INK, 1, 8))
    f.add(T(36, y + 26, d['d3where'], 17, '700', WHITE))
    y += 52
    for lab, tm in d['d3']:
        f.add(T(20, y + 16, lab, 16, '400', MUTED))
        f.add(T(20, y + 42, tm, 22, '700'))
        y += 58
    f.add(T(20, y + 14, d['d3dl'], 16, '700', RED))
    y += 26
    for (lab, v) in (d['d3T1'], d['d3T2']):
        f.add(R(20, y, 360, 40, WHITE, RED, 2, 8))
        f.add(T(36, y + 26, lab, 17, '700'))
        f.add(T(364, y + 26, v, 18, '700', RED, 'end'))
        y += 48
    f.y = y - 8
    f.lines(d['d3f'], gap=6)
    return f


def dep_4(d):
    f = Fig(d['d4t'])
    y = f.y + 6
    tag = {'ref': (d['ref'], SOFT, INK), 'pick': (d['pick'], RED, WHITE)}
    for head, rows in d['d4']:
        h = 44 + sum(24 if k == 'sub' else 34 for k, _ in rows)
        f.add(R(20, y, 360, h, WHITE, RULE, 1.5, 10))
        f.add(T(36, y + 28, head, 17, '700'))
        yy = y + 42
        for k, s in rows:
            if k == 'sub':
                f.add(T(36, yy + 14, s, 16, '400', MUTED))
                yy += 24
                continue
            lab, bg, fg = tag[k]
            tw = max(len(lab) * (17 if ord(lab[0]) > 0x2E80 else 9.8) + 16, 52)
            f.add(R(36, yy, tw, 26, bg, bg, 1, 13))
            f.add(T(36 + tw / 2, yy + 19, lab, 16, '700', fg, 'middle'))
            f.add(T(36 + tw + 10, yy + 19, s, 16))
            yy += 34
        y += h + 10
    f.y = y - 10
    f.lines(d['d4f'], gap=4)
    return f


def dep_5(d):
    f = Fig(d['d5t'])
    y = f.y + 6
    for lab, rows, bd in ((d['carry'], d['d5c'], INK), (d['checked'], d['d5k'], RULE)):
        h = 48 + 22 * len(rows)
        f.add(R(20, y, 360, h, WHITE, bd, 2 if bd == INK else 1.5, 10))
        f.add(T(36, y + 28, lab, 18, '700'))
        for i, s in enumerate(rows):
            f.add(T(36, y + 52 + 22 * i, s, 16))
        y += h + 12
    h = 24 + 22 * len(d['d5n'])
    f.add(R(20, y, 360, h, RED, RED, 1, 10))
    for i, s in enumerate(d['d5n']):
        f.add(T(36, y + 30 + 22 * i, s, 16, '700', WHITE))
    f.y = y + h
    return f


FIGS = [('palaces-1', palaces_1), ('palaces-2', palaces_2), ('palaces-3', palaces_3), ('palaces-4', palaces_4),
        ('palaces-5', palaces_5), ('palaces-6', palaces_6), ('palaces-7', palaces_7),
        ('seoul-areas-1', areas_1), ('seoul-areas-2', areas_2),
        ('food-1', food_1), ('food-2', food_2), ('food-3', food_3), ('food-4', food_4),
        ('departure-day-1', dep_1), ('departure-day-2', dep_2), ('departure-day-3', dep_3),
        ('departure-day-4', dep_4), ('departure-day-5', dep_5)]

if __name__ == '__main__':
    for lang in LANGS:
        for name, fn in FIGS:
            write(lang, name, fn(S[lang]).svg())
    print('wrote', len(LANGS) * len(FIGS), 'files to', OUT)
