# 공개 전 독립 검토 — buy-from-home(K-뷰티, 집에서 받는 법) + 링크·제휴·수익 구조 변경

- 판정자: **독립 검토(이 페이지 작성자 아님)**. 파일은 고치지 않았다(이 검토 파일만 씀).
- 대상: 브랜치 claude/determined-euler-xsz86i, `git diff origin/main...HEAD -- content/*/buy-from-home.md content/*/olive-young.md content/*/shopping.md content/*/disclosure.md data/affiliates.json` (커밋 c4df4fe까지) + 검토 중 더해진 커밋 1d34af1·2848f2b(Stylevana 줄, 출처 ㉓㉔ — 아래 6절).
- 원문 대조: wondu-archive `staging/overnight-2026-11-27/raw/buy-from-home/`(2차·round3), `raw-from-scratchpad/buy-from-home-raw/`(CJ뉴스룸·일본 세관 1차 사본), `raw-from-scratchpad/stylevana-wondu-screens-2026-11-27/`(110.webp~114.png). 태그를 벗겨 글자 검색. 일본 쪽은 cp932 해독. 웹은 열지 않음. 제휴 링크(awin1.com)는 열지 않음.
- 기준: trendmin-threads/CLAUDE.md '콘텐츠 제작 원칙', 원두 [7eb4ec94#3295] "틀린정보만 없으면돼", [7eb4ec94#2990] 불확실 정보는 예상+출처 아니면 뺌, [7eb4ec94#2954] 3 쓸 수 있는 사람 기준, [7eb4ec94#963] 내외국인 구분 없음, [7eb4ec94#1605] 임의 분류 금지, ops/shop-spec.md.
- 빌드: `git archive origin/main` → scratchpad/rv3build에 대상 파일 복사(1d34af1·2848f2b 반영본으로 다시 복사) → `python3 build.py` = built 160 pages. 내부 링크 4,308개 중 깨짐 0. 페이지 안 `#` 앵커 깨짐 0. '확인 못'·마크다운 잔여(`**`, `](`) 0. 화면: scratchpad/rv3shots2/{ko,en,ja,zh-tw}_390_tall.png, *_1280.png.
  - 주의: 처음 찍은 화면(scratchpad/rv3shots/)은 이미 떠 있던 다른 서버(포트 8765, 13:40 시작, 옛 빌드)를 찍은 것이라 버림. rv3shots2만 이 검토의 근거.

## 숫자 요약

| 항목 | 수 |
|---|---|
| 원문 사본과 직접 글자 대조한 사실(숫자·기한·조건·인용) | 109개 (올리브영 10, iHerb 12, 일본 10, 영국 7, 캐나다 6, 호주 5, 싱가포르 7, 대만 3, 홍콩 1, EU 7, iHerb K-Beauty 분류 7, Stylevana 배송 23 + 파손·보험·반품 11) |
| 원문과 글자가 다른 것 | 0 |
| 조건이 빠져 틀리게 읽히는 곳 | 2 (싱가포르 'S$400은 물건 값만', Stylevana 미국 배송 지연 안내 누락) |
| 원문 사본 없음(대조 불가) | 0 (처음엔 Stylevana 파손·보험 '선택'·반품 ㉔이 사본 없음이었으나, 뒤에 저장된 115~119.png로 모두 대조함 — 6절) |
| 4개 언어 숫자 불일치 | 0 (언어별 순서 차이·zh-tw 실수 목록 1줄 교체는 현지화, 사실 차이 아님) |
| 광고 표시 문제 | 2 (첫 화면에 안 보임 / 'Stylevana 링크'가 이제 3개인데 제휴는 1개) |
| 반드시 고칠 것 | 6 |
| 권고 | 11 |

## 1. 반드시 고칠 것 (공개 전)

### 필수 1. 광고 표시가 첫 화면에 없다 — 수익 구조 페이지의 "맨 위에 밝힌다"와 어긋남
- 위치: content/{ko,en,ja,zh-tw}/buy-from-home.md:20 (비교 표 ·'표에 숫자가 없는 칸' 안내 다음).
- 사실: 390px 화면에서 광고 표시는 약 1,560px 아래(세 번째 화면), 1280px에서도 첫 화면 밖(rv3shots2/ko_390_tall.png, en_1280.png). front matter에 `disclosure`가 없어 사이트 공통 '일부 제휴 링크' 문구도 없다.
- 어긋나는 문장: content/ko/disclosure.md:8 "제휴 링크가 있는 페이지는 맨 위에 그 사실을 밝히고" (en "Pages with affiliate links say so at the top").
- `disclosure: yes`를 켜지 않은 것은 맞다: 켜면 Travelpayouts·Skimlinks 스크립트(동의 시)가 붙어 "다른 쇼핑몰 링크는 일반 링크"가 틀릴 수 있다(build.py 583~584줄). 제휴 링크 자체는 다음 절 버튼에 "(제휴 링크)"로 표시되고, 광고 표시는 그 버튼(:36)보다 앞에 있다 — 클릭 전 표시는 됨. 문제는 '맨 위' 약속과 첫 화면.
- 고칠 것: :20의 `<aside class="tr-note">…광고 표시…</aside>`를 :7 `tr-cta` 줄 바로 다음(“한눈에 비교” h2 앞)으로 옮긴다. 문장은 필수 2로 바꾼 것을 쓴다. 4개 언어 같은 자리.

### 필수 2. 광고 표시 문장 "이 페이지의 Stylevana 링크는 제휴 링크" — 지금은 Stylevana 링크가 3개, 제휴는 1개
- 위치: buy-from-home.md:20 (4개 언어).
- 사실: 1d34af1·2848f2b 뒤 출처 ㉓ `https://www.stylevana.com/en_US/shippings`, ㉔ `…/returns_and_exchanges`가 일반 링크(rel="noopener")로 더해졌다. 빌드 결과 언어마다 stylevana.com 직접 링크 2개 + awin1.com 1개(rel="sponsored noopener" 1개).
- 고칠 글:
  - ko: `<b>광고 표시.</b> 이 페이지에서 'Stylevana(제휴 링크)' 버튼 하나만 제휴 링크(Awin)예요. 이 버튼으로 산 주문에서 Nadri가 수수료를 받을 수 있고, 내는 금액은 같아요. 출처에 적은 Stylevana 주소를 포함해 다른 링크는 모두 일반 링크예요. 올리브영(Rakuten)에는 신청해 두었어요. 자세히: <a href="/ko/disclosure/">Nadri의 수익 구조</a>.`
  - en: `<b>Advertising notice.</b> Only one link on this page is an affiliate link (Awin): the button labelled "Stylevana (affiliate link)". Nadri may earn a commission on orders made through it; you pay the same price. Every other link, including the Stylevana addresses in the sources, is an ordinary link. We have applied to Olive Young (Rakuten). More: <a href="/disclosure/">How Nadri makes money</a>.`
    (뜻: 이 페이지의 제휴 링크(Awin)는 'Stylevana (affiliate link)' 버튼 하나뿐. 수수료를 받을 수 있고 내는 값은 같음. 출처의 Stylevana 주소를 포함해 나머지는 일반 링크. 올리브영(Rakuten)에 신청함.)
  - ja: `<b>広告について。</b> このページのアフィリエイトリンク(Awin)は「Stylevana(アフィリエイトリンク)」のボタン1つだけです。このボタン経由の注文でNadriが紹介料を受け取ることがあり、お客様の支払う金額は変わりません。出典に載せたStylevanaのアドレスを含め、ほかのリンクはすべて通常のリンクです。オリーブヤング(Rakuten)には申請中です。詳しくは<a href="/ja/disclosure/">Nadriの収益について</a>。`
    (뜻: ko와 같음)
  - zh-tw: `<b>廣告說明。</b> 這一頁只有「Stylevana(聯盟連結)」這一個按鈕是聯盟行銷連結(Awin)。透過這個按鈕下的訂單,Nadri 可能拿到佣金,你支付的價格不變。包括出處裡的 Stylevana 網址在內,其他連結都是一般連結。Olive Young(Rakuten)已申請。詳情:<a href="/zh-tw/disclosure/">Nadri 的收入來源</a>。`
    (뜻: ko와 같음)

### 필수 3. 출처 번호 범위가 ㉒에서 멈춤
- 위치: buy-from-home.md:18 (4개 언어) "번호 ①~㉒는 맨 아래 출처예요" / "Numbers ①–㉒" / "番号①〜㉒" / "編號 ①~㉒".
- 사실: 출처가 ㉔까지 있다(1d34af1·2848f2b).
- 고칠 글: ko `번호 ①~㉔는` / en `Numbers ①–㉔ are` / ja `番号①〜㉔は` / zh-tw `編號 ①~㉔ 是`.

### 필수 4. 싱가포르 "'S$400'은 물건 값만" — 미등록 판매자 경우엔 틀리게 읽힘
- 위치: ko:104, en:88, ja:104, zh-tw:80 (싱가포르 자세히 첫 줄). 요약 표 ko:56 / en:54 / ja:56 / zh-tw:53 오른쪽 칸도 관련.
- 원문(sg_gst-on-low-value-goods.txt): "Low-value goods are goods with a sales value of S$400 or less … Sales value refers to the price of the goods only" — 이것은 **결제 때 GST(등록 판매자)** 판단 기준. 반면 "GST is charged at import if: The overseas seller is not GST-registered, and The total Cost, Insurance and Freight (CIF) value of the shipment exceeds S$400"(미등록 판매자는 배송비·보험 포함).
- 왜 틀리게 읽히나: 첫 줄이 조건 없이 "S$400은 물건 값만, S$395+배송비 S$25 = S$395"라고 해서, 미등록 판매자에게 S$395 + 배송비 S$25(CIF S$420)를 산 사람은 "도착 때 GST 없음"으로 읽는다. 원문 기준으로는 도착 때 GST 대상. 요약 표 오른쪽 칸 "소포가 S$400 넘으면"도 무엇을 더하는지 없음.
- 고칠 글(첫 줄 제목·본문):
  - ko `<b>등록 판매자 기준 'S$400'은 물건 값만</b><span>GST 등록 판매자에게 살 때는 배송비·보험료·세금을 빼고 물건 한 개 값으로 봐요. 물건 S$395 + 배송비 S$25 = S$395로 봐요 ⑰. 미등록 판매자는 아래처럼 배송비·보험까지 더해요.`
  - en `<b>For GST-registered sellers, "S$400" means the item price only</b><span>Shipping, insurance and tax are left out, item by item. An item at S$395 + S$25 shipping counts as S$395 ⑰. For sellers not registered for GST, shipping and insurance are added (see below).`
    (뜻: GST 등록 판매자일 때 S$400은 물건 값만. 미등록 판매자는 배송비·보험을 더함)
  - ja `<b>登録済みの販売者なら「S$400」は商品代だけ</b><span>GST登録済みの販売者から買うときは、送料・保険料・税金を除いた1品の値段で見ます。商品S$395+送料S$25=S$395とみなします ⑰。未登録の販売者は、下のとおり送料・保険も足します。`
  - zh-tw `<b>向有 GST 登記的賣家買:「S$400」只算商品價格</b><span>不算運費、保險費、稅,每件分開看。商品 S$395 + 運費 S$25 = 算 S$395 ⑰。未登記的賣家要加上運費和保險(見下方)。`
  - 요약 표 오른쪽 칸: ko `미등록 판매자에게 산 소포가 물건+배송비+보험 합계(CIF) S$400 넘으면 도착 때 GST ⑰` / en `Shipment from a seller not registered for GST, goods + shipping + insurance (CIF) over S$400: GST on arrival ⑰` / ja `未登録の販売者から買った小包が商品+送料+保険(CIF)でS$400を超えると到着時にGST ⑰` / zh-tw `向未登記賣家買的包裹,商品+運費+保險(CIF)超過 S$400,到貨時繳 GST ⑰`.

### 필수 5. Stylevana 미국 배송 기간 — 사이트의 '지연 예상' 안내가 빠짐
- 위치: buy-from-home.md:16 Stylevana 줄 '배송 기간' 칸 (4개 언어).
- 원문(112.png, Ship to US 표 아래 *): "Subsequent to the announcement of the latest customs rules, we have identified new shipping solutions with our courier partners … Please expect there might be some delay in parcel delivery to the United States." (뜻: 최근 세관 규칙 발표 뒤 배송 방법을 바꿨고, 미국행은 늦어질 수 있음). 111.png: "Shipping may also take longer during sale periods, holidays and extreme weather."(세일·휴일·악천후엔 더 걸림), "closed on Saturdays, Sundays and on Hong Kong Public Holidays"(토·일·홍콩 공휴일 휴무).
- 왜: 페이지는 "미국 일반 8~15영업일"만 써서 지금(블랙프라이데이 세일 기간) 그대로 믿게 읽힌다. 같은 화면의 조건이 빠짐.
- 고칠 글(배송 기간 칸 끝에 덧붙임):
  - ko `미국행은 '늦어질 수 있다'고 안내해요. 세일 기간·휴일엔 더 걸려요 ㉓`
  - en `For the US, the store warns of possible delays. Sale periods and holidays take longer ㉓`
  - ja `米国あては「遅れる可能性がある」と案内しています。セール期間・休日はさらにかかります ㉓`
  - zh-tw `寄美國的部分,網站說明可能延誤。特賣期間、假日會更久 ㉓`

### 필수 6. 개인정보 처리방침에 Awin이 없다
- 위치: content/{ko,en,ja,zh-tw}/privacy.md:18 '제휴 파트너' 줄 (이번 diff 밖의 파일).
- 사실: 지금 문장은 "제휴 링크를 클릭하면 파트너 사이트(예: 클룩, Yesim)가 … 쿠키를 설정할 수 있어요". Awin 링크는 클릭이 먼저 제휴 네트워크 Awin(awin1.com)을 거쳐 기록된 뒤 Stylevana로 넘어간다. 개인정보 페이지는 제3자를 이름으로 나열하는데(Cloudflare·Travelpayouts·Skimlinks) Awin은 없다. '파트너 사이트'라는 일반 문장으로 일부는 덮이지만 이름이 빠져 목록이 불완전.
- 고칠 글:
  - ko `- **제휴 파트너.** 제휴 링크를 클릭하면 제휴 네트워크(예: Awin, Travelpayouts)와 파트너 사이트(예: 클룩, Yesim, Stylevana)가 추천 실적을 인정받기 위해 클릭을 기록하고 쿠키를 설정할 수 있어요. 파트너 사이트에 들어간 뒤에는 그 사이트의 개인정보 처리방침이 적용돼요.`
  - en `- **Affiliate partners.** When you click an affiliate link, the affiliate network (for example Awin or Travelpayouts) and the partner site (for example Klook, Yesim or Stylevana) may record the click and set cookies to credit the referral. Their own privacy policies apply once you are on their site.`
    (뜻: 제휴 링크 클릭 시 제휴 네트워크(Awin·Travelpayouts)와 파트너 사이트가 클릭을 기록하고 쿠키를 둘 수 있음)
  - ja `- **アフィリエイトパートナー。** アフィリエイトリンクをクリックすると、アフィリエイトネットワーク(例:Awin、Travelpayouts)とパートナーのサイト(例:Klook、Yesim、Stylevana)が紹介の成果を記録するため、クリックを記録しCookieを設定することがあります。相手のサイトに移った後は、そのサイト自身のプライバシーポリシーが適用されます。`
  - zh-tw `- **聯盟行銷合作夥伴。** 當你點擊聯盟行銷連結時,聯盟網路(例如 Awin、Travelpayouts)和合作夥伴網站(例如 Klook、Yesim、Stylevana)可能會記錄點擊並設定 Cookie 來認列轉介。進入對方網站後,即適用該網站自己的隱私權政策。`
  - privacy.md를 고치면 `updated` 날짜도 바꾼다(approved가 있으면 BRIEF 규칙대로 뺌).

## 2. 권고 (고치면 더 정확, 공개를 막지는 않음)

1. **EU '누가 내나'**(ko:72, en:104, ja:72, zh-tw:96): 원문 "Who is responsible for paying the duty? The declarant of the good, i.e. seller or importer"(낼 책임이 누구에게 있나). 페이지 "판매자나 수입 대행자가 내요"는 '나는 안 낸다'로 읽힐 수 있다(실제로 결제 금액이나 배달 청구에 들어갈 수 있으나 그건 원문에 없음 → 쓰지 말고 말만 좁힘). 제안: ko "세관에 낼 책임은 신고하는 쪽, 곧 판매자나 수입 대행자에게 있어요. 소비자가 직접 신고·납부하는 건 아주 드문 경우라고 해요 ㉑." (4개 언어 같은 뜻으로)
2. **EU 제외 조건**: 원문 "Excluding goods benefiting from preferential trade agreements … as long as the VAT has not been collected using IOSS and they are declared in H1"(FTA 특혜 물품은 IOSS로 VAT를 걷지 않고 H1 신고한 경우 제외). 한국–EU FTA가 있어 드물게 해당. 표의 "€150 이하 소포도 … €3"는 대부분 맞음. 접기 안에 한 줄 더하면 정확.
3. **올리브영 글로벌 US$60 표 칸**(:13): 근거 문장은 "전 세계 공통 … 60달러 이상이었으나"(5월 회사 발표). 카드(:24)에는 "내 나라 기준은 결제 화면에서 확인"이 있는데 첫 표에는 없다. ja·zh-tw 독자가 표만 보고 자기 기준으로 읽기 쉬움. 표 칸에 "(내 나라 기준은 결제 화면)" 덧붙이기.
4. **올리브영 US '연 날 2026년 5월 29일'**(카드): 근거 ①은 5월 21일 보도자료의 예정("29일 … 동시 론칭"). 열린 뒤 확인한 원문 없음. "2026년 5월 29일 열기로 발표" 또는 "(5월 21일 발표)"로.
5. **카드 '다른 쇼핑몰(예: Stylevana)에서 산다면'**(:24): 이제 Stylevana가 비교 표에 있어 "위 표의 네 칸을 직접 채워 보세요"와 어긋남. "(예: Stylevana)"를 빼고 "표에 없는 쇼핑몰에서 산다면"으로.
6. **Stylevana 배송 칸 다른 조건**(112·113.png): 외딴 지역 추가 요금(미국 $11, 필리핀 $34)·2~3영업일 더(111.png), 우체국 사서함·배송대행 주소·호텔로는 안 보냄(111.png). 반송·분실 위험이 있는 '배송대행 주소 불가'는 쓸 수 있는 사람 기준([7eb4ec94#2954] 3)에 중요.
7. **일본 '받는 법'**: "국제우편이고 세금 합계가 1만 엔 이하면 배달될 때 세금을 내고" — 원문은 "課税価格が20万円以下の場合"(과세가격 20만 엔 이하일 때) 아래 항목. 화장품 주문에선 드물지만 조건 한 마디("과세가격 20만 엔 이하 우편").
8. **en '지난 3월'**: en "Last March"는 2026년 3월인지 흐림 → "In March 2026". ko "지난 3월"·ja "この3月"·zh-tw "今年 3 月"은 문제 없음.
9. **쿠키 안내 띠**: 사이트 공통 문구가 "제휴 쿠키(Travelpayouts, Skimlinks)"만 말한다. 이 페이지는 스크립트 0개(NADRI_DEFER=[])라 동의해도 아무것도 안 불러옴 — 틀린 건 아니나, Awin은 클릭 때 쿠키라 띠와 무관함을 개인정보 페이지(필수 6)에서 설명하면 충분.

## 3. 사실 대조 상세 (판정 1)

| 묶음 | 페이지 내용 | 원문 사본 | 판정 |
|---|---|---|---|
| ① CJ 2026-05-21 | US$35·US$60(“이었으나”)·블루밍턴·5~7영업일→절반·29일 론칭 | buy-from-home-raw/cja_3.htm | 일치. US$60은 "2026년 5월 회사 발표"로 날짜 붙임 — 맞음(권고 3·4) |
| ② CJ 2026-03-02 | 연 4회(3·6·9·12월)·30% 이상 장바구니·앱 20% 선착순 | cja_1.htm | 일치 |
| ⑩ 회사 사이트 | 150개 나라·빠르면 5일·지역마다 다름 | raw/oy_corp_global.txt | 일치 |
| ⑪ iHerb 배송 | 180개 넘는 나라·미·한·홍·사우디·$25 Limited Time Only·My Destination·화면 'United States' | round3/www.iherb.com_shipping.txt | 일치. '미국행'으로 조건 붙인 것 맞음 |
| ⑫ iHerb 반품 | 30일/자체 브랜드 90일(iHerb에서 산 경우)·48시간·14일·해외 라벨 없음·7~10영업일/35일·사진·Orders→Refunds/Returns | round3/www.iherb.com_info_returns.txt | 일치 |
| ㉒ iHerb 분류 | K-Beauty Cleansers·Face Masks·Toners·Moisturizers·Treatments & Serums·Sunscreen·Hair Care | round3/iherb_k-beauty.txt | 일치. iHerb 자체 분류를 그대로 씀 → [#1605] 통과 |
| ③~⑨ 일본 | 1만 엔 면제·×0.6·니트/가죽 제외·화장품 무세(令和8年4月1日現在)·10%·24개·통관료·특송 대행 수수료·우편 한 상자/분할 합산·운임·보험 포함 | buy-from-home-raw/ cj_1405·1006·1204·1111·1806·3002, kojinyunyu | 일치(권고 7) |
| ⑬ 영국 | £135·판매자 VAT·초과 시 VAT+관세·3주 보관·BOR 286/C285·북아일랜드 €3+€2·특별소비세 물품 | raw/uk_tax.txt | 일치 |
| ⑭⑮ 캐나다 | CAN$20·GST/HST·PST·전체 금액·제외 품목·E14·처리 수수료·택배 대행 | raw/ca_courier.txt, ca_postal2.txt | 일치. 표가 '우편'으로 범위를 밝힘 |
| ⑯ 호주 | AUD1,000·2018-07-01 판매자 GST·초과 시 신고서+수수료·술담배·반품 시 관세 환급 불가 | raw/au_buy2.txt | 일치 |
| ⑰⑱ 싱가포르 | S$400·S$395+S$25·등록/미등록·CIF·물건별·14일·SAM·이중 청구 환급 | raw/sg_*.txt | 숫자 일치, **조건 누락 1(필수 4)** |
| ⑲ 홍콩 | 네 가지 과세 물품 | raw/hk_dc.txt | 일치. '화장품·옷 없음'은 목록 대조라고 출처에 밝힘 |
| ⑳ 대만 | NT$2,000·반년 6번 초과·택배사가 먼저 냄 | raw/tw_courier.txt | 일치 |
| ㉑ EU | €3·€150·6월 30일 종료·2028-07-01·종류(세번)별·티셔츠 예·신고자·'very residual'·수수료 가을 결정 | raw/eu_news.txt | 일치(권고 1·2) |

4개 언어: 숫자 토큰을 언어별로 세어 비교 — 차이는 표기 차이(1만 엔/10,000/1万円, 60%/×0.6 등)뿐. 세금 표 행 순서는 언어별 다름(ko 일본 먼저 / en 영국 먼저 / ja 일본 먼저 / zh-tw 대만 먼저) — progress.md 기록대로 의도. zh-tw 실수 목록은 일본 '24개' 줄 대신 대만 '반년 6번' 줄 — 사실 오류 아님.

## 4. 광고 표시·제휴 (판정 2)

| 점검 | 결과 |
|---|---|
| 제휴 링크 수 | 언어마다 awin1.com 1개, rel="sponsored noopener" 1개, 이름 "Stylevana(제휴 링크)/(affiliate link)/(アフィリエイトリンク)/(聯盟連結)" |
| data/affiliates.json `stylevana_home` | url이 4개 페이지 href(&amp; 풀어서)와 글자 그대로 같음. build.py는 이 키를 쓰지 않음(기록용) |
| 다른 쇼핑몰 링크 | 올리브영·iHerb·출처 링크 모두 rel="noopener"만 — 일반 링크. 맞음 |
| 사이트 공통 고지·스크립트 | front matter에 disclosure 없음 → 공통 문구 없음, NADRI_DEFER=[] (스크립트 0). 본문 "다른 링크는 일반 링크"와 맞음 |
| 페이지 안 광고 표시 | 있음, 그러나 첫 화면 밖(필수 1), 'Stylevana 링크' 개수 어긋남(필수 2) |
| disclosure.md 10줄(4개 언어) | "Stylevana 링크 하나, buy-from-home 페이지" — 실제와 맞음. KKday만 '승인·미사용'으로 남김 맞음. ko만 "제휴 버튼은 … 링크"라고 함(en·ja·zh-tw는 '링크') — 뜻은 통함 |
| olive-young.md·shopping.md 링크 줄 | 4개 언어 모두 /{lang}/buy-from-home/ 으로 감, 빌드 링크 깨짐 0 |
| 개인정보 페이지 | Awin 이름 없음(필수 6) |
| shop-spec "올리브영(Rakuten) 링크가 들어가는 페이지는 원두 직접 승인"(ops/shop-spec.md:76) | 이 페이지의 올리브영 링크는 일반 링크라 Rakuten 링크 아님 → 해당 없음으로 판정. 원두 [7eb4ec94#3526] "(나)로 진행해"가 공개 절차 |

## 5. 원칙 (판정 3)

| 원칙 | 판정 | 근거 |
|---|---|---|
| 두괄식 [#1192] | 통과 | 첫 화면: 제목·세 가지 질문(lede)·바로가기 3개 → 비교 표 → 자세히 |
| A to Z [#1227] | 부분 | 세금은 나라별 '기준→넘으면→내는 법→공식 링크'. 쇼핑몰은 iHerb 반품 3단계까지, 올리브영 반품은 '안내에서 확인' |
| 따라 하기 [#1233] | 부분 | 세금 판단은 이 페이지로 가능. 올리브영 반품·나라별 배송비는 사이트 차단으로 없음 |
| 블로그 수준 금지 [#1239] | 통과 | 8개 지역 세관 원문 비교 + 쇼핑몰 3곳 공식 수치. 일반 블로그에 없는 수준 |
| '확인 못 함' 칸 | 0개 | 빌드 html 검색 '확인 못' 0. 빈칸은 "○○ 안내에서 확인"으로 바뀜 |
| 불확실 정보 [#2990] | 부분 | 숫자 모두 출처·날짜 있음. 예정 발표를 사실처럼 쓴 1곳(권고 4). Stylevana 줄은 원두 화면 110~119로 전부 대조됨(6절) |
| 내외국인 구분 없음 [#963] | 통과 | '내 나라(받는 곳)'로만 나눔 |
| 임의 분류 금지 [#1605] | 통과 | 나라 구분은 각 세관, K-Beauty 분류는 iHerb 것 |
| 실사 우선 [#1245] | 미반영(그대로) | 사진·공식 화면 0. 이전 독립 검토와 같음 — 공개를 막는 항목으로 보지 않음([7eb4ec94#3295]) |

## 6. 추가 검토 — 커밋 1d34af1·2848f2b (Stylevana 줄, 출처 ㉓㉔)

근거 화면: wondu-archive `raw-from-scratchpad/stylevana-wondu-screens-2026-11-27/`
- 배송 안내(stylevana.com/en_US/shippings): 110.webp(주소창, 처리 시간 목록), 111.png(배송 과정·보내는 곳·표준/익스프레스), 112.png(미국·싱가포르 표), 113.png(필리핀·브루나이), 114.png(남아공·이스라엘·Delivery Time), 115.png(보험·세금·분실), 116.png(파손·누락).
- 반품 안내(stylevana.com/en_US/returns_and_exchanges): 117.png(주소창, Return Policy·Return Types 표), 118.png(How to Make a Return·불량/오배송), 119.png(Change of Mind·Terms and Conditions).
- 115~119는 검토 도중 메인 세션이 더 저장한 것. 처음 판정('원문 사본 없음')은 이 화면으로 바꿈.

| 페이지(ko 기준, 4개 언어 같음) | 화면 원문 | 판정 |
|---|---|---|
| 미국 스토어(en_US) 보내는 곳: 미국·싱가포르·필리핀·브루나이·남아공·이스라엘 | 111: "we currently ship to the United States, Singapore, Philippines, Brunei, South Africa and Israel." | 일치 |
| 다른 나라는 위쪽 국기에서 내 나라 스토어 | 111: "please click on the country name icon above"; 110 위쪽 미국 국기 | 일치 |
| 홍콩 창고에서 보냄 | 111: "All orders will be shipped from our Hong Kong warehouse" | 일치 |
| 물건 준비 시간은 따로 | 110: "order processing time varies … availability status"; 114 Delivery Time | 일치 |
| 미국 US$35 이상(프리미엄 익스프레스) | 111: "Premium Express Shipping is FREE for all orders above $35"; 112 표 Premium Express ≥$35 FREE, Standard ≥$35 N/A | 일치(일반 배송은 무료 없음 — 칸이 '프리미엄 익스프레스'로 밝힘) |
| 싱가포르 US$35 / 필리핀 US$29 / 브루나이 US$58 / 남아공 US$79 / 이스라엘 US$120 | 112~114 각 표 "Order Value ≥$35 / ≥$29 / ≥$58 / ≥$79 / ≥$120 — FREE" | 일치(5개) |
| 미국 일반 8~15·익스프레스 4~9영업일 | 112: "Within 8 - 15 business days" / "Within 4 - 9 business days" | 일치, **지연 안내 누락(필수 5)** |
| 싱가포르 3~7 / 필리핀 3~6 / 브루나이 7~12 / 남아공 12~20 / 이스라엘 6~10영업일 | 112~114 "Within 3 - 7 / 3 - 6 / 7 - 12 / 12 - 20 / 6 - 10 Business Days" | 일치(5개) |
| 통화 'US$' | 110: "Once payment (settled in USD)" | 일치 |
| 배송 보험은 선택, 주문 금액의 4% | 115: "We offer optional insurance for each shipping service … The insurance fee is 4% of the order subtotal." | 일치 |
| 파손·누락: '배송 완료' 뒤 48시간 안 | 116: "within 48 hours of receipt*" / "*The receiving date is the date that parcel status is shown as 'delivered'" (파손·누락 두 절 모두) | 일치 |
| 주문번호와 상자·물건 사진으로 신고 | 116: "order number, item name and all photos of the package, including inner and outer box, courier bag, wrapped bubbles and product photos" | 일치(줄여 씀 — 상품명·SKU·완충재·라벨 사진은 생략, 틀림은 아님) |
| 받은 날부터 14일 안에 신청 | 117: "You have 14 days from the receipt date to request a return"; 118: "Return requests past 14 days will be rejected." | 일치 |
| 안 쓴 새 제품·원래 포장 그대로 | 117: "only applies to unused items with all new and original packaging, as well as having original tags attached" | 일치 |
| 홍콩 창고로 보냄 | 117: "For any return cases, please send your parcel to our Hong Kong Warehouse." | 일치 |
| 단순 변심: 반품 배송비 내가 냄 | 119: "You will be responsible for the return shipping charges for change of mind return reason." | 일치 |
| 단순 변심: 환불은 쿠폰 코드 | 119: "Refunds for change of mind items will be issued in the form of a coupon code." | 일치(권고 10) |
| 샘플·사은품·클리어런스 반품 안 됨 | 117 표: "Samples, Free Gifts, Clearance — Not Available"(불량·오배송·변심 모두) | 일치 |
| 피부 트러블 반품 안 됨 | 119 T&C 4: "We do not offer refunds or returns in cases involving allergic reactions or adverse skin conditions" | 일치 |

- 4개 언어: Stylevana 줄의 나라 6곳·금액 6개·영업일 7쌍·4%·48시간·14일·불가 품목이 4개 언어 모두 같음(1d34af1·2848f2b diff 대조). 차이 없음.
- 출처 표기: 48시간·보험 문장 끝에 ㉓, 반품 문장에 ㉔ — 화면 주소(110·117 주소창)와 맞음.
- 출처 ㉓㉔의 Stylevana 주소는 일반 링크 → 필수 2와 연결.
- 커밋 21dd8a0 메시지 '7장'과 그 커밋의 실제 5장은 다르다(뒤에 115~119 추가). 보관소 커밋 기록만 맞추면 됨.

### 6-1. Stylevana 줄 권고 (화면에 있는데 페이지에 없는 조건)

10. **반품 조건 두 가지 더**(118·119): "Returns must be packed and shipped within 7 business days after our Vana Returns Team authorizes the return. If you do not ship … we will regard your return request as cancelled."(승인 뒤 7영업일 안에 안 보내면 취소), "the original shipping fee you paid for on your order is non-refundable"(처음 낸 배송비는 안 돌려줌). 또 불량·오배송도 돈이 아니라 "replacement item instead of a refund. If replacement items are out of stock, item value will be refunded in the form of coupon code"(교환품, 품절이면 쿠폰). 지금 칸은 '단순 변심은 쿠폰'만 써서 불량이면 돈으로 받는다고 읽힐 수 있음. 제안(ko): "승인 뒤 7영업일 안에 보내야 해요. 처음 낸 배송비는 안 돌려줘요. 불량·오배송은 교환품(품절이면 쿠폰)이에요 ㉔" — en/ja/zh-tw 같은 뜻.
11. **분실·브루나이**(115): 분실 의심은 "within 14 business days* after the tracking is sent to you"(송장번호 받은 뒤 14영업일 안 신청). 브루나이는 "customers are considered the Importer of Record and are solely responsible for all applicable taxes, duties … No refund or replacement will be issued for items seized"(고객이 수입자, 세금 전부 고객 부담, 압수 시 환불·교환 없음). 브루나이 독자에겐 중요([7eb4ec94#2954] 3).

## 7. 범위 밖이지만 알림

- `git diff origin/main...HEAD` 전체에는 build.py(목차·사진 짝 배치 변경), data/shop-trends.json, drafts 다수, static 그림이 함께 있다. 이 검토는 위 대상 파일만 봤다. main에 올릴 때 대상 파일만 골라 올리는지 메인 세션이 확인해야 함.
- 이 검토 중 포트 8765에 다른 http 서버(13:40 시작)가 떠 있어 옛 빌드를 보여 줬다. 그 프로세스는 내가 띄운 것이 아니라 건드리지 않았다. 내 서버는 포트 8791.
