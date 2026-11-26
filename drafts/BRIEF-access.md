# Brief: accessibility redesign (2026-11-26) — read fully before editing a page

## The owner's words (verbatim, 2026-11-26)
- "현재수준으로는 접근성이 너무 안좋아 … 글만 써있어서 매우 피곤하고, 그냥 글로만 되어 있는 사전펴서 읽는 느낌인데 누가 쓰려고 하겠어."
- "실제 전자입국신고서 캡쳐본을 가져와서 각항목마다 표시를 해서 어디에는 뭘써야 되는지 설명을 해야 이해를 하지."
- "접근성을 어린아이도 편하게 볼 수 있을정도로 바꿔야돼."
- "접근성이 매우 낮음이야, 매우높음으로 바꿔야돼."
- "굉장히 많이 필요해 각각의 요소에 전부, 작은 아이콘 부터 시작해서 정보를 위한 그림까지, 그리고 우리 수익화와 직접 연결할 방법을 찾아야 하고 제휴도 늘려야하고"
- "우리 원칙서에 있잖아. 사람의 심리를 움직여야 한다고"
- Picture quality bar: "최소 퀄리티는 공식사이트에 나와있는 그림 퀄리티 정도야. 실사수준에 최대한 가깝게 정보를 표기해야 도움이돼." Hand-drawn SVGs are "storyboard" quality — replace them with real images wherever possible.
- Every language edition (including ko) speaks to whoever is reading, about their situation — no Korean/foreigner split, no "helping a foreign friend" framing (owner 2026-11-26 10:00: "한국인/외국인 구분을 할게 아니라 모두가 필요한 정보를 잘 깔끔하게 고시하면 상황에 맞게 모두가 쓸 수 있는거지").

## Before you start and after you finish (owner 2026-11-26 10:10: "모든 새로운 작업이 시작 될때마다 다시 원칙학습하고 검토해서 수행하고 수행 뒤에도 또 검토해")
- Before: read /home/user/wondu-archive/docs/원칙서-current.md in full (parts 1–5), then write one paragraph in your report: the essence of this page (why a visitor opens it, what they must do next, how each part helps and where it connects them).
- After: an independent reviewer (not you) checks your page against the 10 principles, the owner's words above and that essence. Leave your page in a state you would defend line by line.

## Start from the essence (owner, 2026-11-26 09:56: "어떤 행동을 해야할지 고민을 할때 기준은 \"본질\"이라니까 이걸 하는 목적을 다시 생각하고 어떻게 유저들에게 도움이 되고 연결이 될까를 생각해.")
Before every layout choice ask: why does a visitor open this page, what must they do next, and how does each element help them do it and connect them onward (to the official site, to our next page, or to a product that genuinely helps)? Delete what doesn't serve that; show what does. There is NO limit on the number of images — the owner: "사진을 한 장 넣으라는 제한은 없었어. 필요하다면 10장을 넣어도 되지". Use as many real images as understanding needs.

## Target: someone skimming the page on a phone understands it in under one minute
1. **First screen**: the reader instantly sees what this is, whether it applies to them and what to do — with real images (as many as needed) + a big reassuring line + the main action link(s). Little visible text.
2. **Do this**: numbered steps; each step = the real image(s) it needs (annotated with numbered red boxes where it shows a screen/machine/sign) + one short phrase per number. Short words, no jargon.
3. **Icons on every element**: who, time, cost, where, warning, tip, done, card/cash, train/bus, etc. Use the free icon set already in static/icons/ (Lucide, ISC license; see static/icons/LICENSE.txt). If you need an icon that isn't there, download that single SVG from the Lucide GitHub repository and add its name to LICENSE.txt. No CDN.
4. **One honest decision**: where a product genuinely helps (affiliate), show it as a picture + one sentence ("not required, but…") + the button. Only live keys in data/affiliates.json; `disclosure: yes` when used. Money never decides the order.
5. **Common mistakes**: a short list with a warning icon.
6. **Everything else collapsed**: `<details><summary>…</summary>` on its own line, markdown inside, `</details>` on its own line. Sources go inside a collapsed block too.
7. **No fact loss**: every fact/number on the current page must survive (visible or collapsed). Compare with `git show HEAD:content/<lang>/<slug>.md` and list anything removed with the reason (only if wrong/outdated).

## Images: where they come from (owner decision 2026-11-26 09:25)
- First: licensed real photos already collected in static/photo/ with data/photos.json (source, author, license, attribution). Put the attribution in the caption.
- Then: screenshots of GOVERNMENT / public-agency websites (e.g. e-arrivalcard.go.kr, k-eta.go.kr, seoul.go.kr, airport.kr if it is a public corporation page) — allowed under Copyright Act Art. 24-2 (public works free use; checked on law.go.kr 2026-11-26). Owner rule (2026-11-26 10:08): "캡쳐화면을 쓰되, 그냥 그대로 쓰지 말고, 일부씩 잘라서 쓰거나 간단한 편집을 해서 쓰라고" — never a whole screen as-is: crop to the part that matters for that step and add simple edits (numbered red boxes, highlight, blur irrelevant parts). Capture with Playwright (require('playwright'); chromium.launch() no options) at 390×844, annotate by injecting CSS outlines + numbered badges before the screenshot. Never submit forms, never enter real personal data. Caption: "Screen: <site> (<agency>), captured <date>".
- Company websites/apps (Klook, Olive Young, Global Blue, AREX operator, etc.): only if that site's terms clearly allow reuse; otherwise keep the capture in your scratch folder and list it in your report with the terms text.
- No AI-generated scenes, no altered signage, no images from blogs/news/SNS.
- Save images as .webp (or .jpg) ≤780px wide under static/fig/<lang>/<slug>-<name>.webp (language-specific screens) or static/photo/. The build accepts {{fig:name|caption}} for .svg/.webp/.jpg/.png.

## Process
- Edit content/en and content/ko first; then ja and zh-tw with the same structure (use the site's own language screen if available).
- Run `python3 build.py`, serve dist/ and screenshot each edited page at 390 width; look at them yourself and fix cramped/confusing spots. Save the page screenshots to your scratch folder.
- Do not use git except read-only; do not push; the coordinator commits.
- Report in Korean: what changed per page, images used (with licenses), what you could not get, loss-check result, screenshot paths.
