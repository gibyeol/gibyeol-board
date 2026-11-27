# ktx-busan 4개 언어 + Klook 제휴 2개 — 독립 검토 (2026-11-27)

검토자: 독립 검토(이 수정을 쓰지 않음). 읽기만 함, 대상 파일은 고치지 않음.
대상: 브랜치 claude/determined-euler-xsz86i — 70158db(content/{ko,en,ja,zh-tw}/ktx-busan.md), bbac05b(data/affiliates.json klook_korailpass), f2739ad(klook_ktx 버튼 en·ja·zh-tw, ko 주석 삭제).
원두 기준: [7eb4ec94#3526] "(나)로 진행해" / [7eb4ec94#3295] "틀린정보만 없으면돼" / [7eb4ec94#2990] "확실하지 않은 정보는 예상과 근거의 출처가 있다면 출처를 남기고 예상이라고 쓰고, 아니면 다뺴." / [7eb4ec94#2954] "3. 모든 판단근거는 실제로 쓸 수있는 사용자에게 맞는 정보전달이 되느냐야. …"

## 숫자 요약
- 판정 항목 21개: 통과 18 / 반드시 고칠 것 3 (그 밖에 권장 2: 그림, 입석)
- 빌드: 160쪽, 에러 0, ktx-busan 4쪽 h2 앵커 id가 main과 같음, 4쪽 내부 링크 깨짐 0, 남은 `{{ }}` 0
- 웹 확인: korail.com·letskorail.com 은 이 환경에서 연결 끊김(1회 시도, 우회 안 함) → 작성자 작업 폴더의 받아 둔 원문 HTML로 판정. klook.com/transport/?target_product_id=6(제휴 아닌 원래 주소)은 열림. tpx.li 제휴 링크는 열지 않음.

## 반드시 고칠 것

### 1. ja·zh-tw의 외국인 웹페이지 링크 — 근거 없음 (en·ko 링크와 letskorail 이동은 근거 있음, 단 보관소에 없음)
- 위치: ja 37줄 `https://www.korail.com/global/jpn/main`, zh-tw 37줄 `https://www.korail.com/global/tw/main`.
- 이유:
  - en·ko 37/36줄 `https://www.korail.com/global/eng/main`은 한국관광공사 원문 HTML(작성자 작업 폴더 /tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/ktx/vk_227786.html, 2025-05-30)에 "Korail Website: <a href='https://www.korail.com/global/eng/main'>"로 실려 있다 → 근거 있음.
  - letskorail.com → korail.com: 같은 폴더 lk_home.html이 letskorail 접속 결과로 korail.com 페이지(og:url "www.korail.com", 제목 "코레일 승차권예매")를 받았다 → 근거 있음.
  - 그러나 jpn·tw 주소는 어떤 원문에도 없다(grep 0건). 같은 폴더의 g_eng_pass.html과 lk_home.html은 바이트까지 같은 빈 껍데기(SPA) 화면이라, 주소를 열었을 때 화면이 떴다는 것만으로는 그 언어 화면이 있다는 근거가 되지 않는다. 또 한국관광공사 vk_198570.txt(2026년 8월 갱신)는 웹 언어를 "Korean, English, Japanese, Simplified Chinese, Vietnamese, Thai, Indonesian"으로 적어 중국어는 간체만이다 — zh-tw '中文畫面'이 번체 화면처럼 읽힐 수 있다. 이 환경에서 korail.com은 연결이 끊겨(1회) 독립 확인도 못 했다. 원두 [7eb4ec94#2990] 기준 확인 안 된 주소는 올리지 않는다.
  - 위 두 근거 파일(vk_227786.html, lk_home.html)은 세션 작업 폴더에만 있고 wondu-archive/raw-from-scratchpad/ktx-2026-11-27/ 에는 없다(.txt 사본에는 주소가 빠짐). 보관소에 넣어야 근거가 남는다.
- 고칠 글(근거 있는 영어 화면 주소로 바꿈):
  - ja 37: "KORAILの外国人向けウェブページ([英語画面](https://www.korail.com/global/eng/main))は英語・中国語・日本語・タイ語・ベトナム語など7言語で、…"(뒤는 2번 날짜 반영)
    (뜻: 코레일 외국인용 웹페이지(영어 화면 링크)는 …)
  - zh-tw 37: "Korail外國旅客網頁([英文畫面](https://www.korail.com/global/eng/main))支援英文、中文、日文、泰文、越南文等7種語言,…"(뒤는 2번 날짜 반영)
    (뜻: Korail 외국인용 웹페이지(영어 화면 링크)는 …)
  - 또는 작성자가 jpn·tw 주소에 실제 일본어·중국어(번체/간체) 화면이 뜨는 캡처를 보관소에 저장하면 그대로 둘 수 있다(zh-tw는 간체면 '中文(簡體)畫面'으로).
  - vk_227786.html과 lk_home.html을 wondu-archive/raw-from-scratchpad/ktx-2026-11-27/ 에 복사(이건 작성자 일).

### 2. "7개 언어" 현재형 — 날짜 빠짐
- 위치: ko 36, en 37, ja 37, zh-tw 37.
- 근거 원문 molit_260921.txt(2026년 9월 20일): "현재 영어·중국어·일본어·태국어·베트남어 등 7개 언어를 지원하고 있는 외국인 대상 웹페이지에 프랑스어·독일어·몽골어를 추가해 연말까지 총 10개 언어로 서비스를 확대할 계획이다." 글자는 맞지만 '현재'는 9월 기준이다. 11월 27일 글에 날짜 없이 "7개 언어이고"라고 쓰면, 이미 언어가 늘었을 경우 틀린 정보가 된다.
- 고칠 글(링크는 1번 반영 뒤 그대로 둠):
  - ko 36: "코레일 외국인용 웹페이지([영어 화면](https://www.korail.com/global/eng/main))는 2026년 9월 국토교통부 발표 기준 영어·중국어·일본어·태국어·베트남어 등 7개 언어이고, 연말까지 프랑스어·독일어·몽골어를 더할 계획이에요."
  - en 37: "Korail's website for visitors ([English](https://www.korail.com/global/eng/main)) ran in seven languages, including English, Chinese, Japanese, Thai and Vietnamese, as of the transport ministry's September 2026 announcement, with French, German and Mongolian planned by the end of 2026."
    (뜻: 2026년 9월 국토부 발표 기준 7개 언어였고, 2026년 말까지 3개 추가 계획)
  - ja 37: "…は、2026年9月の国土交通部の発表時点で英語・中国語・日本語・タイ語・ベトナム語など7言語で、年末までにフランス語・ドイツ語・モンゴル語を加える計画です。"
    (뜻: 2026년 9월 국토부 발표 시점 7개 언어, 연말까지 3개 추가 계획)
  - zh-tw 37: "…依韓國國土交通部2026年9月的公告支援英文、中文、日文、泰文、越南文等7種語言,預計年底前再加法文、德文、蒙古文。"
    (뜻: 2026년 9월 국토부 공고 기준 7개 언어, 연말 전 3개 추가 예정)

### 3. SRT 제외 문장 — 날짜 빠짐, 같은 쪽 68·69줄과 어긋남
- 위치: ko 102, en 103, ja 103, zh-tw 103.
- 지금 글(ko 102): "…한국관광공사 안내로는 SRT·지하철·임시 관광열차는 안 되고 좌석 지정은 하루 두 번까지예요. 공식 안내를 따르세요."
- 이유: 근거 vk_rail.txt "更新日期 : 2026.08.07"(2026년 8월 7일 갱신), "(SRT、地铁及临时旅游列车除外)"(SRT·지하철·임시 관광열차 제외). 같은 쪽 ko 68줄은 "2026년 8월 기준 … 통합 뒤에 바뀌었는지는 확인하지 못했어요"라고 했는데, 102줄은 날짜 없이 지금도 그런 것처럼 단정한다. 9월 통합 뒤 바뀌었는지 모르는 내용이다.
- 고칠 글:
  - ko: "클룩 화면에는 'KTX를 포함한 모든 열차 무제한'이라고 돼 있지만, 한국관광공사 안내(2026년 8월 갱신)로는 SRT·지하철·임시 관광열차는 안 되고 좌석 지정은 하루 두 번까지예요. 공식 안내를 따르세요."
  - en: "Klook's page says \"unlimited access to all trains, including the high-speed KTX\". The Korea Tourism Organization's guide (updated August 2026) says SRT, the subway and temporary tourist trains are excluded and seat reservations are limited to two a day. Go by the official rules."
    (뜻: 한국관광공사 안내(2026년 8월 갱신)로는 SRT·지하철·임시 관광열차 제외, 좌석 지정 하루 2번)
  - ja: "Klookの画面には「KTXを含むすべての列車が乗り放題」とありますが、韓国観光公社の案内(2026年8月更新)では、SRT・地下鉄・臨時の観光列車には使えず、座席指定は1日2回までです。公式の案内に従ってください。"
    (뜻: 한국관광공사 안내(2026년 8월 갱신)로는 …)
  - zh-tw: "Klook頁面寫著「包含KTX在內所有列車無限次搭乘」,但韓國觀光公社的說明(2026年8月更新)是SRT、地鐵和臨時觀光列車不能用,而且每天最多劃位2次。請以官方說明為準。"
    (뜻: 한국관광공사 설명(2026년 8월 갱신)으로는 …)

## 권장(공개를 막지는 않음)
- 그림 ktx-busan-1(static/fig/{ko,en,ja,zh-tw}/ktx-busan-1.svg) '어디서 사나'에 아직 "letskorail.com"이 있다. 넘어가니 틀린 건 아니지만 본문("코레일 외국인용 웹페이지")과 이름을 맞추는 것이 좋다.
- (선택) 2×N 문장 뒤에 "입석은 횟수 제한 없음"을 더할 수 있다. 근거 vk_rail.txt "每日最多可指定两次座位，站票不受限制"(하루 최대 2번 좌석 지정, 입석은 제한 없음).

## 통과 항목(근거)
| # | 사실 | 판정 | 근거 원문 |
|---|---|---|---|
| 1 | 2개월 전 예매, 외국인도 같음, 항공권 살 때 함께 예매하려는 목적 | 통과 | molit_260921.txt "내·외국인의 … 10월 1일부터 … 2개월 전으로 확대", "항공권을 구매하는 시점에 철도 승차권도 함께 예매" |
| 2 | 10개 언어 계획(프랑스·독일·몽골어, 연말) | 통과(날짜는 고칠 것 2) | molit_260921.txt |
| 3 | 해외 카드 비자·마스터·유니온페이 | 통과 | molit_260921.txt "비자·마스터·유니온페이 등 해외 신용카드 중심으로 제공". 원문은 앱/웹 구분을 하지 않음 — 글도 구분하지 않아 틀린 곳은 없음 |
| 4 | '나의 티켓' 4개 언어 이름 | 통과 | app_ios_kr "■ 나의 티켓" / app_ios "■ My Ticket" / app_ios_jp "■ マイチケット" / app_ios_tw "■ 我的票券" |
| 5 | '여행 서비스 예약'에서 패스 | 통과 | kr "■ 여행 서비스 예약 … 여행패스" / en "■ Travel Service Reservation … KORAIL Passes" / jp "■ 旅行サービスの予約 … Korail Pass" / tw "■ 預約旅行服務" |
| 6 | 승차권 사진 저장 | 통과 | kr "사진 : 승차권 저장 및 공유" (4개 언어 같은 줄) |
| 7 | 앱 지원 언어 7개 | 통과 | app_ios_kr 240줄 "한국어, 베트남어, 영어, 일본어, 중국어(간체), 중국어(번체), 태국어" |
| 8 | 서울역 AI 통역 창구·2025년 4월 Apple Pay | 통과 | vk_227786.txt(05/30/2025) "dedicated ticket counters equipped with real-time interpretation services powered by AI. Since April, Apple Pay has also been accepted". 글에 '2025년 5월 안내'가 붙어 있음 |
| 9 | 코레일패스 구매처 웹사이트·역 | 통과 | vk_1563646.txt "can be purchased through the KORAIL website or at train stations" |
| 10 | 하루 2번 좌석 지정, 제외 열차 문구 | 통과(날짜는 고칠 것 3) | vk_rail.txt |
| 11 | 54,400원 × 횟수 표 | 통과 | 108,800 / 163,200 / 217,600 / 272,000 / 326,400 계산 맞음, 4개 언어 같음, '우리 계산' 표시 있음 |
| 12 | 최대 2×N 지정석 | 통과 | 하루 2번 지정에서 나온 계산, '우리 계산' 표시, '지정석'으로 한정 |
| 13 | Klook 패스 사용 3단계 | 통과 | korailpass-124.png "How to use Korail Pass" 3줄과 같음 |
| 14 | Klook 조건(한국 여권 불가, 13세+, 0~5세 1명, 여권당 1장, 몇 분 안 확정) | 통과 | korailpass-125.png |
| 15 | Klook 'unlimited' 인용, 버튼 "(2–5 days)" | 통과 | korailpass-123.png "unlimited access to all trains, including the high-speed KTX", "2, 3, 4 or 5 flexible days" |
| 16 | en·ko 링크 /global/eng/main | 통과(보관소 사본 필요) | scratchpad/ktx/vk_227786.html 한국관광공사 'Korail Website' 링크 |
| 17 | letskorail.com → korail.com | 통과(보관소 사본 필요) | scratchpad/ktx/lk_home.html og:url www.korail.com |
| 18 | klook_ktx 버튼 "구간·날짜 고르기" | 통과 | klook.com/transport/?target_product_id=6 화면 글: "From / To / Departure date / Search", "Enter your departure and arrival points, and select dates". 그 화면의 "Book 3 months in advance"는 쪽 어디에도 쓰이지 않음(4개 파일 grep: '3개월/three months'는 부산 버스 시범 '석 달'뿐) |

## 제휴·표시
- 버튼: en·ja·zh-tw만 2개(klook_ktx 55줄 '어디서 사나' 목록 바로 아래, klook_korailpass 93줄 '어디서 사나요' 바로 아래). ko는 0개, 주석도 삭제됨(빌드 결과 'aff' 0).
- 버튼 글: 상품 이름·기간·화면에서 하는 일(구간·날짜)뿐, 할인·최저가 같은 말 없음 → 사실만.
- disclosure: yes — en·ja·zh-tw 본문 맨 위에 광고 표시 문단 1개, 버튼 옆 '광고 링크' 표시, `NADRI_DEFER`에 Travelpayouts·Skimlinks 두 스크립트(동의 뒤 로드). ko는 disclosure 없음, `NADRI_DEFER=[]` — 제휴 링크가 없으니 맞음.
- ko 92줄 "코레일패스는 외국 여권 소지자용이에요(한국 여권 불가)." — Klook 화면 "not available for Korean passport holders", vk_rail "外国人专用"과 맞음. 원두 [7eb4ec94#2954](쓸 수 있는 사람 기준)에 맞게 ko에는 버튼을 두지 않음.
- affiliates.json: klook_korailpass(https://klook.tpx.li/kMxVKo8D), klook_ktx(https://klook.tpx.li/ry4uqBR8) — 원두가 만든 링크라는 것은 커밋 설명 기준, 링크 자체는 열지 않음.

## 빌드
- /tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/rv4build: `git archive origin/main` + 4개 파일 + data/affiliates.json(f2739ad 기준) → `python3 build.py` "built 160 pages", 에러 0.
- main 그대로 빌드한 것과 비교: 바뀐 파일은 ktx-busan 4쪽, guides 목록 4쪽(description), sitemap.xml뿐.
- h2 id: 4개 언어 모두 main과 같음(바꾼 제목 3개는 `<h2 id="…">`로 옛 id 유지). 다른 쪽에서 ktx-busan#… 로 들어오는 링크 0건.
- ktx-busan 4쪽 내부 링크·앵커 깨짐 0.
