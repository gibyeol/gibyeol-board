# 독립 검토: 공항철도 직통열차 Klook 비교표·바우처 활성화 3가지 (2026-11-27)

- 검토자: 독립 검토 하위 작업(이 수정을 쓰지 않음). 읽기만 함, 내용 파일은 고치지 않음.
- 대상: 브랜치 claude/determined-euler-xsz86i, 커밋 38e2156 + a271a7c. `git diff origin/main a271a7c -- content/*/airport-to-seoul.md content/*/seoul-subway.md` (8개 파일, +236 −32). 그 뒤 커밋(88919ee, efda024)은 이 8개 파일을 바꾸지 않음(확인함).
- 근거: Klook 화면 22장 `wondu-archive/raw-from-scratchpad/klook-wondu-screens-2026-11-27/arex-128.webp ~ arex-149.png` 전부 열어 봄. 공항철도 공식 `https://www.airportrailroad.com/train/express/guide`, `/train/express/introduce`, `/ticket/rsv` (2026-11-27 curl, 모두 200, 우회 없음). Klook 사이트·tpx.li는 열지 않음.
- 원두 원문: [7eb4ec94#3526] "(나)로 진행해" · [7eb4ec94#3295] "틀린정보만 없으면돼" · [7eb4ec94#2990] "확실하지 않은 정보는 예상과 근거의 출처가 있다면 출처를 남기고 예상이라고 쓰고, 아니면 다뺴." · [7eb4ec94#1227] A to Z · [7eb4ec94#1233] 따라 하기 · [7eb4ec94#1192] 두괄식 · [7eb4ec94#963] 한국인·외국인 구분 없음.

## 숫자 요약

| 항목 | 결과 |
|---|---|
| 화면 영어 이름 대조 (Account, Bookings, Status:Awaiting activation, Go to activate, Select ticket, Date, Departure Time, Status:Activated, Train no., Car no., See voucher, Voucher no., Express Train Ticket Vending Machine, ENGLISH - KRW, Express Train, Departure Station, Arrival Station, Train Time, Ticket Reservation, Reserve, Member Reservation, Non-member Reservation, Verification Code, Ticket Confirmation Number, Re-enter, Change Seat, Discount, Exchange Code, Verify, Total Amount, 0 KRW, Pay) | 32개 중 32개 화면과 글자 그대로 맞음 |
| 숫자·규정 사실 (13자리, 6자리 2곳, 6~12세, 0~5세, 어른 1명당 1명, 앱 활성화 시 가장 이른 열차 자동·그날만, 열차 고른 뒤 환불 불가·변경 창구, 휠체어석 현장 구매만, 어른 13,000원, 짐 1개+손가방 1개, 먹고 마시기 금지, 짐 두는 곳, 유모차·휠체어) | 14개 중 12개 맞음, 2개 고칠 것(아래 필수 1·2) |
| '08~22시' 같은 시간 숫자 | 이번 변경에 해당 숫자 없음(새로 들어간 시각 숫자 0개) |
| 예시 화면의 가격·날짜·번호(US$ 25.50·6.5, ₩8,700, 2024·2020 날짜, A1034, 9394199322896, 4829175632048, 예약번호) | 0개 들어감 (통과) |
| 4개 언어 같은 내용 | 4개 언어 줄 수 같음(각 303줄), 내용 같음. 낱말 차이 1곳(권장 1) |
| '우리 판단' 표시 | 판단 문장 3곳 모두 표시됨(비교표 위 결론, 3가지 순서, 직통열차 고르는 기준) |
| Klook 안내를 공식 규정처럼 쓴 곳 | 1곳(필수 2: 0~5세 "공식 안내와 클룩 안내가 같아요") |
| 버튼 글 변경(airport·subway × 4개 언어 = 8곳) | 8곳 모두 화면 사실과 맞음 |
| 빌드(origin/main + 바뀐 8개 파일) | 160쪽 빌드 성공. 8개 페이지(4개 언어 × 2) 내부 링크·앵커 깨짐 0, 안 바뀐 마크다운 표시({{…}}, **…**, ](#…)) 0 |
| 반드시 고칠 것 | 2건 (각 4개 언어 × 해당 줄) |
| 권장 | 3건 |

## 1. 사실 대조 (화면·공식 원문)

| 페이지 글 | 근거 | 판정 |
|---|---|---|
| 안 바꾼(활성화 안 한) 바우처로는 못 탐 | arex-131 "an unactivated Klook voucher can't be used to board the train" | 맞음 |
| 바꾸는 3가지: 클룩 앱·공항철도 공식 웹사이트·현장 발매기 | arex-131 STEP 2 "Activate on the Klook app / AREX official website / at the on-site AREX ticket machines" | 맞음 (페이지는 ①앱 ②발매기 ③웹사이트 순서, '우리 판단'으로 순서 이유 표시) |
| ① Account → Bookings → AREX 예약 | arex-134 "Go to Account > Bookings and click on your AREX booking" | 맞음 |
| ① Status:Awaiting activation → Go to activate | arex-132 | 맞음 |
| ① Select ticket·Date·Departure Time, 가장 이른 열차·좌석 자동, 그날만 사용 | arex-132 "The earliest train available within the selected period will be automatically assigned. Once activated, the tickets can be used only on the same day." arex-133 "(Seats will be assigned automatically)" | 맞음 |
| ① 화면 위 안내: 열차 고른 뒤 환불 안 됨, 변경은 창구 | arex-133 "Tickets cannot be refunded after selecting the train number, changes need to be made at the counter" | ① 3번 안에서는 맞음. **비교표·'산 다음 5'에서는 세 방법 전부로 넓혀 씀 → 필수 1** |
| ① Status:Activated, QR, Train no., Car no.(호차·좌석) | arex-133·135 ("Car no. 05 7D") | 맞음 |
| ② See voucher → Voucher no. 13자리 | arex-136 "click 'See voucher' to retrieve your 13-digit code", arex-139 "Find the 13-digit code", "Voucher no." | 맞음 |
| ② 직통열차 승차권발매기 / Express Train Ticket Vending Machine | arex-139 기계 사진 위 표지 글자 | 맞음 |
| ② 출발 날짜·시간·좌석 고르면 종이 승차권 | arex-139 "Reserve departure date, time and seat on the ticket machine", arex-138 "board the train with your physical ticket", arex-140 | 맞음. 메뉴 이름 미확인을 밝힘(좋음) |
| ③ 오른쪽 위 언어(ENGLISH - KRW), Express Train 탭, Departure Station·Arrival Station·Train Time | arex-141 | 맞음 |
| ③ Ticket Reservation → Reserve | arex-142 | 맞음 |
| ③ Member / Non-member Reservation, 비회원은 이메일만 | arex-143 "If you select Non-Member Reservation, only your email address is required." | 맞음 |
| ③ 6자리 Verification Code, Ticket Confirmation Number 6자리, Re-enter | arex-144 "Please enter the 6-digit number." ×2, "Please enter it again." | 맞음 |
| ③ Change Seat | arex-145 | 맞음 |
| ③ Discount → Exchange Code 13자리 → Verify → Total Amount 0 KRW → Pay → QR | arex-146·147 / 공식 guide "교환번호 13자리 입력 칸과 인증버튼" | 맞음 (공식 원문으로도 13자리 확인) |
| 6~12세: 클룩은 어른과 같은 값, 어린이 요금은 현장 구매 | arex-148 "If you wish to purchase tickets at the child rate (ages 6-12), please make your purchase on-site. Child and adult tickets are sold for the same price on Klook" | 맞음 |
| 6~12세: 발매기 인원 선택에서 '어린이' | 공식 guide "어른(만 13세 이상) … 어린이(만6세~12세)", "04. 인원(어른, 어린이) 선택" | 맞음 |
| 0~5세 무료(자리 안 차지), 어른 1명당 1명, 더 있거나 자리 필요하면 어린이 표, "공항철도 공식 안내와 클룩 안내가 같아요" | Klook arex-148 "Children aged 0-5 can enter free of charge provided they will not occupy separate seats", "A paying adult can only bring 1 child". 공식 guide는 "보호자 1인이 동반하는 유아가 1인을 초과하거나 좌석이 필요한 경우 어린이로 승차권을 구매하셔야 합니다"만 있음. 공식 guide·introduce 어디에도 '0~5세'·'무료' 글자 없음 | **'0~5세'·'무료'는 Klook 글. "공식과 같다"는 부풀림 → 필수 2** |
| 휠체어석: 공식 안내 현장 구매만 | 공식 guide "4.휠체어 좌석은 현장구매만 가능합니다." | 맞음 |
| 어른 13,000원 | 공식 introduce "어른 : 13,000원" | 맞음 |
| 짐 1개+손가방 1개, 먹고 마시기 금지, 짐 두는 곳, 유모차·휠체어 | arex-148 | 맞음, "공식 페이지에서는 확인하지 못했어요"로 출처 구분(좋음) |
| 값: "클룩 결제 화면에 나와요. 공식 요금과 비교해 보고 사세요" | arex-129 "cheaper than buying on-site!"는 Klook 홍보 문구 | 홍보 문구를 옮기지 않고 비교만 권함. 통과 |
| 예시 화면의 가격·날짜 | arex-132~147의 US$ 25.50, ₩8,700, 2024·2026 날짜, 열차번호, 바우처 번호 | 페이지에 0개. 통과. 출처 줄에 "화면 속 가격과 날짜는 예시 화면이라 쓰지 않았어요" 명시 |

## 2. '우리 판단' 표시·Klook 안내를 공식처럼 쓴 곳

- 통과: "우리 판단: 공항에서 사도 충분해요"(ko:220), "우리 판단: 휴대폰 인터넷이 되면 ①, 안 되면 ②"(ko:241), 기존 "우리 판단: 숙소가 서울역 근처일 때".
- 통과: 환불·변경 안내마다 "(클룩 앱 화면 안내)"로 출처를 붙임. 휠체어석은 "공식 안내:"로 붙임.
- 불합격 1곳: ko/en/ja/zh-tw:233 "(공항철도 공식 안내와 클룩 안내가 같아요)" — 필수 2.
- 표시 없는 추론 1곳(권장 2): ② 1번 "도착 전에 적어 두면 휴대폰 인터넷이 없어도 돼요".

## 3. 버튼 글 변경

- airport-to-seoul:237, seoul-subway:135 × 4개 언어 = 8곳. "클룩에서 직통열차 바우처 미리 사기(타기 전 열차표로 바꿔요)" 등.
- 근거: arex-131 "Book your AREX voucher on klook", "To exchange your voucher for the AREX train ticket", "an unactivated Klook voucher can't be used to board the train". → '바우처'·'타기 전 교환' 모두 화면 사실과 맞음. 통과.
- 같은 버튼 essentials.md:158도 커밋 efda024에서 같은 뜻으로 맞춰짐(확인만, 이번 검토 대상 아님).
- 남은 어긋남(권장 3): seoul-subway:137 버튼 바로 아래 문장은 아직 "클룩에서 산 표는 확인서의 사용 방법을 따르세요"(옛 안내). 틀린 말은 아니지만, 버튼은 '바꿔야 한다'고 하고 아래 문장은 바꾸는 방법으로 이어 주지 않음(A to Z).

## 4. 빌드

- 방법: `/tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/rv5build`에 `git archive origin/main | tar -x`, 바뀐 8개 파일을 a271a7c 판으로 덮어씀, `python3 build.py` → "Built 160 pages".
- 검사: 8개 결과 페이지(ko·ja·zh-tw·영어 루트 × airport-to-seoul·seoul-subway)의 모든 내부 href를 dist 안 파일·id와 대조. 깨진 링크 0, 없는 앵커 0. 앵커 #pick, #express, #express-buy, #express-klook, #express-klook-how, #late, #prep, #bus, #taxi 모두 4개 언어에 있음. seoul-subway의 `/…/airport-to-seoul/#prep` 4개 언어 모두 열림.
- 비교표는 4개 언어 모두 `<table>`로 그려짐(페이지당 표 2개: 기존 1 + 새 1). 접힘 안의 굵은 글씨·목록·링크도 그려짐(남은 `**`, `](#`, `{{` 0개).
- Klook 버튼은 4개 언어 모두 같은 제휴 주소(klook_airport)로 그려짐. 주소 자체는 열지 않음(지시대로).

## 반드시 고칠 것

### 필수 1. 환불·변경 안내를 세 방법 전부로 넓혀 씀 (근거 넘김)
- 근거 화면: "Tickets cannot be refunded after selecting the train number, changes need to be made at the counter"는 **클룩 앱 활성화 화면(Select ticket, arex-133)에만** 있음. 공식 웹사이트(③)·발매기(②)로 바꾼 표에 같은 규정이 적용되는지는 화면·공식 원문 어디에도 없음. 공식 guide에는 웹 예매 표의 열차·좌석 변경 기능(3회까지)이 따로 있어, 웹으로 바꾼 표는 다를 수도 있음(확인 안 됨). [7eb4ec94#2990] 기준으로 범위를 좁히거나 '확인 못 함'으로 써야 함.
- 위치와 고칠 글:
  - **ko:228** 지금 "| 바꾸기·환불 | 열차를 고른 뒤에는 환불이 안 되고, 변경은 창구에서(클룩 앱 화면 안내). 열차 고르기 전 취소는 클룩 예약 화면의 규정을 보세요 | …"
    → "| 바꾸기·환불 | 클룩 앱에서 열차를 고르면 그 뒤에는 환불이 안 되고, 변경은 창구에서 해요(클룩 앱 화면 안내). 공식 웹사이트·발매기로 바꾼 표의 변경·환불은 확인하지 못했어요. 열차 고르기 전 취소는 클룩 예약 화면의 규정을 보세요 | (오른쪽 칸 그대로) |"
  - **en:228** → "| Change or refund | If you activate in the Klook app: no refund after you pick a train, and changes are made at the counter (Klook app screen). For a voucher exchanged on the AREX website or at a machine, we have not confirmed the rules. For cancelling before that, see the rules on your Klook booking | (unchanged) |"
  - **ja:228** → "| 変更・払い戻し | Klookアプリで列車を選んだ後は払い戻し不可、変更は窓口で(Klookアプリ画面の案内)。公式サイト・券売機で引き換えた切符の変更・払い戻しは確認できていません。選ぶ前の取り消しはKlook予約画面の規定を見てください | (そのまま) |"
  - **zh-tw:228** → "| 變更、退票 | 在Klook App選了車次後不能退票,變更要到櫃台(Klook App畫面的說明)。在官方網站或售票機換的車票怎麼變更、退票,我們還沒確認。選車次前能否取消,請看Klook訂單畫面的規定 | (不變) |"
  - **ko:279** 지금 "… 클룩 바우처로 바꾼 표는 열차를 고른 뒤에는 환불이 안 되고, 변경은 창구에서 해요(클룩 앱 화면 안내)."
    → "… 클룩 앱에서 바꾼 표는 열차를 고른 뒤에는 환불이 안 되고, 변경은 창구에서 해요(클룩 앱 화면 안내). 공식 웹사이트·발매기로 바꾼 표는 확인하지 못했어요. 직통열차 고객안내센터에 물어보세요."
  - **en:279** → "… A ticket activated in the Klook app: no refund after you pick the train, and changes are made at the counter (Klook app screen). For a voucher exchanged on the AREX website or at a machine we have not confirmed the rules; ask at the Express customer service center."
  - **ja:279** → "… Klookアプリで引き換えた切符は、列車を選んだ後は払い戻しできず、変更は窓口で(Klookアプリ画面の案内)。公式サイト・券売機で引き換えた切符は確認できていません。直通列車カスタマーセンターで聞いてください。"
  - **zh-tw:279** → "… 在Klook App換的車票,選了車次後不能退票,變更要到櫃台(Klook App畫面的說明)。在官方網站或售票機換的車票我們還沒確認,請問直達車旅客服務中心。"

### 필수 2. 0~5세 줄: Klook 글을 "공식과 같다"고 씀 (Klook 안내를 공식처럼)
- 근거: '0~5세'·'무료'·'어른 1명당 1명'은 Klook(arex-148) 글. 공식 guide 원문은 "보호자 1인이 동반하는 유아가 1인을 초과하거나 좌석이 필요한 경우 어린이로 승차권을 구매하셔야 합니다"뿐이고, 나이 범위(0~5)와 '무료'라는 글자는 공식 guide·introduce에 없음. 뜻은 맞물리지만 "같아요"는 공식이 말하지 않은 것을 공식에 붙임.
- 위치와 고칠 글 (각 언어 **:233**):
  - ko 지금 "0~5세 아이: 자리를 따로 차지하지 않으면 무료예요. 어른 1명당 1명까지이고, 더 있거나 자리가 필요하면 어린이 표를 사요(공항철도 공식 안내와 클룩 안내가 같아요)."
    → "0~5세 아이: 클룩 안내는 '자리를 따로 차지하지 않으면 무료, 어른 1명당 1명까지, 더 있으면 어린이 표'예요. 공항철도 공식 안내는 '보호자 1명이 데려가는 유아가 1명을 넘거나 좌석이 필요하면 어린이 표'예요."
  - en → "Children aged 0–5: Klook says they ride free if they do not take their own seat, one per paying adult, and each extra child needs a child ticket. The AREX official guide says: if one guardian brings more than one infant, or an infant needs a seat, buy a child ticket."
  - ja → "0〜5歳の子ども:Klookの案内は「自分の席を使わなければ無料、大人1人につき1人まで、それ以上は子どもの切符」。空港鉄道の公式案内は「保護者1人が連れる幼児が1人を超えるか、席が必要なら子どもの切符」です。"
  - zh-tw → "0〜5歲的孩子:Klook的說明是「不另外占座位就免費,每位成人限帶1名,超過的要買兒童票」。機場鐵路官方說明是「一位監護人帶的幼兒超過1名,或幼兒需要座位,就要買兒童票」。"

## 권장 (틀린 정보는 아님)

1. **zh-tw:243** "(最快)"(가장 빠름) — ko "가장 짧아요"·en "shortest"·ja "いちばん短い"는 '단계가 가장 짧음'. 앱이 가장 빠르다는 근거는 없음 → "(步驟最少)".
2. **② 1번(4개 언어 :252)** "도착 전에 적어 두면 휴대폰 인터넷이 없어도 돼요" — 화면에 없는 추론. 바우처 번호는 예약 확인 화면에서 볼 수 있다는 근거는 있음(arex-136). "우리 판단:"을 붙이면 됨. 예: ko "도착 전에 적어 두세요(우리 판단: 그러면 휴대폰 인터넷이 없어도 발매기에 넣을 수 있어요)."
3. **seoul-subway:137(4개 언어)** "클룩에서 산 표는 확인서의 사용 방법을 따르세요" → 바꾸는 방법으로 바로 연결. ko "클룩 바우처는 타기 전에 열차표로 바꿔야 해요: [바꾸는 3가지](/ko/airport-to-seoul/#express-klook-how)." / en "A Klook voucher must be turned into a train ticket before boarding: [3 ways](/airport-to-seoul/#express-klook-how)." / ja "Klookのバウチャーは乗る前に乗車券に引き換えが必要です:[引き換える3つの方法](/ja/airport-to-seoul/#express-klook-how)。" / zh-tw "Klook憑證上車前要先換成車票:[換票的3種方法](/zh-tw/airport-to-seoul/#express-klook-how)。"

## 참고 (고칠 필요 없음, 기록만)

- 공식 guide의 발매기 화면 설명에 탭 "도착역/열차선택/인원선택/좌석선택/구매방식/결제금액"이 있음. 클룩 바우처 번호를 넣는 메뉴가 '구매방식'일 가능성이 있으나 원문에 없어 확인 안 됨 → 페이지의 "메뉴 이름은 확인하지 못했어요"는 맞는 처리.
- Klook 화면 속 2020년 종이 승차권(arex-140)에는 "출발 5분 전까지 탑승"이 찍혀 있고, 공식 guide는 "열차 출발시각 3분 전 까지 승강장". 페이지는 공식(3분)을 씀 → 맞음.
- 판정자: 이 문서 전체가 독립 검토(작성자 아님). 화면 22장은 이미지로 직접 봄, 공식 3쪽은 2026-11-27 직접 받아 글자 검색.
