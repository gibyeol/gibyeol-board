# Brief for writing a Nadri guide page (read fully before writing)

Nadri (https://nadri-guide.pages.dev) is a Korea travel guide in four editions: en (US-first English), ja (Japan), zh-tw (Taiwan, Traditional Chinese), ko (Korean readers). Goal: a visitor can solve Korea travel A to Z here, with information we checked.

## Principles (non-negotiable)
1. Start from the reader's real job: who is reading, what they are trying to get done right now. Answer the question people actually search, in their words (see /home/claude/trendmin-threads/ops/questions-2026-11.md).
2. Only checked facts. Every number, date, price, rule needs an official or major-press source you actually opened, with its date. If you cannot confirm it, leave it out or say plainly it is unconfirmed. Never invent experiences ("I tried", "my friend said"), reviews or quotes.
3. Judgment, not lists. Open with our call (a short "one-line judgment" table: situation → what to do → why). Pick three, show why, say what you left out and who does NOT need it. Opinions are clearly ours, grounded in the facts.
4. Reader's side, not the brand's. No fake urgency, no inflated discounts, no disparaging people, places or countries. Medical/beauty topics: facts and process only, no outcome promises.
5. Localize, do not translate. Same facts in every edition, but each edition answers what that market asks (ja: yen, JCB, repeat visitors, gentle tone; zh-tw: TWD, Taiwan habits, numbers first, Taiwan terms; en: insider "what locals do", plain and light; ko: Korean readers, natural 해요체 as in content/ko/*.md).
6. Every thing we name gets a way to reach it. The build auto-links names registered in /home/claude/gibyeol-board/data/links.json. If you name an app or official service that is not there, add a proposal to your report with VERIFIED official URL / App Store id / Google Play package (from the store listing or official site). Inline official links in Markdown are fine too.
7. Quality over quantity. 700–1,400 words per edition is plenty. No filler, no "In conclusion".

## Format (look at these first)
- Examples: /home/claude/gibyeol-board/content/en/essentials.md, content/en/airport-to-seoul.md, drafts/money/en.md, and the same files in ko/ja/zh-tw.
- Supported Markdown (build.py subset): front matter; ## and ### headings; paragraphs; - lists; 1. lists; | tables |; > note lines; **bold**; [links](url); raw HTML lines; shortcodes on their own line: {{aff:KEY|label}} (affiliate, only if genuinely the easiest option for the reader; live keys: yesim_kr, klook_esim, klook_esim_alt, klook_airport, klook_tmoney, klook_wowpass) — if you use one, set `disclosure: yes`.
- Front matter:
```
---
title: ...
description: ... (one sentence, ≤160 chars)
lede: ... (2 sentences, our judgment)
section: <slug-group, e.g. essentials | seoul | transport | shopping>
updated: 2026-11-25
---
```
- End with `## Sources` (or the localized heading used in that language's existing pages) and a `<p class="sources">…</p>` line listing sources with dates.
- Internal links use the language prefix: en "", ja "/ja", zh-tw "/zh-tw", ko "/ko" (e.g. /ja/tax-refund/). Live pages: essentials, airport-to-seoul, tax-refund, olive-young, deals, money, seoul-areas, winter, getting-around, e-arrival-card, ktx-busan, convenience-store, everyday, departure-day, guides. Link to them instead of repeating their content.

## Output
Write four files: /home/claude/gibyeol-board/drafts/<slug>/en.md, ko.md, ja.md, zh-tw.md. Do not touch content/, build.py, data/ or git. Then self-check every fact against your notes, and report back: slug, titles, a list of facts with source URL+date, links.json proposals (verified), and anything you left out as unconfirmed.
