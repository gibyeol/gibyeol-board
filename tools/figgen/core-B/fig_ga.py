import sys
sys.path.insert(0, '/tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/core-B/tools')
from figlib import *

D = {
 'en': dict(
  t1=['Adult fares by transport card'],
  bars=[('Subway, first 10 km', '₩1,550', 1550), ('City bus, blue or green', '₩1,500', 1500), ('Night bus (N)', '₩2,500', 2500),
        ('Red wide-area bus', '₩3,000', 3000), ('Taxi, first 1.6 km', '₩4,800', 4800)],
  f1=['Single subway ticket ₩1,650 + ₩500 deposit', 'Village bus ₩1,200 · yellow bus ₩1,400'],
  t2=['Climate Card short-term pass'],
  price=['1 day ₩5,000 · 2 days ₩8,000', '3 days ₩10,000 · 5 days ₩15,000', '7 days ₩20,000 · card ₩3,000'],
  yes='Covered', no='Not covered',
  ylist=['Seoul subway', 'Seoul city buses, night too', 'Getting off at Incheon Airport'],
  nlist=['Shinbundang Line, GTX', 'Red wide-area and airport buses', 'Stations outside Seoul'],
  t3=['The subway in three taps'],
  s3=[('Tap in', ['The reader shows your balance']), ('Change lines inside', ['Follow the line number and', 'colour; no extra gate']),
      ('Tap out', ['The fare is worked out', 'by distance'])],
  f3=['Single ticket: get the ₩500 deposit back'],
  t4=['On the bus: tap twice'],
  s4=[('Board: tap your card', ['On the reader by the door']), ('Get off: tap again', ['Skip it and the transfer breaks']),
      ('Next ride within 30 min', ['60 min from 9 p.m. to 7 a.m.', 'No second base fare'])],
  f4=['Up to four transfers · same route again', 'does not count'],
  t5=['After dinner: how to get back'],
  q1=['Is your last train still running?', 'Check Naver Map'], a1=['Subway'],
  q2=['Is there an N bus on your way?'], a2=['N bus, ₩2,500', '11 p.m.–6 a.m.'],
  a3=['Taxi: k.ride or Kakao T', 'Late night: up to 40% more'],
  yes_l='Yes', no_l='No',
  t6=['Regular taxi: base fare', 'by time of night'],
  rows6=[('4 a.m.–10 p.m.', '₩4,800', 4800, ''), ('10–11 p.m.', '₩5,800', 5800, '+20%'), ('11 p.m.–2 a.m.', '₩6,700', 6700, '+40%'),
         ('2–4 a.m.', '₩5,800', 5800, '+20%')],
  f6=['First 1.6 km, mid-size taxi.', 'Distance and time charges rise by', 'the same rate.'],
  t7=['k.ride for visitors'],
  s7=[('Sign up', 'Google, Apple or email'), ('Add an overseas card', 'Registered in the app'),
      ('Call a taxi', 'Search and chat auto-translated'), ('Get out', 'The fare is charged after the ride')],
 ),
 'ko': dict(
  t1=['어른 교통카드 요금'],
  bars=[('지하철, 10km까지', '1,550원', 1550), ('시내버스 파랑·초록', '1,500원', 1500), ('심야버스(N)', '2,500원', 2500),
        ('광역버스(빨강)', '3,000원', 3000), ('택시, 1.6km까지', '4,800원', 4800)],
  f1=['1회용 승차권 1,650원 + 보증금 500원', '마을버스 1,200원 · 노랑 버스 1,400원'],
  t2=['기후동행카드 단기권'],
  price=['1일 5,000원 · 2일 8,000원', '3일 10,000원 · 5일 15,000원', '7일 20,000원 · 카드값 3,000원'],
  yes='돼요', no='안 돼요',
  ylist=['서울 지하철', '서울 시내버스(심야 포함)', '인천공항역 하차'],
  nlist=['신분당선, GTX', '광역버스·공항버스', '서울 밖 역'],
  t3=['지하철은 태그 세 번'],
  s3=[('탈 때 태그', ['단말기에 잔액이 떠요']), ('역 안에서 환승', ['노선 번호와 색을 따라가요,', '개찰구는 다시 안 나가요']),
      ('나갈 때 태그', ['요금은 거리로 계산돼요'])],
  f3=['1회용 승차권은 보증금 500원 환급'],
  t4=['버스는 두 번 태그'],
  s4=[('탈 때 태그', ['문 옆 단말기에']), ('내릴 때 한 번 더', ['안 찍으면 환승이 끊겨요']),
      ('30분 안에 다음 차', ['밤 9시~아침 7시는 1시간', '기본요금을 다시 안 내요'])],
  f4=['최대 4번 환승 · 같은 노선 재탑승은', '환승 아님'],
  t5=['저녁 뒤, 숙소까지 어떻게?'],
  q1=['막차가 아직 있나요?', '네이버 지도로 확인'], a1=['지하철'],
  q2=['가는 길에 N버스가 있나요?'], a2=['심야버스 2,500원', '밤 11시~새벽 6시'],
  a3=['택시: k.ride·카카오 T', '심야엔 최대 40% 더'],
  yes_l='예', no_l='아니요',
  t6=['중형택시 시간대별', '기본요금'],
  rows6=[('새벽 4시~밤 10시', '4,800원', 4800, ''), ('밤 10~11시', '5,800원', 5800, '+20%'), ('밤 11시~새벽 2시', '6,700원', 6700, '+40%'),
         ('새벽 2~4시', '5,800원', 5800, '+20%')],
  f6=['1.6km까지, 중형택시 기준', '거리·시간 요금도 같은 비율로 올라요'],
  t7=['외국인 친구용 k.ride'],
  s7=[('가입', '구글·애플 계정이나 이메일'), ('해외 카드 등록', '앱에서 등록'),
      ('택시 호출', '검색·기사 채팅 자동 번역'), ('하차', '요금은 내린 뒤 자동 결제')],
 ),
 'ja': dict(
  t1=['大人・交通カードの運賃'],
  bars=[('地下鉄、10kmまで', '1,550ウォン', 1550), ('市内バス 青・緑', '1,500ウォン', 1500), ('深夜バス(N)', '2,500ウォン', 2500),
        ('広域バス(赤)', '3,000ウォン', 3000), ('タクシー、1.6kmまで', '4,800ウォン', 4800)],
  f1=['1回用乗車券1,650ウォン+保証金500ウォン', 'マウルバス1,200・黄色バス1,400ウォン'],
  t2=['Climate Card(気候同行カード)', '短期券'],
  price=['1日5,000 · 2日8,000ウォン', '3日10,000 · 5日15,000ウォン', '7日20,000 · カード代3,000ウォン'],
  yes='使える', no='使えない',
  ylist=['ソウルの地下鉄', 'ソウルの市内バス(深夜も)', '仁川空港駅での降車'],
  nlist=['新盆唐線、GTX', '広域バス・空港バス', 'ソウル市外の駅'],
  t3=['地下鉄はタッチ3回'],
  s3=[('乗るときタッチ', ['画面に残高が出ます']), ('駅の中で乗り換え', ['路線番号と色をたどる、', '改札は出ません']),
      ('出るときタッチ', ['運賃は距離で決まります'])],
  f3=['1回用乗車券は保証金500ウォンが戻る'],
  t4=['バスは2回タッチ'],
  s4=[('乗るときタッチ', ['ドア横の読み取り機に']), ('降りるときもタッチ', ['忘れると乗り換えが途切れる']),
      ('30分以内に次へ', ['夜9時〜朝7時は60分', '基本運賃は二重にかからない'])],
  f4=['乗り換えは4回まで · 同じ路線の', '再乗車は対象外'],
  t5=['夕食のあと、どう帰る?'],
  q1=['終電はまだある?', 'NAVERマップで確認'], a1=['地下鉄'],
  q2=['帰り道にNバスはある?'], a2=['深夜バス2,500ウォン', '夜11時〜朝6時'],
  a3=['タクシー:k.ride・Kakao T', '深夜は最大40%増し'],
  yes_l='はい', no_l='いいえ',
  t6=['一般タクシー', '時間帯ごとの基本料金'],
  rows6=[('朝4時〜夜10時', '4,800ウォン', 4800, ''), ('夜10〜11時', '5,800ウォン', 5800, '+20%'), ('夜11時〜深夜2時', '6,700ウォン', 6700, '+40%'),
         ('深夜2〜4時', '5,800ウォン', 5800, '+20%')],
  f6=['1.6kmまで、中型タクシー', '距離・時間料金も同じ割合で上がる'],
  t7=['旅行者向けk.ride'],
  s7=[('登録', 'Google・Apple・メール'), ('海外カードを登録', 'アプリで登録'),
      ('タクシーを呼ぶ', '検索とチャットは自動翻訳'), ('降りる', '料金は降車後に自動決済')],
 ),
 'zh-tw': dict(
  t1=['成人刷交通卡票價'],
  bars=[('地鐵,10公里內', '1,550韓元', 1550), ('市區公車 藍、綠', '1,500韓元', 1500), ('深夜公車(N)', '2,500韓元', 2500),
        ('廣域公車(紅)', '3,000韓元', 3000), ('計程車,1.6公里內', '4,800韓元', 4800)],
  f1=['單程票1,650韓元+押金500韓元', '社區公車1,200・黃色公車1,400韓元'],
  t2=['氣候同行卡短期券'],
  price=['1日5,000 · 2日8,000韓元', '3日10,000 · 5日15,000韓元', '7日20,000 · 卡片3,000韓元'],
  yes='可以', no='不行',
  ylist=['首爾地鐵', '首爾市區公車(含深夜)', '仁川機場站下車'],
  nlist=['新盆唐線、GTX', '廣域公車、機場巴士', '首爾以外的車站'],
  t3=['地鐵刷三次'],
  s3=[('進站刷卡', ['螢幕顯示餘額']), ('站內轉乘', ['看路線號碼和顏色,', '不用出閘門']),
      ('出站刷卡', ['票價按距離計算'])],
  f3=['單程票出站可退500韓元押金'],
  t4=['公車刷兩次'],
  s4=[('上車刷卡', ['門邊的讀卡機']), ('下車再刷', ['沒刷就斷了轉乘']),
      ('30分鐘內搭下一班', ['晚上9點到早上7點是60分鐘', '不用再付一次基本票價'])],
  f4=['最多轉乘4次 · 重搭同一路線', '不算轉乘'],
  t5=['吃完晚餐,怎麼回去?'],
  q1=['末班車還有嗎?', '用 NAVER 地圖查'], a1=['地鐵'],
  q2=['回去的路上有 N 公車嗎?'], a2=['深夜公車2,500韓元', '晚上11點〜早上6點'],
  a3=['計程車:k.ride 或 Kakao T', '深夜最多貴40%'],
  yes_l='有', no_l='沒有',
  t6=['一般計程車', '各時段起跳價'],
  rows6=[('早上4點〜晚上10點', '4,800韓元', 4800, ''), ('晚上10〜11點', '5,800韓元', 5800, '+20%'), ('晚上11點〜凌晨2點', '6,700韓元', 6700, '+40%'),
         ('凌晨2〜4點', '5,800韓元', 5800, '+20%')],
  f6=['1.6公里內,中型計程車', '里程、時間費率也以同比例加成'],
  t7=['k.ride 給旅客的用法'],
  s7=[('註冊', 'Google、Apple 或 email'), ('綁海外信用卡', '在 App 裡綁定'),
      ('叫車', '搜尋和聊天自動翻譯'), ('下車', '下車後自動扣款')],
 ),
}


def gate(x, y):
    return (R(x, y + 8, 10, 40, INK, 'none', 0, 2) + R(x + 34, y + 8, 10, 40, INK, 'none', 0, 2)
            + R(x + 12, y + 18, 20, 12, RED, 'none', 0, 3))


def bus(x, y):
    return (R(x, y + 8, 46, 34, WHITE, INK, 2, 6) + R(x + 6, y + 14, 34, 10, SOFT, 'none', 0, 2)
            + f'<circle cx="{x + 11}" cy="{y + 44}" r="4" fill="{INK}"/><circle cx="{x + 35}" cy="{y + 44}" r="4" fill="{INK}"/>\n')


def steps(f, items, icon):
    for i, (head, subs) in enumerate(items):
        h = 40 + 22 * len(subs)
        f.add(R(16, f.y, 368, h, WHITE, RED if i == 2 and icon == 'bus' else RULE, 1.5))
        if icon == 'gate' and i != 1:
            f.add(gate(30, f.y + h / 2 - 28))
        elif icon == 'gate':
            f.add(f'<path d="M30,{f.y + h / 2} h44 M62,{f.y + h / 2 - 10} l12,10 l-12,10" stroke="{INK}" stroke-width="3" fill="none"/>\n')
        else:
            f.add(bus(28, f.y + h / 2 - 28))
        f.add(T(92, f.y + 28, f'{i + 1}. {head}', 17, '700'))
        for k, s in enumerate(subs):
            f.add(T(92, f.y + 52 + 22 * k, s, 16, '400', MUTED))
        f.y += h + 10


for lang, d in D.items():
    # 1 fares
    f = Fig(d['t1'])
    for lab, val, v in d['bars']:
        f.add(T(20, f.y + 18, lab, 16))
        bw = 250 * v / 4800
        f.add(R(20, f.y + 28, bw, 20, SOFT if v < 4800 else RED, 'none', 0, 4))
        f.add(T(20 + bw + 10, f.y + 44, val, 16, '700'))
        f.y += 60
    f.footer(d['f1'], gap=-4)
    write(lang, 'getting-around-1', f.svg())

    # 2 climate card
    f = Fig(d['t2'])
    f.add(R(16, f.y, 368, 28 + 22 * len(d['price']), SOFT, 'none', 0))
    for i, s in enumerate(d['price']):
        f.add(T(32, f.y + 26 + 22 * i, s, 16, '700'))
    f.y += 28 + 22 * len(d['price']) + 12
    for head, lst, col in ((d['yes'], d['ylist'], RED), (d['no'], d['nlist'], MUTED)):
        h = 44 + 24 * len(lst)
        f.add(R(16, f.y, 368, h, WHITE, col, 2 if col == RED else 1.5))
        f.add(T(32, f.y + 28, head, 17, '700', col))
        for i, s in enumerate(lst):
            mark = '✓' if col == RED else '×'
            f.add(T(32, f.y + 54 + 24 * i, f'{mark} {s}', 16, '400', INK))
        f.y += h + 10
    f.y -= 10
    write(lang, 'getting-around-2', f.svg())

    # 3 subway taps
    f = Fig(d['t3'])
    steps(f, d['s3'], 'gate')
    f.footer(d['f3'], gap=-8)
    write(lang, 'getting-around-3', f.svg())

    # 4 bus
    f = Fig(d['t4'])
    steps(f, d['s4'], 'bus')
    f.footer(d['f4'], gap=-8)
    write(lang, 'getting-around-4', f.svg())

    # 5 decision
    f = Fig(d['t5'])

    def q(lines):
        h = 20 + 24 * len(lines)
        f.add(R(16, f.y, 368, h, SOFT, RULE, 1.5))
        for i, s in enumerate(lines):
            f.add(T(32, f.y + 30 + 24 * i, s, 17 if i == 0 else 16, '700' if i == 0 else '400', INK if i == 0 else MUTED))
        f.y += h

    def ans(lines):
        top = f.y
        f.add(arrow(300, top, top + 34))
        f.add(T(310, top + 24, d['yes_l'], 16, '700', RED))
        h = 20 + 22 * len(lines)
        f.add(R(150, top + 34, 234, h, WHITE, RED, 2.5))
        for i, s in enumerate(lines):
            f.add(T(166, top + 34 + 28 + 22 * i, s, 17 if i == 0 else 16, '700' if i == 0 else '400'))
        f.add(f'<line x1="60" y1="{top}" x2="60" y2="{top + 34 + h + 14}" stroke="{INK}" stroke-width="2.5"/>\n')
        f.add(T(70, top + 24, d['no_l'], 16, '700', MUTED))
        f.y = top + 34 + h + 14
        f.add(arrow(60, f.y - 2, f.y + 22))
        f.y += 22

    q(d['q1']); ans(d['a1']); q(d['q2']); ans(d['a2'])
    h = 20 + 22 * len(d['a3'])
    f.add(R(16, f.y, 368, h, WHITE, INK, 2))
    for i, s in enumerate(d['a3']):
        f.add(T(32, f.y + 28 + 22 * i, s, 17 if i == 0 else 16, '700' if i == 0 else '400'))
    f.y += h
    write(lang, 'getting-around-5', f.svg())

    # 6 taxi
    f = Fig(d['t6'])
    for lab, val, v, pct in d['rows6']:
        hot = pct == '+40%'
        f.add(T(20, f.y + 18, lab, 16, '700' if hot else '400', RED if hot else INK))
        if pct:
            f.add(T(380, f.y + 18, pct, 16, '700', RED if hot else MUTED, 'end'))
        bw = 250 * v / 6700
        f.add(R(20, f.y + 28, bw, 20, RED if hot else SOFT, 'none', 0, 4))
        f.add(T(20 + bw + 10, f.y + 44, val, 16, '700'))
        f.y += 60
    f.footer(d['f6'], gap=-4)
    write(lang, 'getting-around-6', f.svg())

    # 7 k.ride phone
    f = Fig(d['t7'])
    ph = 40 + 78 * len(d['s7'])
    f.add(R(40, f.y, 320, ph, WHITE, INK, 3, 26))
    f.add(R(170, f.y + 12, 60, 8, SOFT, 'none', 0, 4))
    y = f.y + 34
    for i, (a, b) in enumerate(d['s7']):
        f.add(f'<circle cx="74" cy="{y + 22}" r="15" fill="{RED}"/>\n')
        f.add(T(74, y + 28, str(i + 1), 16, '700', WHITE, 'middle'))
        f.add(T(100, y + 22, a, 17, '700'))
        f.add(T(100, y + 46, b, 16, '400', MUTED))
        y += 78
    f.y += ph
    write(lang, 'getting-around-7', f.svg())
print('done')
