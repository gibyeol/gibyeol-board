# 사이트 전체 불확실 정보 점검 (2026-11-27)

원두 기준 원문:
- [7eb4ec94#2954] "1. 불확실한 정보를 올리면 안돼는건 모든 곳에 적용이야. … 3. 모든 판단근거는 실제로 쓸 수있는 사용자에게 맞는 정보전달이 되느냐야. 외국인도 쓸 수있는 거면 외국인에게도 보여도 되는거고."
- [7eb4ec94#2990] "3. 이것도 다시 말하지만 확실하지 않은 정보는 예상과 근거의 출처가 있다면 출처를 남기고 예상이라고 쓰고, 아니면 다뺴."
- 함께 적용: [7eb4ec94#1176] "지어낸 경험담이 아니에요" 같은 문구 삭제.

## 범위와 방법 (먼저 읽을 것)

- 대상: origin/main의 `content/{ko,en,ja,zh-tw}/*.md` 39쪽 × 4개 언어 전부(build.py는 front matter의 status를 보지 않고 content 폴더의 모든 쪽을 게시함 — 확인: build.py에 status 필터 없음). `data/site.json`(UI 문구), `data/trending.json`, `data/affiliates.json`(버튼 라벨), 쪽 안 그림(SVG 글자) 일부. `data/deals.json`은 제외(다른 작업 진행 중).
- 브랜치 `claude/determined-euler-xsz86i`에만 있는 5쪽(abroad-esim, airport-to-seoul, disclosure, essentials, seoul-subway)은 브랜치 판을 기준으로 봤어요(이미 고친 판이라서).
- 작업 중 origin/main이 바뀜: 62d862c(올리브영 12월 세일 '예상' 표기, winter-light-puffer 헤드리스로 읽은 사실 삭제, 홈 머리기사 자동 생성)·1c1c2ab. 이 두 쪽은 바뀐 판을 기준으로 다시 봤어요.
- 분류
  - **확실**: 쪽의 출처 목록에 그 사실을 담은 출처가 있음. 단, 이번에 원문을 다시 연 것은 일부뿐이에요(아래 '검증 한계').
  - **예상 가능**: 근거 출처는 있지만 지금 상태를 확인 못 함 → 근거·출처와 함께 '예상'으로 바꿈.
  - **근거 없음**: 쪽에도, 저장된 자료에도 출처가 없음(빈도·최상급·체감·일반화·추측 포함) → 삭제하거나 출처가 말하는 범위로 줄임.
  - **판단(표시됨)**: '우리 판단/저희 판단'으로 밝힌 권고(예: 현금 10만 원, 한복은 두세 시간만). 사실 주장이 아니라 권고라서 지우지 않고 목록만 남김 → 원두가 정할 것.
- 언어별로만 있는 내용(ja·zh-tw 전용 문단)은 숫자 대조(언어별 숫자 차이 추출)와 '확인 못 함' 표현 검색으로 찾았어요.

## 검증 한계 (숨기지 않음)

- 이번 세션에서 열린 곳: koreaherald.com, zdnet.co.kr, airport.kr, wowpass.io, tmoney.co.kr, sedaily.com. 막힌 곳(프록시 403 또는 연결 끊김): mediahub.seoul.go.kr, news.seoul.go.kr, royal.khs.go.kr, koreatimes, yna, korea.net, visitkorea(국문), cu·oliveyoung·korail, klook(affiliate.klook.com 403). e-arrivalcard.go.kr FAQ는 한 번 시도했지만 연결이 끊겨 못 열었어요.
- 그래서 '확실' 판정은 대부분 **쪽에 적힌 출처 목록과 확인 날짜**에 기댄 것이고, 출처 원문과 글자 대조는 하지 못했어요. 특히 각 쪽 출처 목록에 "이번에 다시 열지 못함"으로 적힌 항목들은 이전 판 확인을 그대로 믿은 것이에요.
- '확실' 문장은 하나하나 세지 않았어요(39쪽 수백 문장). 아래 표의 숫자는 **바꾼(또는 판단으로 남긴) 항목 수**이고, 확실은 '나머지 사실 문장 전부'예요.
- 독립 검토는 아직 없어요. 이 표는 Claude(작성자) 자체 판정이에요.

## 쪽별 요약

| 쪽 | 근거 없음(삭제·축소) | 예상 가능(예상으로) | 확실 | 판단(표시됨, 남김) | 재승인 필요(approved 줄 삭제) |
|---|---|---|---|---|---|
| index(홈) | 2 | 0 | 나머지 | 0 | 해당 없음(home) |
| about | 2 | 0 | 나머지 | 0 | ko·en·ja·zh-tw |
| privacy | 1 | 0 | 나머지 | 0 | ko·en·ja·zh-tw |
| name | 1 | 0 | 나머지 | 0 | ko·en·ja·zh-tw |
| data/site.json 태그라인(ko) | 1 | 0 | – | 0 | – |
| e-arrival-card | 2(+zh-tw 문구 1) | 0 | 나머지 | 1 | 없음(원래 승인 전) |
| essentials | 4 | 0 | 나머지 | 1 | 없음(브랜치에서 이미 삭제됨) |
| airport-to-seoul | 4 | 0 | 나머지 | 1 | 없음 |
| abroad-esim | 2 | 0 | 나머지 | 1 | 없음 |
| getting-around | 2 | 0 | 나머지 | 1 | en·ja·zh-tw |
| seoul-subway | 2 | 0 | 나머지 | 3 | 없음 |
| ktx-busan | 1(+ja 1) | 1 | 나머지 | 1 | en·ja·zh-tw |
| jeju | 4(+ja 1·zh-tw 1) | 0 | 나머지 | 2 | en·ja·zh-tw |
| olive-young | 1 | (main 62d862c에서 처리) | 나머지 | 1 | 없음 |
| daiso | 1 | 0 | 나머지 | 1 | 없음 |
| convenience-store | 1 | 0 | 나머지 | 0 | 없음 |
| kbeauty-how-to-choose | 1 | 0 | 나머지 | 0 | 없음 |
| shopping-streets | 1(본문 2곳+그림 4개 언어) | 0 | 나머지 | 2 | 없음 |
| emergency | 5 | 0 | 나머지 | 0 | en·ja·zh-tw |
| everyday | 3 | 0 | 나머지 | 0 | en·ja·zh-tw |
| food | 2 | 0 | 나머지 | 0 | en·ja·zh-tw |
| health | 2 | 0 | 나머지 | 1 | en·ja·zh-tw |
| money | 1(+zh-tw 문구 1) | 0 | 나머지 | 2 | ko·en·ja·zh-tw |
| concert-trip | 1 | 0 | 나머지 | 1 | en·ja·zh-tw |
| palaces | 2 | 1 | 나머지 | 1 | ko·en·ja·zh-tw |
| seoul-areas | 5(+zh-tw 2) | 0 | 나머지 | 1 | ko·en·ja·zh-tw |
| winter | 10(+ja 1·zh-tw 1) | 0 | 나머지 | 2 | ko·en·ja·zh-tw |
| departure-day, duty-free, tax-refund, skin-clinic, seoul-bus, first-trip, deals(본문), disclosure(브랜치), guides, shopping, updates, reuse, winter-light-puffer(62d862c 뒤) | 0 | 0 | 전부 | 일부 | – |

## 항목별 판정

표의 '파일:줄'은 고치기 전 판의 ko 줄(브랜치 판 기준 5쪽 포함, 언어판 전용이면 그 언어 줄). 표에 줄이 없는 '그대로' 행은 여러 줄에 걸친 확인 결과예요. 4개 언어의 정확한 전·후 문장은 맨 아래 **부록: 바꾼 문장 원문(4개 언어)**에 파일:줄과 함께 모두 있어요.

### index (홈)
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| 전자입국신고서는 "72시간 전부터 / 도착 전 72시간 안에" | 4 | content/ko/index.md:22 | 근거 없음(출처와 다름) | 같은 사이트 전자입국신고서 쪽: 공식 FAQ(2026-11-26 확인) "한국 시간 기준 도착일 3일 전부터, 31일 도착이면 29·30·31일" | "도착 3일 전부터 / 한국 날짜로 도착 3일 전부터" |
| 즉시 환급 "15,000원 이상 100만 원까지" | 4 | :22 | 근거 없음(경계 틀림) | 택스리펀드 쪽 출처(비짓서울·올리브영 FAQ·법령): 100만 원 **미만** | "100만 원 미만" |
| eSIM "설정 메뉴에서 2분이면 확인" | 4 | :26 | 근거 없음 | 시간 출처 없음 | "설정 메뉴에서 확인할 수 있어요" |
| 직통열차 43분·13,000원, 올리브영 연 4회·약 7일 | 4 | :22 | 확실 | 공항 쪽(공항철도 2026-11-26·27 확인), CJ뉴스룸 | 그대로 |

### about / privacy / name / site.json
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| "그중 절반은 이미 오래된 정보" | 4 | about.md:10 | 근거 없음 | 수치 출처 없음 | "그중에는 이미 바뀐 정보도 섞여 있어요" |
| "모든 사실은 게시 전에 에디터가 확인" | 4 | about.md:15 | 근거 없음(사실과 다름) | 승인 전 쪽은 바이라인이 "아직 Nadri 에디터 검토 전"(data/site.json byline_pending) | "각 페이지 위에 공식 정보로 마지막 확인한 날짜와 에디터 승인 여부를 표시" |
| 제휴 파트너 예시 "클룩, 아고다, 에어알로" | 4 | privacy.md:19 | 근거 없음(사실과 다름) | data/affiliates.json: Airalo·Agoda url 비어 있음, 링크 중인 곳은 Klook·Yesim(브랜치 수익 구조 쪽과 같게) | "클룩, Yesim" |
| "같은 이름을 가진 사람 수를 세는 나라는 없어서" | 4 | name.md:18 | 근거 없음 | 출처 없음. 일부 나라 통계청은 이름별 인구 수를 공개함(예: 스페인 INE — Claude 지식, 이번에 원문 미확인) | "사람 수가 아니라 아기 이름 순위예요" |
| 태그라인 "직접 확인한 정보로" | ko | data/site.json | 근거 없음('직접'=현장 확인으로 읽힘, 소개 쪽 "가 보지 않은 곳을 가 본 것처럼 쓰지 않음"과 충돌) | – | "확인한 정보로"(en·ja·zh-tw는 원래 '직접' 없음) |

남은 것(고치지 않음, 원두 판단 필요): `static/name-i18n.js`에 같은 "No country publishes how many living people share a first name" 문구가 17개 언어로 있음. 17개 언어 동시 수정이라 이번에 손대지 않았어요.

### e-arrival-card
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| "휴대폰으로 10분쯤"(lede·사실 칩·마지막 장면), "몇 분이면 끝나요" | 4 | :4, :10, :26, :195 | 근거 없음 | 공식 FAQ에 소요 시간 없음 | 시간 표현 삭제 |
| zh-tw "依官方規定拼出的畫面,不是編出來的心得。" | zh-tw | zh-tw:199 | 원두 [7eb4ec94#1176] 삭제 대상 | – | 삭제 |
| 3일 전부터, 72시간 효력, 9명·1,000명, 환승, 종이 신고서 | 4 | 여러 줄 | 확실 | 공식 FAQ 34개(2026-11-26 확인) | 그대로 |
| 'unknown' 칸 설명 | 4 | :72 | 판단(표시됨: "화면을 보고 우리가 판단") | – | 그대로 |

### essentials (브랜치 판)
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| SKT 요금제 "2~90일, 통화는 충전, 핫스팟 안 됨", "통화·문자 되는" 버튼 라벨 | 4 | :55, :63, :65 | 근거 없음 | 같은 쪽 출처: "클룩 eSIM 상품 페이지 — 자동 접속 차단으로 열지 못함". 이번에도 affiliate.klook.com 403. 원래 상품 주소는 원두 확인 대기(drafts/az-affiliate/wondu-items.md 1번) | 조건 삭제, "상품 페이지에서 확인" 안내, 버튼 "클룩에서 SKT eSIM 요금제 더 보기" |
| "(일부 예약·배달 앱은 한국 번호를 요구해요)" | 4 | :63 | 근거 없음 | 음식 쪽 출처: 배민은 7월부터 한국 번호 불필요, 네이버는 여권 인증 | 삭제 |
| "먼저 내 폰 확인(1분)" | 4 | :51 | 근거 없음 | – | "(1분)" 삭제 |
| 카카오맵 "구글 지도와 가장 비슷한 느낌", 카카오 T "영어 화면 지원. 카드로 결제" | 4 | :116–117 | 근거 없음 | 출처 없음. 대중교통 쪽(k.ride 앱스토어 정보): 해외 카드는 k.ride | "네이버 지도와 비교용", "한국 번호·국내 카드가 있을 때. 해외 카드는 k.ride" |
| K-ETA 22개 국가·지역·3년·1만 원, 공항철도 티머니 15,000원 | 4 | :18, :41, :95 | 확실(일부는 "이번에 다시 열지 못해 이전 확인 유지"로 쪽에 표시) | k-eta.go.kr 공지, 코리아헤럴드 10947683(저장본 staging/az-affiliate-2026-11-27/raw) | 그대로 |
| "eSIM이 가장 간편" | 4 | :49 | 판단(표시됨: "저희 판단") | – | 그대로 |

### airport-to-seoul (브랜치 판)
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| 일반열차 "출퇴근 시간엔 붐벼서 큰 캐리어는 좀 버거워요" | 4 | :17 | 근거 없음 | 혼잡 출처 없음 | 삭제 |
| "직통열차는 출퇴근 인파를 피하는 게 아낀 시간보다 더 크게 느껴져요" | 4 | :19 | 근거 없음(체감) | – | 삭제 |
| "문이 안 열리면 카드 잔액이 모자란 경우가 많아요" | 4 | :99 | 근거 없음(빈도) | – | "단말기에 뜬 잔액을 보고, 모자라면 …충전" |
| "10분만 준비하면 첫 1시간이 편해요" | 4 | :236 | 근거 없음 | – | "세 가지만 정해 두세요." |
| 시간·요금·막차·버스 번호·택시 정액·ATM 위치 | 4 | 여러 줄 | 확실 | 공항철도·인천공항·Visit Seoul·서울시(2026-11-26·27 확인, 저장본 staging/az-affiliate-2026-11-27/raw/arex-*, airport-kr-*) | 그대로 |
| 2터미널 직통열차 방향, ATM 해외 카드 가능 여부 | 4 | :23, :90 | (확인 못 함을 밝히고 행동 안내 — 불확실 정보를 사실로 쓰지 않음) | – | 그대로 |

### abroad-esim (브랜치 판)
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| "2분 안에 확인", "공항에서 QR 찾다가 탑승 방송 듣는 게 제일 흔한 실수" | 4 | :3, :37 | 근거 없음 | – | 삭제 |
| "그보다 앞서 나온 국내 모델은 지원하지 않을 가능성이 높으니" | 4 | :23 | 예상 가능(이미 근거와 함께 '가능성'으로 씀: 2022-09-01 개통 시작, 첫 모델 폴드4) | 삼성전자서비스·세계일보 | 그대로 |

### getting-around / seoul-subway
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| "2025년 5월 1~8호선 첫차·막차 30분 앞당김 발표 … 시행됐는지 확인하지 못했어요" | 4 | getting-around:82, seoul-subway:207 | 근거 없음(지금 상태 미확인. 막차 시각처럼 행동을 바꾸는 정보) | 서울시 영문 누리집 2025-05-27, 코리아헤럴드 2025-05-22 — 계획만 있고 시행 확인 출처 없음. 이번에 코리아헤럴드 검색도 시도했으나 확인 못 함 | 삭제, "지금 시각은 역과 요일마다 다르니 그날 네이버 지도로 확인" |
| 표 "막차 시각이 바뀌었을 수 있어요" | 4 | seoul-subway:151 | 근거 없음 | – | "2022년 연장은 평일만이라 주말은 더 일찍 끊겨요"(서울시 2022-05-30 출처) |
| "버스에 오른 뒤엔 해결할 방법이 없는 유일한 문제" | ko·en·ja | getting-around:27 | 근거 없음(같은 쪽에 계좌이체 대안이 있음) | 서울시 현금 없는 버스 안내 | "해결하기 어려워요" |
| 요금 1,550원, 환승 30분/1시간, 현금 없는 버스 183/396 | 4 | 여러 줄 | 확실 | 서울시(2026-11-26 확인) | 그대로 |
| 기후동행카드 "하루 3번 이상, 3일 이상" | 4 | getting-around:24 | 판단(표시됨, 요금 계산 근거 있음) | – | 그대로 |
| "캐리어가 있다면 평일 아침 7~9시는 피하세요", "노약자석 앉지 마세요" | 4 | seoul-subway | 판단(표시됨, 서울시 2014 분석 근거) | – | 그대로 |

### ktx-busan
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| "지금도 비슷하다고 보면 되고"(2024년 소요 시간) | 4 | :45 | 예상 가능 | 코레일 "본격 단축은 2028년 이후"(이데일리 2024-04-22) | "그래서 지금도 비슷할 것으로 예상해요" |
| 부산시 "유라시아플랫폼 무인 짐 보관소, 시기 미정" | 4 | :82 | 근거 없음(쓸 수 있는 시점 없음 — 원칙 3) | 계획 보도만 | 삭제 |
| ja "新しい券売機 … 日本語表示にも対応" | ja | ja:38 | 근거 없음(ja에만 있는 주장, 출처 목록에 없음) | – | 삭제 |
| zh-tw "桃園、高雄都有每日直飛金海" | zh-tw | zh-tw:19, :70 | 확실 | 韓國觀光公社 2026年9月(쪽 출처) | 그대로 |
| 코레일패스 SRT 사용(2026년 8월 기준 안 됨, 통합 뒤 미확인) | 4 | :36 | 예상 가능(이미 근거와 안전한 행동으로 씀) | VisitKorea 2026-08 | 그대로 |

### jeju
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| "비행은 짧아도 양쪽 공항에서 하루 대부분이 가요" | 4 | :21 | 근거 없음 | – | 삭제 |
| 숙소 표 "풍경은 제일 덜하고", "저녁에 할 게 적고", "공항에서 제일 멀어요" | 4 | :61–63 | 근거 없음 | – | "남쪽보다 추워요(기상청 겨울 평균 최고기온)", "201번 버스 간격이 30~80분", "공항에서 멀어요. 공항 리무진 정류장은 현장에서 확인" |
| ja "成田–済州 週4便(夏ダイヤ)… 冬ダイヤ以降は確認できなかった" | ja | ja:32 | 근거 없음(지금 운항 미확인) | Aviation Wire 2026-02-10은 여름 운항만 | 문단과 그 출처 삭제 |
| zh-tw "台灣虎航 桃園–濟州 … 冬季是否續飛沒能確認" | zh-tw | zh-tw:32 | 근거 없음(지금 운항 미확인) | 工商時報 2026-04-10은 4월 프로모션만 | 문단과 그 출처 삭제 |
| zh-tw 臺灣 국제운전면허(TVBS 2022) | zh-tw | | 확실(날짜·재확인 안내와 함께 표기) | TVBS 2022-02 | 그대로 |
| "3일뿐이라면 제주는 다음으로", ja "2回目以降の韓国で…" | 4/ja | | 판단 | – | 그대로 |

### olive-young / daiso / convenience-store / kbeauty / shopping-streets
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| "세일 주간엔 작은 지점이 더 한산할 수 있어요" | 4 | olive-young:43 | 근거 없음 | – | 삭제 |
| 12월 올영세일 날짜·어워즈 | 4 | olive-young(main 62d862c) | 예상 가능 → 이미 main 62d862c가 근거와 함께 '예상'으로 바꿈 | CJ뉴스룸 | (이번 작업에서 손대지 않음) |
| 다이소 강남터미널점 "통로가 미로 같아서" | 4 | daiso:36 | 근거 없음 | – | "버스를 기다리는 동안 들를 수 있어요. 출발 시간을 꼭 확인하세요." |
| 편의점 "다섯 곳 중 한 곳은 밤에 문을 닫거나 무인으로 바뀌어요" | 4 | convenience-store:25 | 근거 없음('무인으로 바뀜') | 머니투데이(24시간 78%)는 무인 전환을 말하지 않음 | "나머지 약 22%, 다섯 곳 중 한 곳꼴은 24시간 점포가 아니에요" |
| SPF "50을 넘으면 실제 차이가 크지 않아서 묶어 표시" | 4 | kbeauty:57 | 근거 없음(이유 부분) | 출처(기능성화장품 심사 규정 제13조)는 표시 방식만 | "50을 넘는 숫자는 따로 적지 않아요(식약처 고시)" |
| 명동 "문 연 직후가 좋다(저희 추측)" | 4 | shopping-streets:19, :53, 그림 shopping-streets-1 | 근거 없음(사실에 대한 추측 — 혼잡 자료 없음) | – | 본문 삭제, 그림 4개 언어 '이른 시간' → '—' |
| 성수 평일(코리아헤럴드 주말 대기), 홍대 늦은 오후(영업시간 근거) | 4 | | 확실 / 판단(근거 표시) | | 그대로 |

### emergency / everyday / food / health / money / concert-trip
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| 긴급 lede "대부분의 나쁜 순간은 … 잠깐의 지연으로 끝나요" | 4 | emergency:4 | 근거 없음 | – | "출발 전에 번호 세 개를 저장하고 이 페이지를 열어 두세요." |
| "택시 분실물은 대개 가장 잘 해결되는 일" | 4 | emergency:53 | 근거 없음 | – | 삭제 |
| "외국 정부들이 가장 많이 경고하는 위험" | 4 | emergency:89 | 근거 없음(최상급) | 미국 국무부·캐나다 정부(쪽 출처) | "미국·캐나다 정부의 여행 안내가 경고하는 위험" |
| "카드가 안 되면 대개 해외 카드사가 막은 것" | 4 | emergency:97 | 근거 없음(빈도) | 돈 쪽 출처는 반대로 '가게 계약' 원인을 말함 | "해외 카드사가 거래를 막았을 수 있어요" |
| "대부분은 이 페이지를 한 번도 안 쓰고 끝나요", "(5분)" | 4 | emergency:25, :116 | 근거 없음 | – | 삭제 |
| 2인분 "여행자 경험담이 많아요" | 4 | everyday:35 | 근거 없음(빈도) | 코리아타임스 2025-11-15(안내문 화제)는 '있음'만 뒷받침 | "요구하는 곳이 있어요" |
| "호텔과 공항에서는 대체로 통하지만 작은 식당은 어려울 때가 많아요" | 4 | everyday:51 | 근거 없음 | 영국 정부는 택시 기사만 말함 | 삭제, 영국 정부 문장만 |
| "치안이 좋다 보니 긴장이 풀리기 쉬워요. 진짜 조심할 건 그 정도" | 4 | everyday:68 | 근거 없음 | – | 삭제 |
| 고기 "2인분부터인 곳이 많아요" | 4 | food:21 | 근거 없음(빈도) | – | "2인분부터 받는 곳이 있어요" |
| "배민은 외국인 이용이 가장 크게 바뀐 배달 앱" | 4 | food:61 | 근거 없음(최상급) | 아시아경제·코리아헤럴드·코리아타임스(바뀐 3가지) | "외국인이 쓰기 쉽게 세 가지가 바뀌었어요" |
| 아플 때 lede "대부분 … 순서로 해결돼요", "대부분 저녁이면 닫아요" | 4 | health:4, :62 | 근거 없음 | – | "가벼운 증상이라면 … 순서로 찾아가요", "밤이나 휴일에 문 연 곳을 찾는 방법" |
| 카드 두 장 "다른 한 장으로 되는 경우가 많아요" | 4 | money:18 | 근거 없음(빈도) | – | "다른 브랜드 카드로 다시 시도할 수 있어요" |
| zh-tw "依下面查證過的事實拼出的畫面,不是編出來的心得。" | zh-tw | money:20 | 원두 [7eb4ec94#1176] 삭제 대상 | – | 삭제 |
| 서울월드컵경기장 "6만 6천 석, 잔디 보호로 그라운드석 보통 안 팔아요" | 4 | concert-trip:72 | 근거 없음 | 출처 목록에 없음 | 삭제(역 안내만 남김) |
| 현금 10만 원, 사설 환전소가 유리 | 4 | money | 판단(표시됨) / 확실(지구를 걷는 법 2026-03-04) | | 그대로 |

### palaces / seoul-areas / winter
| 주장 | 언어 | 파일:줄 | 분류 | 근거/출처 | 바꾼 것 |
|---|---|---|---|---|---|
| 수요일 무료 "시행 중인지 확인하지 못했으니" | 4 | palaces:61 | 예상 가능 | 세계일보 2026-05-27(발표: 덕수궁 8월, 창덕·창경·종묘 10월부터) | "발표대로라면 지금 시행 중일 것으로 예상해요(근거: 세계일보 2026년 5월 27일 보도)…" |
| 한복 "긴 치마로 자갈길 하루 종일 힘들어요", "11~1월엔 고름을 채운 채로 추워요" | 4 | palaces:69 | 근거 없음(체감) | – | 삭제(관람료 절약 폭·시간만 남김) |
| 명동 "큰길은 가게가 닫을 때까지 붐벼요", 서울역 "저녁 산책할 거리가 적고", 홍대 "주말 밤엔 시끄러워요", 동대문 "아침엔 할 게 적어요" | 4 | seoul-areas:37,45,52,66 | 근거 없음 | 홍대는 서울시 핼러윈 추산(12만 5천 명), 동대문은 코리아타임스 '24시간 패션 중심지'로 대체 | 각 문장 삭제 또는 출처 범위 문장 |
| "들어오는 질문은 위 일곱 곳에 몰려 있어요" | 4 | seoul-areas:90 | 근거 없음(받은 질문 자료 없음) | – | "이 페이지는 위 일곱 곳만 다뤄요" |
| zh-tw "台灣旅客最常問的就是這題", 표 "大街到打烊前都很擠 / 週末晚上很吵" | zh-tw | zh-tw:32, :39 | 근거 없음 | – | 삭제 / "觀光客多 / 夜裡人潮多" |
| 겨울 lede "맑고 건조한 추위", 핫팩 "하루 종일 버텨요", "난방이 세서 금방 더워요", "세 달 모두 숫자보다 춥게", "상당수는 잠깐 날리는 정도", "추위의 대부분을 막아 줘요", "−5°C를 견디기 힘들게 만드는 건 귀와 손에 닿는 바람", 11월 말·3월 초 옷차림, "서울 시내는 한산해지고", "지난해 막차 연장" | 4 | winter:4, 18, 19, 34, 38, 46, 48, 56, 60, 90 | 근거 없음 | 출처 목록에 없음. 체감온도는 YTN 2025-12-26 수치로 대체 | 삭제 또는 기상청·YTN 수치 문장 |
| ja "カイロは日本から持って行っても大丈夫", zh-tw "台灣冬天穿的外套通常不夠" | ja·zh-tw | | 근거 없음(언어판 전용) | – | 삭제 |
| 평년 기온표, 2027 설 연휴, 궁궐 연휴 개방(규정 적용 예상), 박물관 휴관 | 4 | | 확실 / 예상 가능(이미 규정·2026 사례 근거로 씀) | 기상청·우주항공청·국가유산청 규정 | 그대로 |
| "실내는 따뜻해요(난방)" | 4 | winter | 근거 없음(상식 수준) — 그림(winter-1)에도 있어 남김 | – | 그대로, 원두 판단 |

## 바꾸지 않은 쪽과 이유

- departure-day, duty-free, tax-refund, skin-clinic, seoul-bus, first-trip: 사실 문장마다 쪽 출처 목록에 대응 출처와 확인 날짜가 있음(일부 "다시 열지 못함" 표기). 근거 없는 빈도·최상급 표현을 찾지 못했어요. 다만 원문 글자 대조는 못 했어요.
- deals.md 본문, disclosure(브랜치 판), guides, shopping, updates, reuse: 사이트 자체 정책·기록이라 외부 사실 주장이 거의 없음.
- winter-light-puffer: main 62d862c에서 헤드리스로 읽은 사실을 이미 내림. 남은 무신사 수치는 '운영자 확인 화면'(원두 화면, 날짜·시각 표기)이라 확실로 봄. "이미 경량 패딩이 있다면 새로 살 이유는 색과 모양 정도라고 봐요"는 판단(표시됨).
- data/trending.json: 쪽의 +718%(코리아헤럴드 2026-10-20)와 같음 → 확실.

## 언어판별 '쓸 수 있는 사람' 점검 (원칙 3)

- 올리브영 올영데이(회원 전용 쿠폰): en·ja·zh-tw 홈에는 이미 빠져 있고, 올리브영 쪽은 "추가 쿠폰은 한국 회원 몫"이라 일정 맞추지 말라고 안내 → 문제 없음.
- jeju ja·zh-tw의 직항 문단: 지금 탈 수 있는지 모르는 항공편이라 삭제(위).
- 그 밖에 언어판에서 독자가 쓸 수 없는 정보를 보여 주는 곳은 찾지 못했어요(deals.json은 범위 밖).

## 원두가 정할 것

1. 필수 준비 쪽 클룩 'SKT eSIM(통화·문자)' 버튼: 상품 조건을 확인할 수 없어 설명을 지우고 버튼 라벨을 중립으로 바꿨어요. 버튼 자체를 남길지(상품 원래 주소를 알려 주시면 조건을 확인해 다시 씀) 정해 주세요.
2. `static/name-i18n.js` 17개 언어의 "이름별 사람 수를 세는 나라는 없다" 문구: 같이 고칠지.
3. '판단(표시됨)' 권고(현금 10만 원, 한복 두세 시간, 3일 여행이면 제주 미루기 등)와 상식 수준 문장(겨울 실내 난방)을 남길지.
4. 이번에 approved 줄을 지운 쪽(위 요약 표 마지막 칸)의 재승인.

## 커밋

- bbe9129 불확실 정보 점검 7: ja KTX — 출처에 없는 '새 발권기 일본어 표시 지원' 문구 삭제(ko·en·zh-tw에는 �
- ccc21ea 불확실 정보 점검 6: 궁궐·숙소 지역·겨울 — 궁궐 수요일 무료를 근거(세계일보 2026-05-27)와 함께 
- f853bce 불확실 정보 점검 5: 긴급·생활·음식·아플 때·돈·콘서트 — 근거 없는 빈도·최상급·일반화('대�
- c29347e 불확실 정보 점검 4: 쇼핑 — 근거 없는 추측·평가 삭제(올리브영 '세일 주간 작은 지점이 한산', �
- 7cb92cc 불확실 정보 점검 3: 교통·제주 — 시행 여부를 확인 못 한 '1~8호선 첫차·막차 30분 앞당김' 문장 �
- d916640 불확실 정보 점검 2: 전자입국신고·필수 준비·공항·해외 eSIM — 근거 없는 소요 시간('10분', '2분',
- ef316f0 불확실 정보 점검 1: 홈·소개·개인정보·이름 — 전자입국신고 '72시간'→'도착 3일 전'(공식 FAQ), �

빌드: 각 묶음마다 작업 사본(/tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/ua-site)에서 `python3 build.py` → 156쪽 생성, 오류 없음. main에는 올리지 않았어요.

## 부록: 바꾼 문장 원문(4개 언어, 고치기 전 판의 파일:줄)

### index

- `content/ko/index.md:22` (ko)  
  전: <h4>전자입국신고서는 72시간 전부터</h4><p>도착 전 72시간 안에 공식 사이트에서만 내요.  
  후: <h4>전자입국신고서는 도착 3일 전부터</h4><p>한국 날짜로 도착 3일 전부터 공식 사이트에서만 내요.
- `content/ko/index.md:22` (ko)  
  전: 15,000원 이상 100만 원까지면  
  후: 15,000원 이상 100만 원 미만이면
- `content/ko/index.md:26` (ko)  
  전: 두 가지 모두 설정 메뉴에서 2분이면 확인돼요.  
  후: 두 가지 모두 설정 메뉴에서 확인할 수 있어요.
- `content/en/index.md:22` (en)  
  전: <h4>The e-Arrival Card opens 72 hours out</h4><p>File it in the 72 hours before you land, on the official site only.  
  후: <h4>The e-Arrival Card opens 3 days before you land</h4><p>File it from 3 days before your arrival date (Korea time), on the official site only.
- `content/en/index.md:22` (en)  
  전: from ₩15,000 up to ₩1,000,000 gets  
  후: from ₩15,000 up to just under ₩1,000,000 gets
- `content/en/index.md:26` (en)  
  전: Both checks take two minutes in your settings menu.  
  후: You can check both in your settings menu.
- `content/ja/index.md:22` (ja)  
  전: <h4>電子入国申告は72時間前から</h4><p>到着前72時間以内に、公式サイトだけで。  
  후: <h4>電子入国申告は到着3日前から</h4><p>韓国の日付で到着3日前から、公式サイトだけで。
- `content/ja/index.md:22` (ja)  
  전: 15,000ウォン以上100万ウォンまでなら  
  후: 15,000ウォン以上100万ウォン未満なら
- `content/ja/index.md:26` (ja)  
  전: どちらも設定メニューで2分あれば確認できます。  
  후: どちらも設定メニューで確認できます。
- `content/zh-tw/index.md:22` (zh-tw)  
  전: <h4>電子入境卡 72 小時前開放</h4><p>抵達前 72 小時內,只在官方網站填。  
  후: <h4>電子入境卡抵達前 3 天開放</h4><p>以韓國日期計,抵達前 3 天起,只在官方網站填。
- `content/zh-tw/index.md:22` (zh-tw)  
  전: 15,000 韓元以上、100 萬韓元以內  
  후: 15,000 韓元以上、未滿 100 萬韓元
- `content/zh-tw/index.md:26` (zh-tw)  
  전: 兩項都能在設定選單裡 2 分鐘確認完。  
  후: 兩項都能在設定選單裡確認。

### about

- `content/ko/about.md:10` (ko)  
  전: 찾아 맞춰야 하고, 그중 절반은 이미 오래된 정보예요.  
  후: 찾아 맞춰야 하고, 그중에는 이미 바뀐 정보도 섞여 있어요.
- `content/ko/about.md:15` (ko)  
  전: 모든 사실은 게시 전에 에디터가 확인하고, 각 페이지에는 마지막으로 확인한 날짜를 표시해요.  
  후: 각 페이지 위에는 공식 정보로 마지막으로 확인한 날짜와, Nadri 에디터가 그 판을 승인했는지를 표시해요.
- `content/en/about.md:10` (en)  
  전: from a dozen places, half of them out of date.  
  후: from a dozen places, some of them already out of date.
- `content/en/about.md:15` (en)  
  전: Every fact is checked by an editor before publishing, and each page shows the date it was last checked.  
  후: Each page shows, at the top, the date it was last checked against official information and whether a Nadri editor has approved that version.
- `content/ja/about.md:10` (ja)  
  전: 十数か所から寄せ集めることになり、その半分は情報が古くなっています。  
  후: 十数か所から寄せ集めることになり、中にはすでに古くなった情報も混じっています。
- `content/ja/about.md:15` (ja)  
  전: 公開前にはすべての事実を編集者が確認し、各ページには最終確認日を表示しています。  
  후: 各ページの上部には、公式情報で最後に確認した日付と、その版をNadriの編集者が承認したかどうかを表示しています。
- `content/zh-tw/about.md:10` (zh-tw)  
  전: 其中一半還是過時的資訊。  
  후: 其中也混著已經過時的資訊。
- `content/zh-tw/about.md:15` (zh-tw)  
  전: 每一項事實在發布前都經過編輯確認,每一頁也都標示最後確認的日期。  
  후: 每一頁上方都標示最後用官方資訊確認的日期,以及該版本是否經過 Nadri 編輯核准。

### privacy

- `content/ko/privacy.md:19` (ko)  
  전: (예: 클룩, 아고다, 에어알로)  
  후: (예: 클룩, Yesim)
- `content/en/privacy.md:19` (en)  
  전: (for example Klook, Agoda or Airalo)  
  후: (for example Klook or Yesim)
- `content/ja/privacy.md:19` (ja)  
  전: (例:Klook、Agoda、Airalo)  
  후: (例:Klook、Yesim)
- `content/zh-tw/privacy.md:19` (zh-tw)  
  전: (例如 Klook、Agoda 或 Airalo)  
  후: (例如 Klook 或 Yesim)

### name

- `content/ko/name.md:18` (ko)  
  전: 같은 이름을 가진 사람 수를 세는 나라는 없어서, 사람 수 대신 순위로 보여 줘요.  
  후: 사람 수가 아니라 아기 이름 순위예요.
- `content/en/name.md:18` (en)  
  전: No country counts how many living people share a first name, so we show ranks, not head counts.  
  후: These are baby-name ranks, not counts of people.
- `content/ja/name.md:18` (ja)  
  전: 同じ名前の人の数を数える国はないため、人数ではなく順位で示します。  
  후: 人数ではなく、赤ちゃんの名前の順位です。
- `content/zh-tw/name.md:18` (zh-tw)  
  전: 沒有國家統計同名的人數,所以用排名而不是人數。  
  후: 這是新生兒名字的排名,不是人數。

### data/site.json

- `data/site.json:246` (-)  
  전: "tagline": "한국 여행을 더 쉽게. 직접 확인한 정보로 여행·쇼핑·문화를 안내해요."  
  후: "tagline": "한국 여행을 더 쉽게. 확인한 정보로 여행·쇼핑·문화를 안내해요."

### e-arrival-card

- `content/ko/e-arrival-card.md:4` (ko)  
  전: lede: 무료, 휴대폰으로 10분쯤, 도착 3일 전부터.  
  후: lede: 무료, 휴대폰으로, 도착 3일 전부터.
- `content/ko/e-arrival-card.md:10` (ko)  
  전: <li><i class="ic ic-clock" aria-hidden="true"></i>10분쯤</li>  
  후: (삭제)
- `content/ko/e-arrival-card.md:26` (ko)  
  전: (공식 신고서는 무료이고 몇 분이면 끝나요)  
  후: (공식 신고서는 무료예요)
- `content/ko/e-arrival-card.md:195` (ko)  
  전: 공식 사이트에서 10분쯤. 발급번호가  
  후: 공식 사이트에서 내요. 발급번호가
- `content/en/e-arrival-card.md:4` (en)  
  전: lede: Free, about 10 minutes on your phone, in the 3 days before you land.  
  후: lede: Free, on your phone, in the 3 days before you land.
- `content/en/e-arrival-card.md:10` (en)  
  전: <li><i class="ic ic-clock" aria-hidden="true"></i>About 10 minutes</li>  
  후: (삭제)
- `content/en/e-arrival-card.md:26` (en)  
  전: (the official form is free and takes minutes)  
  후: (the official form is free)
- `content/en/e-arrival-card.md:195` (en)  
  전: About ten minutes on the official site, and the PDF  
  후: File it on the official site, and the PDF
- `content/ja/e-arrival-card.md:4` (ja)  
  전: lede: 無料、スマホで10分ほど、到着の3日前から。  
  후: lede: 無料、スマホで、到着の3日前から。
- `content/ja/e-arrival-card.md:10` (ja)  
  전: <li><i class="ic ic-clock" aria-hidden="true"></i>10分ほど</li>  
  후: (삭제)
- `content/ja/e-arrival-card.md:26` (ja)  
  전: (公式の申告書は無料で、数分で終わります)  
  후: (公式の申告書は無料です)
- `content/ja/e-arrival-card.md:195` (ja)  
  전: 公式サイトで10分ほど。発行番号入りの  
  후: 公式サイトで提出。発行番号入りの
- `content/zh-tw/e-arrival-card.md:4` (zh-tw)  
  전: lede: 免費,用手機約 10 分鐘,抵達前 3 天開放。  
  후: lede: 免費,用手機填,抵達前 3 天開放。
- `content/zh-tw/e-arrival-card.md:10` (zh-tw)  
  전: <li><i class="ic ic-clock" aria-hidden="true"></i>約 10 分鐘</li>  
  후: (삭제)
- `content/zh-tw/e-arrival-card.md:26` (zh-tw)  
  전: (官方表單免費,幾分鐘就填完)  
  후: (官方表單免費)
- `content/zh-tw/e-arrival-card.md:195` (zh-tw)  
  전: 在官網花大約 10 分鐘,把含核發號碼的  
  후: 在官網填好,把含核發號碼的
- `content/zh-tw/e-arrival-card.md:199` (zh-tw)  
  전: 依官方規定拼出的畫面,不是編出來的心得。⏎  
  후: (삭제)

### essentials

- `content/ko/essentials.md:51` (ko)  
  전: **먼저 내 폰 확인(1분):**  
  후: **먼저 내 폰 확인:**
- `content/ko/essentials.md:55` (ko)  
  전: 한국 번호로 전화·문자를 받아야 하면 그 아래 SKT 통화·문자 요금제예요.  
  후: 한국 번호가 필요하면 그 아래 SKT 상품을 보세요.
- `content/ko/essentials.md:63` (ko)  
  전: 통화와 문자를 받을 한국 번호가 필요하다면(일부 예약·배달 앱은 한국 번호를 요구해요) 아래 요금제를 보세요. SK텔레콤망을 쓰고, 2~90일 동안 이용할 수 있으며, 통화는 충전으로 추가하지만 핫스팟 공유는 안 돼요.  
  후: 한국 번호가 필요하다면 아래 상품을 보세요. 이용 기간, 통화·문자 조건, 핫스팟 공유 여부는 저희가 상품 페이지를 열지 못해 적지 않았어요. 사기 전에 상품 페이지에서 확인하세요.
- `content/ko/essentials.md:65` (ko)  
  전: {{aff:klook_esim_alt\|통화·문자 되는 SKT eSIM}}  
  후: {{aff:klook_esim_alt\|클룩에서 SKT eSIM 요금제 더 보기}}
- `content/ko/essentials.md:116` (ko)  
  전: \| 카카오맵 \| 길 안내 \| 비교용으로 좋음. 구글 지도와 가장 비슷한 느낌 \|  
  후: \| 카카오맵 \| 길 안내 \| 네이버 지도와 비교용 \|
- `content/ko/essentials.md:117` (ko)  
  전: \| 카카오 T \| 택시 \| 영어 화면 지원. 카드로 결제하거나 차 안에서 결제 \|  
  후: \| 카카오 T \| 택시 \| 한국 번호·국내 카드가 있을 때. 해외 카드는 외국인용 k.ride ([서울 대중교통](/ko/getting-around/)) \|
- `content/en/essentials.md:51` (en)  
  전: **Check your phone first (1 minute):**  
  후: **Check your phone first:**
- `content/en/essentials.md:55` (en)  
  전: If you need a Korean number for calls and texts, the SKT plan below them.  
  후: If you need a Korean number, see the SKT product below them.
- `content/en/essentials.md:63` (en)  
  전: Need a Korean number for calls and texts (some booking and delivery apps ask for one)? The plan below runs on SK Telecom, lasts 2 to 90 days and adds calls as a top-up, but does not allow hotspot sharing.  
  후: Need a Korean number? See the product below. We could not open the product page, so we have not listed its validity, call and text terms or hotspot rules. Check them on the product page before you buy.
- `content/en/essentials.md:65` (en)  
  전: {{aff:klook_esim_alt\|SKT eSIM with calls and texts}}  
  후: {{aff:klook_esim_alt\|More SKT eSIM plans on Klook}}
- `content/en/essentials.md:116` (en)  
  전: \| Kakao Map \| Directions \| A good second opinion; feels closest to Google Maps \|  
  후: \| Kakao Map \| Directions \| To compare with Naver Map \|
- `content/en/essentials.md:117` (en)  
  전: \| Kakao T \| Taxis \| English interface. Pay by card or in the car \|  
  후: \| Kakao T \| Taxis \| If you have a Korean number and card. With a foreign card, use k.ride, the visitor app ([Getting around](/getting-around/)) \|
- `content/ja/essentials.md:51` (ja)  
  전: **まず自分のスマホを確認(1分):**  
  후: **まず自分のスマホを確認:**
- `content/ja/essentials.md:55` (ja)  
  전: 韓国の番号で電話・SMSを受ける必要があるなら、その下のSKT通話・SMSプランです。  
  후: 韓国の番号が必要なら、その下のSKTの商品を見てください。
- `content/ja/essentials.md:63` (ja)  
  전: 電話・SMS用に韓国の番号が必要なら(予約・配達アプリで求められることがあります)、下のプランを。SKテレコム回線で2〜90日、通話は追加チャージで使えます。テザリングは不可です。  
  후: 韓国の番号が必要なら、下の商品を見てください。利用期間、通話・SMSの条件、テザリングの可否は、商品ページを開けなかったため載せていません。買う前に商品ページで確認してください。
- `content/ja/essentials.md:65` (ja)  
  전: {{aff:klook_esim_alt\|通話・SMS付きのSKT eSIMを見る}}  
  후: {{aff:klook_esim_alt\|KlookでSKT eSIMのほかのプランを見る}}
- `content/ja/essentials.md:116` (ja)  
  전: \| カカオマップ \| ルート検索 \| セカンドオピニオンに。Googleマップに近い操作感 \|  
  후: \| カカオマップ \| ルート検索 \| NAVERマップとの比較に \|
- `content/ja/essentials.md:117` (ja)  
  전: \| Kakao T \| タクシー配車 \| 英語表示あり。カード払いも可 \|  
  후: \| Kakao T \| タクシー配車 \| 韓国の番号と韓国のカードがある場合。海外カードなら外国人向けのk.ride([ソウルの移動](/ja/getting-around/)) \|
- `content/zh-tw/essentials.md:51` (zh-tw)  
  전: **先確認你的手機(1 分鐘):**  
  후: **先確認你的手機:**
- `content/zh-tw/essentials.md:55` (zh-tw)  
  전: 需要用韓國門號接電話、收簡訊,就看再下面那款 SKT 通話簡訊方案。  
  후: 需要韓國門號,就看再下面那款 SKT 商品。
- `content/zh-tw/essentials.md:63` (zh-tw)  
  전: 需要韓國門號打電話、收簡訊(有些訂位、外送 App 會要求)?下面這款使用 SK Telecom 網路,效期 2 到 90 天,通話需另外加值,不支援熱點分享。  
  후: 需要韓國門號?看下面這款商品。效期、通話簡訊條件、能不能分享熱點,我們打不開商品頁所以沒寫,購買前請在商品頁確認。
- `content/zh-tw/essentials.md:65` (zh-tw)  
  전: {{aff:klook_esim_alt\|查看含通話簡訊的 SKT eSIM}}  
  후: {{aff:klook_esim_alt\|在 Klook 看更多 SKT eSIM 方案}}
- `content/zh-tw/essentials.md:116` (zh-tw)  
  전: \| Kakao Map \| 路線查詢 \| 拿來交叉比對;操作最接近 Google Maps \|  
  후: \| Kakao Map \| 路線查詢 \| 和 NAVER 地圖交叉比對 \|
- `content/zh-tw/essentials.md:117` (zh-tw)  
  전: \| Kakao T \| 叫計程車 \| 有英文介面,可用信用卡 \|  
  후: \| Kakao T \| 叫計程車 \| 有韓國門號和韓國信用卡時用。外國卡請用旅客版 k.ride([首爾交通](/zh-tw/getting-around/)) \|

### airport-to-seoul

- `content/ko/airport-to-seoul.md:17` (ko)  
  전: 지하철처럼 자유석. 출퇴근 시간엔 붐벼서 큰 캐리어는 좀 버거워요.  
  후: 지하철처럼 자유석.
- `content/ko/airport-to-seoul.md:19` (ko)  
  전: 직통열차는 긴 비행 뒤에 출퇴근 인파를 피하는 게 아낀 시간보다 더 크게 느껴져요.  
  후: (삭제)
- `content/ko/airport-to-seoul.md:99` (ko)  
  전: 문이 안 열리면 카드 잔액이 모자란 경우가 많아요. 위 3단계처럼  
  후: 문이 안 열리면 단말기에 뜬 잔액을 보고, 모자라면 위 3단계처럼
- `content/ko/airport-to-seoul.md:236` (ko)  
  전: 10분만 준비하면 첫 1시간이 편해요.  
  후: 세 가지만 정해 두세요.
- `content/en/airport-to-seoul.md:17` (en)  
  전: Unreserved seats, like the subway. Fills with commuters at rush hour, so a big suitcase is harder.  
  후: Unreserved seats, like the subway.
- `content/en/airport-to-seoul.md:19` (en)  
  전: The Express skips the commuter crowd, which after a long flight matters more than the minutes saved.  
  후: (삭제)
- `content/en/airport-to-seoul.md:99` (en)  
  전: If it stays shut, the balance is usually too low: top up at a machine as in step 3 and tap again.  
  후: If it stays shut, check the balance on the reader; if it is too low, top up at a machine as in step 3 and tap again.
- `content/en/airport-to-seoul.md:236` (en)  
  전: Ten minutes of planning makes the first hour easy.  
  후: Settle three things.
- `content/ja/airport-to-seoul.md:17` (ja)  
  전: 地下鉄と同じ自由席。朝夕のラッシュは混み、大きなスーツケースだと少し大変かも。  
  후: 地下鉄と同じ自由席。
- `content/ja/airport-to-seoul.md:19` (ja)  
  전: 直通列車は、通勤ラッシュに巻き込まれないのが、長いフライトの後には時間以上にありがたいところ。  
  후: (삭제)
- `content/ja/airport-to-seoul.md:99` (ja)  
  전: 開かないときは残高不足のことが多いです。上の3番のように  
  후: 開かないときは読み取り機に出た残高を見て、足りなければ上の3番のように
- `content/ja/airport-to-seoul.md:236` (ja)  
  전: 10分の準備で、最初の1時間が楽になります。  
  후: 3つだけ決めておきましょう。
- `content/zh-tw/airport-to-seoul.md:17` (zh-tw)  
  전: 座位跟地鐵一樣不對號,上下班尖峰很擠,大行李箱會比較辛苦。  
  후: 座位跟地鐵一樣不對號。
- `content/zh-tw/airport-to-seoul.md:19` (zh-tw)  
  전: 直達車不用跟通勤族擠,長途飛行後這點比省下的時間更重要。  
  후: (삭제)
- `content/zh-tw/airport-to-seoul.md:99` (zh-tw)  
  전: 閘門不開多半是餘額不足:像上面第3步那樣  
  후: 閘門不開時先看感應器上的餘額,不夠就像上面第3步那樣
- `content/zh-tw/airport-to-seoul.md:236` (zh-tw)  
  전: 花10分鐘準備,第一個小時就輕鬆了。  
  후: 先決定三件事。

### abroad-esim

- `content/ko/abroad-esim.md:3` (ko)  
  전: 내 폰이 eSIM을 쓸 수 있는지 2분 안에 확인하는 법.  
  후: 내 폰이 eSIM을 쓸 수 있는지 확인하는 법.
- `content/ko/abroad-esim.md:37` (ko)  
  전:  공항에서 QR 코드 찾다가 탑승 안내 방송 듣는 게 제일 흔한 실수라서.  
  후: (삭제)
- `content/en/abroad-esim.md:3` (en)  
  전: and how to check in two minutes whether your phone can take an eSIM.  
  후: and how to check whether your phone can take an eSIM.
- `content/en/abroad-esim.md:37` (en)  
  전:  The most common mistake is hunting for a QR code at the airport while boarding is being called.  
  후: (삭제)
- `content/ja/abroad-esim.md:3` (ja)  
  전: 自分のスマホがeSIMを使えるかを2分で確かめる方法。  
  후: 自分のスマホがeSIMを使えるかを確かめる方法。
- `content/ja/abroad-esim.md:37` (ja)  
  전: 空港でQRコードを探しているうちに搭乗案内が始まる、というのがいちばんよくある失敗です。  
  후: (삭제)
- `content/zh-tw/abroad-esim.md:3` (zh-tw)  
  전: 以及如何在 2 分鐘內確認手機能不能用 eSIM。  
  후: 以及如何確認手機能不能用 eSIM。
- `content/zh-tw/abroad-esim.md:37` (zh-tw)  
  전: 最常見的失誤,是在機場找 QR code 找到廣播登機。  
  후: (삭제)

### getting-around

- `content/ko/getting-around.md:27` (ko)  
  전:  버스에 오른 뒤엔 해결할 방법이 없는 유일한 문제예요.  
  후:  버스에 오른 뒤엔 해결하기 어려워요.
- `content/ko/getting-around.md:82` (ko)  
  전:  2025년 5월엔 1~8호선 첫차·막차를 30분 앞당기겠다고 발표했는데, 실제로 시행됐는지는 확인하지 못했어요. 역마다 다르니 네이버 지도로 확인하세요.  
  후:  지금 시각은 역과 요일마다 다르니 그날 네이버 지도로 확인하세요.
- `content/en/getting-around.md:28` (en)  
  전: it is the one problem you cannot fix once you are on a bus.  
  후: it is hard to sort out once you are on a bus.
- `content/en/getting-around.md:81` (en)  
  전:  In May 2025 it announced moving Lines 1–8 first and last trains 30 minutes earlier; we could not confirm that this has happened. Times also differ by station, so check yours in Naver Map.  
  후:  Today's times differ by station and day, so check yours in Naver Map on the day.
- `content/ja/getting-around.md:28` (ja)  
  전: バスに乗ってからでは解決できない、唯一の問題です。  
  후: バスに乗ってからでは解決しにくいからです。
- `content/ja/getting-around.md:81` (ja)  
  전: 2025年5月には1〜8号線の始発・終電を30分早める方針を発表しましたが、実施されたかは確認できていません。駅によっても違うので、NAVERマップで確かめてください。  
  후: 今の時刻は駅と曜日で違うので、当日NAVERマップで確かめてください。
- `content/zh-tw/getting-around.md:81` (zh-tw)  
  전: 2025年5月又宣布1~8號線首末班車提早30分鐘,但我們無法確認是否已實施。各站時間不同,請用 NAVER 地圖確認。  
  후: 現在的時間各站、各天不同,請當天用 NAVER 地圖確認。

### seoul-subway

- `content/ko/seoul-subway.md:151` (ko)  
  전: \| 주말은 더 일찍 끊기고, 막차 시각이 바뀌었을 수 있어요 \|  
  후: \| 2022년 연장은 평일만이라 주말은 더 일찍 끊겨요 \|
- `content/ko/seoul-subway.md:207` (ko)  
  전: - 2025년 5월 서울시는 1~8호선 첫차·막차를 30분씩 앞당기겠다고(이르면 2025년 8월) 발표했어요. 실제로 시행됐는지는 확인하지 못했어요.⏎  
  후: (삭제)
- `content/en/seoul-subway.md:151` (en)  
  전: \| Weekends stop earlier, and times may have moved \|  
  후: \| The 2022 extension was weekdays only, so weekends stop earlier \|
- `content/en/seoul-subway.md:207` (en)  
  전: - In May 2025 Seoul announced moving Lines 1–8 first and last trains 30 minutes earlier from as early as August 2025. We couldn't confirm whether it happened.⏎  
  후: (삭제)
- `content/ja/seoul-subway.md:151` (ja)  
  전: \| 週末は早く終わり、終電時刻が変わった可能性もあります \|  
  후: \| 2022年の延長は平日だけなので、週末は早く終わります \|
- `content/ja/seoul-subway.md:207` (ja)  
  전: - 2025年5月、ソウル市は1〜8号線の始発と終電をそれぞれ30分早める計画(早ければ2025年8月から)を発表しました。実際に実施されたかは確認できていません。⏎  
  후: (삭제)
- `content/zh-tw/seoul-subway.md:151` (zh-tw)  
  전: \| 週末收班較早,末班時間也可能已調整 \|  
  후: \| 2022年延長只限平日,週末收班較早 \|
- `content/zh-tw/seoul-subway.md:207` (zh-tw)  
  전: - 2025年5月首爾市宣布,1~8號線首班車和末班車各提前30分鐘(最快2025年8月起)。是否已經實施,我們沒能確認。⏎  
  후: (삭제)

### ktx-busan

- `content/ko/ktx-busan.md:45` (ko)  
  전: 지금도 비슷하다고 보면 되고, 정확한 시간은 예매할 때 확인하세요.  
  후: 그래서 지금도 비슷할 것으로 예상해요. 정확한 시간은 예매할 때 확인하세요.
- `content/ko/ktx-busan.md:82` (ko)  
  전:  부산시는 부산역 유라시아플랫폼에 무인 짐 보관소를 만든다고 했지만 시기는 밝히지 않았어요.  
  후: (삭제)
- `content/en/ktx-busan.md:46` (en)  
  전: so expect about the same today.  
  후: so we expect about the same today.
- `content/en/ktx-busan.md:83` (en)  
  전:  The city says it is adding self-service storage at the station's Eurasia Platform but gave no date.  
  후: (삭제)
- `content/ja/ktx-busan.md:38` (ja)  
  전: 148駅に海外のクレジットカードが使える新しい券売機が入り、日本語表示にも対応しています。  
  후: 148駅に海外のクレジットカードが使える新しい券売機が入っています。
- `content/ja/ktx-busan.md:46` (ja)  
  전: 今もほぼ同じと考えてよさそうです。  
  후: 今もほぼ同じと予想しています。
- `content/ja/ktx-busan.md:83` (ja)  
  전: 釜山市は駅のユーラシアプラットフォームに無人の荷物預かりを設けるとしていますが、時期は未定です。  
  후: (삭제)
- `content/zh-tw/ktx-busan.md:46` (zh-tw)  
  전: 所以現在大致一樣。  
  후: 所以我們預估現在大致一樣。
- `content/zh-tw/ktx-busan.md:83` (zh-tw)  
  전: 釜山市說會在車站的歐亞平台設無人行李寄放,但沒公布時間。  
  후: (삭제)

### jeju

- `content/ko/jeju.md:21` (ko)  
  전:  비행은 짧아도 양쪽 공항에서 하루 대부분이 가요.  
  후: (삭제)
- `content/ko/jeju.md:61` (ko)  
  전: \| 풍경은 제일 덜하고 남쪽보다 추워요 \|  
  후: \| 남쪽보다 추워요(기상청 겨울 평균 최고기온) \|
- `content/ko/jeju.md:62` (ko)  
  전: \| 저녁에 할 게 적고, 버스 간격이 30~80분 \|  
  후: \| 201번 버스 간격이 30~80분 \|
- `content/ko/jeju.md:63` (ko)  
  전: \| 공항에서 제일 멀어요 \|  
  후: \| 공항에서 멀어요. 공항 리무진 정류장은 현장에서 확인 \|
- `content/en/jeju.md:22` (en)  
  전:  The flight is short, but airport time on both ends eats most of a day.  
  후: (삭제)
- `content/en/jeju.md:62` (en)  
  전: \| The least scenic, and cooler than the south \|  
  후: \| Cooler than the south (KMA winter average highs) \|
- `content/en/jeju.md:63` (en)  
  전: \| Fewer evening options; buses can be 30–80 minutes apart \|  
  후: \| Bus 201 runs every 30–80 minutes \|
- `content/en/jeju.md:64` (en)  
  전: \| Furthest from the airport \|  
  후: \| Far from the airport; confirm limousine stops on site \|
- `content/ja/jeju.md:22` (ja)  
  전: 両側の空港で一日の大半がなくなります。  
  후: (삭제)
- `content/ja/jeju.md:32` (ja)  
  전: **日本から直行便:** 大韓航空が2026年夏ダイヤ(3月29日〜10月24日)に成田–済州を週4便(月・水・金・日)運航していました。冬ダイヤ以降の運航は今回確認できなかったので、予約前に大韓航空のサイトでご確認ください。⏎⏎  
  후: (삭제)
- `content/ja/jeju.md:64` (ja)  
  전: \| 景色はいちばん地味で、南より寒め \|  
  후: \| 南より寒め(気象庁の冬の平均最高気温) \|
- `content/ja/jeju.md:65` (ja)  
  전: \| 夜の選択肢が少なく、バスは30〜80分間隔 \|  
  후: \| 201番バスは30〜80分間隔 \|
- `content/ja/jeju.md:66` (ja)  
  전: \| 空港からいちばん遠い \|  
  후: \| 空港から遠い。リムジンの乗り場は現地で確認 \|
- `content/ja/jeju.md:89` (ja)  
  전: <a href="https://www.aviationwire.jp/archives/337821" rel="noopener" target="_blank">Aviation Wire、大韓航空の済州–成田線</a>(2026年2月10日)、  
  후: (삭제)
- `content/zh-tw/jeju.md:22` (zh-tw)  
  전: 飛行時間雖短,兩邊機場加起來就去掉大半天。  
  후: (삭제)
- `content/zh-tw/jeju.md:32` (zh-tw)  
  전: **台灣直飛濟州:** 台灣虎航2026年4月促銷時有桃園–濟州航線。班次和冬季是否續飛,我們這次沒能確認,訂票前請看虎航官網。⏎⏎  
  후: (삭제)
- `content/zh-tw/jeju.md:64` (zh-tw)  
  전: \| 風景最普通,比南邊冷 \|  
  후: \| 比南邊冷(氣象廳冬季平均最高氣溫) \|
- `content/zh-tw/jeju.md:65` (zh-tw)  
  전: \| 晚上選擇少,公車30〜80分鐘一班 \|  
  후: \| 201路公車30〜80分鐘一班 \|
- `content/zh-tw/jeju.md:66` (zh-tw)  
  전: \| 離機場最遠 \|  
  후: \| 離機場遠;機場巴士站牌請現場確認 \|
- `content/zh-tw/jeju.md:89` (zh-tw)  
  전: <a href="https://www.ctee.com.tw/news/20260410701162-430201" rel="noopener" target="_blank">工商時報,台灣虎航促銷含桃園–濟州</a>(2026年4月10日);  
  후: (삭제)

### olive-young

- `content/ko/olive-young.md:43` (ko)  
  전: 세일 주간엔 작은 지점이 더 한산할 수 있어요. 큰 매장은  
  후: 큰 매장은
- `content/en/olive-young.md:43` (en)  
  전: In sale week, smaller branches can be calmer. The big stores  
  후: The big stores
- `content/ja/olive-young.md:43` (ja)  
  전: セール週は小さな支店のほうが空いていることも。大型店は  
  후: 大型店は
- `content/zh-tw/olive-young.md:43` (zh-tw)  
  전: 特賣週時,小分店可能比較好逛。大型店  
  후: 大型店

### daiso

- `content/ko/daiso.md:36` (ko)  
  전:  버스 기다리는 시간에 들르기 좋지만 통로가 미로 같아서 시간을 꼭 확인하세요.  
  후:  버스를 기다리는 동안 들를 수 있어요. 출발 시간을 꼭 확인하세요.
- `content/en/daiso.md:36` (en)  
  전:  Handy while you wait for a bus, but the aisles are a maze, so watch the time.  
  후:  You can drop in while you wait for a bus; keep an eye on your departure time.
- `content/ja/daiso.md:36` (ja)  
  전: バスの待ち時間に寄れますが、通路が迷路のようなので時間に注意。  
  후: バスの待ち時間に寄れます。出発時刻には注意を。
- `content/zh-tw/daiso.md:36` (zh-tw)  
  전: 等車時可以逛,但走道像迷宮,注意時間。  
  후: 等車時可以逛,注意發車時間。

### convenience-store

- `content/ko/convenience-store.md:25` (ko)  
  전:  나머지 다섯 곳 중 한 곳은 밤에 문을 닫거나 무인으로 바뀌어요.  
  후:  나머지 약 22%, 다섯 곳 중 한 곳꼴은 24시간 점포가 아니에요.
- `content/en/convenience-store.md:25` (en)  
  전:  The other one in five closes at night, and some become unstaffed after hours.  
  후:  The other one in five is not a 24-hour store.
- `content/ja/convenience-store.md:25` (ja)  
  전: 残りの5軒に1軒は夜に閉まるか無人になります。  
  후: 残りの5軒に1軒ほどは24時間営業ではありません。
- `content/zh-tw/convenience-store.md:25` (zh-tw)  
  전: 剩下每五家就有一家晚上關門或轉為無人店。  
  후: 剩下大約每五家就有一家不是 24 小時店。

### kbeauty-how-to-choose

- `content/ko/kbeauty-how-to-choose.md:57` (ko)  
  전:  50을 넘으면 실제 차이가 크지 않아서 이렇게 묶어 표시해요.  
  후:  50을 넘는 숫자는 따로 적지 않아요(식약처 고시).
- `content/en/kbeauty-how-to-choose.md:57` (en)  
  전:  Above 50 the real difference is small, which is why it is grouped.  
  후:  Numbers above 50 are not printed separately (MFDS notice).
- `content/ja/kbeauty-how-to-choose.md:57` (ja)  
  전: 50を超えると実際の差は大きくないので、まとめて表示します。  
  후: 50を超える数字は個別に書きません(食薬処の告示)。
- `content/zh-tw/kbeauty-how-to-choose.md:57` (zh-tw)  
  전: 超過 50 實際差別不大,所以統一標示。  
  후: 超過 50 的數字不另外標(食藥處告示)。

### shopping-streets

- `content/ko/shopping-streets.md:19` (ko)  
  전:  문 연 직후가 좋다고 봐요.  
  후: (삭제)
- `content/ko/shopping-streets.md:53` (ko)  
  전: - **가기 좋은 시간:** 문 연 직후. 혼잡 자료가 아니라 저희 추측이에요.⏎  
  후: (삭제)
- `content/en/shopping-streets.md:19` (en)  
  전:  Our call: go right after opening.  
  후: (삭제)
- `content/en/shopping-streets.md:53` (en)  
  전: - **Best time:** right after opening. That is our guess, not crowd data.⏎  
  후: (삭제)
- `content/ja/shopping-streets.md:19` (ja)  
  전: 開店直後がいいと私たちは考えます。  
  후: (삭제)
- `content/ja/shopping-streets.md:53` (ja)  
  전: - **行くのにいい時間:** 開店直後。混雑データではなく私たちの推測です。⏎  
  후: (삭제)
- `content/zh-tw/shopping-streets.md:19` (zh-tw)  
  전: 我們認為剛開門時最好。  
  후: (삭제)
- `content/zh-tw/shopping-streets.md:53` (zh-tw)  
  전: - **適合的時間:** 剛開門。這是我們的推測,不是人潮資料。⏎  
  후: (삭제)

### shopping-streets-1

- `static/fig/ko/shopping-streets-1.svg:9` (ko)  
  전: >이른 시간<  
  후: >—<
- `static/fig/en/shopping-streets-1.svg:9` (en)  
  전: >Earlier in the day<  
  후: >—<
- `static/fig/ja/shopping-streets-1.svg:9` (ja)  
  전: >早めの時間<  
  후: >—<
- `static/fig/zh-tw/shopping-streets-1.svg:9` (zh-tw)  
  전: >早點去<  
  후: >—<

### emergency

- `content/ko/emergency.md:4` (ko)  
  전:  번호 세 개를 저장하고 이 페이지를 열어 두면, 대부분의 나쁜 순간은 사고가 아니라 잠깐의 지연으로 끝나요.  
  후:  출발 전에 번호 세 개를 저장하고 이 페이지를 열어 두세요.
- `content/ko/emergency.md:25` (ko)  
  전: **떠나기 전에 (5분):**  
  후: **떠나기 전에:**
- `content/ko/emergency.md:53` (ko)  
  전: 대개 가장 잘 해결되는 일이에요.   
  후: (삭제)
- `content/ko/emergency.md:89` (ko)  
  전: 외국 정부들이 가장 많이 경고하는 위험이에요.  
  후: 미국·캐나다 정부의 여행 안내가 경고하는 위험이에요.
- `content/ko/emergency.md:97` (ko)  
  전: 대개 한국 문제가 아니라 해외 카드사가 막은 거예요. 카드 뒷면의  
  후: 카드를 발급한 해외 카드사가 거래를 막았을 수 있어요. 카드 뒷면의
- `content/ko/emergency.md:116` (ko)  
  전: 대부분은 이 페이지를 한 번도 안 쓰고 끝나요. 위의 5분은, 혹시 쓰게 될 때 고민하지 않기 위해서예요.  
  후: 위의 준비는, 혹시 이 페이지를 쓰게 될 때 고민하지 않기 위해서예요.
- `content/en/emergency.md:4` (en)  
  전:  Save three numbers, keep this page open, and most bad moments become a delay rather than a disaster.  
  후:  Before you go, save three numbers and keep this page open.
- `content/en/emergency.md:24` (en)  
  전: **Before you go (five minutes):**  
  후: **Before you go:**
- `content/en/emergency.md:52` (en)  
  전: Usually the most fixable one.   
  후: (삭제)
- `content/en/emergency.md:88` (en)  
  전: is the risk foreign governments warn about most.  
  후: is a risk the US and Canadian travel advisories warn about.
- `content/en/emergency.md:96` (en)  
  전: That is usually a block from your bank abroad, not a problem in Korea. Call your bank's  
  후: Your card issuer at home may have blocked the payment. Call your bank's
- `content/en/emergency.md:115` (en)  
  전: Most people never use this page. The five minutes above are so you don't have to think if you do.  
  후: The prep above is so you don't have to think if you ever need this page.
- `content/ja/emergency.md:4` (ja)  
  전: 番号を3つ保存して、このページを開いておけば、たいていのピンチは「大事件」ではなく「少しの遅れ」で済みます。  
  후: 出発前に番号を3つ保存して、このページを開いておきましょう。
- `content/ja/emergency.md:24` (ja)  
  전: **出発前に(5分):**  
  후: **出発前に:**
- `content/ja/emergency.md:52` (ja)  
  전: たいてい一番取り戻しやすいトラブルです。  
  후: (삭제)
- `content/ja/emergency.md:88` (ja)  
  전: 各国政府がいちばん注意を呼びかけているリスクです。  
  후: 米国・カナダ政府の渡航情報が注意を呼びかけているリスクです。
- `content/ja/emergency.md:96` (ja)  
  전: たいていは韓国側ではなく、日本のカード会社による利用制限です。  
  후: 日本のカード会社が利用を止めている可能性があります。
- `content/ja/emergency.md:115` (ja)  
  전: ほとんどの人は、このページを一度も使わずに旅を終えます。上の5分は、もし使うことになったとき迷わないためのものです。  
  후: 上の準備は、もしこのページを使うことになったとき迷わないためのものです。
- `content/zh-tw/emergency.md:4` (zh-tw)  
  전: 存好三個號碼、把這頁開著,大部分的倒楣時刻只會變成「耽擱一下」,不會變成「出大事」。  
  후: 出發前存好三個號碼,把這頁開著。
- `content/zh-tw/emergency.md:24` (zh-tw)  
  전: **出發前(5 分鐘):**  
  후: **出發前:**
- `content/zh-tw/emergency.md:52` (zh-tw)  
  전: 通常最容易找回。  
  후: (삭제)
- `content/zh-tw/emergency.md:88` (zh-tw)  
  전: 是各國政府最常提醒的風險。  
  후: 是美國、加拿大政府旅遊資訊提醒的風險。
- `content/zh-tw/emergency.md:96` (zh-tw)  
  전: 通常不是韓國的問題,而是台灣發卡銀行擋下的。  
  후: 可能是台灣的發卡銀行擋下了交易。
- `content/zh-tw/emergency.md:115` (zh-tw)  
  전: 大多數人一次都用不到這頁。上面那 5 分鐘,是為了萬一用到時不必多想。  
  후: 上面的準備,是為了萬一用到這頁時不必多想。

### everyday

- `content/ko/everyday.md:35` (ko)  
  전:  고깃집이나 전골집에서 혼자 온 손님에게 2인분 주문을 요구한다는 여행자 경험담이 많아요.  
  후:  고깃집이나 전골집에는 혼자 온 손님에게 2인분 주문을 요구하는 곳이 있어요.
- `content/ko/everyday.md:51` (ko)  
  전:  호텔과 공항에서는 대체로 통하지만 택시나 작은 식당에서는 어려울 때가 많아요. 영국 정부도  
  후:  영국 정부는
- `content/ko/everyday.md:68` (ko)  
  전: 치안이 좋다 보니 오히려 긴장이 풀리기 쉬워요. 진짜 조심할 건 그 정도예요.⏎  
  후: (삭제)
- `content/en/everyday.md:34` (en)  
  전:  Some restaurants ask solo diners to order two servings, and travellers commonly run into this at grill-your-own BBQ and hot-pot places.  
  후:  Some grill-your-own BBQ and hot-pot places ask solo diners to order two servings.
- `content/en/everyday.md:50` (en)  
  전:  In practice: hotel and airport staff usually manage, while taxi drivers and small restaurant owners often do not.  
  후: (삭제)
- `content/en/everyday.md:69` (en)  
  전: Feeling safe is not the same as being safe late at night, and the low crime rate can make people drop their guard. That is the only real warning.⏎  
  후: (삭제)
- `content/ja/everyday.md:34` (ja)  
  전: 焼肉や鍋の店では、ひとり客に2人前の注文を求める店があると多くの旅行者が報告しています。  
  후: 焼肉や鍋の店には、ひとり客に2人前の注文を求める店があります。
- `content/ja/everyday.md:50` (ja)  
  전: ホテルや空港ではたいてい対応してもらえますが、タクシーや小さな食堂では韓国語だけということもよくあります。英国政府も  
  후: 英国政府は
- `content/ja/everyday.md:67` (ja)  
  전: 治安が良いぶん、つい気が緩むこと。注意すべきなのは、ほぼそれだけです。⏎  
  후: (삭제)
- `content/zh-tw/everyday.md:34` (zh-tw)  
  전: 很多旅客反映,烤肉和火鍋店會要求一人客點 2 人份。  
  후: 有些烤肉和火鍋店會要求一人客點 2 人份。
- `content/zh-tw/everyday.md:50` (zh-tw)  
  전: 飯店和機場通常可以用英文溝通,但計程車和小餐館常常只有韓文。英國政府也提醒  
  후: 英國政府提醒
- `content/zh-tw/everyday.md:67` (zh-tw)  
  전: 因為治安好,反而容易鬆懈。真正要注意的大概就這一點。⏎  
  후: (삭제)

### food

- `content/ko/food.md:21` (ko)  
  전:  테이블에서 굽는 고기는 2인분부터인 곳이 많아요 \|  
  후:  테이블에서 굽는 고기는 2인분부터 받는 곳이 있어요 \|
- `content/ko/food.md:61` (ko)  
  전: 배민(배달의민족)은 2026년에 외국인 이용이 가장 크게 바뀐 배달 앱이에요.  
  후: 배민(배달의민족)은 2026년에 외국인이 쓰기 쉽게 세 가지가 바뀌었어요.
- `content/en/food.md:22` (en)  
  전:  Meat grilled at the table is often sold two servings minimum \|  
  후:  Some places sell table-grilled meat two servings minimum \|
- `content/en/food.md:62` (en)  
  전: Baemin (Baedal Minjok) is the delivery app that changed most for visitors in 2026:  
  후: Baemin (Baedal Minjok) made three changes in 2026 that help visitors:
- `content/ja/food.md:22` (ja)  
  전:  テーブルで焼く肉は2人前からの店が多いです \|  
  후:  テーブルで焼く肉は2人前からの店があります \|
- `content/ja/food.md:62` (ja)  
  전: 배민(ペダルの民族)は2026年に旅行者向けがいちばん変わった配達アプリです。  
  후: 배민(ペダルの民族)は2026年、旅行者が使いやすくなる変更が3つありました。
- `content/zh-tw/food.md:22` (zh-tw)  
  전: \| 桌邊烤肉常常兩人份起跳 \|  
  후: \| 有些店桌邊烤肉兩人份起跳 \|
- `content/zh-tw/food.md:62` (zh-tw)  
  전: 배민(外賣民族)是 2026 年對外國旅客改變最多的外送 App:  
  후: 배민(外賣民族)2026 年有三項改變,讓外國旅客更好用:

### health

- `content/ko/health.md:4` (ko)  
  전: lede: 여행 중 생기는 병은 대부분 약국, 24시간 편의점, 동네 의원 순서로 해결돼요.  
  후: lede: 여행 중 가벼운 증상이라면 약국, 24시간 편의점, 동네 의원 순서로 찾아가요.
- `content/ko/health.md:62` (ko)  
  전: 대부분 저녁이면 닫아요. 문 연 곳을 찾는 방법:  
  후: 밤이나 휴일에 문 연 곳을 찾는 방법:
- `content/en/health.md:4` (en)  
  전: lede: Most travel illnesses in Korea are solved at a pharmacy, a 24-hour convenience store or a small neighborhood clinic, in that order.  
  후: lede: For minor illness on the road, go to a pharmacy, a 24-hour convenience store or a small neighborhood clinic, in that order.
- `content/en/health.md:63` (en)  
  전: Most close in the evening. To find one that is open:  
  후: To find one open at night or on a holiday:
- `content/ja/health.md:4` (ja)  
  전: lede: 旅先の体調不良は、たいてい薬局、24時間コンビニ、街のクリニックの順で片づきます。  
  후: lede: 旅先の軽い体調不良なら、薬局、24時間コンビニ、街のクリニックの順に頼ります。
- `content/ja/health.md:63` (ja)  
  전: 多くは夕方に閉まります。開いている薬局の探し方:  
  후: 夜や休日に開いている薬局の探し方:
- `content/zh-tw/health.md:4` (zh-tw)  
  전: lede: 旅途中的小病,大多照藥局、24 小時便利商店、巷口診所的順序就能解決。  
  후: lede: 旅途中的小病,依序找藥局、24 小時便利商店、巷口診所。
- `content/zh-tw/health.md:63` (zh-tw)  
  전: 大多傍晚就關。找有開的藥局:  
  후: 晚上或假日找有開的藥局:

### money

- `content/ko/money.md:18` (ko)  
  전:  한 장이 거절돼도 다른 한 장으로 되는 경우가 많아요.  
  후:  한 장이 거절되면 다른 브랜드 카드로 다시 시도할 수 있어요.
- `content/en/money.md:18` (en)  
  전:  When one is turned down, the other often goes through.  
  후:  If one is turned down, you can try the other brand.
- `content/ja/money.md:32` (ja)  
  전: 1枚が通らなくても、もう1枚で済むことが多いからです。  
  후: 1枚が通らないとき、別のブランドで試せるからです。
- `content/zh-tw/money.md:20` (zh-tw)  
  전: 依下面查證過的事實拼出的畫面,不是編出來的心得。  
  후: (삭제)
- `content/zh-tw/money.md:60` (zh-tw)  
  전: 一張被拒時,另一張常常就能過。  
  후: 一張被拒時,可以改用另一個卡組織的卡試試。

### concert-trip

- `content/ko/concert-trip.md:72` (ko)  
  전:  6만 6천 석이 넘지만 잔디 보호 때문에 그라운드석은 보통 팔지 않아요.  
  후: (삭제)
- `content/en/concert-trip.md:71` (en)  
  전:  More than 66,000 seats, but ground-level tickets are usually not sold, to protect the pitch.  
  후: (삭제)
- `content/ja/concert-trip.md:71` (ja)  
  전:  6万6千席以上ありますが、芝を守るためグラウンド席は通常販売されません。  
  후: (삭제)
- `content/zh-tw/concert-trip.md:71` (zh-tw)  
  전:  超過66,000席,但為了保護草皮,搖滾區(場地區)通常不開賣。  
  후: (삭제)

### palaces

- `content/ko/palaces.md:61` (ko)  
  전:  공식 누리집을 열어 지금 시행 중인지 확인하지 못했으니 [royal.khs.go.kr](https://royal.khs.go.kr)에서 확인하세요.  
  후:  발표대로라면 지금 시행 중일 것으로 예상해요(근거: 세계일보 2026년 5월 27일 보도). 공식 누리집에서는 확인하지 못했으니 가기 전에 [royal.khs.go.kr](https://royal.khs.go.kr)에서 확인하세요.
- `content/ko/palaces.md:69` (ko)  
  전:  아끼는 돈은 1,000~3,000원뿐이고, 입고 반납하는 데 시간이 들고, 긴 치마로 자갈길을 하루 종일 걷기는 힘들어요.  
  후:  아끼는 돈은 1,000~3,000원뿐이고, 입고 반납하는 데 시간이 들어요.
- `content/ko/palaces.md:69` (ko)  
  전:  11~1월엔 고름을 채운 채로 추워요.  
  후: (삭제)
- `content/en/palaces.md:61` (en)  
  전:  We could not confirm on the official site that it is running; check [royal.khs.go.kr](https://royal.khs.go.kr) first.  
  후:  If it went ahead as announced, it should be running now; that is our expectation, based on Segye Ilbo's report of 27 May 2026. We could not confirm it on the official site, so check [royal.khs.go.kr](https://royal.khs.go.kr) first.
- `content/en/palaces.md:69` (en)  
  전:  The saving is only 1,000–3,000 won, fitting and returning take time, long skirts on gravel tire you, and in winter you will be cold.  
  후:  The saving is only 1,000–3,000 won, and fitting and returning take time.
- `content/ja/palaces.md:61` (ja)  
  전: 公式サイトで実施中かを確認できなかったので、[royal.khs.go.kr](https://royal.khs.go.kr)で確かめてください。  
  후: 発表どおりなら実施中と予想しています(根拠:世界日報 2026年5月27日の報道)。公式サイトでは確認できなかったので、[royal.khs.go.kr](https://royal.khs.go.kr)で確かめてください。
- `content/ja/palaces.md:69` (ja)  
  전: 浮くのは1,000〜3,000ウォンだけで、着付けと返却に時間がかかり、長いスカートで砂利道を一日歩くのは疲れます。  
  후: 浮くのは1,000〜3,000ウォンだけで、着付けと返却に時間がかかります。
- `content/ja/palaces.md:69` (ja)  
  전: 11〜1月はひもを留めたままでは寒いです。  
  후: (삭제)
- `content/zh-tw/palaces.md:61` (zh-tw)  
  전: 我們無法打開官網確認是否已實施,出發前請到 [royal.khs.go.kr](https://royal.khs.go.kr) 確認。  
  후: 照發布內容,現在應已實施,這是我們的預估(根據:世界日報 2026 年 5 月 27 日報導)。我們無法打開官網確認,出發前請到 [royal.khs.go.kr](https://royal.khs.go.kr) 確認。
- `content/zh-tw/palaces.md:69` (zh-tw)  
  전: 省下的門票只有 1,000~3,000 韓元,換裝和歸還要花時間,穿長裙在碎石路走一整天很累,11~1 月繫好帶子也還是冷。  
  후: 省下的門票只有 1,000~3,000 韓元,換裝和歸還要花時間。

### seoul-areas

- `content/ko/seoul-areas.md:37` (ko)  
  전: 관광객 중심 동네예요. 큰길은 가게가 닫을 때까지 붐벼요.  
  후: 관광객 중심 동네예요.
- `content/ko/seoul-areas.md:45` (ko)  
  전: 저녁 산책할 거리가 적고, 출구를 잘못 나가면 시간이 많이 들어요.  
  후: 출구를 잘못 나가면 시간이 들어요.
- `content/ko/seoul-areas.md:52` (ko)  
  전: 주말 밤엔 시끄러워요. 잠귀가 밝다면  
  후: 밤늦게까지 사람이 모이는 거리예요(위 핼러윈 추산 참고). 잠귀가 밝다면
- `content/ko/seoul-areas.md:66` (ko)  
  전: 자려는 시간에 가장 활기차고, 아침엔 할 게 적어요.  
  후: 밤에 활기찬 동네예요(코리아타임스 '24시간 패션 중심지'). 잠귀가 밝다면 숙소 위치를 확인하세요.
- `content/ko/seoul-areas.md:90` (ko)  
  전:  좋은 동네지만 들어오는 질문은 위 일곱 곳에 몰려 있어요.  
  후:  좋은 동네지만 이 페이지는 위 일곱 곳만 다뤄요.
- `content/en/seoul-areas.md:37` (en)  
  전: it is built around visitors. The main streets stay crowded until the shops close.  
  후: it is built around visitors.
- `content/en/seoul-areas.md:45` (en)  
  전: few streets for an evening walk, and the wrong exit costs time.  
  후: the wrong exit costs time.
- `content/en/seoul-areas.md:52` (en)  
  전: weekend nights are loud. Light sleepers  
  후: it draws crowds late into the night (see the Halloween estimate above). Light sleepers
- `content/en/seoul-areas.md:66` (en)  
  전: it is liveliest when you want to sleep, and quiet in the morning.  
  후: it is busiest at night (the Korea Times calls it a '24-hour fashion hub'). Light sleepers should check where the hotel sits.
- `content/en/seoul-areas.md:90` (en)  
  전: They're fine, but the questions we see are about the seven above.  
  후: They're fine, but this page covers only the seven above.
- `content/ja/seoul-areas.md:37` (ja)  
  전: 旅行者向けの街です。大通りは閉店まで混んでいます。  
  후: 旅行者向けの街です。
- `content/ja/seoul-areas.md:45` (ja)  
  전: 夜に散歩する通りが少なく、出口を間違えると時間がかかります。  
  후: 出口を間違えると時間がかかります。
- `content/ja/seoul-areas.md:52` (ja)  
  전: 週末の夜はにぎやかです。音が気になる方は  
  후: 夜遅くまで人が集まる街です(上のハロウィーンの推計を参照)。音が気になる方は
- `content/ja/seoul-areas.md:66` (ja)  
  전: 寝たい時間にいちばんにぎやかで、朝はすることが少なめ。  
  후: 夜ににぎわう街です(コリアタイムズは「24時間のファッション拠点」と表現)。音が気になる方はホテルの場所を確認を。
- `content/ja/seoul-areas.md:90` (ja)  
  전: いい街ですが、寄せられる質問は上の7つに集中しています。  
  후: いい街ですが、このページは上の7つだけを扱います。
- `content/zh-tw/seoul-areas.md:32` (zh-tw)  
  전: 台灣旅客最常問的就是這題。數字先放前面:  
  후: 數字先放前面:
- `content/zh-tw/seoul-areas.md:39` (zh-tw)  
  전: \| 缺點 \| 觀光客多,大街到打烊前都很擠 \| 週末晚上很吵 \|  
  후: \| 缺點 \| 觀光客多 \| 夜裡人潮多 \|
- `content/zh-tw/seoul-areas.md:50` (zh-tw)  
  전: 這區是為觀光客打造的,大街到店家打烊都很擠。  
  후: 這區是為觀光客打造的。
- `content/zh-tw/seoul-areas.md:58` (zh-tw)  
  전: 晚上能散步的街少,出口走錯很花時間。  
  후: 出口走錯會花時間。
- `content/zh-tw/seoul-areas.md:65` (zh-tw)  
  전: 週末晚上很吵,淺眠的人  
  후: 夜裡人潮聚集到很晚(見上面萬聖節的推估),淺眠的人
- `content/zh-tw/seoul-areas.md:79` (zh-tw)  
  전: 你想睡的時候最熱鬧,早上沒什麼事做。  
  후: 晚上最熱鬧(韓國時報稱它為「24 小時時尚中心」),淺眠的人先確認飯店位置。
- `content/zh-tw/seoul-areas.md:103` (zh-tw)  
  전: 都不錯,但我們收到的問題集中在上面七區。  
  후: 都不錯,但這頁只談上面七區。

### winter

- `content/ko/winter.md:4` (ko)  
  전: lede: 1월 서울은 생각보다 춥지만, 맑고 건조한 추위라 옷만 잘 챙기면 충분히 다닐 만해요.  
  후: lede: 1월 서울은 아침 최저기온이 평균 −5.5°C예요. 옷을 제대로 챙기면 다닐 수 있어요.
- `content/ko/winter.md:18` (ko)  
  전: \| 어디서나 팔고, 주머니에 넣으면 하루 종일 버텨요 \|  
  후: \| 편의점에서 겨울 내내 팔아요 \|
- `content/ko/winter.md:19` (ko)  
  전: \| 실내는 난방이 세서 두꺼운 옷 한 벌이면 금방 더워요 \|  
  후: \| 실내는 난방이 돼서, 겹옷이면 들어가서 벗기 쉬워요 \|
- `content/ko/winter.md:34` (ko)  
  전: 12월과 2월은 조금 덜하지만, 한강 바람과 빌딩 사이 바람 때문에 세 달 모두 숫자보다 춥게 느껴져요.  
  후: 바람이 불면 체감온도가 기온보다 훨씬 낮아져요(위 2025년 12월 26일: 기온 −11.8°C, 체감 −18.6°C).
- `content/ko/winter.md:38` (ko)  
  전: 이고, 그중 상당수는 잠깐 날리는 정도예요.  
  후: 이에요.
- `content/ko/winter.md:46` (ko)  
  전:  추위의 대부분을 이게 막아 줘요.  
  후: (삭제)
- `content/ko/winter.md:48` (ko)  
  전:  −5°C를 견디기 힘들게 만드는 건 귀와 손에 닿는 바람이에요.  
  후: (삭제)
- `content/ko/winter.md:56` (ko)  
  전: 11월 말이나 3월 초에 온다면 가벼운 코트와 겹옷이면 대개 충분해요. 평범한 겨울이라면 시내에서 방한 부츠까지는 필요 없고, 미끄럽지 않은 신발이면 돼요.  
  후: 11월 말이나 3월 초에 온다면 그때 기온을 기상청 예보로 먼저 확인하세요. 신발은 미끄럽지 않은 것이면 돼요.
- `content/ko/winter.md:60` (ko)  
  전: 많은 사람이 고향에 가기 때문에 서울 시내는 한산해지고, 기차와 고속도로는 붐벼요.  
  후: 많은 사람이 고향에 가서 기차가 붐벼요(아래 2026년 예매율).
- `content/ko/winter.md:90` (ko)  
  전:  지난해에는 행사에 맞춰 지하철·버스 막차를 연장했어요.  
  후: (삭제)
- `content/en/winter.md:4` (en)  
  전: lede: Seoul in January is colder than most visitors expect, but it is a dry, bright cold you can dress for.  
  후: lede: A January morning in Seoul averages −5.5°C. Dress for it properly and you can get around.
- `content/en/winter.md:18` (en)  
  전: \| Cheap, everywhere, and they work in a coat pocket all day \|  
  후: \| Convenience stores stock them all winter \|
- `content/en/winter.md:19` (en)  
  전: \| Indoors is heated, and you will overheat in a ski-weight outfit \|  
  후: \| Indoors is heated, so layers are easier to take off \|
- `content/en/winter.md:34` (en)  
  전: December and February are a little milder, but the wind along the Han River and between tall buildings makes any of the three feel colder than the number.  
  후: When the wind blows, the wind chill can be far below the temperature (26 December 2025 above: −11.8°C, feeling like −18.6°C).
- `content/en/winter.md:38` (en)  
  전:  Many of those are light flurries.  
  후: (삭제)
- `content/en/winter.md:46` (en)  
  전:  This does most of the work.  
  후: (삭제)
- `content/en/winter.md:48` (en)  
  전:  Wind on your ears and hands is what makes −5°C miserable.  
  후: (삭제)
- `content/en/winter.md:56` (en)  
  전: if you are coming in late November or early March, a lighter coat plus layers is usually enough. Snow boots are not needed for the city in a normal winter. Shoes with a decent grip are.  
  후: if you are coming in late November or early March, check the weather agency forecast for those dates first. Shoes with a decent grip are enough.
- `content/en/winter.md:60` (en)  
  전: Many Koreans travel to see family, so Seoul's own streets go quiet while trains and highways fill up.  
  후: Many Koreans travel to see family, so trains fill up (see the 2026 booking figures below).
- `content/en/winter.md:90` (en)  
  전:  Last year the city ran later trains and buses for the event.  
  후: (삭제)
- `content/ja/winter.md:4` (ja)  
  전: lede: 1月のソウルは思っている以上に寒いですが、晴れて乾いた寒さなので、服装さえ合わせれば十分に歩けます。  
  후: lede: 1月のソウルの朝の最低気温は平均−5.5°C。服装をしっかり合わせれば歩けます。
- `content/ja/winter.md:18` (ja)  
  전: \| どこでも売っていて、ポケットに入れておけば一日もちます \|  
  후: \| コンビニで冬の間ずっと売っています \|
- `content/ja/winter.md:19` (ja)  
  전: \| 室内は暖房がしっかり効いていて、厚着だとすぐ暑くなります \|  
  후: \| 室内は暖房があるので、重ね着なら入ってから脱ぎやすい \|
- `content/ja/winter.md:34` (ja)  
  전: 12月と2月は少しやわらぎますが、漢江沿いやビルの間を吹く風があるので、どの月も数字より寒く感じます。  
  후: 風があると体感温度は気温よりかなり低くなります(上の2025年12月26日:気温−11.8°C、体感−18.6°C)。
- `content/ja/winter.md:40` (ja)  
  전: 寒さのほとんどをこれが防ぎます。  
  후: (삭제)
- `content/ja/winter.md:42` (ja)  
  전: −5°Cをつらくするのは、耳と手に当たる風です。  
  후: (삭제)
- `content/ja/winter.md:46` (ja)  
  전: 日本から持って行っても、現地で買っても大丈夫です。  
  후: (삭제)
- `content/ja/winter.md:50` (ja)  
  전: 11月下旬や3月上旬なら、軽めのコートと重ね着でたいてい足ります。普通の冬なら、街中でスノーブーツまでは必要ありません。滑りにくい靴があれば十分です。  
  후: 11月下旬や3月上旬なら、その時期の気温を気象庁の予報で先に確認してください。靴は滑りにくいものなら十分です。
- `content/ja/winter.md:54` (ja)  
  전: その多くはちらつく程度です。  
  후: (삭제)
- `content/ja/winter.md:60` (ja)  
  전: 多くの人が帰省するので、ソウル市内は静かになり、鉄道や高速道路は混みます。  
  후: 多くの人が帰省するので、鉄道は混みます(下の2026年の予約率を参照)。
- `content/ja/winter.md:90` (ja)  
  전: 昨年は行事に合わせて地下鉄・バスの終電を延長しました。  
  후: (삭제)
- `content/zh-tw/winter.md:4` (zh-tw)  
  전: lede: 1 月的首爾平均最低溫 −5.5°C,對從台灣出發的人來說是真的冷,但多半是晴朗乾冷,穿對就能整天走。  
  후: lede: 1 月的首爾早上平均最低溫 −5.5°C,衣服穿對就能出門走。
- `content/zh-tw/winter.md:18` (zh-tw)  
  전: \| 到處都買得到,放口袋撐一整天 \|  
  후: \| 便利商店整個冬天都有賣 \|
- `content/zh-tw/winter.md:19` (zh-tw)  
  전: \| 室內暖氣很強,穿太厚一進門就熱 \|  
  후: \| 室內有暖氣,洋蔥式穿法進門好脫 \|
- `content/zh-tw/winter.md:34` (zh-tw)  
  전: 12 月和 2 月稍微好一點,但漢江邊和大樓之間的風很大,三個月都比數字感覺更冷。  
  후: 有風時體感溫度會比氣溫低很多(上面 2025 年 12 月 26 日:氣溫 −11.8°C,體感 −18.6°C)。
- `content/zh-tw/winter.md:38` (zh-tw)  
  전: ,其中很多只是飄一下  
  후: (삭제)
- `content/zh-tw/winter.md:46` (zh-tw)  
  전:  大部分的冷都靠它擋。台灣冬天穿的外套通常不夠,這件值得另外準備。  
  후: (삭제)
- `content/zh-tw/winter.md:48` (zh-tw)  
  전:  −5°C 難受的是吹在耳朵和手上的風。  
  후: (삭제)
- `content/zh-tw/winter.md:56` (zh-tw)  
  전: 11 月底或 3 月初去,一件輕外套加上多層次通常就夠。一般冬天在市區不需要雪靴,穿止滑的鞋就好。  
  후: 11 月底或 3 月初去,先用氣象廳預報確認當時氣溫。鞋子穿止滑的就好。
- `content/zh-tw/winter.md:60` (zh-tw)  
  전: 很多韓國人回老家,首爾市區會變安靜,火車和高速公路則很擠。  
  후: 很多韓國人回老家,火車很擠(見下方 2026 年訂票率)。
- `content/zh-tw/winter.md:90` (zh-tw)  
  전: ;去年有配合活動延長地鐵和公車末班車  
  후: (삭제)
