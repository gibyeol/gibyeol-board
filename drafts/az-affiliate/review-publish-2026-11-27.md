# A to Z 2단계 5쪽 공개 전 독립 검토 — 틀린 정보·확실처럼 쓴 불확실 (2026-11-27, 작성자 아닌 Claude)

원두 원문(기준):
- [7eb4ec94#3427] "나로해." — (나) 오늘 불확실 정보 점검처럼 재검토 뒤 공개, 원두는 나중에 전수조사.
- [7eb4ec94#3295] "(가)로하고나서 이번건은 일단 그냥 다 공개하자 추후에 내가 페이지 전수조사해서 수정해야할 부분들 말해줄게. 틀린정보만 없으면돼"
- [7eb4ec94#2990] "3. 이것도 다시 말하지만 확실하지 않은 정보는 예상과 근거의 출처가 있다면 출처를 남기고 예상이라고 쓰고, 아니면 다뺴."
- [7eb4ec94#2954] "3. 모든 판단근거는 실제로 쓸 수있는 사용자에게 맞는 정보전달이 되느냐야."

검토 대상: 브랜치 claude/determined-euler-xsz86i(c3a1569)의 airport-to-seoul, essentials, seoul-subway, abroad-esim, disclosure × ko·en·ja·zh-tw = 20쪽. `git diff origin/main...HEAD`(origin/main = c972659)에서 새로 공개될 문장만 뽑아(스크립트: 태그를 뺀 문장 중 main에 없는 것) 원문 사본과 대조했어요. 행 번호는 브랜치 판. 4개 언어 행 번호가 다른 곳은 따로 적었어요.
대조 원문: wondu-archive `staging/az-affiliate-2026-11-27/raw/`(MANIFEST.md). 기록: trendmin-threads ops/affiliate-signup-list.md, ops/affiliate-plan.md. 웹: apple.com 1회 시도(실패, 아래 ⑥) 말고는 열지 않음. tpx.li·klook·yesim·reddit·미러 열지 않음.
판정 표시: **확실**(원문 문장과 같음) / **경향**(원문이 넓은 범위로 뒷받침하거나 영어 원문을 옮김) / **추론**(원문에서 끌어냄) / **근거 없음**.

---

## ① 숫자 요약

| 항목 | 수 |
|---|---|
| 대조한 새 사실(숫자·요금·시간·장소·단계·조건·제휴 상태) | 49 |
| 원문과 맞음(확실 41, 경향·추론이지만 맞음 6) | 47 |
| 틀린 정보 | **0** |
| 확실하지 않은데 확실하게 쓴 문장 | **2** (essentials:128 '휴대폰에 받아 둘', essentials:69 'QR은 보통 메일·앱으로' — 4개 언어 각각) |
| 목록 누락(틀린 문장은 아니나 사실보다 좁음) | **1** (disclosure:10 KKday 빠짐 — 4개 언어) |
| 4개 언어 사실 불일치 | 0 (zh-tw 글자 오타 1, 뜻은 같음) |
| 빌드·링크·접힘·표 깨짐 | **0** (156쪽 빌드, 20쪽 모두 문제 0) |
| 이번 변경 밖(이미 공개 판에 있음)에서 본 의심 | 3 (⑥) |

---

## ② 반드시 고칠 것 (공개 전)

### 필수 1. essentials:128 — 클룩 직통열차 표를 "휴대폰에 받아 둘 수 있다"고 단정 (4개 언어 같은 행)
- 지금 글
  - ko: "표는 공항 지하 1층 발매기에서 사도 되고(해외 카드 돼요), 아래 버튼으로 미리 휴대폰에 받아 둘 수도 있어요."
  - en: "Buy the ticket at the machines on the airport's B1 (foreign cards work), or get it on your phone in advance with the button below." (뜻: 공항 B1 기계에서 사거나(해외 카드 됨), 아래 버튼으로 미리 휴대폰에 받으세요.)
  - ja: 「切符は空港地下1階の券売機で買えます(海外のカード可)し、下のボタンで事前にスマホに入れておくこともできます。」(뜻: 공항 지하 1층 발매기에서 살 수 있고, 아래 버튼으로 미리 스마트폰에 넣어 둘 수도 있어요.)
  - zh-tw: 「車票可以在機場地下 1 樓的售票機買(海外信用卡可用),也可以用下面的按鈕先存到手機。」(뜻: 공항 지하 1층 발매기에서 살 수 있고, 아래 버튼으로 미리 휴대폰에 저장할 수도 있어요.)
- 이유(**근거 없음 → 확실처럼 씀**): 버튼(klook_airport)의 상품 페이지를 열지 못했어요(raw/klook-home-403.html, DataDome 차단). sources-phase2.md "확인 못 한 것: 클룩에서 산 직통열차 표가 공항철도 QR 승차권으로 바로 오는지, 교환번호로 바꾸는 방식인지". 같은 브랜치의 airport-to-seoul '산 다음: 직통열차 타기' 1번(:224)은 이 점을 "클룩에서 샀다면 확인서에 적힌 사용 방법을 따르세요"로 정직하게 썼는데, essentials만 '휴대폰에 받는다'고 단정해 쪽끼리도 어긋나요. 교환 방식이면 사용자가 공항에서 바로 게이트로 가려다 막혀요([#2954] 기준).
- 고칠 글
  - ko: "표는 공항 지하 1층 발매기에서 사도 되고(해외 카드 돼요), 아래 버튼으로 미리 예매할 수도 있어요(받는 법·쓰는 법은 예약 확인서를 따르세요)."
  - en: "Buy the ticket at the machines on the airport's B1 (foreign cards work), or book ahead with the button below (follow your booking confirmation for how to collect and use it)."
  - ja: 「切符は空港地下1階の券売機で買えます(海外のカード可)。下のボタンで事前に予約することもできます(受け取り方・使い方は予約確認書に従ってください)。」
  - zh-tw: 「車票可以在機場地下 1 樓的售票機買(海外信用卡可用),也可以用下面的按鈕先預訂(怎麼領、怎麼用請照預訂確認單)。」

### 필수 2. essentials:69 — "QR코드는 보통 판매처 메일이나 앱으로 와요" (4개 언어 같은 행)
- 지금 글: ko 위 문장 / en "The QR code usually comes by email or in the seller's app" (뜻: QR코드는 보통 메일이나 판매처 앱으로 와요) / ja「QRコードはふつう販売元のメールかアプリで届きます」/ zh-tw「QR 碼通常會寄到電子郵件或在賣家的 App 裡」(뜻은 같음).
- 이유(**근거 없음, 빈도 표현**): Yesim·클룩 둘 다 열지 못했어요(MANIFEST: yesim 202 본문 0·WAF challenge, klook 403). 저장된 Apple·삼성 원문은 "이동통신사에서 제공한 QR 코드"(samsung-sec-newsalert-3184)처럼 받는 경로를 말하지 않아요. 오늘 불확실 정보 점검이 지운 '근거 없는 빈도' 표현과 같은 유형이에요([#2990] "아니면 다뺴"). 틀렸을 가능성은 낮지만(경향), 근거가 없으니 빼는 게 기준에 맞아요. 뒤의 괄호만으로 행동 안내는 충분해요.
- 고칠 글
  - ko: "설치는 **출국 전, 와이파이에서** 해 두세요. QR코드를 받는 방법은 구매 확인서를 보세요."
  - en: "Install it **before you fly, on wifi**. Your order confirmation says how you receive the QR code."
  - ja: 「インストールは**出発前に、Wi-Fiで**済ませましょう。QRコードの受け取り方は購入確認書を見てください。」
  - zh-tw: 「請在**出發前、連著 Wi-Fi** 安裝好。QR 碼怎麼收,請看購買確認信。」

### 필수 3. disclosure:10 — '승인됐지만 아직 링크를 걸지 않은 곳'에 KKday가 빠짐 (4개 언어 같은 행)
- 지금 글: ko "승인됐지만 아직 링크를 걸지 않은 곳: Awin을 통한 스타일바나(Stylevana, 2026년 11월 27일 기준)." / en "Approved but not linked yet: Stylevana through Awin (as of Nov 27, 2026)." / ja「承認済みでまだリンクしていないもの:Awin経由のStylevana(2026年11月27日時点)。」/ zh-tw「已核准、尚未放上連結:透過 Awin 的 Stylevana(2026 年 11 月 27 日為止)。」
- 이유(**확실 — 누락**): trendmin-threads ops/affiliate-signup-list.md 65행 "KKday는 Travelpayouts에서 이미 연결됨(원두: Join 버튼 없음, 화면에 'Generate links for Nadri-guide' 링크 생성기) … 링크는 상품 데이터에 맞춰 만들 때 생성(지금 만들지 않음)". 승인·연결됐고 링크가 없는 상태라 이 목록에 들어가야 해요. 문장 하나하나는 틀리지 않았지만, 바로 앞 문장("승인되면 이 목록에 더해요")이 목록을 빠짐없이 관리한다고 말하므로 빠진 곳이 있으면 수익 구조 설명이 사실보다 좁아요. 지금 KKday 링크는 사이트 어디에도 없음(content·data grep 0건) → "지금 버튼은 모두 Klook·Yesim" 문장은 맞아요.
- 고칠 글
  - ko: "승인됐지만 아직 링크를 걸지 않은 곳: Travelpayouts를 통한 KKday, Awin을 통한 스타일바나(Stylevana)(2026년 11월 27일 기준)."
  - en: "Approved but not linked yet: KKday through Travelpayouts, and Stylevana through Awin (as of Nov 27, 2026)."
  - ja: 「承認済みでまだリンクしていないもの:Travelpayouts経由のKKday、Awin経由のStylevana(2026年11月27日時点)。」
  - zh-tw: 「已核准、尚未放上連結:透過 Travelpayouts 的 KKday、透過 Awin 的 Stylevana(2026 年 11 月 27 日為止)。」
- 원두 확인 1줄(필수 아님): Sovrn(계정 만듦, 화면 "Clicks generated prior to approval are not eligible … No guarantee of approval" — 뜻: 승인 전 클릭은 수익 대상 아님, 승인 보장 없음 → 계정 심사 중으로 보임, 원두 결정 (가) 링크 안 담 [7eb4ec94#2069])과 iHerb(Awin, 신청 여부 기록 없음 — signup-list 42행)는 '심사 대기' 목록에 넣을지 원두가 정할 일이에요. 기록상 상태가 불확실해서 Claude가 넣지 않는 게 [#2990]에 맞아요.

---

## ③ 사실 대조표 (새로 공개될 문장)

### airport-to-seoul (4개 언어 같은 행 번호; ko 행으로 적음)
| # | 사실 | 쪽 위치 | 판정 | 근거(원문 사본 파일:행) |
|---|---|---|---|---|
| A1 | 직통 표: 1·2터미널 지하 1층 교통센터 자동발매기·직통열차 고객안내센터, 공식 예매 | :17, :23, :183 | 확실 | arex-train-express-guide.txt:293~296, arex-express-introduce.txt:301~303 |
| A2 | 해외 카드 됨 | :17 | 경향(원문은 '승차권 구입' 전체 기준, 발매기 한정 문장 아님) | guide.txt:297~311 |
| A3 | 발매기 6단계, 언어 한·영·중·일, 어른 만 13세 이상·어린이 만 6~12세, '확인' | :24 | 확실 | guide.txt:384, 387, 393, 443, 447, 450~451, 458, 466 |
| A4 | 안내 화면 예시는 서울역 기계 | :27 | 추론(근거 있음: 도착역 선택지가 1·2터미널, 제목 '서울역→1터미널 43분') | guide.txt:385, 389 |
| A5 | QR코드를 게이트에, 지하 4층 타는 곳(1·2터미널 공통) | :25, :225~226 | 확실 | guide.txt:383, 467~469, 483 |
| A6 | 1터미널 '교통센터를 바라보고 오른쪽(서쪽)' | :23, :225 | 이미 공개 판(:66, d9890fe)에 있는 사실의 반복 — 이번에 원문 재확인 안 함 | – |
| A7 | 2터미널 방향·ATM 해외 카드·2터미널 ATM '확인 못 함' 표시 | :23, :90, :225 | 정직 표시(불확실을 사실로 쓰지 않음) | MANIFEST(ap_ko 1512 "메뉴 없음") |
| A8 | 공항철도 티머니 15,000원 = 카드 5,000 + 교통비 10,000, 1·2터미널 공항철도역 자판기, 해외 카드, 재충전 미공개 | :90 | 확실 | koreaherald-10947683.txt:78~81 |
| A9 | 2026년 11월 23일부터 판매 | :90 | 추론(맞음): 기사 게시 2026-11-24(화), "began selling … on Monday" → 11-23(월, `date`로 확인) | koreaherald.txt:73, 78 |
| A10 | 공용 ATM: 1터미널 지하 1층 일반열차 승차권 발매기 인근, 24시간, 1층 4·6·9·11번 출입구 | :90 | 확실 | airport-kr-ap_ko-1008.txt:382~418 |
| A11 | 와우패스 기기 버튼: ko '카드 발급'→'예약 코드로 발급', en 'Get a new Card'→'Issue via Code', ja「カード発行」→「引き換えコード発行」, zh-tw「發行新卡」→「使用預約碼領取」 | :208 | 확실(앞 검토 필수 1·2 반영 확인) | wowpass-guide-key-strings-ko-en-ja-zhTW.txt:4, 10, 16, 22 |
| A12 | 앱 등록·분실 시 정지로 와우패스 잔액 보호, 티머니 잔액은 재발급해도 못 찾음 | :209 | 확실 | wowpass-ko-guide-strings.txt:321, 423 |
| A13 | 16종 화폐 현금·신용카드, 앱에서 해외 카드 | :210 | 확실 | strings.txt:289, 293 |
| A14 | 티머니 잔액 따로(역·편의점 원화 현금, 앱 NFC), 안 하면 잔액 부족 | :211 | 확실/추론(원문 "별도로 충전해야 이용할 수 있어요") | strings.txt:309, 312, 313 |
| A15 | 출금 1회 10만 원·수수료 1,000원·1,000원 미만 동전 불가, 티머니 환불 500원·5만 원 이상 본사 | :212 | 확실 | strings.txt:298, 315, 325, 326, 329 |
| A16 | 와우패스 기기 찾기 링크(ko·en·ja·zh-TW 각 언어 주소) | :210 | 확실(4개 모두 200) | MANIFEST '독립 검토 반영 때 추가 열람' |
| A17 | 공식 승차권은 결제하면 QR 생성 | :224 | 확실 | sources-phase2.md 공항철도 인용, guide.txt:383 |
| A18 | 공항철도가 Klook을 제휴 여행사로 둠 | :224 | 확실 | arex-train-express-partners.txt("제휴사 여행사 … KLOOK") |
| A19 | 출발 3분 전 승강장, 호차·좌석은 승차권 | :227 | 확실 | guide.txt:380 |
| A20 | '승차권 변경/반환'(홈페이지·앱), 변경 3회, 당일 2회 이상 수수료 | :228 | 확실(en·ja·zh-tw는 "한국어 화면 이름 + 우리 번역" 표시 있음) | guide.txt:14, 71, 변경 문단 "승차권 변경은 3회까지 … 당일 2회 이상" |
| A21 | 클룩 티머니·와우패스·직통 표의 받는 곳·쓰는 법 | :189~198, :224 | 확인 못 함 → 쪽이 "예약 확인서를 따르세요" + "저희가 아직 확인하지 못했어요"로 정직 표시 | MANIFEST klook 403 |
| A22 | "직통열차는 서울역까지만" | :17, :179 | 확실 | arex-express-introduce.txt:293~297(서울역↔공항) |
| A23 | 직통 막차 22:48/22:40, Visit Seoul '1~2시간 잡으라' | :162 | 기존 사실의 재표현(불확실 정보 재검토 U18 통과) | drafts/uncertain-audit-rereview-2026-11-27.md:73 |

### essentials (4개 언어 같은 행)
| # | 사실 | 쪽 위치 | 판정 | 근거 |
|---|---|---|---|---|
| E1 | 아이폰 XS·XR 이후, 설정→일반→정보→이동통신사 잠금 'SIM 제한 없음' | :51 | 확실 | apple-ko-kr-118227.txt:26; sources-phase2 Apple 118227 인용 |
| E2 | 중국 본토는 18 Pro·18 Pro Max·Duo·17e·Air만, 홍콩·마카오 nano-SIM 두 개 듀얼 SIM | :51 | 확실(앞 검토 필수 5 반영) | 118227.txt:32~35 |
| E3 | 갤럭시: 설정→휴대전화 정보→상태 정보에 EID가 보이면 eSIM 폰, EID는 상자에도 | :51 | 경향: 원문은 영어 "Settings > About phone > Status", "on the box"(samsung-ie-esim.txt:546~547). 한국어·일본어·중국어 메뉴 이름은 옮긴 것, 'EID가 보이면 eSIM 폰'은 추론. 틀렸다는 근거는 없음 | 권고 ⑤-3 |
| E4 | 아이폰 설치(QR·길게 누르기·링크→허용), 여행용 eSIM 켜기(iOS 26), 셀룰러 데이터 회선, 한 번에 한 번호, 데이터 로밍 뜻, 원래 번호 로밍 요금, 안 될 때 | :73~77 | 확실 | 118669·118227:68~75·109317·guide-iph3dd5f213.txt:1168·102478 (sources-phase2 인용과 글자 대조) |
| E5 | 갤럭시 SIM 관리자→eSIM 추가→QR 코드 스캔, 활성화 코드 입력(ja「有効化コードを入力」로 고쳐짐), 모바일 네트워크→데이터 로밍, 회색이면 모바일 데이터 | :81~84 | 확실(ko·ja·zh-tw 설치 메뉴) / 경향(데이터 로밍 경로는 영국 영어 원문을 옮김, 출처 줄에 '옮김' 표시) | samsung-sec-newsalert-3184.txt:105~173, samsung-jp/tw-esim, samsung-uk-data-roaming |
| E6 | "설치한 뒤에는 환불이 안 되는 곳이 있어요" | :57 | 확실(와우패스 eSIM 한 곳의 예) | sources-phase2 와우패스 eSIM 인용 |
| E7 | QR코드는 '보통' 메일·앱으로 옴 | :69 | **근거 없음** → 필수 2 | – |
| E8 | SKT 상품의 한국 번호·기간·핫스팟은 상품 페이지 확인 | :55, :63 | 정직 표시(재검토 U1 통과) | uncertain-audit-rereview:50 |
| E9 | 공항철도 티머니 카드(11/23 출시, 15,000원 등) | :95 | 확실(A8·A9과 같음) | koreaherald.txt |
| E10 | 와우패스 티머니 잔액 따로(역·편의점 현금, 앱에서 옮김) | :96 | 확실 | strings.txt:309, 312 |
| E11 | 카카오 T(한국 번호·국내 카드, 해외 카드는 k.ride), Subway Korea(노선도 확인용) | :117, :119 | 불확실 정보 재검토 통과 항목 | uncertain-audit-rereview:64 |
| E12 | "숙소가 서울역 근처면 직통이 제일 빨라요(1터미널 43분)" | :128 | 경향(같은 사이트 airport-to-seoul 비교: 직통 43분, 일반 59분, 버스 60~80분, 택시 시간은 없음) | content/ko/airport-to-seoul.md:17~19 |
| E13 | "아래 버튼으로 미리 휴대폰에 받아 둘 수도" | :128 | **근거 없음** → 필수 1 | – |

### seoul-subway (ko 행)
| # | 사실 | 쪽 위치 | 판정 | 근거 |
|---|---|---|---|---|
| S1 | 처음 카드: 편의점·역 기계, 충전은 현금, 현금 없으면 공항철도역 자판기 15,000원 해외 카드 | :94 | 확실 | koreaherald.txt:79~81 |
| S2 | 와우패스: 교통 티머니 잔액 따로(역·편의점 현금, 앱) | :102 | 확실 | strings.txt:309~313 |
| S3 | 공식 승차권 QR을 직통 게이트 QR 스캐너에 | :126 | 확실 | guide.txt:483 |
| S4 | 2022년 평일 막차 새벽 1시 무렵(주말 제외), 2025년 5월 1~8호선 30분 앞당김 발표(이르면 8월), 시행 미확인·'예상' | :151, :206~207 | 확실/예상 표기 — [#2990] 형식(출처+예상) | uncertain-audit-rereview:49(코리아헤럴드 2025-05-22 원문 대조) |

### abroad-esim (ko 행)
| # | 사실 | 쪽 위치 | 판정 | 근거 |
|---|---|---|---|---|
| B1 | 중국 본토·홍콩·마카오 예외(본문·목록) | :21, :26 | 확실 | 118227.txt:32~35 |
| B2 | 아이폰 7단계: 옵션 이름 '여행용 eSIM 전용'·'여행용 SIM 및 현재 eSIM', 데이터 로밍, 원래 유심 로밍 끄기, 귀국 시 iOS 26 자동 전환·'이 회선 켜기', 안 될 때 | :44~53 | 확실 | 118227.txt:68~83, 109317, guide-iph3dd5f213.txt:1168, 102478 |
| B3 | 갤럭시 5단계(설치·켜기·데이터 로밍·귀국 시 모바일 데이터 되돌리기·재시동) | :55~61 | 확실/경향(영국 원문 옮김, 표시 있음) | samsung-sec-newsalert-3184, samsung-uk-dual-sim("Tap Calls, Text Messages or Mobile data / Tap the SIM card…") |
| B4 | 출처 목록(Apple 5, 삼성 3, 확인 못 한 것) | :74~81 | 확실(주소마다 raw 저장본 있음) | MANIFEST |

### disclosure (4개 언어 같은 행, 문단은 :10)
| # | 사실 | 판정 | 근거 |
|---|---|---|---|
| D1 | 지금 제휴 버튼은 모두 Travelpayouts 경유 Klook·Yesim | 확실 | data/affiliates.json url 있는 키 12개 전부 klook.tpx.li·yesim.tpx.li; content 전체에서 awin1·kkday·agoda·trip.com·skim 직접 링크 0건(grep) |
| D2 | 제휴 안내 쪽에서만, 쿠키 '동의' 뒤에만 Travelpayouts·Skimlinks 스크립트 | 확실 | build.py:605~608, data/site.json defer_scripts.disclosure(tpembars.com, skimresources 313714X1802466) |
| D3 | 심사 대기: Agoda·Trip.com(Travelpayouts), YesStyle(Awin), Olive Young(Rakuten) | 기록상 확실 | ops/affiliate-plan.md "Agoda·Trip.com (Travelpayouts) 승인 대기"; affiliate-signup-list.md:40("YesStyle.com 가입 요청"), :50(올리브영 US·APAC&EMEA 신청 완료) |
| D4 | Stylevana(Awin) 승인, 링크 없음 | 확실 | affiliate-signup-list.md:69 (원두 메일 [7eb4ec94#2899]) |
| D5 | 거절·미가입(Airalo·FlexOffers·Amazon·Coupang)을 쓰는 곳으로 적지 않음 | 확실 — 4개 언어 모두 없음. 지금 공개 판(main)의 disclosure는 Airalo·Amazon·Coupang을 파트너로 적고 있어, 이번 공개가 틀린 정보를 고침. privacy 4개 언어에도 Airalo 없음(grep) | affiliate-signup-list.md(Airalo 거부, FlexOffers 거절) |
| D6 | KKday | **누락** → 필수 3 | affiliate-signup-list.md:65 |

---

## ④ 4개 언어 같은 사실인가

- 새 문장의 숫자를 언어별로 모아 비교(스크립트): 차이는 날짜 표기(11월 27일 / 27 November), 만 단위 표기(1만 5천 / 15,000, 10만 / 100,000), 출처 줄의 날짜 개수뿐. 다른 숫자·다른 조건 0건.
- 단계 수·버튼·'확인 못 함' 표시: 4개 언어 같음(airport 접힘 3개, essentials 아이폰 5·갤럭시 4, abroad-esim 아이폰 6·갤럭시 5).
- 앞 검토(review-independent-phase2.md)의 언어 불일치 지적 반영 확인: en 와우패스 버튼 공식 영어로, ja·zh-tw 와우패스 버튼은 각 언어 공식 문구로(원문 저장 뒤), ja 삼성 「有効化コードを入力」, '충전식'→'교통비가 들어 있는'(ko·ja·zh-tw), zh-tw 「機場快線」 0건(「機場鐵路」로 통일).
- 글자 오타(뜻 같음, 권고): zh-tw/essentials.md:55 「購買前請先在商品頁確認**再**下面那款 SKT 商品」 → 「確認**在**下面那款」 또는 「確認下面那款」.

## ⑤ 권고 (틀린 정보는 아님)

1. essentials:96(4개 언어) 와우패스 "주요 역 기계에서 **자국 통화로** 충전해요" / en "with your home currency" / ja「円から」/ zh-tw「用外幣」 — 원래 있던 구절. 와우패스 원문은 "16종 화폐"(strings.txt:293)라 '자국 통화'는 16종에 없는 통화 사용자에게 과장. 같은 사이트 airport :210은 "16종 화폐 현금"으로 씀 → 맞추기 권고.
2. byline 날짜: airport-to-seoul·seoul-subway·abroad-esim의 `updated: 2026-11-26` — 새 내용은 11월 27일 확인 출처. 쪽 맨 위에 "2026-11-26 공식 정보로 확인"이 보임(빌드 dist/ko/airport-to-seoul 확인). 틀린 날짜라기보다 늦은 확인일을 빼먹은 것 → 2026-11-27로 맞추기 권고.
3. essentials:51 갤럭시 EID 경로 — 한국어 메뉴 이름은 영어 원문을 옮긴 것인데, ko 출처 줄(:138)에는 '옮김' 표시가 아일랜드 문서에 없음(zh-tw에는 있음). "삼성 아일랜드 eSIM 사용하기(EID 위치, 영어 메뉴 이름을 우리말로 옮김)"처럼 맞추기.
4. abroad-esim:37 "출국 하루이틀 전 … 설치까지 끝내 두는 걸 추천해요"(원래 있던 판단 문장, 이번에 이유 문장만 지움) — 상품에 따라 설치 시점부터 기간이 시작되는지는 Yesim·클룩을 못 열어 확인 못 함. 같은 쪽 단계에 "판매처 안내가 다르면 그 안내를 따르세요"가 있어 틀렸다고 보지는 않음.

## ⑥ 이번 변경 밖(이미 main에 공개된 문장)에서 본 의심 — 원두 전수조사 때 참고

1. **abroad-esim:21(4개 언어) "한국에서 산 아이폰은 eSIM과 일반 유심 칸이 둘 다 있어요"** — **추론(Claude 일반 지식, 원문 미확인)**: iPhone Air는 나라와 관계없이 eSIM 전용으로 나온 것으로 알고 있어요. 그렇다면 이 문장은 iPhone Air에 대해 틀려요. 저장된 Apple 원문(118227.txt:28 "일부 국가 또는 지역에서는 eSIM만 지원하는 iPhone 모델")은 eSIM 전용 모델이 있다는 것만 말하고, 한국 판매 모델 목록은 없어요. 확인하려고 apple.com/kr/iphone-air/specs/를 1회 열었으나 응답 없음(000, 0바이트) → 더 시도하지 않음. 이번 공개로 생기는 문제는 아니지만, [#2990]에 따라 확인 전까지 "한국에서 산 아이폰은 대부분 …" 같은 단정을 빼거나 "모델마다 달라요(설정 → 일반 → 정보에서 확인)"로 바꾸는 것을 권해요.
2. **klook_airport 버튼 상품이 '직통열차' 표이고 '휴대폰에 받는' 방식이라는 전제** — 버튼 이름 airport:220 "공항철도 직통열차 미리 예매하기", 사진 설명 airport:218 "직통열차 표를 휴대폰에.", seoul-subway:122 "직통열차 표를 도착 전에 휴대폰에 받아 두고 싶다면"(모두 main에 이미 있음). '직통열차'는 공항철도 직통열차 제휴사 목록에 KLOOK이 있어 **경향**으로 뒷받침되지만(partners.txt), '휴대폰에 받는다'는 근거 없음(필수 1과 같은 이유). affiliates.json label은 "AREX airport train ticket on Klook"(직통 여부 없음). 상품 원래 주소 확인은 원두 대기(drafts/az-affiliate/wondu-items.md 1번).
3. **1터미널 '교통센터를 바라보고 왼쪽(동쪽) 일반열차, 오른쪽(서쪽) 직통열차'**(airport:66, 이번에 :23·:225에 반복) — d9890fe "airport.kr 안내도 사실로 다시 그림"에서 온 것. 이번 검토는 안내도 원본을 다시 보지 않았어요(저장된 ap_en/1512는 글자 라벨만). 틀렸다는 근거는 없음.

## ⑦ 빌드·화면 깨짐 점검

- 방법: `git archive HEAD`로 브랜치 사본(scratchpad rv/site)을 만들고 `python3 build.py` → "built 156 pages", 오류 0.
- 20쪽(5쪽 × 4개 언어) 결과 HTML을 스크립트로 검사: `{{` 노출 0, `**` 노출 0, 마크다운 링크 미변환 0, `<details>`·`<table>`·`<ul>`·`<ol>`·`<li>` 여닫음 짝 맞음, 내부 링크의 쪽·앵커(#prep, #taxi, #pick, #tmoney 등) 모두 존재, 그림 파일 모두 존재. 표(essentials 2개, seoul-subway 1개, airport 1개)가 `<td>`로 나옴, 원문 `|` 노출 0.
- 제휴 버튼: 쪽마다 `rel="sponsored"`, 버튼 글자는 쪽이 준 글자(affiliates.json label은 화면에 안 나옴 — 앞 재검토와 같음).
- 화면 캡처(390px)는 이번에 찍지 않음 → 이번 판정은 HTML 구조까지만(가로 넘침은 보지 않음).

## ⑧ 이 검토가 못 한 것·약한 것

- 클룩·Yesim·티머니 사이트, tpx.li는 열지 않음(차단·지시). 클룩 상품 조건은 여전히 빈칸이고, 쪽은 그 빈칸을 "확인서를 따르세요"로 정직하게 표시함(필수 1·2는 그 원칙이 빠진 두 곳).
- 사실 대조는 2026-11-27 저장본 기준. 공식 사이트가 그 뒤 바뀌었는지는 모름.
- 기존 공개 문장(main에 이미 있는 것)은 ⑥에 적은 것 말고는 대조하지 않음(이번 범위 밖).
- disclosure의 '심사 대기' 상태는 운영 기록(원두 화면 기록) 기준. 각 네트워크 대시보드는 보지 못함.
- 판정자: 독립 검토(이 5쪽을 쓰지 않은 Claude). 작성자 자체 점검(phase2-review.md)과 앞 독립 검토는 참고만 하고 결론은 원문 사본으로 다시 냄.
