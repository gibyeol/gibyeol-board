# shopC progress (olive-young, tax-refund) — 2026-11-26

Writer: shopC subagent. Git read-only; coordinator commits.
Photo catalog entries: drafts/photos-shopC.json. Substitutes: /home/user/trendmin-threads/ops/improvements.md.
Screenshots: /tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/shopC/

## Status
- [x] olive-young (ko, en, ja, zh-tw) — done. approved: none; updated 2026-11-26; build OK; internal links/anchors OK; screenshots scratchpad/shopC/{ko_,,ja_,zh-tw_}olive-young-part*.png (pages >15,000px are shot in 3,000px parts; ko_olive-young.png is a stale blank full-page shot, ignore).
- [x] tax-refund (ko, en, ja, zh-tw) — done. approved: none; updated 2026-11-26; build OK; links OK; screenshots scratchpad/shopC/{ko_,,ja_}tax-refund-part*.png, zh-tw_tax-refund.png.
- Also touched: content/*/seoul-subway.md line 17 (added id="map-app" to step 1 so olive-young can link the map-app section; no text change); static/fig/ko/olive-young-4.svg + tools/figgen/core-B/fig_shop.py ('유행템' → '유행하는 상품'); new tools/figgen/taxrefund_maps.py → static/fig/<lang>/tax-refund-t1map.svg, t2map.svg (README row added).

## olive-young — principle check (each with where on the page)
- 본질(어느 매장이든 서울 사람처럼): PASS — "매장은 네 종류예요"(동네/글로벌관광상권/타운/특화), "매장 안에서: 입구 → 구역 → 써 보기 → 계산대"(any store, Myeongdong Town floor list as the worked example), "가까운 매장 찾기"(skill for any store), 교환·환불, 회원·쿠폰.
- 두괄식: PASS — first screen: title/lede, 3 buttons (계산하는 법·가까운 매장 찾기·다음 세일), hero, 4 key facts (여권 실물, ₩15,000, 봉투 유료, 다음 세일), who-qualifies note; details (table, sources) collapsed.
- A to Z (every verb): PASS — 찾기(지도 앱 3 steps + /seoul-subway/#map-app), 영업시간 보기, 길찾기, 가기(역·출구·거리·주소), 고르기/써 보기(+kbeauty link), 묻기(국기 배지·AI 도우미), 여권 내기→결제→확인, 카드 실패/₩100만 이상/₩500만 초과/여권 없음/제외 물품, 봉투·포장(가격), GTF 데스크, 교환·환불(조건 4개), 세일(할인 상황판 link), 회원(글로벌몰), 다시 사기(Global/US links).
- 따라 하기: PASS with one gap — 계산대 3단계 has "how do I know it worked"(낸 금액 < 가격표 합계) and "what if" list. Gap: exit-to-store walking direction in Myeongdong is text (distances + 3 landmarks), not a map (no official geometry today) → improvements.md.
- 길 찾기: PARTIAL→PASS for what is sourced — 명동 타운: 4호선 명동역 8번(356m)·2호선 을지로입구역 5번, 주소, 랜드마크 관광정보센터(5번 출구 211m, 매장 70m)·하동관 50m·로얄호텔서울 70m(Visit Seoul); N 성수: 4번 출구 118m, 연무장길 시작, 출구 앞 팝업 줄, 팩토리얼 성수 건물 + photo. No redrawn map (would need guessed geometry) — logged.
- 실사 우선: PASS with substitutes logged — real photos: hero, Myeongdong till sign, Wonju shelf tag/till (labelled "다른 지점"), Yeonmujang-gil, sunscreen/sheet mask; substitutes (SVG 1–5, other-branch photos, no exit photos) in ops/improvements.md.
- 블로그 수준 아님: PASS — essay paragraph deleted; numbered steps, icons on each element; hard words replaced (기본템→처음 살 것, 구색→상품 종류, 가성비→같은 돈에 더 많이 들어 있는, 유행템→유행하는 상품; 택스리펀드 대상자 explained once in the top note, then "대상").
- 사실 출처: every new fact from a page opened 2026-11-26 (sources block); not reopened today and marked: OY Global US help notice (blocked), zh-tw Taiwan shipping/first-order offer (blocked).
- 사실 손실: numbers diff vs HEAD = none lost (only the deals-board date 11/18 dropped, replaced by CJ 2025-03-24 Olive Day source). Wording removed: "매장이 스캔" (not sourced; now "여권으로 대상 확인", VISITKOREA), essay paragraph (its facts kept).

## tax-refund — principle check
- Action verbs → where/how/link: 찾기(Tax Free 표시: 사진, 없으면 묻기), 여권 내기(사진), 확인하기(낸 금액), 전표 요청(필수 항목·보관), 시내에서 받기(어디서: 전표의 회사 창구·GTF 데스크 명동 타운 2층, 가져갈 것 3개, 한도 600만, 21/15일, Global Blue map link), 체크인(손에 들기, 부칠 때 태그), 세관 확인(키오스크 B·E·J·L/F·G, 검사 대상이면 세관 데스크 E·J/F·G + 가져갈 것, 모바일 확인 URL, 대형 수하물 컨베이어), 돈 받기(28번 게이트 창구·무인기, 탑승동 약국 옆, 2터미널 249/270 vs 250/253, 무인기 사용법, 통화), 막히면(전화 3개), 창구 없는 공항(우편함), 다른 공항(표).
- 따라 하기 — 계산대: PASS (sign photo, till photo, check, what-if list). 시내: PASS for GTF (명동 타운 2층, exit 8) and generic for other companies (map link); no photo (logged). 공항: PASS — real photo of T1 3F departure entrance + redrawn T1/T2 maps (letters, kiosks, customs, gate 28 / 249·270) + 3 numbered steps with what-if; the airport's two pages disagree on T2 counter gates and T1 counter hours (24H in list vs 07:00–22:00 on refund page) — both shown/hours from refund page + VISITKOREA.
- 두괄식: PASS — first screen unchanged in spirit (3 buttons incl. 공항에서, hero, 4 facts); detail tables collapsed.
- 실사 우선: PARTIAL, logged — no licensed photo of kiosk/customs desk/refund counter; maps + departure-hall photo used.
- 블로그 수준 아님: PASS — zh-tw "依這頁的規定拼出的畫面,不是編出來的心得" line deleted (owner 11:09 rule); "끝 장면" sentence replaced with an instruction.
- 사실 손실: numbers diff vs HEAD = none lost. Removed: tax-refund-4 figure (its order "세관 확인 먼저 → 그다음 짐 부치기" conflicts with airport.kr: check in first, keep goods in hand or tag the bag; its facts stay in text); "대부분의 대형 체인(백화점 포함)에 표시" (not verifiable today; replaced by airport.kr "가맹점 확인"); "매장이 스캔" wording.
- Not reopened today (marked in sources): law.go.kr (blocked; same numbers re-checked in VISITKOREA, Visit Seoul, Global Blue, korea.net), operator rate table (5–8% re-checked in OY FAQ).

## Sources opened today (2026-11-26 KST) — research notes
- myeongdongtown.oliveyoung.com/ko,en,ja,zh (company site, facts only): FAQ — 즉시환급 실물 여권·1.5만 원 이상, 위생용품·쇼핑백·건과일 제외; 사후환급(여권 미지참·관세청 미등록·6개월 이상 체류) → 환급전표 → 공항 환급 창구; 영수증 1장 1.5만~100만 원, 한도 500만 원, 5~8%, 천 원 단위; 같은 GTF 전표는 2층 글로벌서비스라운지 GTF 데스크(실물 여권); 교환·환불 15일·미개봉·결제수단+영수증, 환불은 구매 매장만, 교환은 같은/이상 금액 전국; 종이봉투 100원·리유저블백 500원; 선물 포장 기프트박스 1,000~2,500원; 개인물품 보관 안 함; 멤버십 = 한국 거주+본인 명의 연락처, 회원 특가는 한국 계정 회원만, 외국인은 글로벌몰 회원; 화장실 없음; 대량 주문 불가; 명동길 53, 10:00~22:30, 4호선 명동역 8번·2호선 을지로입구역 5번; 층별: 1층 스킨케어·선케어·마스크·기획전·계산대, 2층 헬스·푸드·헤어·맨즈·바디·계산대·툴·메이크업·럭스에딧·향수·글로벌서비스라운지(와이파이·휴식·회원 선물)·GTF 데스크.
- english.visitseoul.net Olive Young (Myeongdong Flagship Store) ENP012015 (edited 2026-11-24): 명동역 8번 출구 356m, 10:00–22:30; nearby: 하동관 50m, 명동관광정보센터 70m, 로얄호텔서울 70m. Myeong-dong Tourist Information Center ENP011469 (edited 2026-09-18): 을지로 66 하나금융그룹 명동사옥 별관 1층, 을지로입구역 5번 출구 211m. Hadonggwan ENP005614: 명동9길 12, 을지로입구역 5번 276m.
- Visit Seoul 'Seongsu-dong' (2025 Seoul Trend Dispatch): 올리브영N 성수 연무장7길 13(팩토리얼 성수), 매일 10:00~22:00, 성수역 4번 출구 118m, 2024년 11월 말 개점, 1,400평, 1층 N.플레이그라운드(팝업, 사진 부스 선착순 300명), 2층 뷰티&컬처(럭스 에딧, 예약 무료 메이크업·퍼스널 컬러), 3층 스킨&웰니스(시트마스크 구역 붐빔), 4층 VIP 라운지; 예약 매주 금요일 정오 다음 주분; 연무장길은 4번 출구에서 시작, 4번 출구 앞 팝업 줄.
- Visit Seoul Tax Refund page: 3개월, 1.5만 원, 6개월 미만 외국인·해외 2년 이상 거주 3개월 미만 체류 한국인; 즉시환급 1회 100만 원 미만, 합계 500만 원 미만; 시내환급, 우편함 환급.
- cjnews.cj.net: 2025-07-22 글로벌관광상권 110여 매장(외국어 직원, 영문 병기, 인기 상품 입구 근처, 즉시환급 '주요 매장', 센트럴 강남 타운 퍼스널 쇼퍼 45분 예약), 2026-08-31 글로벌관광상권 151개(전체 10% 넘음), 타운 평균 200평 이상, AI 쇼핑 어시스턴트 8개 언어(6월, 서울 일부), 2026-03-26 센트럴 명동 타운(3개 층 약 950평, N 성수 다음 2번째, 1,000여 브랜드·1만5천 상품, 마스크 라이브러리, 유인 계산대 22개, 영·중·일 응대 직원 국기 배지), 2026-02-02 외국인 제휴·할인(돈키호테 회원, 유니온페이·알리페이·위챗페이, 와우패스 5%, 트립닷컴; 2025년부터 클룩 모바일상품권), 2025-03-24 올리브 데이(매달 25~27일, 회원 '올리브 멤버스' 대상 쿠폰), 2025-11-28 어워즈(12월 세일과 연계, 대용량·1+1·굿즈 한정 상품), 2026-02-27/06-04/09-06/06-22 세일 날짜·연 4회.
- Korea Times 2026-06-22 (Olive Young Sale, March/June/September/December, 1,500+ brands); Korea Herald 2026-05-21 (US online mall launch on May 29).
- airport.kr ap_ko/1008 facility list + facilityInfo list (T1 P01, concourse P02, T2 P03); airport.kr ap_ko/898 내국세환급 절차.
- english.visitkorea.or.kr Comprehensive Tax Refund Guide (10/20/2025): airport customs/refund counter locations, hours, currencies; downtown limit 600만 원 이하, 여권·전표·신용카드.
- globalblue.com Korea page; korea.net 2023-11-28; Korea Herald 10633779, 10947687.
- Blocked today: law.go.kr, oliveyoung.co.kr, global.oliveyoung.com, help.global.oliveyoung.com (403), overpass/openstreetmap, map.naver/kakao, juso.go.kr, seoulmetro station pages (redirect), asiae, heraldcorp; Commons API rate-limited.

## Review fixes (tax-refund, 4 languages)
- T1 counter hours: body shows both (airport refund page + VISITKOREA 07:00–22:00; airport facility list 24h); sources block updated; map label now "hours: see text".
- T1 map: gate numbers 50 and 2 removed (no official source opened today shows them); only gate 28 kept.
- Downtown: no second official location found today (Global Blue map is script-only; operator sites blocked; Visit Seoul/VISITKOREA list none) → logged in ops/improvements.md.
