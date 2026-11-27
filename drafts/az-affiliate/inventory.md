# 제휴 A to Z 1단계: 목록 (2026-11-27 02:1x KST 작성, Claude)

원두 지시 원문: "제휴 걸려있는 곳과 지금 걸 수 있는 곳과 관련된 부분 A to Z 검토 개선 작업시작해" [7eb4ec94#2827]. 앞선 질문: "점점 수익화와 관련 없는 방향으로 가는거 아니야?" [7eb4ec94#2805].
기준 원문: A to Z [7eb4ec94#1227], 따라 하기 품질 [7eb4ec94#1233], "제휴관련된 부분도 후킹을 위해서는 그림이 무조건 들어가야하지 않겠어?" [7eb4ec94#643]. 전부 trendmin-threads CLAUDE.md '콘텐츠 제작 원칙'과 ops/wondu-words.md에 원문 있음.

이번 단계 범위: 저장소와 저장된 출처만 읽음. 웹은 열지 않음. 사이트 파일(content·data·build.py·static)은 고치지 않음.
읽은 것: `origin/main`(d93021a)의 content/{en,ko,ja,zh-tw}, build.py, data/affiliates.json, data/site.json / trendmin-threads data/site/visits.csv(11/24~11/26 14:42Z) / ops/affiliate-plan.md, ops/affiliate-signup-list.md.

---

## 0. 먼저 알아야 할 것 — 방문 수 (확실, visits.csv)

| 무엇 | 숫자 | 근거 |
|---|---|---|
| visits.csv 전체 페이지 조회(11/24~11/26 14:42Z) | 155 | visits.csv 55줄 합계 |
| 그중 바깥에서 들어온 조회(유입 사이트가 nadri-guide.pages.dev가 아닌 것) | 36 | 같은 파일, referer_host 기준 |
| **제휴 버튼이 있는 4개 페이지의 바깥 조회** | **0** | essentials 7 · airport-to-seoul 4 · seoul-subway 2 · abroad-esim 1 — 전부 ko, KR, desktop, 유입 nadri-guide.pages.dev |
| 바깥 조회 36이 닿은 곳 | 홈(/) 12, 가이드 목록 12(en 6·zh-tw 4·ja 2), 이름 도구 6, 겨울 패딩 6 | 같은 파일 |

- **확실:** 지금 제휴 버튼이 있는 페이지에는 바깥 방문자가 한 명도 없었다. 그래서 '조회수로 우선순위 정하기'는 지금 숫자로는 성립하지 않는다(모두 0 또는 내부 조회).
- **추론:** 제휴 페이지의 조회(KR·desktop·사이트 안에서 이동)는 원두나 작업 확인 조회일 가능성이 크다. 누구의 조회인지는 데이터로 확인할 수 없다.
- **뜻:** A to Z를 고쳐도 바깥 방문이 그 페이지에 닿지 않으면 수익은 0이다. 수익과의 거리는 ① 페이지 완성도(이번 작업) ② 바깥 방문자가 그 페이지로 가는 길(홈·가이드 목록·스레드 → 공항·필수 준비) 둘 다다. ②는 plan.md에 원두 결정 거리로 따로 적는다.

---

## 1. 지금 제휴 버튼이 보이는 페이지 (확실, `git show origin/main`)

버튼 문법: 본문 `{{aff:키|버튼 글자}}` → build.py 66~72행이 data/affiliates.json의 url이 있을 때만 버튼과 '광고 링크' 표시를 그림(빈 url이면 아무것도 안 그림). 할인 상황판 카드의 `"aff"` 키(build.py 205~206행)는 data/에 쓰인 곳이 없음(`git grep '"aff"' origin/main -- data/` 0건).

| 페이지 | 언어 | 제휴 키 (행) | 버튼 수 | 조회 11/24~26 (바깥) | approved 줄 |
|---|---|---|---|---|---|
| essentials (필수 준비) | en·ko·ja·zh-tw 모두 같은 행 | yesim_kr(54), klook_esim(56), klook_esim_alt(60), klook_tmoney(75), klook_wowpass(77), klook_airport(104) | **6** | ko 7 (0) / 나머지 0 | 4개 언어 모두 `approved: 2026-11-26` → 고치면 원두 재승인 |
| airport-to-seoul (공항→서울) | 4개 언어 같은 행 | klook_tmoney(83), klook_tmoney(180, **같은 버튼 두 번**), klook_wowpass(184), klook_airport(188) | 4 | ko 4 (0) / 나머지 0 | 없음(검토 전 상태) |
| seoul-subway (지하철) | 4개 언어 같은 행 | klook_tmoney(98), klook_wowpass(102), klook_airport(120) | 3 | ko 2 (0) / 나머지 0 | 없음 |
| abroad-esim (한국에서 다른 나라로 갈 때 데이터) | 4개 언어 같은 행 | yesim_all(44) | 1 | ko 1 (0) / 나머지 0 | 없음 |

쓰인 키 7개: yesim_kr, yesim_all, klook_esim, klook_esim_alt, klook_tmoney, klook_wowpass, klook_airport (모두 data/affiliates.json에 tpx.li 주소 있음, 3~42행).
안 쓰인 키: 빈 url 4개(airalo_kr 13행, agoda_seoul 43행, yesstyle_oy 48행, coupang_board 53행) / url 있으나 어느 페이지에도 없음 5개(klook_osaka_pass 58행, klook_everland_day 63행, klook_everland_bus 68행, klook_usj 73행, klook_tokyo_disney 78행 — ops/affiliate-plan.md 8행과 같음).

### 1-1. 버튼은 없지만 제휴 스크립트가 도는 페이지
`disclosure: yes`인 페이지는 쿠키 '동의' 뒤에 Travelpayouts·Skimlinks 스크립트를 불러옴(build.py 489~497행, data/site.json 325~329행). 12쪽 × 4개 언어:
abroad-esim, airport-to-seoul, essentials, seoul-subway(버튼 있음) + convenience-store, daiso, deals, duty-free, kbeauty-how-to-choose, olive-young, shopping-streets, tax-refund(버튼 없음, Skimlinks용 — ops/affiliate-signup-list.md 45행).
- **Skimlinks 승인 여부는 기록에 없음**(signup-list 45행은 '신청, 사이트 ID'까지). 승인 전이면 이 8쪽에서 수익은 0이다(추론).
- 이 8쪽 조회: deals 15(바깥 0), olive-young 5(0), convenience-store 1(0), tax-refund 1(0), 나머지 0.

---

## 2. 지금 걸 수 있는 프로그램 (기록상 승인·동작만)

| 프로그램 | 상태 | 근거 |
|---|---|---|
| Travelpayouts 계정 → Klook | 승인·링크 동작 중(키 12개) | affiliate-plan.md 70행, affiliates.json |
| Travelpayouts → Yesim | 승인·링크 동작 중(키 2개) | affiliate-plan.md 70행, affiliates.json 3~12행 |
| Travelpayouts → KKday | 연결됨(링크 생성기 보임), 링크는 아직 0개. 1~3%, 쿠키 30일. 쇼핑 쿠폰 상품 없음 → 투어·체험·eSIM용 | signup-list 64~66행 |
| (주의) Travelpayouts 지급 방법 | **미설정**("set your payout method" 표시) → 쌓여도 못 받음 | signup-list 65행, affiliate-plan.md 129행 |

새 상품 링크는 원두가 Travelpayouts 링크 생성기에서 만들어야 생김(affiliate-plan.md 80행). Claude는 계정에 들어갈 수 없음.

### 2-1. 지금 키로 바로 놓을 수 있는 곳 (새 링크 불필요)

| 페이지 | 자리 (ko 행) | 키 | 적합도 판단 | 조회 (바깥) | approved |
|---|---|---|---|---|---|
| departure-day (출국하는 날) | 55행 "직통열차 승차권이 있어야 해요"(서울역 도심공항터미널 조건) | klook_airport | 높음 — 도심공항 수속에 직통열차 표가 '필수 조건'. 단 **Klook 표로 도심공항 수속이 되는지 확인 필요**(안 되면 버튼이 사람을 틀리게 보냄) | 0 | 4개 언어 approved → 재승인 |
| money (돈 쓰기) | 56~62행 와우패스 절 | klook_wowpass | 중간 — 같은 절이 "미리 예약하면 5,500원(wowpass.io)"이라고 공식 예약을 이미 씀. **Klook 값이 더 비싸면 버튼을 다는 게 원칙 위반**(disclosure.md 17행 "파트너의 상품이 다른 대안보다 못하면 그렇다고 말해요") → Klook 가격 확인 필요 | 0 | 재승인 |
| seoul-areas (숙소 지역) | 43행 서울역 도심공항터미널 "직통열차 승차권이 있으면" | klook_airport | 중간 — departure-day와 같은 확인 필요 | 0 | 재승인 |
| getting-around (서울 대중교통) | 29행 "티머니, 와우패스, 기후동행카드 중 하나" | klook_tmoney, klook_wowpass | 낮음~중간 — 이미 필수 준비·돈 쓰기로 링크를 넘김. 버튼을 더하면 같은 버튼이 사이트에 4곳 반복 | ko 1 (0) | ko는 approved 없음, en·ja·zh-tw approved |
| first-trip (첫 여행 4일) | 36행 "공항에서 교통카드나 WOWPASS, 데이터를 챙기고" | klook_tmoney/wowpass/esim | 낮음 — 이 문장은 다른 페이지로 넘기는 연결 문장. 버튼보다 링크 정리가 맞음(Claude 판단) | 0 | ko 없음, 나머지 approved |
| convenience-store (편의점) | 38~73행 티머니 사고·충전 | — | **버튼 안 맞음** — 이 페이지의 답이 '편의점에서 사기'임. 오히려 반대로, 다른 페이지의 "티머니 사기"가 이 페이지 #tmoney로 이어져야 함(A to Z 링크) | 1 (0) | 없음 |

### 2-2. 승인된 프로그램이지만 원두가 새 링크를 만들어야 놓을 수 있는 곳

| 페이지 | 자리 (ko 행) | 필요한 상품 | 근거 |
|---|---|---|---|
| ktx-busan | 18행 표 "클룩", 37행 "클룩: 2026년 4월 20일부터 코레일 실시간…" | Klook 코레일(KTX) 승차권 | affiliate-plan.md 43행. 본문이 이미 Klook을 정보로 씀 |
| palaces | 69행 "사진이 중요하다면 궁 한 곳 주변에서 두세 시간만 빌리세요" | Klook 또는 KKday 한복 대여 | affiliate-plan.md 47행. 107행 "한복 대여 가격(확인하지 못했어요)" |
| airport-to-seoul | #taxi 절(짐 많은 3~4명) | Klook 인천공항 픽업 차량 | affiliate-plan.md 55행. 본문은 외국인관광택시 정액을 이미 답으로 씀 → 넣을지 원두 판단 |
| jeju | 21행 "렌터카 회사 비교" 뺌 | Klook 제주 렌터카 | affiliate-plan.md 53행 |
| name (이름 도구) | — | Klook 인사동 도장 체험 | affiliate-plan.md 62행, 전략서 69행 |

조회는 위 다섯 쪽 모두 0(name만 20, 바깥 6 — 바깥 방문이 닿는 몇 안 되는 페이지).

---

## 3. 승인 대기·거절 (자리 아님 — 목록만)

| 프로그램 | 상태 | 근거 |
|---|---|---|
| Agoda·Trip.com (Travelpayouts) | 승인 대기 | affiliate-plan.md 72행 |
| Airalo (Impact) | 거절 "Low reach (traffic, followers)" | signup-list 62행 |
| Impact 마켓플레이스 | 브랜드 검색 안 됨, 보류 | signup-list 63행 |
| FlexOffers | 계정·트래픽 소스 거절 | signup-list 67~68행 |
| Awin 계정 | 열림(퍼블리셔 3168168). YesStyle 가입 요청, Stylevana **승인**(2026-11-27 원두 메일 화면, 링크 아직 없음), iHerb 신청 기록 없음. 정산 정보 페이지 오류 | signup-list 39~43행 |
| Rakuten → Olive Young US·APAC&EMEA | 신청 완료, 승인 대기 | signup-list 52행 |
| Skimlinks | 신청, 코드 12쪽에 설치. 승인 여부 기록 없음 | signup-list 45행 |
| Sovrn | 계정만 두고 링크 안 닮(원두 [7eb4ec94#2069]) | signup-list 57행 |
| 올리브영 글로벌 | 자격 없음(한국 183일 거주) | signup-list 44행 |
| Amazon, Coupang, 올리브영·무신사 큐레이터 | 보류 | signup-list 29~30행, affiliate-plan.md 74~75행 |
| Radical Storage·Airalo·EKTA·GetYourGuide (Travelpayouts 안) | 미가입(Join 필요) | affiliate-plan.md 20·24·25·26행 |
| Creatrip | 미가입 | affiliate-plan.md 22행 |

---

## 4. 이번 목록에서 나온 사실 오류·위험 (A to Z 밖이지만 제휴 관련)

1. **수익 구조 페이지(disclosure)가 사실과 다름 — 확실.** ko 11행·en 11행: 파트너로 쿠팡 파트너스(미가입), 에어알로(거절), 아마존(미신청)을 적고 "Nadri는 아마존 어소시에이트로서 적격 구매에 대해 수익을 얻어요"라고 씀. 실제로 쓰는 Travelpayouts·Yesim·KKday·Skimlinks·Awin·Rakuten은 없음. 4개 언어 `approved: 2026-11-26` → 고치면 원두 재승인. (같은 지적: ops/affiliate-plan.md 96행, 아직 안 고침)
2. **광고 표시 문구가 조건부 — 확실(문구), 위험 판단은 경향.** data/site.json 274행 ko "수수료를 받을 수 있고", 55행 en "may earn", 128행 ja "受け取ることがあります", 201행 zh-tw "可能獲得". 추천·보증 심사지침이 "받을 수 있음" 같은 불확정 문구를 불명확 예로 든다는 요약이 있음(affiliate-plan.md 94행, 원문 미열람 → 2단계에서 ftc.go.kr 원문 확인).
3. **essentials 6절 문장과 버튼이 어긋남 — 확실.** ko 100행 "늦게 도착하거나, 짐이 무겁거나, 여럿이 함께 이동한다면 미리 예약한 픽업이 더 간편할 때가 많아요" 바로 뒤 버튼은 공항철도 승차권(104행). '픽업(차량)' 상품은 없음 → 읽는 사람은 버튼이 픽업 예약이라고 오해할 수 있음.
