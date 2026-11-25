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
- **Every shared page exists in every language** (en, ja, zh-tw, ko). A new shared page or change goes into all four `content/<lang>/` folders in the same commit. `build.py` stops with an error if any language is missing a page.
- **Audience-only pages**: a page written for one audience (e.g. Korean travellers going abroad, in `content/ko/`) adds `only: ko` to its front matter and exists only in that language.
- Analytics: put the Cloudflare Web Analytics token in `data/site.json` → `analytics.cloudflare_token` (public value). Or turn on Web Analytics in the Pages project settings instead; then leave the token empty.
- Front matter: `title`, `description`, `lede`, `section` (essentials / oy / tax / deals), `disclosure: yes` on pages with affiliate buttons, `updated`.
- Front matter extras: `report: no` hides the report button, `byline: no` hides the "checked against official sources" line (tools and hubs).
- Shortcodes on their own line: `{{deals}}`, `{{deals:2}}`, `{{aff:key|Button text}}`, `{{guides}}` (all guide groups), `{{guides:olive-young}}` (only the group holding that page).
- Name stamp (`/name/`): `static/name.js` + `static/hanja-ko.js` (Korean readings of CJK characters, from the hanja package / Unicode Unihan). Add checked Latin-alphabet names to the `LIST` string in name.js.
- `robots.txt` asks AI training crawlers to stay out; search crawlers are allowed. See trendmin-threads ops/content-protection.md.
- Every guide ends with a Sources section. Byline is "the Nadri editors"; never write as if we used a product.
