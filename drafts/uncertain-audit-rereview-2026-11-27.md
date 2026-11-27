# 불확실 정보 수정 재검토 (2026-11-27) — 커밋 8b5057b, 797c52d

- 검토자: 독립 검토(이 수정의 작성자 아님, Claude 하위 작업). content/·static/·build.py는 고치지 않았어요.
- 대상: 브랜치 `claude/determined-euler-xsz86i`의 8b5057b(58개 파일), 797c52d(about 4개). 수정 목록은 drafts/uncertain-audit-review-2026-11-27.md '## 반영' 절.
- 기준 원문(요약 안 함):
  - [7eb4ec94#2954] "1. 불확실한 정보를 올리면 안돼는건 모든 곳에 적용이야. … 3. 모든 판단근거는 실제로 쓸 수있는 사용자에게 맞는 정보전달이 되느냐야. 외국인도 쓸 수있는 거면 외국인에게도 보여도 되는거고."
  - [7eb4ec94#2990] "3. 이것도 다시 말하지만 확실하지 않은 정보는 예상과 근거의 출처가 있다면 출처를 남기고 예상이라고 쓰고, 아니면 다뺴."
  - [7eb4ec94#3295] "(가)로하고나서 이번건은 일단 그냥 다 공개하자 추후에 내가 페이지 전수조사해서 수정해야할 부분들 말해줄게. 틀린정보만 없으면돼" (이번 공개 기준)
- 방법: `git show 8b5057b`·`797c52d`를 ko·en·ja·zh-tw word-diff로 줄마다 대조, 각 쪽 출처 목록·같은 쪽 다른 문장·drafts/* 저장본과 글자 대조, 웹 원문은 각 한 번만 시도(우회 없음), 사본에서 빌드.
- 판정 표시: **확실**(원문·파일에서 글자로 확인) / **경향**(근거 있음, 원문 전체는 못 봄) / **추론**(근거 없이 판단).

## 숫자 요약

| 항목 | 건수 |
|---|---|
| 검토 항목 | 26건(O1·A2, U1~U10, U12~U18, U4, A1, 궁궐, W1~W3, A3, A4, 797c52d about). U11은 원두 결정 대기라 대상 아님 |
| 통과 | 25건 |
| 틀린 정보 | 1건(W2 about 괄호 문장 — 고치면서 생긴 것, 아래 '새 오류'와 같은 건) |
| 확실처럼 쓴 불확실 | 고친 문장 안에서는 0건. 고친 문장 밖에 같은 유형이 남은 곳 3건(아래 '나머지', 권장) |
| 새 오류(고치면서 생김) | 1건(W2, 위와 같은 건). 문법·링크·표 깨짐 0건 |
| 4개 언어 불일치(고친 문장) | 숫자·날짜·조건 불일치 0건. 고친 문장 밖 en 전용 차이 2건(나머지 R2·R3) |
| 빌드 | 사본에서 `python3 build.py` → "built 156 pages", 종료 코드 0. `node --check static/name-i18n.js` 통과, SVG 4개 XML 파싱 통과 |

## 반드시 고칠 것

### M1. 소개 쪽 "안내 글이 아닌 페이지에는 없어요" — 같은 소개 쪽 위에 그 표시가 있음 (틀린 정보, 새 오류)

- 위치: content/ko/about.md:14, content/en/about.md:14, content/ja/about.md:14, content/zh-tw/about.md:14 (W2 수정)
- 지금 글(ko): "각 안내 페이지 위에는 … 표시해요(홈, 이름 도구, 쇼핑 모음, 저작권 안내처럼 안내 글이 아닌 페이지에는 없어요)."
- 지금 글(en): "Each guide page shows, at the top, … (pages that are not guides, such as the home page, the name tool, the shopping hub and the copyright page, do not)."
  - 한국어 뜻: 각 가이드 페이지 위에 표시해요(홈, 이름 도구, 쇼핑 모음, 저작권 페이지처럼 가이드가 아닌 페이지는 표시하지 않아요).
- 왜 틀렸나(**확실**): 사본 빌드 결과에서 byline(확인 날짜·승인 표시)이 없는 쪽은 홈·name·reuse·shopping 4종(×4개 언어 = 16쪽)뿐이에요. 가이드가 아닌 쪽 중 **about(이 문장이 있는 바로 그 쪽), privacy, disclosure, updates, deals에는 byline이 있어요**(dist/ko/about/index.html "AI로 조사하고 2026-11-25 공식 정보로 확인했어요. 아직 Nadri 에디터 검토 전이에요.", dist/about/index.html, dist/ko/privacy, dist/ko/disclosure, dist/ko/updates, dist/ko/deals 확인). 괄호가 "가이드가 아닌 페이지에는 없다"로 일반화해서, 읽는 사람이 그 문장 바로 위에서 반례를 봐요. 네 예시(홈·이름 도구·쇼핑 모음·저작권) 자체는 맞아요(build.py:613 `home`·`byline: no` 제외 조건과 일치).
- 고칠 글 제안(일반화를 빼고 실제 4종만):
  - ko: "…표시해요(홈, 이름 도구, 쇼핑 모음, 저작권 안내 페이지에는 이 표시가 없어요)."
  - en: "… (the home page, the name tool, the shopping hub and the copyright page do not show it)."
    - 한국어 뜻: (홈, 이름 도구, 쇼핑 모음, 저작권 페이지에는 이 표시가 없어요.)
  - ja: "…(ホーム、名前ツール、ショッピングのまとめ、著作権のページにはこの表示はありません)。"
    - 한국어 뜻: (홈, 이름 도구, 쇼핑 모음, 저작권 페이지에는 이 표시가 없어요.)
  - zh-tw: "…(首頁、名字工具、購物總覽、著作權說明頁沒有這項標示)。"
    - 한국어 뜻: (홈, 이름 도구, 쇼핑 모음, 저작권 안내 페이지에는 이 표시가 없어요.)
  - 같은 문장의 "각 안내 페이지 위에는"(en "Each guide page")은 그대로 둬도 틀리지 않아요(가이드 쪽은 모두 byline 있음).

반드시 고칠 것은 이 1건뿐이에요.

## 나머지 — 항목별 판정

| # | 위치(고친 뒤) | 판정 | 근거 |
|---|---|---|---|
| O1·A2 | content/{ko}/getting-around.md:82, {en,ja,zh-tw}:80, content/*/seoul-subway.md:151(표), :206~207 | 통과 | **확실**: 코리아헤럴드 2025-05-22 기사(seoul-subway 출처 목록의 koreaherald.com/article/10493311)를 이번에 열어 읽음 — 제목 "Seoul subways to begin and end operation 30 minutes earlier", 본문 "Lines No. 1 through No. 8 will commence operation at 5 a.m. instead of the current 5:30 a.m. from August, and the final trains of the day will also run correspondingly earlier", "initially apply only to subway sections within Seoul". 쪽 문장의 1~8호선·30분·8월·첫차와 막차 모두 기사 범위 안. '시행 미확인'·'예상'과 출처가 붙어 [#2990] 형식에 맞음. 2022년 문장은 "참고"/"2025년 발표 전 기준"으로 시점이 밝혀져 지금 사실처럼 읽히지 않음. 코레일 구간 예외 문장(seoul-subway:208)도 기사 "within Seoul"과 맞음. 약한 점(틀림 아님): 기사는 "from August"라 썼고 쪽은 "이르면 2025년 8월"(더 조심스러운 표현). 기사상 발표일은 수요일(2025-05-21)이고 쪽 괄호의 5월 27일은 서울시 영문 누리집 게시일 — 출처 표기로 읽혀 틀림 아님. 서울시 영문 원문은 못 엶(아래). 4개 언어 숫자·조건 같음. |
| U1 | content/*/essentials.md:55, :63 | 통과 | **확실**: 한국 번호 제공을 단정하지 않고 "사기 전에 상품 페이지에서 확인"으로 바뀜. data/affiliates.json의 klook_esim_alt label("SKT eSIM with calls and texts, up to 90 days")은 화면에 나오지 않음(빌드 결과 dist 전체에서 0건, 버튼 글자는 페이지가 준 "More SKT eSIM plans on Klook"). 4개 언어 같음. |
| U2 | content/zh-tw/ktx-busan.md:38 | 통과 | **확실**: 「也有中文介面」 삭제, 4개 언어 모두 '148개 역, 해외 신용카드 발권기'만 남음. |
| U3 | content/*/ktx-busan.md:10 | 통과 | **확실**: :45와 같은 수치(2시간 17분, 2시간 35~41분)·같은 근거(2024년 보도, 이데일리 2024-04-22)·'예상'. 이데일리 원문은 못 엶. |
| U4 | static/name-i18n.js popularNote(17개 언어) | 통과 | **확실**: 17개 언어 모두 둘째 문장만 빠지고 첫 문장(출생 통계 순위·최근 연도·Behind the Name)은 온전함(커밋 전후 문자열 추출 대조). 같은 주장("No country publishes" 등)이 content·static·data에 남은 곳 0건. |
| A1 | content/{ko,en,zh-tw}/winter.md:55, ja:49 | 통과 | **확실**: "위 기온표는 12~2월 평년값"은 같은 쪽 표(기상청 1991~2020 평년값, 12·1·2월)와 맞음. 링크 https://www.weather.go.kr 4개 언어 모두 빌드에서 정상 링크로 나옴. 약한 점: 링크 대상은 한국어 누리집이라 외국어 독자에게는 '휴대폰 날씨 앱' 쪽이 실제 행동이 될 것(추론). weather.go.kr은 이번에 열지 않음(앞 작업에서 403 기록). |
| 궁궐 | content/*/palaces.md:60 | 통과 | **확실**: 덧붙인 문장의 '10월 8일 보도로 미정'은 같은 쪽 :58과 같음. 4개 언어 같음. 문체 약점(틀림 아님): en은 "We could not confirm whether … We could not confirm it on the official site"로 이어져 둘째 문장의 "it"이 관람료 개편을 가리키는 것처럼 읽힐 수 있음 → "We could not confirm free Wednesdays on the official site"가 더 분명. |
| W1 | content/{ko,en,ja}/seoul-areas.md:51, zh-tw:64 | 통과(약함) | **경향**: 근거는 서울시의 2026년 핼러윈 하룻밤 추산(출처 목록 코리아타임스 2026-10-31) 하나. "핼러윈 같은 날"로 다른 날까지 넓힌 건 약간의 일반화지만 '평소 밤'을 단정하던 이전 판보다 범위가 좁아졌고 틀렸다고 볼 근거는 없음. 절 제목 "젊고 밤이 긴 곳"은 그대로(작성자도 약함으로 적음). |
| W2 | content/*/about.md:14 | **불합격** | 위 M1. |
| W3 | content/*/jeju.md:61 | 통과 | **확실**: 제주 11.2°C, 서귀포 13.6°C는 같은 쪽 :67과 같고, 출처 목록 "기상청, 2025년 겨울철 기후특성(2026년 3월 4일)"과 시기(2025년 12월~2026년 2월)가 맞음. 기상청 원문은 못 봄. |
| A3 | content/*/jeju.md:63 | 통과 | **확실**: "600번이 서귀포까지 가는지는 2020년 자료뿐"은 같은 쪽 :41(제주지방항공청, 에어포탈 2020년 7월 기준)과 맞음. 장점 칸에서 '공항 리무진' 삭제, 4개 언어 같음. |
| A4 | static/fig/*/shopping-streets-1.svg | 통과 | **확실**: 명동 줄 시계 아이콘(circle·path)과 "—" 글자 삭제, 4개 파일 XML 파싱 통과. |
| U5 | content/*/index.md:22 | 통과 | **확실**: "숙소 많은 지역까지 바로"는 airport-to-seoul.md:45(4개 언어)와 같은 범위. |
| U6 | content/*/index.md:26 | 통과 | 판단 표시("저희 판단은 eSIM"). |
| U7 | content/*/essentials.md:22, :90 | 통과 | **경향**: "해외 카드가 안 되는 곳도/이 있어요"는 약한 주장이고 money.md:13과 같음. "티머니 충전은 현금"은 seoul-subway.md:13·:33("티머니 충전은 현금만")과 같음. |
| U8 | content/*/essentials.md:119, ko getting-around.md:52, en·ja·zh-tw:50 | 통과 | '오프라인 작동' 삭제. 사이트 전체에서 Subway Korea 오프라인 주장 0건(grep). |
| U9 | content/ko/seoul-subway.md:153 | 통과 | 일반화 삭제. |
| U10 | content/ko/getting-around.md:42, en·ja·zh-tw:40 | 통과 | '유일/뿐' 최상급 삭제, 4개 언어 같은 뜻. |
| U12 | content/*/winter.md:43, :46(ja :37, :40) | 통과 | 판단 표시, 체감 서술 삭제. :10 난방 장면은 U11과 함께 원두 결정 대기. |
| U13 | content/*/winter.md:31 | 통과 | 2026년 1월 −20°C 문장 4개 언어 모두 삭제(grep 0건). YTN 2025-12-26 수치는 그대로. |
| U14 | content/{ko,en,ja}/seoul-areas.md:48, zh-tw:61 | 통과 | 최상급 삭제. |
| U15 | content/{ko,en,zh-tw}/money.md:4, :13, ja:4 | 통과 | lede "이 세 가지면 헤맬 일 거의 없음" 삭제, 표 "곳이 많아요"→"곳이 있어요". ja 표는 원래 "使えないことがあります"(쓸 수 없을 때가 있어요). |
| U16 | content/ko/everyday.md:10, :42, en·ja·zh-tw:10, :40 | 통과 | "곳이 많아요"→"곳도 있어요". |
| U17 | content/*/airport-to-seoul.md:17, :179 | 통과 | **확실**: "직통열차는 서울역까지만 감"은 같은 쪽 "서울역까지 안 서고"와 공항철도 직통열차 출처 범위. 판단 표시 붙음. |
| U18 | content/*/airport-to-seoul.md:162 | 통과 | **확실**: 같은 쪽 :56 "Visit Seoul은 … 1~2시간을 잡으라고", 출처 목록 "Visit Seoul Airport to Seoul(2026년 6월 기준)"과 같은 권고 표현. |
| 797c52d | content/*/about.md(다른 여행지 문장) | 통과 | '여행지마다 전담 에디터' 삭제, "정해지면 알려 드릴게요". 4개 언어 같은 뜻. |

### 고친 문장 밖에 남은 같은 유형(권장, 틀렸다는 근거는 없음)

| # | 위치 | 지금 글 | 왜 남기면 약한가 | 제안 |
|---|---|---|---|---|
| R1 | content/ko/everyday.md:45, content/{en,ja,zh-tw}/everyday.md:43 | ko "**카드**는 거의 어디서나 돼요." / en "Cards are accepted almost everywhere" / ja 「カードはほぼどこでも使えます」 / zh-tw 「信用卡幾乎到處能刷」 | 같은 쪽의 물 문장(U16)과 essentials(U7)·money(U15)에서 '거의 어디서나'를 지웠는데 이 줄만 남음(같은 유형 빈도 주장, 쪽 출처에 수용률 근거 없음 — **경향**, 출처 목록 확인). 틀렸다는 근거는 없음. | ko "카드를 먼저 내 보세요. 해외 카드가 안 되는 곳도 있어요." 4개 언어 같은 뜻으로. |
| R2 | content/en/ktx-busan.md:45 | "most take roughly 2 hours 35 to 41 minutes" (한국어 뜻: 대부분은 2시간 35~41분쯤 걸려요) | ko·ja·zh-tw :45는 '일반적인 KTX'(일반·ふつう·一般)인데 en만 'most(대부분)'. U3에서 :10의 '대부분'을 지운 것과 같은 유형. | "typical ones take roughly 2 hours 35 to 41 minutes" (한국어 뜻: 일반적인 열차는 2시간 35~41분쯤) |
| R3 | content/en/ktx-busan.md:38 | "Korail has new ticket machines at 148 stations that take overseas credit cards." (한국어 뜻: 코레일은 148개 역에 해외 신용카드를 받는 새 발권기가 있어요) | ko·ja·zh-tw는 "2025년 말 기준/報道" 시점이 붙었는데 en만 지금 사실처럼 씀. | "As of late 2025, Korail had new ticket machines at 148 stations that take overseas credit cards." (한국어 뜻: 2025년 말 기준 148개 역에 …) |

참고(이번 범위 밖, 손대지 않음): content/*/convenience-store.md:87 "카드: 거의 어디서나"는 MUFG 안내가 '편의점에서 카드 사용 가능'이라고 한 것보다 넓게 읽힐 수 있어요(**추론**, 원문 미확인).

## 4개 언어 대조

- 고친 문장의 숫자·날짜·조건(30분, 1~8호선, 2025년 5월, 8월, 2022년, 2시간 17분, 2시간 35~41분, 11.2°C·13.6°C, 600번·2020년, 12~2월 평년값, 10월 8일 '미정', 1~2시간, 148개 역)은 ko·en·ja·zh-tw 모두 같아요(word-diff 대조, **확실**).
- 문장 형태 차이(뜻 같음): en palaces "it" 지시 모호(위 궁궐 칸), zh-tw seoul-areas 줄 번호가 다른 것은 쪽 구성 차이.

## 빌드·형식

- 사본: /tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/rereview-site (git archive HEAD) → `python3 build.py` → "built 156 pages", 종료 코드 0.
- 표: seoul-subway(:151), essentials(:22, :119), jeju(:61, :63) 표가 빌드에서 `<td>`로 정상 출력(셀 내용 확인).
- 링크: winter 날씨누리 링크 4개 언어 정상.
- byline 없는 쪽 목록(dist 전수): 홈·name·reuse·shopping ×4개 언어 = 16쪽 — M1의 근거.

## 못 연 출처(각 한 번만 시도, 우회 없음)

- 서울시 영문 누리집 "autonomous-bus-and-earlier-subway-service-for-early-morning-commuters"(2025-05-27): 연결 실패(curl 000). → O1은 코리아헤럴드 원문으로 판정.
- 이데일리 서울-부산 소요 시간(2024-04-22, marketin.edaily.co.kr): 프록시 403. → U3은 같은 쪽 :45와의 일치만 확인.
- 기상청(날씨누리, 2025년 겨울철 기후특성), 세계일보(2026-05-27), 연합뉴스(10월 8일): 이번에 열지 않음. 판정은 쪽 안 문장·출처 목록 일치까지만이에요.
- 연 것: 코리아헤럴드 2025-05-22 (HTTP 200, 위 O1 인용).

## 판정자

독립 검토(이 수정의 작성자 아님, Claude 하위 작업). 원두에게 보이기 전 M1 1건을 고치고, R1~R3은 원두 [7eb4ec94#3295] 기준(틀린 정보만 없으면 됨)으로는 공개를 막는 항목이 아니라 권장이에요.
