# 독립 검토 — 올겨울 경량 패딩 4개 언어판 (2026-11-26)

- 검토자: 독립 검토(작성자 아님). 브랜치 `claude/determined-euler-xsz86i`, 커밋 295b5cd.
- 대상: `content/{ko,en,ja,zh-tw}/winter-light-puffer.md`, `static/proto.css`, `python3 build.py`로 다시 빌드한 `dist/`(2026-11-26 12:01 UTC).
- 화면 확인 방법: 넘겨받은 스크린샷 8장(`puffer-shots/*-first.png`)과 Playwright 재측정(1280×800, 390×844). 렌더링할 때 외부 요청은 모두 막았다. 무신사·유니클로·아크테릭스 사이트는 열지 않았다.
- 판정 기준: CLAUDE.md '콘텐츠 제작 원칙'과 '⚠ 2026-11-26 오후 원칙 위반 기록', `ops/shop-spec.md`(화면 원칙, 4가지 목표, 11번 내외국인 구분 없음).
- 표기 구분: **확실** = 파일이나 화면에서 직접 확인함. **경향** = 근거는 있지만 1차 출처로 확인하지 못함. **추론** = 내 판단.

## 종합: **FAIL**. 아래 '필수 수정' 10건을 고치기 전에는 공개하지 않는다.
- 번역문의 숫자·날짜·출처·단서("운영자 확인 화면", "판매 순위 아님", "2–4위 미확인", "수치 없음")는 세 언어 모두 빠짐없이 옮겨졌다(확실).
- 막히는 이유는 다섯 가지다.
  - 번역자가 지어낸 인용문이 있다.
  - zh-tw에서 숫자를 잘못 읽을 수 있는 표기가 있다.
  - 무신사 홈으로만 가는 링크의 이름이 목적지를 속인다.
  - 사이드 판매 띠가 한국어 기사로 가는데 그 사실이 보이지 않는다.
  - 택스프리 문장이 대상자를 전제한다.
- 여기에 원본(ko)의 상품명 '원업'이 오기일 가능성이 있다.

---

## 1. 기준별 판정

### 1-1. 충실한 번역 (ko와 줄 단위 대조)

| 항목 | en | ja | zh-tw |
|---|---|---|---|
| 숫자 (+718%, 8배, 104.7억, 181,108,251,218원, 4,781, 79만 8,610, 순위 1·5·6위 금액, 평점·후기 수, 가격, 할인율, 사이즈표, 475m, 11:00~22:00, 1만 5천~100만 원) | PASS (확실: 14·16·19·22·29·41·45·57–66·84·89행) | PASS | PASS |
| 날짜·기준 시각 (10/20, 11/23, 11/26 16:25·17:04, 세일 기간·D-day) | PASS. data-start/end와 deals.json이 일치하고, 11/26 기준 D-1/3/3/4/6이 맞다 | PASS | PASS |
| 단서 문구 ("운영자 확인 화면", "판매 순위 아님", "광고·비경량 제외", "2–4위 미확인", "수치 없음", "어느 순위표인지 기사에 없음", "실시간이라 바뀜", "날짜는 화면에 없음", "제휴 링크 없음") | PASS (15·18·43·44·45·96행) | PASS (같은 행) | PASS (같은 행) |
| "12월 중순" → 판매 예정 | PASS. en 22행 "From mid-Dec". 근거 `data/shop-trends.json:3256` "12월 중순 판매예정" | PASS ("12月中旬から") | PASS ("12 月中旬起") |
| 덧붙인 사실 | **FAIL**: 53·76행. 유니클로·아크테릭스 문장을 번역자가 옮겨 놓고 인용부호로 감쌌다(→ 필수 3) | **FAIL**: 33·53·76행, 같은 문제 | **FAIL**: 33·53·76행, 같은 문제. 31행 "棉質運動褲"에서 '면(棉質)'은 ko "트레이닝 바지"에 없는 말이다(→ 필수 5) |
| 숫자를 잘못 읽을 위험 | PASS (₩10.47bn) | **FAIL**: 14·19행 "104.7億". 통화 표시가 없어서 일본 독자는 엔으로 읽는다(→ 필수 6) | **FAIL**: 13행 "最高折扣 60%". 대만식 '折' 표기와 섞이면 40% 할인으로 읽힐 수 있다. 14·19행 "億"에도 통화가 없다(→ 필수 4·6) |
| 빠진 것 | 없음. 상품명의 '원업'·'시어쉘'은 일부러 한국어 줄에만 남겼다(`drafts/prototype/gen_trend_block.py:127`). 한국어 원명이 바로 아래 줄에 있어 허용한다 | 같음 | 같음 |
| 덧붙였지만 허용하는 것 | 86–89행 "(show the Korean)"과 한국어 문장의 뜻 풀이. 사실을 더하지 않고 언어만 돕는다 | 같음 | 같음 |

### 1-2. 지어낸 사실: 로마자 표기와 유니클로 문구 번역

무신사 사이트는 열지 않았다. 대신 검색 엔진으로 무신사가 아닌 출처(공식몰·29CM·KREAM·언론)를 찾아 대조했다.

| 이름 | 번역자 표기 | 확인 결과 | 판정·처리 |
|---|---|---|---|
| 예일 | Yale | **경향**: KREAM 상품명 "YALE - 예일 웜업 퀼팅자켓_블랙"(kream.co.kr/products/575606), 29CM 브랜드 소개 "예일(YALE)" | 유지. 공식 표기 **YALE**(대문자)로 고친다. 'Yale'로 쓰면 대학과 헷갈린다. 한국어 줄은 이미 있다 |
| 수아레 | Suare | **경향**: 공식몰 제목 "수아레 SUARE"(suare.co.kr) | 유지. **SUARE**로 고친다 |
| 디미트리블랙 | Dimitri Black | **경향**: 29CM "디미트리블랙(DIMITRI BLACK)", KREAM "Dimitri Black" | 지금처럼 한국어 먼저 + 영문 괄호로 유지 |
| 아웃스탠딩 | Outstanding | **경향**: 29CM "아웃스탠딩(OUTSTANDING)", 공식몰 outstanding-co.kr | 지금처럼 한국어 먼저로 유지 |
| 드로우핏 | Draw Fit | **경향**: 출처마다 표기가 다르다. 29CM "DRAWFIT", 공식몰 도메인 draw-fit, PRTD·fruitsfamily "DRAW FIT" | 지금처럼 한국어 먼저로 유지. 표기가 하나로 정해지지 않았으므로 한국어를 주로 쓴다 |
| 무진장 | Mujinjang / ムジンジャン / MUJINJANG | **경향**: 영문 언론(서울경제 영문판 2026-06-16, 디지털투데이 영문판)이 "Mujinjang"을 쓴다 | 유지 |
| 유니클로 제품명 | Light Down Volume, PUFFTECH Compact, Ultra Light Down | **경향**: Gear Patrol·Parade 영문 기사에 "Light Down Volume Jacket"이 나온다 | 유지 |
| 유니클로·아크테릭스 문장 | en 53·76, ja 33·53·76, zh 33·53·76에 인용부호를 달았다 | **확실**: 원문은 유니클로 **한국어** 페이지다. 번역자의 번역을 회사가 직접 쓴 말처럼 보이게 했다. 아크테릭스 원문은 영어인데, ko 번역을 다시 영어로 옮겨 따옴표를 붙였다 | **FAIL** → 필수 3 |

- **새로 발견, 4개 언어 공통(ko 원본 포함):**
  - 1·4위 상품명 "예일 · **원업** 퀼팅자켓"은 오기일 가능성이 있다(경향).
  - KREAM(575606)과 29CM(1669469, 1669468)에는 "**웜업** 퀼팅자켓"으로 나온다. 29CM 정가 99,000원의 약 50%가 49,800원이어서 같은 상품으로 보인다.
  - 이 이름은 독자가 무신사에서 검색할 열쇠다. 잘못되어 있으면 검색 결과가 0건이 된다.
  - 출처는 운영자 화면 전사(`data/shop-trends.json:2409, 2466`)다. 원 스크린샷을 보지 못했으므로 판정은 보류하고 확인을 필수로 둔다(→ 필수 1).
- 이번 표기들은 결과적으로 실제 쓰이는 표기와 대부분 맞았다. 그러나 작성 시점에는 확인 기록이 없었다. 위 출처를 `data/shop-trends.json`이나 진행 기록에 남겨야 "실제 사실만" 기준을 통과한다.

### 1-3. 자연스러운 언어

| 언어 | 판정 | 근거 |
|---|---|---|
| en | PASS(작은 권고 있음) | 쉬운 단어를 쓴다. 39행 "Why is it big?"은 어색하다(→ 선택 2). 41행 "Nadri's reading: we read it as"는 같은 말이 겹친다 |
| ja | PASS(작은 권고 있음) | 전반적으로 자연스럽다. 16행 "パディングジャケット/ジャンパー"는 한국식 차용어라 일본에서는 "中わた"가 보통이다(→ 선택 3). 58행 "背中心〜袖口"는 일본 의류 표준 용어 "裄丈"가 있다 |
| zh-tw | PASS(작은 권고 있음) | 대륙식 용어(信息·質量·網絡·默認·視頻·鏈接·用戶 등)는 grep 0건이다(확실). 門市·結帳·捲尺·樂福鞋·現折·始祖鳥 모두 대만식이다. 13행 "最高折扣 60%"는 필수 4. 15행 "評論"보다 대만 쇼핑몰에서는 "評價"가 보통이다(선택 4) |

### 1-4. 한국인·외국인 구분 (명세 11, [7eb4ec94#963][7eb4ec94#1598])

| 언어 | 판정 | 근거 |
|---|---|---|
| ko | **FAIL** | 86행 "계산대에서 **보여 줄** 문장"은 한국어로 말하지 못하는 사람을 전제한다. "택스프리 되나요? 여권 여기 있어요."는 조건 없이 환급 대상자를 전제한다. 환급은 비거주 외국인과 해외 거주 한국인만 받을 수 있다(`content/en/tax-refund.md` 'Do I qualify?') |
| en | **FAIL**(부분) | 86행 "(show the Korean)"은 국적이 아니라 언어 기준이라 허용한다. 89행 택스프리 문장은 대상자를 전제한다 |
| ja | **FAIL**(부분) | 89행, en과 같다 |
| zh-tw | **FAIL**(부분) | 89행, en과 같다 |

그 밖의 문장("이미 경량 패딩이 있다면", 사이즈 재는 법 등)은 누구에게나 맞다. 분류도 출처의 분류(후기순·브랜드 판매 순위)만 썼다. PASS.

### 1-5. 링크

| 항목 | ko | en | ja | zh-tw |
|---|---|---|---|---|
| 내부 링크 (deals, shopping-streets#seongsu, tax-refund) | PASS: 0건 깨짐, 앵커 `id="seongsu"` 있음 | PASS (`/deals/`, 접두어 없는 en 경로) | PASS (`/ja/…`) | PASS (`/zh-tw/…`) |
| 백화점 칩 → 할인 상황판 | PASS | PASS: `dept-winter-2026`에 en 텍스트가 있고 11/29까지라 보인다 | PASS | PASS |
| 세일 칩 4개 → 원 기사 | 해당 없음(모두 /ko/deals/) | **FAIL** | **FAIL** | **FAIL** |
| 무신사 홈으로만 가는 링크의 정직성 | **FAIL** | **FAIL** | **FAIL** | **FAIL** |
| 성수 매장 경로 일관성 | PASS: shopping-streets ko 63행 "3번 출구에서 475m"와 일치 | PASS | PASS | PASS |

**세일 칩 → 원 기사 판단:**
- 기사와 날짜는 맞다(확실). uniqlo-bf·spao-bf·topten-bf의 출처는 에스콰이어 1913174, musinsa-bf는 전자신문 20261120000177로 deals.json과 같다. 거짓 정보는 아니다.
- 그러나 화면에는 똑같은 칩 5개가 있고, 1개는 사이트의 할인 상황판으로, 4개는 **한국어 뉴스 기사**로 간다. 표시가 없으니 독자는 세일 안내를 기대하고 누른다. 그러면 읽지 못하는 언어의 기사를 받는다.
- 그래서 "오해를 부른다"로 판정한다. 두 가지 중 하나로 고친다.
  - (가) 표시를 달아서 지금 링크를 유지한다(→ 필수 7).
  - (나) deals.json의 네 항목에 en/ja/zh-tw 텍스트를 넣어 할인 상황판으로 연결한다. 이 방법은 원두가 11/26에 승인한 할인 상황판을 바꾸므로 원두 결정이 필요하다.

**무신사 홈 링크 판단** (확실, `dist/ko/winter-light-puffer/index.html`에서 `https://www.musinsa.com/`로 가는 링크 8개):
- "무신사 블프 브랜드 랭킹 보러 가기 →"(20행)는 랭킹이 아니라 홈으로 간다. 이 사실은 HTML 주석 `정확한 랭킹 URL 미확인 → 홈으로 연결`에만 있고 화면에는 없다.
- 상품명 5개의 "상품 이름으로 검색" 안내는 `title` 툴팁뿐이라 휴대폰에서는 보이지 않는다.
- 비교표 머리 "제품 → 공식 페이지"(22행) 아래 무신사 스탠다드 행도 홈으로 간다.
- 링크 이름과 목적지가 다르다. 4개 언어 모두 FAIL이다(→ 필수 8).
- 유니클로 3개, 아크테릭스 1개, 무신사 공지 1개는 실제 상품·공지 URL이다. PASS.

### 1-6. 화면 배치

Playwright로 각 블록의 아래 끝 위치를 쟀다(단위 px, 기준 첫 화면 800).

| | 세일 띠 | 훅(숫자 카드) | 상품 카드(후기순) | 브랜드 막대 | '보러 가기' 버튼 | 비교 접기 |
|---|---|---|---|---|---|---|
| ko | 337 | 431 | 584 | 695 | 725 | 749 |
| en | 365 | 476 | 704 | **853** | **882** | **907** |
| ja | 364 | 472 | 694 | **845** | **904** | **928** |
| zh-tw | 364 | 461 | 671 | **806** | **836** | **861** |

| 항목 | ko | en | ja | zh-tw |
|---|---|---|---|---|
| 가로 넘침 (scrollWidth) | PASS 1280/390 | PASS | PASS | PASS |
| 카드가 문단이 아님 | PASS | PASS (terms·combos·stats 모두 짧은 이름표) | PASS | PASS |
| PC 한 화면 (명세: 훅·상품 카드 전부·세일 띠) | PASS | PASS (명세 최소 기준) | PASS | PASS |
| 승인 템플릿(ko)과 같은 첫 화면 | 기준 | **차이**: 브랜드 막대와 '보러 가기' 버튼 2개가 첫 화면 밖 | **차이**: 같음 | **차이**: 버튼이 첫 화면 밖 |
| 휴대폰 상품명 | **FAIL** | **FAIL** | **FAIL** | **FAIL** |

**휴대폰 상품명 (FAIL, 4개 언어 공통):**
- 원인: `proto.css:53, 58`의 `.rv .nm{white-space:nowrap; text-overflow:ellipsis}`.
- 390px에서 상품명 칸은 약 145px이고, 번역명과 한국어 원명이 **둘 다** 잘린다. 예: "Yale · quilted jacket, bl…", "ムシンサ・スタンダー…", "무신사 스탠다드 · 트랜스폼 라운…".
- 독자는 무엇인지 알 수 없고, 무신사에서 검색할 한국어 이름도 얻지 못한다. 목표 '이해가 확 됨'에 맞지 않는다(→ 필수 10).
- 높이 차이(en +158px)의 원인은 세 가지다. 세일 띠 2줄(+28), 숫자 카드(+17), 상품마다 한국어 원명 줄(+75).
- 쿠키 동의창이 첫 화면 아래를 덮는다. 사이트 공통 사항이라 이 페이지의 검토 범위 밖이다(선택 8).

### 1-7. 머리말(front matter)

| 항목 | ko | en | ja | zh-tw |
|---|---|---|---|---|
| `approved:` 없음 | PASS (grep 0건) | PASS | PASS | PASS |
| 작성자 표시 = 검토 전 문구 | PASS ("아직 Nadri 에디터 검토 전이에요") | PASS ("Not yet reviewed by a Nadri editor") | PASS | PASS |
| `disclosure:` 없음 = 제휴 링크 없음 | PASS | PASS | PASS | PASS |

`disclosure:`를 빼도 되는 근거(모두 확실):
- 외부 링크 16종에 제휴 매개변수가 없다(dist에서 추출).
- `aff-slot`은 HTML 주석일 뿐이다.
- Skimlinks·Travelpayouts 스크립트는 `disclosure: yes` 페이지에만 실린다(`data/site.json` defer_scripts.disclosure, `build.py:498`). 이 페이지에는 스크립트가 없고, 동의창 문구에만 이름이 나온다.

---

## 2. 필수 수정 (공개 전)

ko 원본을 건드리는 항목(1, 8, 9, 10)은 원두가 승인한 v3 틀의 **문구**를 바꾸는 일이다. 그래서 고친 뒤 원두에게 보여야 한다. 배치는 바꾸지 않는다.

### 필수 1. 예일 상품명 '원업' 확인 (4개 언어 16행 + 14행 원명 줄 + `data/shop-trends.json:2409, 2466`)
운영자 원 스크린샷(11/26 17:04 무신사 후기순)에서 '원업'인지 '웜업'인지 확인한다.
- '웜업'이면 모든 `원업 퀼팅자켓`을 `웜업 퀼팅자켓`으로 바꾼다. ko 16행 링크 글자 2곳과 aff-slot 주석, en/ja/zh 16행 `<small class="ko">` 2곳과 주석, JSON 2곳이다.
- 그 뒤 en/ja/zh 번역명에 "Warm-up"을 넣을지는 공식 영문 표기를 확인하기 전까지 넣지 않는다.

### 필수 2. 브랜드 영문 표기 (en·ja·zh-tw 14·16행)
- `Yale` → `YALE` (en 14행 "Most reviews: YALE quilted jacket", 16행 2곳. ja·zh 14·16행 같은 자리)
- `Suare` → `SUARE` (en·ja·zh 16행 5위, 45행 "수아레 (SUARE)")
- 디미트리블랙·아웃스탠딩·드로우핏·Mujinjang은 지금 그대로 둔다. 1-2의 확인 출처를 `data/shop-trends.json`의 해당 항목에 `name_en_source`로 남긴다.

### 필수 3. 번역한 문장을 인용처럼 쓰지 않기

**en**
- 53행: `Uniqlo describes Ultra Light Down as "a regular fit you can wear as outerwear, and also as an inner layer under other outerwear".`
  → `Uniqlo's Korean product page says Ultra Light Down is a regular fit you can wear on its own or as an inner layer under other outerwear (our translation).`
- 76행: `Of these, the one marked "can also be worn as an inner layer under other outerwear" is the regular fit (Ultra Light Down). Arc'teryx calls its trim (fitted) fit "a fit good for layering".`
  → `Of these, the one Uniqlo says can also go under other outerwear is the regular fit (Ultra Light Down). Arc'teryx describes its trim (fitted) fit as good for layering.`

**ja**
- 33행: `「インナーにも着られる」とあるのはレギュラー(ユニクロ)` → `インナーにも着られると説明されているのはレギュラー(ユニクロ)`
- 53행: `ユニクロはウルトラライトダウンを「アウターとしてはもちろん、ほかのアウターのインナーとしても着られるレギュラーフィット」と書いています。`
  → `ユニクロ韓国の商品ページは、ウルトラライトダウンを、アウターとしてもほかのアウターのインナーとしても着られるレギュラーフィットだと説明しています(韓国語から訳しました)。`
- 76행: `このうち「ほかのアウターのインナーとしても着られる」とあるのはレギュラーフィット(ウルトラライトダウン)です。アークテリクスはトリム(フィッテッド)フィットを「重ね着しやすいフィット」と呼んでいます。`
  → `このうち、ほかのアウターのインナーにもなると説明されているのはレギュラーフィット(ウルトラライトダウン)です。アークテリクスはトリム(フィッテッド)フィットを重ね着に向くと説明しています。`

**zh-tw**
- 33행: `寫著「也能當內搭」的是標準版(UNIQLO)` → `標示可以當內搭的是標準版(UNIQLO)`
- 53행: `UNIQLO 寫 Ultra Light Down 是「可以當外套,也可以當其他外套內搭的標準版型」。`
  → `UNIQLO 韓國官網說明 Ultra Light Down 是可以單穿、也可以當其他外套內搭的標準版型(由韓文翻譯)。`
- 76행: `其中寫著「也可以當其他外套內搭」的是標準版型(Ultra Light Down)。始祖鳥把修身(合身)版型叫做「適合多層穿搭的版型」。`
  → `其中,說明可以當其他外套內搭的是標準版型(Ultra Light Down)。始祖鳥說明修身(合身)版型適合多層穿搭。`

### 필수 4. zh-tw 할인율 표기 (13행)
`3 大百貨公司 <b>最高折扣 60%</b>` → `3 大百貨公司 <b>最低 4 折</b>`
(최대 60% 할인 = 정가의 40% = 4折)

### 필수 5. zh-tw 덧붙인 사실 삭제 (31행)
`<span class="none">棉質運動褲</span>` → `<span class="none">休閒運動褲</span>`

### 필수 6. ja·zh-tw 금액 통화

**ja**
- 14행: `<strong>104.7億</strong>` → `<strong>104.7億ウォン</strong>`
- 18행 src 끝에 `・金額はウォン`을 더한다. 막대의 40.1億·38.0億 칸은 폭이 좁아서 그대로 둔다.

**zh-tw**
- 14행: `<strong>104.7億</strong>` → `<strong>104.7 億韓元</strong>`
- 18행 src 끝에 `・金額為韓元`을 더한다.

### 필수 7. 세일 칩이 한국어 기사로 간다는 표시 (en·ja·zh-tw 12–13행)
1. 13행에서 외부 기사로 가는 칩 4개의 `</span></a>` 바로 앞, D-day 뒤에 ` ↗`를 넣는다.
   - 예: `Uniqlo <span class="dday" data-today="Ends today">D-1</span> ↗</a>`
2. 12행 tag 문단 끝 `</p>` 앞에 아래를 넣는다.
   - en: `<span class="src">↗ = opens the Korean news article with the dates</span>`
   - ja: `<span class="src">↗ = 日付が載った韓国語の記事が開きます</span>`
   - zh-tw: `<span class="src">↗ = 開啟刊登日期的韓文報導</span>`

다른 방법은 1-5의 (나)다. deals.json에 번역을 넣는 방법이며, 원두가 정한다.

### 필수 8. 무신사 홈 링크를 정직하게 (4개 언어)

**20행 버튼 2개**

| 언어 | 첫째 버튼 | 둘째 버튼 |
|---|---|---|
| ko | `무신사 홈에서 블프 랭킹 찾기 →` | `무신사 홈에서 '경량 패딩' 검색 →` |
| en | `Musinsa home: find the Black Friday ranking →` | `Musinsa home: search 경량 패딩 →` |
| ja | `ムシンサのトップで ブラックフライデーのランキングを探す →` | `ムシンサのトップで「경량 패딩」を検索 →` |
| zh-tw | `到 MUSINSA 首頁找黑五排名 →` | `到 MUSINSA 首頁搜尋「경량 패딩」→` |

**15행 h3 src 끝에 추가**

| 언어 | 추가 문구 |
|---|---|
| ko | ` · 이름을 누르면 무신사 홈(이름으로 검색)` |
| en | ` · names open Musinsa home; search the Korean name` |
| ja | `・名前はムシンサのトップへ(韓国語名で検索)` |
| zh-tw | `・點名稱到 MUSINSA 首頁(用韓文名稱搜尋)` |

**22행 무신사 스탠다드 행의 링크 글자**

| 언어 | 바꿀 문구 |
|---|---|
| ko | `무신사 스탠다드 라이트 다운 (무신사 홈) →` |
| en | `Musinsa Standard light down (Musinsa home) →` |
| ja | `ムシンサ・スタンダード ライトダウン(ムシンサのトップ) →` |
| zh-tw | `MUSINSA STANDARD 輕羽絨(MUSINSA 首頁) →` |

### 필수 9. 택스프리 문장의 대상 조건과 '보여 줄' 문구

- **ko 86행**
  - 바꿀 문장: `계산대에서 보여 줄 문장: **“이 상품에 쓸 수 있는 쿠폰이 있나요? 앱 쿠폰 적용해 주세요.”** / **“택스프리 되나요? 여권 여기 있어요.”**(한 영수증 1만 5천~100만 원, [택스리펀드](/ko/tax-refund/)).`
  - 새 문장: `계산대에서 쓸 문장(말하거나 화면을 보여 주세요): **“이 상품에 쓸 수 있는 쿠폰이 있나요? 앱 쿠폰 적용해 주세요.”** / 택스리펀드 대상이면 **“택스프리 되나요? 여권 여기 있어요.”**(한 영수증 1만 5천~100만 원, [대상인지 보기](/ko/tax-refund/)).`
- **en 89행**: 맨 앞 `- ` 다음에 `If you qualify for a tax refund: `를 넣는다. 링크 글자 `[tax refund]`는 `[who qualifies]`로 바꾼다.
- **ja 89행**: 맨 앞에 `免税の対象なら: `를 넣는다. `[免税]`는 `[対象か確認]`으로 바꾼다.
- **zh-tw 89행**: 맨 앞에 `符合退稅資格的話:`를 넣는다. `[退稅]`는 `[看是否符合]`로 바꾼다.

### 필수 10. 휴대폰에서 상품명이 잘리지 않게 (`static/proto.css` 94–99행 `@media (max-width:899px)` 블록 안에 한 줄 추가)
```css
  .story .rv .nm,.story .rv .nm .ko{white-space:normal;overflow:visible;text-overflow:clip}
```
PC 규칙(53·58행)은 그대로 둔다. ja PC 2·3위의 번역명은 잘리지만 한국어 원명 줄은 다 보인다(확실, ja-1280-first.png).

---

## 3. 선택 제안 (필수와 별개)

1. **PC 첫 화면을 ko 템플릿과 맞추기(강한 권고).** en·ja·zh-tw는 '보러 가기' 버튼이 첫 화면 밖에 있다(882/904/836px). 줄이는 방법은 두 가지다.
   - (가) 1280px에서 세일 띠를 1줄로 만든다. en "Musinsa Black Friday"를 `Musinsa BF`로 줄이면 약 28px이 준다. 다만 BF 약어가 낯설 수 있다.
   - (나) PC에서 `.rv .nm .ko`를 번역명과 같은 줄 오른쪽에 작게 둔다. `display:inline; margin-left:6px`로 하면 약 75px이 준다.
   - (나)가 효과가 크지만, 잘림이 늘어나는지 다시 확인해야 한다.
2. **en 문구 다듬기**
   - 39행 `Why is it big? More` → `Why is it popular? More`
   - 41행 `*Nadri's reading: we read it as people already buying a lot in August, before the cold.*` → `*Our reading: people were already buying a lot in August, before the cold.*`
3. **ja 문구 다듬기**
   - 16행 `コア パディングジャケット(4色)` → `コア 中わたジャケット(4色)`
   - 16행 `ライト パディングジャンパー 6色(色追加)` → `ライト 中わたブルゾン 6色(色追加)`
   - 58행 `背中心〜袖口` → `裄丈`
   - 13행 `最大60%` → `最大60%OFF`
4. **zh-tw 문구 다듬기**
   - 14·15행 `評論` → `評價`
   - 31행 `薰衣草色外套`·`灰色外套`·`粉彩色外套` → `…羽絨外套`. 칸 폭이 허락하면 바꾼다.
   - 34행 `把自己的外套攤平` → `把自己的羽絨外套攤平`
5. **상품명 툴팁 문구:** en·ja·zh의 `title="Search this name on Musinsa"`류를 "한국어 이름으로 검색"으로 바꾼다.
   - en: `Search the Korean name on Musinsa`
   - ja: `韓国語名でムシンサを検索`
   - zh: `用韓文名稱在 MUSINSA 搜尋`
6. **영문 출처 후보:** 무신사 블프 기간은 영문 기사에도 있다(국민일보 영문판 kmib.co.kr/en/article/20261123501518, 서울경제 영문판, JKN). en 칩을 영어 기사로 연결하면 읽을 수 있는 출처가 된다. 이번 세션에서는 kmib 호스트가 허용되지 않아 **본문을 확인하지 못했다**. 쓰기 전에 본문의 날짜를 대조해야 한다.
7. **ja·zh 가격 표기 통일:** 상품 목록은 `₩49,800`, 숫자 카드·비교표는 `49,800ウォン`/`韓元`이다. 한 가지로 통일한다.
8. **사이트 공통(이 페이지 범위 밖):**
   - 쿠키 동의창이 첫 화면 하단을 덮는다.
   - 머리 숫자가 언어마다 다르다(ko "확인한 세일 28건·공개 코드 5개", en "10 sales checked · 2 public codes"). 번역된 할인 항목 수 차이로 보이지만(추론) 따로 확인이 필요하다.
9. **확인하지 못한 것:** 코리아헤럴드 영문 기사에 나온 상품명(City Leisure Hooded Light Down, Flying 77, Ventus On, Curve Air Shell)과 +718%·8배 문장은 원문과 대조하지 못했다. 이 세션에서 koreaherald.com 접속이 막혀 있었다. ko에서 옮긴 숫자와 번역문의 숫자가 같다는 것만 확인했다.

---

## 4. 이 검토에서 쓴 외부 확인 출처 (무신사 사이트는 열지 않음)
- 예일: https://kream.co.kr/products/575606 , https://www.29cm.co.kr/products/1669469 , https://product.29cm.co.kr/catalog/1669468
- 수아레: https://suare.co.kr/
- 디미트리블랙: https://shop.29cm.co.kr/brand/1883 , https://kream.co.kr/brands/dimitri-black
- 아웃스탠딩: https://shop.29cm.co.kr/brand/1657 , https://outstanding-co.kr/shopinfo/company.html
- 드로우핏: https://shop.29cm.co.kr/brand/16175 , https://draw-fit.com/ , https://www.prtdapp.com/brand/draw-fit
- 무진장 영문 표기: https://en.sedaily.com/news/2026/06/16/musinsas-mujinjang-sale-lifts-online-users-70-percent , https://www.digitaltoday.co.kr/en/view/68790/rising-demand-for-reasonably-priced-products-lifts-musinsas-mujinjang-sale
- 유니클로 Light Down Volume: https://www.gearpatrol.com/outdoors/uniqlo-light-down-volume-jacket-sale/ , https://parade.com/shopping/uniqlo-light-down-volume-jacket
- 위 내용은 검색 엔진 결과 요약으로 확인했다. 각 페이지를 직접 열어 대조하지는 않았으므로 '경향' 등급이다.
