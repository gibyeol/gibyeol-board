# References: how top brands present a light down jacket on PC (2026-11-26)

Study only. The screenshots are in the scratchpad (/tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/fashion/ref/), and they are never published.
Method: one headless Chromium page per site at 1280×800 (locale ko-KR) through the session proxy. Any challenge or 403 was skipped and noted. No retry and no workaround.

## Reachability today
| Site | Page tried | Result |
|---|---|---|
| Uniqlo KR | uniqlo.com/kr/ko/products/E470067-000/00 (남성 울트라라이트다운재킷), E492179 (젠더리스 라이트다운볼륨재킷), E486819 (남성 PUFFTECH컴팩트재킷) | Loaded normally (200, no challenge). Plain curl got 403, but the browser page was served without a challenge. |
| Uniqlo KR magazine | uniqlo.com/kr/ko/contents/lifewear-magazine/lightness-essentials/ | **Access Denied**, skipped |
| Arc'teryx US | arcteryx.com/us/en/shop/mens/cerium-hoody-0521 | Loaded (200) |
| COS | cos.com/en-us/…/funnel-neck-nylon-down-puffer-jacket-navy-1336464001 | **403 Access Denied**, skipped |
| Zara | zara.com/us/en/down-blend-puffer-jacket-p03286303.html | **403 Access Denied**, skipped |
| Patagonia | patagonia.com/product/mens-down-sweater-jacket/84675.html | Error page ("We're working on it"), no product |
| Nike KR | nike.com/kr/w?q=패딩 | Client-side application error, no product |
| Unsplash / Pexels / Photo Korea search | search pages | Unsplash shows a bot wall (307 redirect to a challenge), Pexels 403, Photo Korea mediaList 403. All skipped |
| nbkorea.com, thenorthfacekorea.co.kr, mlb-korea.com, arcteryx.co.kr, patagonia.co.kr | home | Not allowed by this session's network |

## What fits on one 1280×800 screen (product page)
- **Uniqlo KR:** left 60%: images. Right 40%, all above the fold: name → colour swatches (3 circles, colour name in text) → size buttons XS–4XL (sold-out ones crossed out) + "사이즈 안내" link with the tip "구매한 제품과 치수를 비교할 수 있습니다" → **price, large (99,900원)** → **rating 4.4 (119) beside the price** → availability ("12월 중순 판매예정") → quantity + main button → store stock. No spec text on the first screen.
- **Arc'teryx:** a sale banner across the very top ("Black Friday Sale: Up to 40% off", ends Dec 1). Then breadcrumb, left two image columns. Right: name, "New colour" badge, **star rating 3.9 (278)**, **one-line pitch** ("Light, warm down hoody shines as an alpine midlayer and versatile standalone."), **price** ($400), colour swatches (5) with colour name, size buttons. Specs sit below the fold.

## How each element is presented
| Element | Uniqlo KR | Arc'teryx |
|---|---|---|
| First thing | name + colour + size + price | name + rating + one-line pitch + price |
| Key specs / fill | collapsed "소재 정보 / 세탁 방법": shell nylon, fill 90% down / 10% feather; fit as a one-word tag "보통 핏(레귤러)" | Icon tiles ("High warmth-to-weight ratio: 850-fill down", "Packable design"), then a spec list: **Weight 338 g**, **Fit: Fitted**, centre back length M 72 cm, fill 850 European white goose down |
| Colour choice | round swatches + colour code/name (02 LIGHT GRAY) | round swatches + colour name |
| Size guide / calculator | modal with two tabs: **제품 치수** (garment laid flat: length, shoulder, chest width, sleeve) and **신체 치수** (body chest range per size, e.g. M 88–96 cm). Also "구매한 제품과 사이즈 비교" and "신장별 착용 가이드" | "Sizing chart & Fit guide" link + a fit sentence ("trimmer fit … fits over first layers or under outer layers") |
| Fit info | review fit poll **작다 / 딱맞다 / 크다**, each review shows bought size + height/weight band; model height + size worn on images | model height + size worn on the first image |
| Fabric & care | care in plain words: 손세탁만, 드라이클리닝·건조기 불가, how to restore loft | Materials & Care block, per layer |
| Reviews & rating | stars + count next to price; reviews with date, size, colour, fit | stars + count under the name |
| Price & sale | big price; listing tiles carry tags "기간한정가격", "가격인하" | site-wide sale banner with end date at the top |

## What to borrow for Nadri (not a shop: we inform and send people on)
1. **Number first, big:** price or the strongest number is the largest text; the rating (with review count) sits next to it as social proof (real numbers only).
2. **One-line pitch** under the name (Arc'teryx). Everything else goes into collapsed blocks.
3. **Swatches, not paragraphs**, for colour.
4. **Size = two clear tables** (body chest → size; garment flat measurements) plus a "compare with a jacket you own" step. This is exactly Uniqlo's model.
5. **Fit as a tag** (슬림 / 레귤러 / 오버사이즈), which suits a comparison table.
6. **Sale banner with an end date** at the top (Arc'teryx).
7. Specs as short label–value pairs, not prose.

## Owner's infographic references (from the 15:5x messages; images as described in ops/shop-spec.md)
- NSTEADY colour-block card: one top colour (burgundy) + 4 bottom colours (cream, mid-blue denim, black, beige), shown as flat colour blocks with names.
- 오늘의 옷장 colour-tip table: clothing icons with ○△× for each combination.
- Shirt-colour coordination table (product photos; we can't copy the photos, only the structure).
- Size-conversion charts: one row per size, columns = measurements or countries.
Nadri version: flat colour blocks + names, **only combinations a source states**; size table from an official brand chart.
