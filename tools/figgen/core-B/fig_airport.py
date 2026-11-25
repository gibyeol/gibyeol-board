import sys
sys.path.insert(0, '/tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/core-B/tools')
from figlib import *

D = {
 'en': dict(
  t1=['From Terminal 1 into Seoul'],
  c1=[('AREX Express', '₩13,000', ['43 min nonstop to Seoul Station']),
      ('AREX all-stop', '₩4,750 by card', ['59 min to Seoul Station,', 'stops at Hongdae and Gongdeok']),
      ('Limousine bus', '₩16,000–18,000', ['About 60–80 min to hotel areas']),
      ('International Taxi', '₩70,000–95,000', ['Fixed fare by Seoul zone,', 'mid-size, tolls included'])],
  f1=['Adult fares, checked 26 Nov 2026'],
  t2=['Terminal 1: where to go'],
  b1=('1F', 'Limousine bus', ['Tickets: counters and kiosks', 'Your ticket shows the stop']),
  mid='Go down to B1',
  b2=('B1', 'Transportation Center', ['AREX Express: ticket counter', 'AREX all-stop: card machines,', 'convenience store, tap in']),
  f2=['Terminal 2: bus tickets and AREX', 'are both on the basement level'],
  t3=['Late at night from Terminal 1'],
  rows=[('22:48', 'Last AREX Express', True), ('23:40', 'N6703 · Jamsil, Gwangnaru', False),
        ('23:50', 'N6701 · Seoul Stn, Dongdaemun', False), ('00:00', 'N6002 · Hongdae, Cheongnyangni', False),
        ('00:10', 'N6000 · Gangnam', False)],
  f3=['Bus times: first departures.', 'Night bus ₩17,000–18,000, ticket at', 'the counter or a machine.', 'AREX all-stop: check the AREX site.']),
 'ko': dict(
  t1=['1터미널에서 서울까지'],
  c1=[('공항철도 직통열차', '13,000원', ['서울역까지 안 서고 43분']),
      ('공항철도 일반열차', '교통카드 4,750원', ['서울역까지 59분,', '홍대입구·공덕에 정차']),
      ('공항 리무진버스', '16,000~18,000원', ['숙소 많은 지역까지 약 60~80분']),
      ('외국인관광택시', '70,000~95,000원', ['서울 구역별 정액,', '중형·통행료 포함'])],
  f1=['어른 요금, 2026년 11월 26일 확인'],
  t2=['1터미널: 어디로 갈까'],
  b1=('1층', '공항 리무진버스', ['표: 매표소와 무인 발매기', '정류장은 표에 적혀 있어요']),
  mid='지하 1층으로',
  b2=('B1', '교통센터', ['직통열차: 안내센터에서 표', '일반열차: 카드 발매기·편의점,', '태그하고 탑승']),
  f2=['2터미널: 버스 매표소와 공항철도', '모두 지하층'],
  t3=['밤늦게 1터미널에서'],
  rows=[('22:48', '직통열차 막차', True), ('23:40', 'N6703 · 잠실·광나루', False),
        ('23:50', 'N6701 · 서울역·동대문', False), ('00:00', 'N6002 · 홍대·청량리', False),
        ('00:10', 'N6000 · 강남', False)],
  f3=['버스는 1터미널 첫차 시각', '심야버스 17,000~18,000원,', '표는 매표소·발매기에서', '일반열차 막차는 공항철도 사이트 확인']),
 'ja': dict(
  t1=['第1ターミナルからソウルへ'],
  c1=[('AREX直通列車', '13,000ウォン', ['ソウル駅までノンストップ43分']),
      ('AREX一般列車', '交通カード4,750ウォン', ['ソウル駅まで59分、', '弘大入口・孔徳に停車']),
      ('空港リムジンバス', '16,000〜18,000ウォン', ['ホテルの多いエリアへ約60〜80分']),
      ('外国人観光タクシー', '70,000〜95,000ウォン', ['ソウルの区域別定額、', '中型・高速料金込み'])],
  f1=['大人運賃・2026年11月26日確認'],
  t2=['第1ターミナル:どこへ行く?'],
  b1=('1階', '空港リムジンバス', ['切符:売り場と券売機', '乗り場は切符に記載']),
  mid='地下1階へ',
  b2=('B1', '交通センター', ['直通列車:専用カウンター', '一般列車:カード販売機・', 'コンビニ、タッチで乗車']),
  f2=['第2ターミナル:バス売り場もAREXも', '地下階'],
  t3=['夜遅く、第1ターミナルから'],
  rows=[('22:48', '直通列車の最終', True), ('23:40', 'N6703 · 蚕室・広渡口', False),
        ('23:50', 'N6701 · ソウル駅・東大門', False), ('00:00', 'N6002 · 弘大・清凉里', False),
        ('00:10', 'N6000 · 江南', False)],
  f3=['バスは第1ターミナルの始発時刻', '深夜バス17,000〜18,000ウォン、', '切符は売り場か券売機で', '一般列車の最終はAREXサイトで']),
 'zh-tw': dict(
  t1=['從第1航廈進首爾'],
  c1=[('機場鐵路直達車', '13,000韓元', ['不停站到首爾站43分鐘']),
      ('機場鐵路普通車', '交通卡4,750韓元', ['到首爾站59分鐘,', '停弘大入口、孔德']),
      ('機場巴士', '16,000〜18,000韓元', ['到飯店密集區約60〜80分鐘']),
      ('外國人觀光計程車', '70,000〜95,000韓元', ['依首爾區域定額,', '中型車、含過路費'])],
  f1=['成人票價,2026年11月26日確認'],
  t2=['第1航廈:往哪走'],
  b1=('1樓', '機場巴士', ['車票:售票處、售票機', '乘車處印在車票上']),
  mid='下到地下1樓',
  b2=('B1', '交通中心', ['直達車:專用櫃台買票', '普通車:交通卡販賣機、', '便利商店,刷卡進站']),
  f2=['第2航廈:巴士售票處和機場鐵路', '都在地下樓層'],
  t3=['深夜從第1航廈出發'],
  rows=[('22:48', '直達車末班', True), ('23:40', 'N6703 · 蠶室、廣渡口', False),
        ('23:50', 'N6701 · 首爾站、東大門', False), ('00:00', 'N6002 · 弘大、清涼里', False),
        ('00:10', 'N6000 · 江南', False)],
  f3=['巴士為第1航廈首班發車時間', '深夜巴士17,000〜18,000韓元,', '在售票處或售票機買票', '普通車末班請查機場鐵路官網']),
}

for lang, d in D.items():
    # 1: option cards
    f = Fig(d['t1'])
    for name, price, det in d['c1']:
        h = 70 + 22 * len(det)
        f.add(R(16, f.y, 368, h))
        f.add(T(32, f.y + 28, name, 18, '700'))
        f.add(T(32, f.y + 54, price, 18, '700', RED))
        for i, s in enumerate(det):
            f.add(T(32, f.y + 78 + 22 * i, s, 16, '400', MUTED))
        f.y += h + 10
    f.footer(d['f1'], gap=0)
    write(lang, 'airport-to-seoul-1', f.svg())

    # 2: floors at T1
    f = Fig(d['t2'])
    for k, blk in enumerate([d['b1'], d['b2']]):
        fl, head, lines = blk
        h = 52 + 22 * len(lines)
        f.add(R(16, f.y, 368, h, WHITE, RED if k else RULE, 2.5 if k else 1.5))
        f.add(R(16, f.y, 72, h, SOFT, 'none', 0))
        f.add(T(52, f.y + h / 2 + 8, fl, 22, '700', INK, 'middle'))
        f.add(T(104, f.y + 30, head, 17, '700'))
        for i, s in enumerate(lines):
            f.add(T(104, f.y + 56 + 22 * i, s, 16))
        f.y += h
        if k == 0:
            f.add(arrow(52, f.y + 6, f.y + 52))
            f.add(T(80, f.y + 36, d['mid'], 16, '700', RED))
            f.y += 58
    f.footer(d['f2'], gap=6)
    write(lang, 'airport-to-seoul-3', f.svg())

    # 3: late timeline
    f = Fig(d['t3'])
    f.y += 6
    top = f.y
    step = 48
    n = len(d['rows'])
    f.add(f'<line x1="92" y1="{top + 10}" x2="92" y2="{top + step * (n - 1) + 10}" stroke="{RULE}" stroke-width="4"/>\n')
    for i, (tm, lab, hot) in enumerate(d['rows']):
        y = top + step * i
        f.add(T(20, y + 16, tm, 17, '700', RED if hot else INK))
        f.add(f'<circle cx="92" cy="{y + 10}" r="8" fill="{RED if hot else WHITE}" stroke="{RED if hot else INK}" stroke-width="2"/>\n')
        f.add(T(110, y + 16, lab, 16, '700' if hot else '400', RED if hot else INK))
    f.y = top + step * (n - 1) + 20
    f.add(f'<line x1="20" y1="{f.y + 8}" x2="380" y2="{f.y + 8}" stroke="{RULE}" stroke-width="1.5" stroke-dasharray="5 5"/>\n')
    f.y += 8
    f.footer(d['f3'], gap=4)
    write(lang, 'airport-to-seoul-7', f.svg())
print('done')
