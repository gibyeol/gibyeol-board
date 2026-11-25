# Figure generators (static/fig/<lang>/*.svg)

Phone-first rule: viewBox width 400, min font-size 16 (see drafts/BRIEF-2026-11-26.md).
Which script owns which figures — run only the owner, or you overwrite later fixes:

| Figures | Owner script |
|---|---|
| shopping-streets-1..7, daiso-2, daiso-4, kbeauty-how-to-choose-4 | gen-shopping.py |
| seoul-subway-1, -4..8, seoul-bus-4..5 | gen_transit.py |
| seoul-subway-2..3, seoul-bus-1..3, daiso-1, daiso-3 | gen-4pages.py (its shopping-streets and daiso-2 data are OUTDATED — do not copy those outputs) |
| kbeauty-how-to-choose-1..3 | gen-kbeauty.py |
| e-arrival-card-*, money-*, tax-refund-* | core-A/ |
| airport-to-seoul-*, getting-around-*, olive-young-*, duty-free-* | core-B/ |
| palaces-1..7, seoul-areas-1..2, food-1..4, departure-day-1..5 | gen-guides2.py |
| essentials-1..5, first-trip-1..3, emergency-1..4, convenience-store-1..3 (essentials also shows airport-to-seoul-1, owned by core-B) | gen-guides1.py |
| health-1..5, skin-clinic-1..3, concert-trip-1..3 | gen-guides4.py |
| jeju-1..3, ktx-busan-1..4, winter-1..2, everyday-1..2 (everyday also shows emergency-1 and seoul-subway-7, owned by gen-guides1.py and gen_transit.py) | gen-guides3.py |

Check every output with verify.js at 340px (text ≥13px, no overflow/overlap) before copying into static/fig.
