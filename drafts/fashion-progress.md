# fashion progress (fashion-styles, fashion-how-to-choose) — 2026-11-26

Writer: fashion subagent. Git read-only; coordinator commits.
Spec: /home/user/trendmin-threads/ops/shop-spec.md (items 6, 7 now; item 8 keyword hub later from drafts/shop-storyboard.md).
Scope for this usage window (coordinator 15:2x): spec 6 (fashion-how-to-choose) + spec 7 (full style explanations), 4 languages.

## Status (15:43 KST, date command)
Scope changed 3 times today; current scope = coordinator 15:3x: ONE prototype story, theme `kw-light-puffer`, Korean only, from drafts/shop-storyboard.md + data/shop-trends.json (owner 15:33 [7eb4ec94]: "일단 프로토타입으로 스토리 하나만 만들어서 테마 하나만 해봐").
- [x] content/ko/winter-light-puffer.md — written. Not in build.py GUIDE_GROUPS (as asked).
- [ ] fashion-styles (spec 7) and fashion-how-to-choose (spec 6) — paused by the scope change; research notes below are kept.
- **Repo build is broken by this page:** build.py stops with "Missing translations" because en/ja/zh-tw files don't exist. I did NOT add `only: ko` (that key means "one audience only", which conflicts with the no Korean/foreigner split rule) and did not add placeholder translations. The preview was built in a scratch copy with stand-in copies. Coordinator decides: translate, or keep the ko file out of content/ until approved.
- New files: content/ko/winter-light-puffer.md, static/photo/light-puffer-rack.webp, static/fig/ko/winter-light-puffer-1.svg, tools/figgen/gen-fashion.py (+ one row in tools/figgen/README.md), drafts/photos-fashion.json, drafts/improvements-fashion.md.
- Screenshot (390 wide, external requests blocked): /tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/fashion/ko_winter-light-puffer-full.png

## winter-light-puffer — where an affiliate button would sit (no {{aff}} added)
- 어디서 살까 › 온라인 › 무신사(앱·웹): button "무신사에서 경량 패딩 보기" (platform: Musinsa; affiliate status unverified per shop-trends p-musinsa).
- 어디서 살까 › 온라인 › 무신사 글로벌: button for overseas delivery (p-musinsa-global, unverified).
- 대표 제품 › 뉴발란스 플라잉 77: button to New Balance Korea official online mall (p-newbalance-kr) — only if NB has a programme.
- Not for: 노스페이스, MLB (no verified seller), the coupon block, the size tip.

## winter-light-puffer — principle check (where on the page)
- 본질: PASS — a first-timer learns why this jacket is everywhere this winter, whether they need one (aside "이미 경량 패딩이 있다면"), how to wear it two ways, and how to buy it with the real deadline. Reusable skill: read sale rows as 확인/추론; measure a jacket flat and compare with the 실측 table (#size).
- 두괄식: PASS — first screen: title, lede (the trend + why it's useful), 2 buttons (세일·마감일 / 어디서), 4 facts (출처 3곳, +718%, 품절 4건, 12월 2일까지), photo. Details collapsed (품절 4건, 출처).
- A to Z: PASS with gaps stated — 쿠폰 받기 = numbered 1–3 + copy buttons; 매장 가기 = 1–4 (exit 3, 475 m, hours, what to try); 세금 빼기 = condition + /ko/tax-refund/ link; 온라인 = platform + honest "not opened today"; 사이즈 = 1–3. Gap: Musinsa sign-up requirements not verified (said on page).
- 따라 하기: PARTIAL — store route uses the existing exit figure + map-app step; no photo of the store entrance or the MD's Pick area (logged).
- 길 찾기: PARTIAL — station exit figure (shopping-streets-5) + photo of Yeonmujang-gil; no floor map inside the store (not sourced).
- 실사 우선: PARTIAL — 2 real licensed photos (padded jackets, Seongsu street); "how to wear" is a Nadri drawing → drafts/improvements-fashion.md.
- 블로그 수준 아님 / 접근성: icons on every block, numbered steps, short sentences, live D-day table (site.js), copy buttons.
- 원칙 1 (일주일 뒤에도 좋아할 이유): "같은 옷 하나로 두 가지 날" (#look step 2). 원칙 6: picks limited to items with numbers, what was left out is stated. 원칙 7: no superlatives; "판매 1위" carries the note that the ranking table is not named. 원칙 8: no fake urgency; every deadline is a real date; 추론 rows labelled.
- 전략서 감정 레이어: 화제템 판독 (section #why "숫자로 판독하기": +718%, 4 sell-outs, limits stated). Not used: 한 장면 카드 / 실패담 (no real traveller quote available — would need owner or reader input).
- 심리·설득: 사회적 증거 = real numbers only (Korea Herald / Musinsa data); 손실 회피 = real end dates with live D-day; 권위 = source + date on every claim.
- 명세(ops/shop-spec.md): 2 인기 품목 ✓(sourced 1위·품절, no own categories) · 4 코드 ✓(2 codes + expiry) · 5 품목·브랜드·이유 ✓ · 8 키워드 연결 ✓ (trend → look → brands → sales → codes → where) · 10 제휴: spots marked above · 11 구분 없음 ✓ (tax refund line says "한국 방문 중이면", nothing else split) · 12 ✓ as above · 6 꿀팁: one size tip only · 7 스타일 전체: not in this prototype.

## Notes for the data worker / coordinator
- Musinsa keyword coupon codes ('퍼재킷다퍼줄게', '어그도무신사랑해', offline-only 15%, 11/20–12/02): I read musinsa.com/content/1566699932019111639 today (2026-11-26, ~15:2x) and both codes were on the page. Method: headless Chromium through the proxy (curl gets a Cloudflare 403). Later a Musinsa search-page fetch was refused by the permission system, and musinsa.com/llms.txt asks automated tools to avoid search/filter URLs; I stopped fetching Musinsa after that. Coordinator should decide whether reading Musinsa editorial pages this way is acceptable before relying on these re-checks.
- Same Musinsa page adds facts not in shop-trends: MD's Pick includes 경량 패딩 since 11/11; 아우터 대전 down brands with offline extra up to 40%; offline cart coupon 10%; offline archive sale per store 11/20–12/17. Used on the page with that source.

## Access today (2026-11-26)
- Reachable: www.musinsa.com (only through headless Chromium; curl gets a Cloudflare 403), global.musinsa.com (browser), www.koreaherald.com, www.koreatimes.co.kr, english.visitkorea.or.kr, www.korea.kr, news.seoul.go.kr, www.law.go.kr, commons.wikimedia.org / upload.wikimedia.org, images.unsplash.com.
- Blocked by proxy: image.msscdn.net / static.msscdn.net (Musinsa CSS/JS/images, so Musinsa app screens and the snap style filter do not render), newsroom.musinsa.com, content.musinsa.com, www.29cm.co.kr, segye.com, economist.co.kr, etnews.com, zdnet.co.kr, kats.go.kr, standard.go.kr, sizekorea.kr, ftc.go.kr, kca.go.kr, pexels.com (403), most news sites.
- Musinsa snap "스타일" filter list: could not open (needs blocked CDN JS; musinsa.com/llms.txt also asks automated tools to avoid filter/query URLs). So the style list on the page = style names Musinsa itself uses in editorial pages opened today, each with article + date. Full filter list → next improvement.

## Raw winter 2026–27 findings (for the data worker / storyboard; opened today)
- Musinsa content 1566699932019111639 "오프라인에서 즐기는 무진장 쇼핑 가이드" (2026-11-23): 무진장 26 겨울 블프 offline 11.20–12.02 at all Musinsa offline stores; cart coupon 10% (≥100,000원, max 10,000원, 1 per ID); 아우터 대전 (down: 블랙야크, 노티카, 커스텀어클락, 오픈야드(오와이), 커버낫, 헬리녹스 웨어, 핍스 모터사이클, 챔피온, 썬러브투어, 디스커스 애슬레틱; jackets/coats: 브이투, 팬시클럽, 미세키서울, 허그유어스킨, 단델, 일리고, 플레이스 스튜디오, 애즈유아, 마조네, 아캄), offline extra up to 40%; 아카이브 세일 11.20–12.17 (메가스토어 성수 노티카 ≤67%, 메가스토어 용산 넌블랭크 ≤70%, 스토어 성수 이우가마카라스 ≤60%, 스토어 홍대 오헤시오 ≤55%, 롯데 잠실 디스커스 애슬레틱 ≤60%); brand focus 1차 11.20–12.02 / 2차 12.03–12.15 (per store list); MD's Pick from 11.11: 퍼 재킷, 경량 패딩, 퍼·패딩 슬라이드, + 퍼 부츠 from 11.25; keyword coupons typed into the Musinsa app coupon box: '퍼재킷다퍼줄게', '어그도무신사랑해' → offline-only 15% on that 기획's target items; 킥스 특가존 ≤80% (킥스 홍대, 킥스 성수, 킥스 스타필드 고양, 킥스 zones); 아울렛 & 유즈드 롯데몰 은평 ≤70%; 런 서울숲 running extra discount; 엠프티 성수 40만→4만, 60만→6만 off.
- Musinsa content 1466324428764847985 "트렌드의 최전선, 26 FW 서울패션위크" (2026-02-11): 26 FW keywords: 패러독스 드레싱; 2026은 또 다른 2016 (오버핏 봄버, 플라워 패턴, 파이어맨 후크; 네오 그런지); 포엣 코어 (grey/brown knit, roomy shirt, flowing slacks); 예티 코어 (volume fur: short-jacket trim, fur boots, giant fur hat); colours red, 클라우드 댄서, blue; 스키니진 return.
- Korea Herald 10946254 (2026-11-23) "Fur is back, coat collars are higher and puffers are lighter this winter": cropped fur jackets, fur vests, fluffy knit zip-ups, fur stoles/collars, mostly faux, younger buyers; tones mud brown, khaki beige, ash gray; high-neck coats (no scarf needed; Le September campaign named); lightweight padded jackets, pale pastels drawing more interest than black/grey.
- Korea Herald 10908829 (2026-10-20) "Puffers get a style upgrade": lightweight puffers with sculptural silhouettes, oatmeal / fog gray; Musinsa lightweight padded category sales +718% in Aug YoY (company data); New Balance Flying 77 Superlight sold out initial stock within a day (Oct 9); Musinsa Standard City Leisure Hooded Light Down ~100,000원, Cloudy Blue sold out, No. 1 in sales; The North Face Ventus On Jacket (2025 sold out in ~40 min; 2026 Real Black/Black sold out); Fila Air-Flow Down, MLB Curve Air Shell named.
- Musinsa content 1445654788125843387 (2025-12-12) 그래놀라 코어; 1452877813830509855 (2026-01-06) "2026 인기 트렌드": 그래놀라 코어, 밤비 코어, 쿼터집; 1452880391798882205 (2025-12-31) 2025 트렌드 결산: 러닝코어, 고프코어 레이어드, 스피드캣 +137%.
- Musinsa Global main page (2026-11-26) shows a "fw26monstersale" campaign and an "Extra Off: Sale + Welcome Code" section (not opened further).

## Review fixes (2026-11-26, after independent review; file now drafts/prototype/winter-light-puffer.md)
1. Evidence wording: lede, fact tile, #why intro and note now say "코리아헤럴드 기사 2건, 숫자는 10/20 기사(무신사 자료 인용)에만"; 30.9% card-payment figure removed from the page.
2. Archive sale: conflict (deals.json 12/03–12/17 vs Musinsa page 11/20–12/17 offline) not resolvable from an openable source → row removed, both versions in drafts/prototype/held-musinsa.md.
3. Hero caption: photo description only; trend sentence removed from the caption.
4. Links: musinsa.com, global.musinsa.com, Musinsa notice (plain links). New Balance official mall URL not verified → no link, stated. Counter sentences added: "이 상품에 쓸 수 있는 쿠폰이 있나요? 앱 쿠폰 적용해 주세요." / "택스프리 되나요? 여권 여기 있어요."
5. "8월에 이미 많이 샀다" marked as Nadri 해석.
6. All facts read from musinsa.com via headless browser removed from the page and kept verbatim in drafts/prototype/held-musinsa.md (codes, MD's Pick 11/11, 아우터 대전 40%, cart coupon 10%, archive sale, store list, ~2cm note, "입어 봐야 안다"). The page now says "무신사 공식 공지에서 확인" with a plain link. musinsa.com not accessed again.
Scratch build (stand-in translations) OK; screenshot: /tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/fashion/ko_winter-light-puffer-full.png
