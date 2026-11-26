# Brief: accessibility redesign (2026-11-26) — read fully before editing a page

## The owner's words (verbatim, 2026-11-26)
- "현재수준으로는 접근성이 너무 안좋아 … 글만 써있어서 매우 피곤하고, 그냥 글로만 되어 있는 사전펴서 읽는 느낌인데 누가 쓰려고 하겠어."
- "실제 전자입국신고서 캡쳐본을 가져와서 각항목마다 표시를 해서 어디에는 뭘써야 되는지 설명을 해야 이해를 하지."
- "접근성을 어린아이도 편하게 볼 수 있을정도로 바꿔야돼."
- "접근성이 매우 낮음이야, 매우높음으로 바꿔야돼."
- "굉장히 많이 필요해 각각의 요소에 전부, 작은 아이콘 부터 시작해서 정보를 위한 그림까지, 그리고 우리 수익화와 직접 연결할 방법을 찾아야 하고 제휴도 늘려야하고"
- "우리 원칙서에 있잖아. 사람의 심리를 움직여야 한다고"
- Picture quality bar: "최소 퀄리티는 공식사이트에 나와있는 그림 퀄리티 정도야. 실사수준에 최대한 가깝게 정보를 표기해야 도움이돼." Hand-drawn SVGs are "storyboard" quality — replace them with real images wherever possible.
- Korean edition: "한국인들을 위한 컨텐츠가 필요함" — the ko page speaks to the Korean reader directly. Do NOT frame it as "helping a foreign friend" (remove 친구 framing).

## Target: someone skimming the page on a phone understands it in under one minute
1. **First screen** (before any scrolling, 390×844): one real image (photo or official screen) + one big reassuring line ("What it is, for whom, how long, how much") + 1–2 buttons/links for the main action. At most 2–3 lines of visible text.
2. **Do this**: numbered steps; each step = one real image (annotated with numbered red boxes where it shows a screen/machine/sign) + one short phrase per number. Short words, no jargon.
3. **Icons on every element**: who, time, cost, where, warning, tip, done, card/cash, train/bus, etc. Use the free icon set already in static/icons/ (Lucide, ISC license; see static/icons/LICENSE.txt). If you need an icon that isn't there, download that single SVG from the Lucide GitHub repository and add its name to LICENSE.txt. No CDN.
4. **One honest decision**: where a product genuinely helps (affiliate), show it as a picture + one sentence ("not required, but…") + the button. Only live keys in data/affiliates.json; `disclosure: yes` when used. Money never decides the order.
5. **Common mistakes**: a short list with a warning icon.
6. **Everything else collapsed**: `<details><summary>…</summary>` on its own line, markdown inside, `</details>` on its own line. Sources go inside a collapsed block too.
7. **No fact loss**: every fact/number on the current page must survive (visible or collapsed). Compare with `git show HEAD:content/<lang>/<slug>.md` and list anything removed with the reason (only if wrong/outdated).

## Images: where they come from (owner decision 2026-11-26 09:25)
- First: licensed real photos already collected in static/photo/ with data/photos.json (source, author, license, attribution). Put the attribution in the caption.
- Then: real screenshots of official websites/apps captured with Playwright (require('playwright'); chromium.launch() no options) at 390×844, annotated by injecting CSS outlines + numbered badges into the live page before the screenshot. Never submit forms, never enter real personal data, stop before any send/payment. Check and report the site's usage terms (KOGL/copyright notice). Caption: "Screenshot: <site>, captured <date>".
- No AI-generated scenes, no altered signage, no images from blogs/news/SNS.
- Save images as .webp (or .jpg) ≤780px wide under static/fig/<lang>/<slug>-<name>.webp (language-specific screens) or static/photo/. The build accepts {{fig:name|caption}} for .svg/.webp/.jpg/.png.

## Process
- Edit content/en and content/ko first; then ja and zh-tw with the same structure (use the site's own language screen if available).
- Run `python3 build.py`, serve dist/ and screenshot each edited page at 390 width; look at them yourself and fix cramped/confusing spots. Save the page screenshots to your scratch folder.
- Do not use git except read-only; do not push; the coordinator commits.
- Report in Korean: what changed per page, images used (with licenses), what you could not get, loss-check result, screenshot paths.
