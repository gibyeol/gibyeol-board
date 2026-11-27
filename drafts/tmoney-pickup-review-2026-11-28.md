# 티머니 수령·사이트맵 독립 검토 (2026-11-28 KST)

- 검토자: 독립 검토(작성자 아님). 고치지 않고 판정만 함.
- 대상: 브랜치 claude/determined-euler-xsz86i, 커밋 02660e9(사이트맵 modified), db78d68(ko), c071c40(en·ja·zh-tw)
- 원 출처: /home/user/wondu-archive/raw-from-scratchpad/klook-tmoney-2026-11-28/167~172.png (6장 모두 Read로 확인). Klook 사이트·제휴 링크는 열지 않음.
- 실행: `python3 build.py` → 160쪽 생성. 이전 커밋 6874861을 별도 작업 폴더에 빌드해 sitemap.xml을 비교함.

## 결론
반드시 고칠 것: 없음(이번 3개 커밋 범위).
권고 4건, 범위 밖 확인 필요 1건(아래).

## A. 사실 대조 (화면 ↔ 글)

| 글의 내용 | 화면 근거 | 판정 |
|---|---|---|
| 1터미널 1층 7번 출구 쪽 서점(Book Store) 07:00~21:00 | 171.png "Incheon International Airport T1 · Location name: Book Store · 1st Floor, Exit 7 · Opening hours: 07:00–21:00" | 통과 ('쪽'은 화면에 없는 말이나 뜻 왜곡 아님) |
| 2터미널 3층 F 카운터, Travel Mate & Book Store 06:30~21:30 | 171.png "T2 · Travel Mate & Book Store · 3rd Floor, Counter F · 06:30–21:30" | 통과 |
| 두 상품 모두 같은 곳에서 받음(암시) | 171.png 머리 "T-MONEY CARD ONLY / KRW 10,000 TOP-UP" | 통과 |
| 상품 두 가지: 카드만 / 카드+1만 원 | 169.png "T-Money card only", "T-Money card + KRW 10,000 balance" | 통과 |
| 24시간 전까지 무료 취소 | 169.png "Free cancellation (24 hours notice)" | 통과 |
| 고른 날짜에만 받을 수 있음 | 169.png "Valid on the selected date" | 통과(태그를 '받는 날'로 읽은 해석. 무리 없음) |
| 6~12세·13~19세: 산 뒤 편의점 계산대에서 생년월일 등록, 여권 | 172.png "registering their birth date at the convenience store counter; present an ID or passport" | 통과('ID or passport'를 '여권'으로 좁힘. 외국인 독자 기준이라 문제 아님) |
| 0~5세 기차 빼고 교통비 없음(클룩 안내) | 172.png "Children (aged 0-5): Free of transportation charges (except on trains)" | 통과, 출처 표시 있음 |
| 충전 1,000~90,000원, 잔액 최대 50만 원 | 172.png "between KRW 1,000 and KRW 90,000 at a time; the maximum card balance is KRW 500,000" | 통과 |
| 충전 장소: 지하철역 충전기(인천공항역 포함), 티머니 표시 편의점 | 172.png Top-up locations 1·2 | 통과 |
| 확인서 결제 뒤 몇 분 안 | 172.png "You'll get confirmation within minutes." | 사실은 맞음. 다만 클룩 주장인데 '산 다음' 1번에 출처 표시 없이 단정(권고 2) |
| "2터미널은 3층. 입국장(1층)에서 올라가야" | '3층'은 171.png. '입국장 1층'은 같은 페이지 content/ko/airport-to-seoul.md:71·73(인천국제공항공사 안내도 기반 2터미널 그림·본문 "2터미널은 입국장(1층)에서…") | 통과(페이지 다른 곳 근거 있음) |
| 가격(US$ 3.75 / 11.25)·예시 날짜(Today/Tomorrow/30 Nov) | 169.png에만 있음 | 글에 안 들어감(grep 0건) — 통과 |
| 화면 확인일 "2026년 11월 28일" | 169.png 날짜 칩 "Today / Tomorrow / 30 Nov" → 오늘 = 28일과 맞음. 커밋 시각 17:2x UTC = 11/28 02:2x KST | 통과 |

과장·화면에 없는 단정: 위 '확인서 몇 분'(권고 2) 외 없음. 지우진 '클룩 사이트가 자동 접속을 막아…' 문장은 삭제됨(차단 우회 없이 운영자 화면으로 대체) — 적절.

## B. 원두 원칙

- 불확실한 정보 금지 [7eb4ec94#2954]·"근거를 들어서 예상한다고 해" [7eb4ec94#2931]: 표 머리에 출처(클룩 상품 페이지, 운영자 화면, 날짜) 있음 — 통과. 다만 표 아래 목록(상품·취소·어린이 등록·충전)도 전부 클룩 안내인데 출처 표시는 0~5세 줄에만 '(클룩 안내)'가 붙음(권고 1).
- 바우처 우선 문구("확인서에 다른 곳이 적혀 있으면 확인서를 따르세요") — 클룩 화면이 바뀔 가능성에 대한 대비로 적절.
- A to Z·따라 하기: 밤 도착 대안 링크 `#buy-tmoney` → 4개 언어 모두 3단계 h3(id="buy-tmoney")로 감. 3단계 1·2번에 지하 1층 편의점·발매기, 공항철도역 티머니 자판기(해외 신용카드)가 실제로 있음 — 통과. 다만 "늦으면 … 바로 사요"인데 지하 1층 편의점·자판기의 밤 운영 시간 근거는 페이지에 없음(권고 3).
- 길 찾기: 받는 곳의 층·출구/카운터는 화면대로 있음. 2터미널 1층→3층 이동 방법(엘리베이터·에스컬레이터 위치, 랜드마크)과 1터미널 '7번 출구'를 입국장에서 찾는 방향은 없음. 화면에 그 정보가 없으므로 지어내지 않은 것은 맞으나, 원두 길 찾기 기준 [7eb4ec94#1242]에는 약함(권고 4).
- 클룩 화면 172.png "Different accessibility is provided for locations, please refer to the locations website before the visit"는 반영 안 됨(권고 4에 포함).

## C. 4개 언어·빌드

- ko·ja·zh-tw·en 의 표·목록·'산 다음' 1번 뜻 같음. 숫자 기계 추출 비교: 06:30·07:00·21:00·21:30·1만(10,000)·24시간·6~12·13~19·0~5·1,000~90,000·50만(500,000)·7번·3층·F 모두 일치.
- zh-tw 표 2터미널은 "F櫃台的書店(Travel Mate & Book Store)"로 'Travel Mate'를 중국어 본문에서 뺐으나 괄호 원문에 있음 — 문제 아님.
- build 결과 dist/{ko,ja,zh-tw}/airport-to-seoul/index.html, dist/airport-to-seoul/index.html: `id="buy-tmoney"` 각 1개, `href="#buy-tmoney"` 각 1개, 표가 `<table>`로 정상 렌더(머리 3칸·2행), 목록 `<ul>`, '산 다음' `<ol class="steps">` 정상. 깨진 표 기호(`|---|`) 노출 0.

## D. 사이트맵

- 6874861 빌드와 비교: lastmod가 바뀐 URL은 정확히 12개(공항·할인판·이름 × ko·ja·zh-tw·en), 모두 2026-11-28. 나머지 148개 그대로 — 통과.
- 'modified' 값이 페이지 HTML에 노출되지 않음(dist에서 'modified' 글자는 기존 본문 출처 문구 "modified 2025-11-25", 사진 크레딧 "(modified: light auto-contrast)"뿐) — 통과.
- 화면 확인일(byline): 공항 en·ko 모두 이전과 같은 2026-11-26, 할인판 2026-11-24 — 바뀌지 않음, 통과. build.py는 byline에 `updated`만 씀(build.py:626~630).

## 반드시 고칠 것
없음.

## 권고
1. ko·ja·zh-tw·en '도착 전에 준비' 표 아래 목록 전체가 클룩 안내임을 표시(예: 목록 머리 "아래는 클룩 상품 페이지 안내"). 지금은 0~5세 줄에만 '(클룩 안내)'.
2. '산 다음' 1번 "예약 확인서는 결제 뒤 몇 분 안에 와요" → 클룩 안내로 표시하고 172.png의 "안 오면 클룩 고객센터" 문장을 같이(4번과 연결).
3. 밤 대안 "지하 1층 편의점·공항철도역 자판기에서 바로 사요": 밤 시간대 운영 근거가 페이지에 없음. 공식 운영 시간을 확인해 적거나, 확인 전이면 '운영 시간은 확인 못 함'으로.
4. 길 찾기: 2터미널 1층→3층, 1터미널 입국장에서 7번 출구 방향을 기존 터미널 그림·랜드마크로 잇기(근거 확보 시). 172.png "장소마다 접근성이 다름" 안내 반영 검토.

## 범위 밖 확인 필요 (이번 3개 커밋 아님)
- 할인판(deals) 4개 언어: front matter `approved: 2026-11-26`, `modified: 2026-11-28`. 0bc33de(11/28 data/deals.json 변경) 뒤에도 approved가 남아 화면이 "Nadri 에디터 승인"으로 나옴(dist/deals/index.html byline "approved by a Nadri editor"). drafts/BRIEF-access.md:57 "승인 뒤 고치면 approved: 줄을 지운다" 규칙과 어긋날 수 있음. 원두가 11/28 변경본을 승인했는지 원두 원문으로 확인 필요. build.py:629는 approved >= updated만 보므로 modified를 보지 않음.
