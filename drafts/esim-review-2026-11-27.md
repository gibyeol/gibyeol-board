# essentials eSIM 절 독립 검토 (2026-11-27)

- 검토자: 독립 검토(이 수정을 쓰지 않은 하위 작업). 읽기만 함, 대상 파일은 고치지 않음.
- 대상: 브랜치 `claude/determined-euler-xsz86i` 커밋 88919ee(eSIM 절) + efda024(klook_airport 버튼 글), `git diff origin/main HEAD -- content/*/essentials.md`
- 근거: Klook 'South Korea SKT Unlimited Data eSIM with Free T-Money Card' 화면 8장 `wondu-archive/raw-from-scratchpad/klook-wondu-screens-2026-11-27/skt-esim-150.webp ~ skt-esim-157.png`(원두가 브라우저로 연 화면), 공항철도 `arex-128.webp`·`arex-129.png`·`arex-131.png`. Klook 사이트·tpx.li는 열지 않음.
- 원두 원문 기준: [7eb4ec94#3526] "(나)로 진행해" / [7eb4ec94#3295] "틀린정보만 없으면돼" / [7eb4ec94#2990] 불확실 정보는 예상+출처, 없으면 뺌 / [7eb4ec94#2954] 실제로 쓸 수 있는 사람 기준 / [7eb4ec94#963] 한국인·외국인 구분 없음 / [7eb4ec94#1227] A to Z.

## 숫자 요약

- 화면과 대조한 사실 26개 × 4개 언어: 26개 모두 화면 글자와 맞음(틀린 사실 0).
- 가격: 0곳(US$ 8.95 등 화면 가격 안 들어감). '010'·'한국 번호' 같은 화면에 없는 말: 새 글에 0곳(기존 143행 카카오 T 표의 '한국 번호'는 이번 변경 아님).
- 비교 문장이 다른 상품을 '안 된다'로 깎은 곳: 0.
- 해석 2곳: 둘 다 틀린 번역 아님(약점 1곳은 아래 권장).
- 버튼 글 2개(klook_esim_alt, klook_airport): 사실과 맞음.
- 빌드: 160쪽 생성, 4개 언어 essentials 내부 링크·앵커 깨짐 0, `{{` 미처리 0, `<details>` 열림/닫힘 2/2, klook_esim_alt(NYU2lYBJ)·klook_airport(u3y9PkpB) 버튼 각 1개 렌더.
- **반드시 고칠 것: 0건.** 고치기 권장: 4건. 남는 약점(고칠 글 없음): 3건.

## 1. 새 사실 ↔ 화면 대조 (ko 기준 줄, en·ja·zh-tw 같은 줄 번호)

| # | 글(ko) | 화면 원문 (위치) | 판정 |
|---|---|---|---|
| 1 | 결제하고 30분 안에 메일 (78) | "eSIM will be delivered to your email within 30 minutes of payment" (151, 154) | 맞음 |
| 2 | 발신 kbooks-global@usimkorea.kr (78) | "30 minutes after payment at Klook, You can get an email from kbooks-global@usimkorea.kr." (154) | 맞음 |
| 3 | 확인 메일 안 보이면 클룩 고객센터 (78) | "If you don't see any confirmation, reach out to our customer support." (156) | 맞음 |
| 4 | 기본 무제한 (65) | "Data is unlimited by default" (151) / "Unlimited (e SIM)" (152) | 맞음 |
| 5 | 4G LTE (65) | "Internet speed 4G LTE 100Mpbs" (153) | 맞음(속도 수치는 안 씀) |
| 6 | 핫스팟 안 됨 (65) | "Hotspot Sharing No" (153) | 맞음 |
| 7 | 속도·사용량 예고 없이 제한 (65) | "Under the Fair Usage Policy, data speed and usage may be limited … without prior notice" (155) | 맞음 |
| 8 | 페이스타임·보이스톡 같은 인터넷 통화 됨 (65) | "m-VoIP (Face time, Kakao Talk voice talk, etc.) service is available" (155) | 맞음 |
| 9 | 입국 뒤 08~22시 여권 인증 (66, 87) | "Passport information verification can be done between 08 a.m. and 10 p.m. after immigration to Korea" (154) | 맞음 |
| 10 | 인증하면 데이터+전화·문자 (66) | "If you do Passport information verification, you can use phone calls and texts as well as data" (154) | 맞음 |
| 11 | 인증 안 하면 데이터만 (66) | "If you don't do Passport information verification, only the data is available" (154) | 맞음 |
| 12 | 인증 뒤 음성 충전 따로 결제 (66, 88) | "After Passport information verification, please top-up payment for voice charging" (154) / "additional top-ups are required to use calls and texts" (151) / "Data, In&Out Calls and Texts (Extra Top-up)" (152·153) | 맞음 |
| 13 | 외국인 전용·한국 여권 인증 불가 (55, 64) | "This product is for foreigners only and Passport information verification is not possible with Korean passports" (154) | 맞음 |
| 14 | 인증 안내 한·영·일·중(번체·간체) (87) | "How to Passport information verification KR / EN / JP / CN(T) / CN(S)" (154) | 맞음 |
| 15 | 3일 이상 무료 티머니 (69, 89) | "Free T-Money card is provided for customers who purchase plans of 3 days or more." (151) | 맞음 |
| 16 | 로밍센터 직접 방문·바우처 제시 (69, 89) | "you will have to visit SKT roaming center to pick up the T-money card" (151) / "visiting the SKT Roaming Center (At the airport) and presenting your klook eSIM voucher" (155) | 맞음 |
| 17 | T1 1층 13번 출구, T2 1층 6~7번 출구(24시간) (89) | "terminal 1 : 1F Exit 13", "terminal 2 : 1F, Exit 6-7 (24/7)" (151) | 맞음(24시간은 T2에만 붙임 — 화면대로) |
| 18 | 기간 2~90일 (68) | "Validity 2-90 days" (153) | 맞음 — 다만 선택지는 띄엄띄엄(권장 1) |
| 19 | 연장 불가 (68) | "Extension is not possible as a prepaid eSIM." (155) | 맞음 |
| 20 | 호환 문제 환불·취소 불가 (70) | "No refunds or cancellations can be made due to SIM compatibility issues" (154) / 같은 뜻 (155) | 맞음 |
| 21 | 실물 듀얼 SIM 모델(홍콩·중국판 iPhone Max) 불가 (70) | "Physical dual SIM models(e.g. HK, China iPhone Max models) are not applicable for this eSIM" (154) | 맞음 |
| 22 | 국가 잠금 폰 불가 (70) | "eSIMs cannot be used on country-locked mobile phones" (155) | 맞음(풀이는 3절) |
| 23 | 출국 전 설치 가능·사용일은 도착부터·와이파이 필요·QR 60일·다른 기기 불가 (79) | "You can pre-install it before you depart … date deduction … from the time you arrive in Korea." / "You need a Wi-Fi environment for registration." / "QR code must be used within 60 Days of purchase" / "After scanning the eSIM QR, it's not available on other devices" (155) | 맞음 |
| 24 | iOS 15.0 이상 (70) | "(iOS is at least 15.0 version)" (155) | 맞음 |
| 25 | 등록 뒤 바로 사용 (86) | "You can use it immediately after registering eSIMs" (155) | 맞음 |
| 26 | 설정 경로 아이폰 3단계·안드로이드 3단계·재시동 1~2번·'SKT' 확인 (80~82) | iOS ①②③ (157), Android ①②③ (156), "reboot the device 1-2 times, then check that the carrier 'SKT' has been selected" (156·157) | 맞음 |

4개 언어: 26개 사실이 en·ja·zh-tw에 모두 같은 줄에 같은 내용으로 있음. 차이 2곳: (가) 81행 머리말이 ko만 "갤럭시", 나머지는 "Android(Galaxy)" — 화면 제목은 "eSIM Setting - Android"(156) → 권장 3. (나) en은 "Under the Fair Usage Policy"를 이름까지 씀, ko·ja·zh는 이름 없이 내용만 — 사실 차이 아님.

## 2. 비교 문장 (55행)

- ko "아래 상품 중 전화·문자가 된다고 저희가 상품 화면으로 확인한 것은 이것뿐이에요." en "the only one we have confirmed from its product page", ja "私たちが商品ページで確認できたのはこれだけ", zh "我們從商品頁確認…只有這一款".
- '확인한 것'으로 한정했고, Yesim·klook_esim(5G)이 전화·문자가 '안 된다'고 쓴 곳 없음. 출처 문단에도 "Yesim 상품 페이지와 클룩 SKT 5G eSIM 상품 페이지 확인 못함"을 적음 → 확인 안 한 것을 부정하지 않음. **통과.**
- 그림 essentials-3 카드도 "통화·문자가 포함된 요금제로"(tools/figgen/gen-guides1.py:370)라 어긋나지 않음.

## 3. 해석 2곳

- **"Click 'Main' for main line/iMessage/FaceTime"(157) → ko 80행 "기본 회선·iMessage·FaceTime에는 'Main'(주 회선)을 골라요"** (en "choose "Main" for your main line, iMessage and FaceTime", ja「Main」(主回線), zh「Main」(主要號碼)). 화면 글자 그대로 옮김, 틀린 번역 아님. 약점: 'Main'이 원래 쓰던 회선인지 SKT 회선인지 화면에 없고, 실제 아이폰 화면에 'Main'이라는 글자가 뜨는지 이번에 확인 못함 → 따라 하기 시험에서 막힐 수 있음. 확인 안 된 풀이를 덧붙이면 불확실 정보가 되므로 지금 글을 유지하고 개선 목록에 올리는 것을 권함(약점 1).
- **"country-locked mobile phones"(155) → ko "국가 잠금 폰(한 나라 통신망에서만 쓰게 잠긴 폰)"**, ja「国ロック端末(ある国の通信網でしか使えないようロックされた端末)」, zh「有國家鎖的手機(被鎖定只能在某個國家電信網路使用的手機)」, en은 "country-locked phones" 그대로(풀이 없음). 풀이는 낱말 뜻을 푼 것이고 화면과 어긋나지 않음. 뒤에 위 '먼저 내 폰 확인'(51행: 이동통신사 잠금 'SIM 제한 없음' 확인)으로 보내 행동으로 이어짐. **통과.**

## 4. 버튼 글

- klook_esim_alt "클룩에서 SKT 무제한 데이터 eSIM 보기" / "SKT Unlimited Data eSIM on Klook" / 「KlookでSKT無制限データeSIMを見る」/「在 Klook 看 SKT 無限數據 eSIM」 — 상품 제목(150)과 맞음. 원두 확인: 이 링크의 상품 = 이 화면 상품. 섹션 3에서 이 버튼이 맨 아래 버튼(59·61·72행 순)이라 "맨 아래" 표현도 맞음. **통과.**
- klook_airport (158행) "클룩에서 공항철도 직통열차 바우처 사기(타기 전 열차표로 바꿔요)" ×4 — "Express train: Travel non-stop between Incheon Airport and Seoul Station"(129), "an unactivated Klook voucher can't be used to board the train", "3 ways To exchange your voucher for the AREX train ticket"(131)과 맞음. airport-to-seoul·seoul-subway의 같은 버튼과 뜻이 같음(essentials만 '미리' 대신 '공항철도'). **통과.** 범위 밖 메모: 이 링크(u3y9PkpB)가 그 화면 상품이라는 원두 확인 기록은 이번 근거에 없음(klook_esim_alt만 원두 확인이 붙어 있음).

## 5. 빌드

`git archive origin/main | tar -x` → 4개 essentials.md를 HEAD 것으로 바꿈 → `python3 build.py` → "built 160 pages". 4개 언어 essentials의 `/…` 내부 링크·`#앵커` 전부 대상 있음(깨짐 0). 글 안 상호 참조 이름도 실제 제목과 같음: '먼저 내 폰 확인'·「まず自分のスマホを確認」·「先確認你的手機」·"Check your phone first", '산 다음: eSIM 설치하고 켜기'의 '안 되면'(103행), '4. 돈과 교통카드'(114행) 등 4개 언어 모두 있음.

## 반드시 고칠 것

없음(0건). 화면과 다른 사실, 가격, 화면에 없는 '010·한국 번호', 다른 상품을 깎는 문장을 찾지 못함.

## 고치기 권장 (틀린 사실은 아니나 오해·따라 하기 약점)

### 권장 1 — 기간 선택지가 띄엄띄엄 (68행)
- 지금: ko "2~90일 중 골라요." / en "choose 2 to 90 days." / ja「2〜90日から選びます。」/ zh「2 到 90 天之間選。」
- 이유: 상품 정보표는 "2-90 days"(153)지만 실제 선택지는 2·3·4·5·6·7·8·9·10·15·20·30·60·90일(152). "아무 날수나 고를 수 있다"로 읽힐 수 있음(예: 12일 없음).
- 고칠 글:
  - ko "2~10일, 15·20·30·60·90일 중 골라요."
  - en "choose 2–10, 15, 20, 30, 60 or 90 days."
  - ja「2〜10日、15・20・30・60・90日から選びます。」
  - zh「可選 2 到 10 天,或 15、20、30、60、90 天。」

### 권장 2 — '어느 것이든 괜찮아요'와 한국 여권 제한을 한 문장에 (55행)
- 지금: ko "데이터만 필요하면 아래 버튼 어느 것이든 괜찮아요. … 맨 아래 상품은 외국 여권 소지자만 쓸 수 있어요(한국 여권 불가)."
- 이유: 같은 문단 끝에서 제한을 말하므로 틀린 글은 아님. 다만 첫 문장만 읽는 사람(두괄식으로 읽는 사람)에게는 한국 여권 소지자도 맨 아래 상품을 살 수 있다고 읽힘([7eb4ec94#2954] 실제로 쓸 수 있는 사람 기준).
- 고칠 글(첫 문장만):
  - ko "데이터만 필요하면 아래 버튼 어느 것이든 괜찮아요(맨 아래 상품은 외국 여권 소지자만)."
  - en "for data only, any of the buttons below will do (the last one is for foreign passport holders only)."
  - ja「データだけなら、下のボタンのどれでも大丈夫です(いちばん下の商品は外国のパスポートを持つ人だけ)。」
  - zh「只要上網,下面哪個按鈕都可以(最下面那款只限持外國護照的人)。」

### 권장 3 — ko 머리말 '갤럭시'만 다름 (81행)
- 지금: ko "**갤럭시:**" / 나머지 "Android(Galaxy)"
- 이유: 화면 제목은 "eSIM Setting - Android"(156). 4개 언어 맞춤.
- 고칠 글: ko "**안드로이드(갤럭시):**" (en·ja·zh는 그대로)

### 권장 4 — ko 갤럭시 메뉴 우리말 이름이 아래 상자와 다름 (81행)
- 지금: ko "Add mobile plan(모바일 요금제 추가) → Scan the carrier QR code(통신사 QR 코드 스캔)"
- 이유: 같은 쪽 '산 다음' 상자(107행, 삼성전자 한국 안내 출처)는 한국어 화면 이름을 "eSIM 추가 → QR 코드 스캔"으로 씀. 한국어로 설정한 갤럭시를 쓰는 사람은 '모바일 요금제 추가'를 못 찾을 수 있음. 괄호 안은 영어 화면을 옮긴 말이라 틀린 사실은 아님.
- 고칠 글(ko만): "Add mobile plan(한국어 화면은 'eSIM 추가') → Scan the carrier QR code(한국어 화면은 'QR 코드 스캔')". ja·zh는 각 언어 삼성 화면 이름을 이번에 확인하지 못해 고칠 글을 내지 않음(그대로 둠).

## 남는 약점 (고칠 글 없음, 숨기지 않음)

1. 아이폰 'Main'이 어느 회선인지 화면에 없음(3절). 확인 전에는 풀이를 붙이지 않는 것이 맞고, 개선 목록에 올릴 것.
2. 제1터미널 로밍센터 운영 시간은 화면에 없음(24시간 표기는 T2만). 밤늦게 T1에 도착하는 사람은 티머니를 못 받을 수 있으나 근거가 없어 쓸 수 없음.
3. 화면의 "Validity: Use your voucher on the selected date"(156, 클룩 공통 문구로 보임 — 추론)와 "date deduction … from the time you arrive"(155)가 함께 있음. 글은 뒤엣것만 씀. 날짜를 고르는 칸("Check availability", 152)의 의미는 화면만으로 확정 못함.
