# Nadri

Korea travel, shopping and culture guide. Static site, no dependencies.

## Build
```
python3 build.py      # writes dist/
```
Cloudflare Pages settings: **Build command** `python3 build.py`, **Build output directory** `dist`.

## Where things live
| Path | What |
|---|---|
| `content/<lang>/<slug>.md` | One page. Same slug in several languages = translations (hreflang is automatic) |
| `data/deals.json` | Deals board. Set `confirmed: true` once the store announces dates. Items disappear after `end` |
| `data/affiliates.json` | Paste approved tracking URLs. Empty `url` hides the button everywhere |
| `data/site.json` | Languages, menus, UI text, `base_url` (change when the domain is bought) |
| `static/` | CSS, logo, favicon |

## Writing rules
- **Every page exists in every language, no exceptions** (en, ja, zh-tw, ko). A new page or change goes into all four `content/<lang>/` folders in the same commit. `build.py` stops with an error if any language is missing a page.
- Front matter: `title`, `description`, `lede`, `section` (essentials / oy / tax / deals), `disclosure: yes` on pages with affiliate buttons, `updated`.
- Shortcodes on their own line: `{{deals}}`, `{{deals:2}}`, `{{aff:key|Button text}}`.
- Every guide ends with a Sources section. Byline is "the Nadri editors"; never write as if we used a product.
