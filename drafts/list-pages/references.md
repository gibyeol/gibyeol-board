# References: category list screens (guide list cards draft, 2026-11-26)

Draft for 원두's review. Branch `draft/list-pages`. Not published; main is untouched.
Owner's ask: [7eb4ec94#1466] "카테고리를 눌러서 보이는 이 목록들이 접근성이 굉장히 안좋아 … 이미지나 구조를 바꿔서 개선할 방법을 찾아야해."
Approved reading [7eb4ec94#2500]: text list → cards, each with a picture, a one-line purpose and a key number; research good list screens first.
Reference rule [7eb4ec94#1760]: "각종 레퍼런스를 기준으로 구성".

We borrowed layout ideas only. No design, image, icon or text was copied from any of these sites.

## What I could actually look at today
Method: headless Chrome through the session proxy, 1280 px and 390 px wide, study screenshots kept in the scratchpad only
(`/tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/list-pages/ref/`), never published.
A blocked site was skipped. No retry, no workaround.

| Site | Page | Result |
|---|---|---|
| Visit Seoul (official) | english.visitseoul.net/attractions, /curation, / | Loaded. Screenshots taken |
| VisitKorea (official, KTO) | english.visitkorea.or.kr/svc/main/index.do | Loaded. Screenshots taken |
| Klook | klook.com | 403, skipped |
| Creatrip | creatrip.com/en | 403, skipped |
| App Store (web) | apps.apple.com | 429 (rate limited), skipped |
| Lonely Planet, Airbnb, Trip.com, GetYourGuide, Tripadvisor, Time Out, MyRealTrip | home / list pages | Not allowed by this session's network, skipped |

For Klook, Airbnb and the App Store "Today" tab I only have web-search summaries (third-party write-ups, not the live screens).
Those rows below are marked **(search only)**; treat them as weaker evidence.

## What each reference does, and what we took

| Reference | What we saw | Taken into the draft | Why (owner's words) |
|---|---|---|---|
| **Visit Seoul, Attractions list (PC 1280)** | 4-column grid of picture-on-top cards. Each card: photo, name, 2-line description (cut off with "…"), one line with a number (Tripadvisor rating + review count). Category tabs above the grid (All / Landmark / Palaces / Historical Sites / Galleries & Museums) | **4 columns on PC**, picture on top, one number line on every card that has one, **group links above the grid** | PC must not be a narrow phone column [7eb4ec94#1114]; numbers pull the eye [7eb4ec94#1776] |
| Visit Seoul, same page (phone 390) | One column of full-width picture-on-top cards, each about 300 px tall; text is small grey | **Not taken.** 29 guides at ~300 px each would be a very long scroll. We use compact rows on phones instead (next row) | 두괄식 [7eb4ec94#1192]: the core of every guide should be visible quickly |
| Visit Seoul, weak points | Description cut mid-sentence with "…"; card text very small on PC; a cookie bar covers cards | **Avoided:** our line is a whole sentence (never cut), card text ≥ 0.9 rem, title 1.06–1.12 rem bold | Accessibility "어린아이도 편하게" [7eb4ec94#860] |
| **VisitKorea, home (phone 390)** | "News & Announcements" as compact rows: small square thumbnail left, bold title right, a date line under it. Category shortcuts as a row of icon + label tiles (Travel Basics, Transportation, Shopping, Food, Accommodations, Weather) | **Phone = compact rows** (square picture 92 px left, title, number, one line right). **Line icons + label** for guides without a photo | Scannable list on phone; icons say the topic before the words are read |
| VisitKorea, weak point | Several thumbnails were grey "VISITKOREA" placeholders | **Avoided:** a card with no real photo gets a clear icon tile (or its key number in big type), never an empty placeholder | "불편한 이미지가 없으며" [7eb4ec94#1776] |
| **App Store "Today" (search only)** | Large story cards where big type carries the card | **Key number as the picture** on PC/tablet for guides without a photo: e.g. "119 · 1339", "−5.5°C", "1,000~3,000원" set large on the night band | A number that is understood at a glance [7eb4ec94#1776] |
| **Klook (search only)** | Activity cards with photo, title and price as a prominent figure; tappable category shortcuts | Key number in **red bold** directly under the title (like a price) | Same |
| **Airbnb (search only)** | Category bar of short labels above the listing grid; picture with fixed aspect ratio; whole card is the link | **Jump links** to the 7 situations (pill-shaped, wrap on phone, no sideways scrolling); fixed 16:10 picture; **whole card is one link** (big tap target) | Accessibility [7eb4ec94#860] |

## Decisions in the draft (Claude's proposal, not owner decisions)
- **Order inside a card (두괄식 [7eb4ec94#1192]):** picture → short title → key number → one line. The full description stays on the guide page itself.
- **All text on a card is copied word for word from that guide** (title before the colon, a number and a sentence from the lede, description or body). `build.py` stops the build if a card number or line is not found on its page. Nothing is written new for the card.
- **Key numbers are only real ones from the page** (e.g. airport: "43~80분 · 4,650~18,000원" from the lede). Guides with no fitting number get none (jeju, olive-young, shopping-streets, duty-free, seoul-areas, food, concert-trip, everyday, first-trip). The deals card counts the deals on now from `data/deals.json` at build time.
- **Pictures:** a guide's own photo where the guide already shows one (10 guides; license in `data/photos.json`, credited under the list with author, license link and "수정함"). Otherwise a Lucide line icon (ISC license, `static/icons/LICENSE.txt`). No drawn people or products [7eb4ec94#1747].
- **Group headings stay** (출발 전 준비 … 응급 상황) with a guide count; '한국 여행 가이드' stays as the sub-heading [7eb4ec94#1146].
- **Widths:** phone 1 column (compact rows) · ≥600 px 2 columns · ≥900 px 3 · ≥1120 px 4. A group with a single guide shows one wide card instead of a lone small card.

## Open for 원두
1. Photos: `data/photos.json` already has licensed photos that the guides themselves do not show yet (palace-1..3, bukchon-1, jeju-1/2, ktx-1, busan-1/2, food-1, market-1/2, winter-1, myeongdong-1, seongsu-1, hongdae-1/2, seoul-taxi, tmoney-card). Using them would turn most dark icon tiles into real photos (owner prefers real photos [7eb4ec94#1245]). The draft does not use them because the brief said "reuse the page's own hero photo, else icon". Switching is one field per guide in `data/list-cards.json` plus relaxing one rule in `check_cards()` (today a card photo must already appear on its guide).
2. Convenience-store card: the store-front photo (CU sign, recognisable) is used. The ramyeon-wall photo on the same page is more "군침" but shows a ramyeon-themed store, not a typical one.
