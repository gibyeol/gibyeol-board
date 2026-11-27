# Held: facts read from Uniqlo KR and Arc'teryx US product pages through a headless browser (2026-11-26)

Status: HELD, removed from the live page content/<lang>/winter-light-puffer.md (all 4 languages) on 2026-11-27.
Why: 원두 [7eb4ec94#2990] "차단은 우회하지 않는다" (trendmin-threads CLAUDE.md, 위반 기록 4번). These facts were read with headless Chromium:
- Uniqlo KR: "Plain curl got 403, but the browser page was served without a challenge" (drafts/prototype/references.md:9) = the same pattern as the Musinsa case (curl blocked, browser got through) → block bypass.
- Arc'teryx US: loaded in the same headless browser (references.md:11). No block was recorded for it, but no plain-fetch check was recorded either, so it cannot be shown to be a non-bypass read → held with Uniqlo until re-checked. Whether this one counts as a bypass is the owner's call.
- Musinsa link sentence "매장 쿠폰·코드: 무신사 공식 공지" (and en/ja/zh-tw): the claim that the notice carries coupons/codes came from the headless read of musinsa.com (held-musinsa.md) → removed with it.
Re-check on 2026-11-27: plain curl to www.uniqlo.com and arcteryx.com is refused by this session's network proxy (403 connect_rejected), so nothing could be re-confirmed by an allowed method.

Removed (verbatim originals: git c51c7f3, content/{ko,en,ja,zh-tw}/winter-light-puffer.md):
1. "공식몰 사양 비교" table: Uniqlo Light Down Volume / PUFFTECH Compact / Ultra Light Down rows (price, fill, fit, rating, status) and the Arc'teryx Cerium row; the Musinsa Standard row (Korea Herald) went with the table — the same fact stays in "왜 뜨나요" (첫 물량 품절).
2. "가슴둘레(cm) → 사이즈" scale (Uniqlo body size chart).
3. Label words box: 합성 충전재, 핏(유니클로), 포켓터블, 발수 — kept 필파워 and 솜털:깃털 (Wikipedia), dropped the "예: 90 : 10" example.
4. Tip "울트라라이트다운은 손세탁만, 건조기 X".
5. "사이즈 더 보기": step 1 (Uniqlo chart), Uniqlo quote in step 3, Uniqlo men's Ultra Light Down garment size table, online-only and washing line. Kept the generic measuring steps.
6. "용어 더 보기": Arc'teryx 850 fill example, Uniqlo down ratios, 합성 충전재 / 핏 / 포켓터블 / 발수 bullets. Those four terms are now listed under "아직 쓸 수 있는 출처를 못 찾은 용어".
7. "입어 보고 사기": Uniqlo '매장 재고 현황' sentence; Musinsa coupon/code notice link.
8. Sources: Uniqlo KR product page links and Arc'teryx US product page link.
data/shop-trends.json (branch only, not rendered by build.py) still holds the Uniqlo/Arc'teryx items and the Musinsa codes; not touched.
