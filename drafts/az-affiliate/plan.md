# 제휴 A to Z 개선 계획 (2026-11-27 03:0x KST, Claude 안 — 원두 승인 전)

근거 파일: 같은 폴더 inventory.md, az-airport-to-seoul.md, az-essentials.md, az-seoul-subway.md, az-abroad-esim.md, az-departure-day.md, az-money.md, az-ktx-busan.md. 모두 Claude 자체 점검(독립 검토 아직 없음).

## 0. 순서를 정한 방법과 한계
- 지시는 "방문 수 × 수익 가능성 × 빈칸 크기"였는데, **방문 수는 쓸 수 없었다(확실)**: 제휴 버튼이 있는 4쪽의 바깥 조회가 0이다(inventory.md 0절). 그래서 방문 수 대신 **'바깥 방문이 닿는 곳에서 몇 번 눌러 오나'**를 썼다: 바깥 조회 36 중 홈(/) 12·가이드 목록 12. 홈(content/en/index.md)은 essentials·airport-to-seoul·abroad-esim으로 바로 연결(링크 확인), 가이드 목록은 모든 가이드를 묶어 보여 줌.
- 수익 가능성은 숫자가 없다(Klook 수수료 2~5%는 검색 요약, affiliate-plan.md 19행; 상품 값·클릭·예약 수는 기록 없음). 그래서 **높음/중간/낮음은 추론**이고, 기준은 "그 페이지 독자가 그 자리에서 실제로 돈을 쓰는 결정을 하는가"(원칙 8, 전략서 133행 "버튼은 추천 뒤에 붙을 뿐").
- **이 계획을 다 해도 바깥 방문이 이 페이지들에 오지 않으면 수익은 0이다.** 그래서 마지막 줄(우선 7)에 '방문 길'을 원두 결정 거리로 넣었다.

## 1. 우선순위

| 순 | 무엇 | 덮는 페이지(×4개 언어) | 수익 가능성(추론) | 빈칸 | 2단계에서 열 곳(호스트) | 웹 필요 |
|---|---|---|---|---|---|---|
| 1 | **사실 정정 묶음**: ① essentials 100행 '픽업' 문장과 공항철도 버튼 어긋남 ② airport-to-seoul 티머니 버튼 중복(83·180행) ③ 공항철도역 티머니 자판기 문장을 공항 페이지 3단계에 ④ 우리 페이지끼리 링크(편의점 #tmoney, money 와우패스, seoul-subway 기후동행카드, abroad-esim 확인법) ⑤ seoul-subway 티머니 사진 | essentials, airport-to-seoul, seoul-subway | 간접(신뢰) | 작음·싸게 고침 | 없음 | 아니오 |
| 2 | **Klook 3상품 '산 다음'**: 티머니 공항 수령, 와우패스, 공항철도 직통 — 받는 곳(지도 점)·보여 줄 것·됐는지 아는 법·안 될 때·환불. 와우패스 '교통용 티머니 잔액 따로'를 세 페이지에 같은 문장으로 | airport-to-seoul, essentials, seoul-subway (한 번 확인으로 3쪽) | **높음** — 바깥에서 한 번에 오는 두 쪽(홈→essentials·airport), 도착 직후 실제 구매 결정 | **큼** — 버튼 7개(3쪽 합) 모두 '산 다음' 없음 | www.klook.com(상품 3개 — 원래 주소는 원두가 대시보드에서, wondu-items.md 1번), wowpass.io, www.airportrailroad.com, www.airport.kr | 예 |
| 3 | **eSIM 설치·켜기·원래 유심 데이터 끄기·안 될 때** + 버튼 3개 중 고르는 기준(원칙 6) | essentials 3절, abroad-esim | **높음** — eSIM은 출국 전 '사는' 결정이 확실한 상품. abroad-esim은 홈 '출국' 띠(content/ko/index.md 32행)에서 바로 옴 | **큼** — 폰별 메뉴 순서·그림 0 | yesim.app(주소는 원두 대시보드 원래 링크로 재확인), www.klook.com(SKT eSIM 2개), support.apple.com, www.samsungsvc.co.kr, (다른 나라 갤럭시용 후보) www.samsung.com | 예 + 원두 폰 화면(wondu-items.md 4번) |
| 4 | **광고 표시 정확성**: ① disclosure 페이지 파트너 목록·아마존 문장 정정 ② 버튼 위 문구를 확정형으로("받을 수 있고" → 받는다) | disclosure, 12쪽 머리 문구(data/site.json 55·128·201·274행) | 간접(법·신뢰 위험 줄임) | 중간 | www.ftc.go.kr 또는 www.law.go.kr(추천·보증 심사지침 원문), 일본 문구는 www.caa.go.jp(스텔스 마케팅 고시) 후보 | 예(②만) / ①은 기록만으로 가능 |
| 5 | **departure-day 직통열차 표 사는 길 + klook_airport 놓을지** — Klook 표로 서울역 도심공항 수속이 되는지 확인 뒤에만 | departure-day, seoul-areas 43행 | 중간 — 도심공항 수속은 직통열차 표가 '필수 조건'이라 결정 지점이 분명 | 큼(사는 곳·방법·링크 모두 없음) | www.airportrailroad.com(도심공항터미널·승차권), www.klook.com(공항철도 상품) | 예 |
| 6 | **money 와우패스 사는 길 + Klook 값 비교** — 공식 예약(5,500원, money 62행)보다 비싸면 버튼 안 놓음 | money, departure-day 96행 | 중간~낮음 — 공식 예약이 이미 있음 | 큼 | wowpass.io, www.klook.com | 예 |
| 7 | **ktx-busan Klook 코레일 링크 + 예매 3곳 순서** | ktx-busan | 중간 — 장거리 열차 결제가 막힐 때의 대안(본문 37행) | 큼 | www.klook.com(코레일 상품 — 원두가 링크 생성 후), www.letskorail.com, www.korail.com(코레일+ 안내, 후보) | 예 + 원두 링크 생성 |
| 8 | palaces 한복(69행 뒤), jeju 렌터카, 공항 픽업 차량 | palaces, jeju, airport-to-seoul #taxi | 낮음~중간 | — | www.klook.com (원두 링크 생성 후) | 예 + 원두 |
| 결정 | **바깥 방문이 제휴 페이지에 닿는 길** — 지금 바깥 조회는 홈·가이드 목록·이름 도구·겨울 패딩에만. 이 페이지들에서 공항·필수 준비·eSIM으로 가는 연결을 어떻게 할지 | 홈, 가이드 목록, 이름 도구, 스레드 | 수익과 가장 직접(추론) | — | — | 원두 결정 |

## 2. 2단계 네트워크에 넣을 호스트 (중복 제거)
www.klook.com · wowpass.io · www.airportrailroad.com · www.airport.kr · yesim.app · support.apple.com · www.samsungsvc.co.kr · www.samsung.com(후보) · www.letskorail.com · www.korail.com(후보) · news.seoul.go.kr · www.koreaherald.com · www.ftc.go.kr · www.law.go.kr · www.caa.go.jp(후보) · commons.wikimedia.org · upload.wikimedia.org
- 통신사 3곳(SKT·KT·LG U+) 로밍·고객센터(abroad-esim 2·3번): **정확한 호스트를 지금 기록에서 못 찾음** → 2단계 첫 검색으로 확정 후 추가. 추측해서 적지 않음.
- **넣지 않는 것:** tpx.li(제휴 짧은 주소 — 자동으로 따라가면 클릭이 기록될 수 있음, 추론), www.kkday.com(이 환경에서 403, 봇 차단으로 보여 우회 안 함 — signup-list 64행), app.travelpayouts.com(로그인 필요, 원두 계정).

## 3. 2단계 시작 전 점검 (CLAUDE.md '작업 시작 전 점검' 7개)
1. 저장: 열어 본 원문은 wondu-archive staging/az-affiliate-<날짜>/에 원문 텍스트로 저장, 결과는 이 폴더에 단계마다 커밋.
2. 접근: 위 호스트를 첫 단계에서 curl로 하나씩 열어 보고 막힌 곳은 표로 남김(추정 안 함).
3. 범위: 4개 언어 모두 같은 행이라 ko·en을 먼저 고치고 ja·zh-tw는 같은 구조. ja의 "円からチャージ"(essentials 70행) 같은 언어별 문장은 따로 대조.
4. 검증: 페이지에 넣는 인용·수치는 저장한 원문과 글자 대조(기존 transit 도구 방식).
5. 한도·비용: 상품 페이지 약 6개 + 공식 페이지 약 10개 열람 예상(이 계획의 행 수 기준 추정). Klook 상품 페이지가 스크립트로만 내용을 그리면 본문을 못 읽을 수 있음 → 그때는 원두 화면으로.
6. 무인 실행: 없음. 페이지 수정은 원두 승인 뒤.
7. 막힐 규칙: 회사 화면(Klook·와우패스 앱·코레일+·iOS·One UI 설정)은 약관 확인 전 캡처를 쓰지 않음. 차단은 우회하지 않음. approved 페이지(essentials·departure-day·money·disclosure 등)는 고치면 원두 재승인.

## 4. 지금 하지 않는 것
- 사이트 파일 수정(이번 단계 범위 밖, 원두 지시).
- 승인 대기·거절 프로그램 자리 잡기(inventory.md 3절).
- 숫자(수수료·값) 추정 — 기록에 없는 것은 전부 "확인 필요".
