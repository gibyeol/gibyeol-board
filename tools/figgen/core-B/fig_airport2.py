import sys
sys.path.insert(0, '/tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/core-B/tools')
from figlib import *

D = {
 'en': dict(
  t2=['One line, two kinds of train'], h=('Express', 'All-stop'),
  st=['Incheon Airport T2', 'Incheon Airport T1', '…', 'Hongik Univ. (Hongdae)', 'Gongdeok', 'Seoul Station'],
  f2=['Express: ₩13,000, 43 min from T1,', 'nonstop, reserved seat', 'All-stop by card: ₩4,650 to Hongdae', 'or Gongdeok, ₩4,750 to Seoul Station'],
  t4=['Two cards, two jobs'],
  cards=[('T-money', ['Tap for subway, buses and', 'the AREX all-stop', 'Sold at airport card machines', 'and convenience stores']),
         ('WOWPASS', ['T-money inside for transport', 'Exchange money onto the card', 'Pay in shops with the card'])],
  f4=['T-money can also be pre-ordered', 'for pick-up at the airport'],
  t5=['What your bus ticket shows'],
  fields=['Destination', 'Fare', 'Boarding time', 'Boarding location'], note='Go to this stop',
  tag='Luggage claim tag', tagnote='Match the number when you get off', f5=['Up to 2 bags per person, 28 in or smaller'],
  t6=['International Taxi,', 'Incheon Airport to Seoul'],
  zones=[('Gangseo', '₩70,000'), ('Mapo (Hongdae), Yeongdeungpo…', '₩75,000'), ('Jung (Myeongdong), Jongno…', '₩85,000'),
         ('Gangnam, Seocho…', '₩90,000'), ('Songpa (Jamsil), Gangdong…', '₩95,000')],
  f6=['Mid-size, fixed fare, tolls included', 'Large and deluxe: ₩100,000–140,000']),
 'ko': dict(
  t2=['같은 선로, 두 종류의 열차'], h=('직통', '일반'),
  st=['인천공항2터미널', '인천공항1터미널', '…', '홍대입구', '공덕', '서울역'],
  f2=['직통: 13,000원, 1터미널에서 43분,', '안 서고 지정석', '일반(교통카드): 홍대입구·공덕 4,650원,', '서울역 4,750원'],
  t4=['카드 두 장, 하는 일이 달라요'],
  cards=[('티머니', ['지하철·버스·공항철도 일반열차를', '태그로 결제', '공항 카드 발매기·편의점에서 판매']),
         ('WOWPASS', ['교통용 티머니 내장', '외화를 카드에 환전', '가게에서 카드로 결제'])],
  f4=['티머니는 미리 예약해', '공항에서 받을 수도 있어요'],
  t5=['공항버스 승차권에 적힌 것'],
  fields=['행선지', '요금', '탑승 시각', '탑승 위치(정류장)'], note='이 정류장으로 가요',
  tag='짐표', tagnote='내릴 때 번호를 맞춰요', f5=['짐은 1인 2개, 28인치 이하'],
  t6=['외국인관광택시', '인천공항 → 서울'],
  zones=[('강서', '70,000원'), ('마포(홍대)·영등포 등', '75,000원'), ('중구(명동)·종로 등', '85,000원'),
         ('강남·서초 등', '90,000원'), ('송파(잠실)·강동 등', '95,000원')],
  f6=['중형 정액, 통행료 포함', '대형·모범 100,000~140,000원']),
 'ja': dict(
  t2=['同じ線路に2種類の列車'], h=('直通', '一般'),
  st=['仁川空港第2ターミナル', '仁川空港第1ターミナル', '…', '弘大入口', '孔徳', 'ソウル駅'],
  f2=['直通:13,000ウォン、第1ターミナル', 'から43分、ノンストップ・全席指定', '一般(交通カード):弘大入口・孔徳', '4,650ウォン、ソウル駅4,750ウォン'],
  t4=['カード2枚、役割が違います'],
  cards=[('T-money', ['地下鉄・バス・AREX一般列車に', 'タッチで乗車', '空港のカード販売機と', 'コンビニで販売']),
         ('WOWPASS', ['交通用のT-money機能つき', '外貨をカードに両替', 'お店でカード払い'])],
  f4=['T-moneyは事前予約して', '空港で受け取ることもできます'],
  t5=['空港バスの乗車券に書いてあること'],
  fields=['行き先', '運賃', '乗車時刻', '乗り場'], note='この乗り場へ行きます',
  tag='荷物札', tagnote='降りるとき番号を確認', f5=['荷物は1人2個、28インチ以下'],
  t6=['外国人観光タクシー', '仁川空港 → ソウル'],
  zones=[('江西区', '70,000ウォン'), ('麻浦区(弘大)・永登浦区など', '75,000ウォン'), ('中区(明洞)・鍾路区など', '85,000ウォン'),
         ('江南区・瑞草区など', '90,000ウォン'), ('松坡区(蚕室)・江東区など', '95,000ウォン')],
  f6=['中型・定額・高速道路料金込み', '大型・模範は100,000〜140,000ウォン']),
 'zh-tw': dict(
  t2=['同一條路線,兩種列車'], h=('直達車', '普通車'),
  st=['仁川機場第2航廈', '仁川機場第1航廈', '…', '弘大入口', '孔德', '首爾站'],
  f2=['直達車:13,000韓元,第1航廈出發', '43分鐘,不停站、對號座', '普通車(交通卡):弘大入口、孔德', '4,650韓元,首爾站4,750韓元'],
  t4=['兩張卡,用途不同'],
  cards=[('T-money', ['地鐵、公車、機場鐵路普通車', '刷卡搭乘', '機場交通卡販賣機、便利商店有賣']),
         ('WOWPASS', ['內建交通用T-money', '外幣換成韓元存進卡', '在店家刷卡付款'])],
  f4=['T-money也可以先預訂,', '到機場取卡'],
  t5=['機場巴士車票上寫了什麼'],
  fields=['目的地', '票價', '上車時間', '乘車處'], note='到這個乘車處',
  tag='行李牌', tagnote='下車時核對號碼', f5=['行李每人2件、28吋以下'],
  t6=['外國人觀光計程車', '仁川機場 → 首爾'],
  zones=[('江西區', '70,000韓元'), ('麻浦(弘大)、永登浦等', '75,000韓元'), ('中區(明洞)、鍾路等', '85,000韓元'),
         ('江南、瑞草等', '90,000韓元'), ('松坡(蠶室)、江東等', '95,000韓元')],
  f6=['中型車定額,含過路費', '大型、模範100,000〜140,000韓元']),
}


def card_icon(x, y):
    return (R(x, y, 64, 42, WHITE, INK, 2, 6) + R(x + 8, y + 10, 14, 11, SOFT, INK, 1.2, 2)
            + f'<line x1="{x + 8}" y1="{y + 32}" x2="{x + 52}" y2="{y + 32}" stroke="{RULE}" stroke-width="3"/>\n')


for lang, d in D.items():
    # 2: line schematic
    f = Fig(d['t2'])
    f.add(T(28, f.y + 4, d['h'][0], 17, '700', RED))
    f.add(T(372, f.y + 4, d['h'][1], 17, '700', INK, 'end'))
    top = f.y + 34
    step = 46
    n = len(d['st'])
    xl, xr = 46, 354
    f.add(f'<line x1="{xl}" y1="{top}" x2="{xl}" y2="{top + step * (n - 1)}" stroke="{RED}" stroke-width="5"/>\n')
    f.add(f'<line x1="{xr}" y1="{top}" x2="{xr}" y2="{top + step * (n - 1)}" stroke="{INK}" stroke-width="5"/>\n')
    for i, s in enumerate(d['st']):
        y = top + step * i
        if s == '…':
            f.add(T(200, y + 6, '…', 18, '700', MUTED, 'middle'))
            for k in (-12, 0, 12):
                f.add(f'<circle cx="{xr}" cy="{y + k}" r="3.5" fill="{WHITE}" stroke="{INK}" stroke-width="1.5"/>\n')
            continue
        express = i in (0, 1, n - 1)
        f.add(T(200, y + 6, s, 16, '700' if express else '400', INK, 'middle'))
        f.add(f'<circle cx="{xr}" cy="{y}" r="8" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/>\n')
        if express:
            f.add(f'<circle cx="{xl}" cy="{y}" r="8" fill="{WHITE}" stroke="{RED}" stroke-width="2.5"/>\n')
    f.y = top + step * (n - 1) + 14
    f.footer(d['f2'], gap=6)
    write(lang, 'airport-to-seoul-2', f.svg())

    # 4: two cards
    f = Fig(d['t4'])
    for k, (name, lines) in enumerate(d['cards']):
        h = max(84, 48 + 22 * len(lines))
        f.add(R(16, f.y, 368, h, WHITE, RULE, 1.5))
        f.add(card_icon(28, f.y + 18))
        f.add(T(108, f.y + 30, name, 18, '700', RED))
        for i, s in enumerate(lines):
            f.add(T(108, f.y + 54 + 22 * i, s, 16))
        f.y += h + 12
    f.footer(d['f4'], gap=-4)
    write(lang, 'airport-to-seoul-4', f.svg())

    # 5: bus ticket mock-up
    f = Fig(d['t5'])
    rows = d['fields']
    h = 28 + 58 * len(rows)
    f.add(R(16, f.y, 368, h, WHITE, INK, 2, 8))
    f.add(f'<line x1="16" y1="{f.y + 14}" x2="384" y2="{f.y + 14}" stroke="{RULE}" stroke-width="1.5" stroke-dasharray="4 4"/>\n')
    for i, lab in enumerate(rows):
        y = f.y + 28 + 58 * i
        hot = i == len(rows) - 1
        f.add(T(32, y + 18, lab, 16, '700', RED if hot else INK))
        f.add(R(32, y + 28, 150 if not hot else 120, 14, SOFT, 'none', 0, 4))
        if hot:
            f.add(T(170, y + 41, '← ' + d['note'], 16, '700', RED))
    f.y += h + 16
    th = 62
    f.add(R(16, f.y, 368, th, SOFT, RULE, 1.5, 8))
    f.add(f'<circle cx="40" cy="{f.y + th / 2}" r="7" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>\n')
    f.add(T(60, f.y + 26, d['tag'], 16, '700'))
    f.add(T(60, f.y + 48, d['tagnote'], 16, '400', MUTED))
    f.y += th
    f.footer(d['f5'], gap=6)
    write(lang, 'airport-to-seoul-5', f.svg())

    # 6: taxi zones
    f = Fig(d['t6'])
    vals = [70, 75, 85, 90, 95]
    for i, (lab, val) in enumerate(d['zones']):
        f.add(T(20, f.y + 18, lab, 16, '700' if i == 2 else '400'))
        bw = 220 * vals[i] / 95
        f.add(R(20, f.y + 28, bw, 20, RED if i == 2 else SOFT, 'none', 0, 4))
        f.add(T(20 + bw + 10, f.y + 44, val, 16, '700', RED if i == 2 else INK))
        f.y += 60
    f.footer(d['f6'], gap=-6)
    write(lang, 'airport-to-seoul-6', f.svg())
print('done')
