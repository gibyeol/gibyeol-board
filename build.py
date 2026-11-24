#!/usr/bin/env python3
"""Nadri site builder. No dependencies: python3 build.py -> dist/

content/<lang>/<slug>.md   page source (front matter + markdown subset)
data/site.json             languages, navigation, UI strings
data/affiliates.json       affiliate links; empty url = not shown
data/deals.json            deals board entries
static/                    copied as-is
"""
import html, json, re, shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
SITE = json.loads((ROOT / "data/site.json").read_text(encoding="utf-8"))
AFF = json.loads((ROOT / "data/affiliates.json").read_text(encoding="utf-8"))
DEALS = json.loads((ROOT / "data/deals.json").read_text(encoding="utf-8"))
BASE = SITE["base_url"].rstrip("/")
CURRENT = ' aria-current="true"'


# ---------- markdown subset ----------
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)

    def link(m):
        text, url = m.group(1), m.group(2)
        ext = url.startswith("http")
        attrs = ' rel="noopener" target="_blank"' if ext else ""
        return f'<a href="{url}"{attrs}>{text}</a>'
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, t)


def shortcode(line, lang):
    m = re.fullmatch(r"\{\{(\w+)(?::([\w-]+))?(?:\|(.+))?\}\}", line.strip())
    if not m:
        return None
    kind, key, label = m.groups()
    if kind == "deals":
        return deals_board(lang, limit=int(key) if key else None)
    if kind == "aff":
        a = AFF.get(key, {})
        if not a.get("url"):
            return ""  # not approved yet: render nothing
        return (f'<p class="aff"><a class="aff-btn" href="{a["url"]}" rel="sponsored noopener" '
                f'target="_blank">{inline(label or a.get("label", key))}</a>'
                f'<span class="aff-note">{SITE["ui"][lang]["aff_link"]}</span></p>')
    return None


def md(src, lang):
    out, para, lst, tbl = [], [], None, []

    def flush():
        nonlocal para, lst, tbl
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para = []
        if lst:
            tag, items = lst
            out.append(f"<{tag}>" + "".join(f"<li>{inline(i)}</li>" for i in items) + f"</{tag}>")
            lst = None
        if tbl:
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in tbl
                    if not re.fullmatch(r"\|?[\s:|-]+\|?", r.strip())]
            head, body = rows[0], rows[1:]
            out.append('<div class="table"><table><thead><tr>'
                       + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
                       + "</tbody></table></div>")
            tbl = []

    for raw in src.splitlines():
        line = raw.rstrip()
        sc = shortcode(line, lang) if line.startswith("{{") else None
        if sc is not None:
            flush(); out.append(sc); continue
        if not line.strip():
            flush(); continue
        if line.lstrip().startswith("<"):  # raw HTML line (used by home pages)
            flush(); out.append(line); continue
        if line.startswith("|"):
            if para or lst: flush()
            tbl.append(line); continue
        elif tbl:
            flush()
        h = re.match(r"(#{2,3}) (.+)", line)
        if h:
            flush()
            lvl, text = len(h.group(1)), h.group(2)
            hid = re.sub(r"[^\w]+", "-", text.lower()).strip("-")
            out.append(f'<h{lvl} id="{hid}">{inline(text)}</h{lvl}>'); continue
        if line.startswith("> "):
            flush(); out.append(f'<aside class="note">{inline(line[2:])}</aside>'); continue
        ul, ol = re.match(r"- (.+)", line), re.match(r"\d+\. (.+)", line)
        if ul or ol:
            tag = "ul" if ul else "ol"
            if para: flush()
            if lst and lst[0] != tag: flush()
            if not lst: lst = (tag, [])
            lst[1].append((ul or ol).group(1)); continue
        if lst and raw.startswith("  "):
            lst[1][-1] += " " + line.strip(); continue
        if lst: flush()
        para.append(line.strip())
    flush()
    return "\n".join(out)


def parse(path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        for l in fm.strip().splitlines():
            k, _, v = l.partition(":")
            meta[k.strip()] = v.strip()
    return meta, body


# ---------- deals board ----------
def deals_board(lang, limit=None):
    ui = SITE["ui"][lang]
    items = [d for d in DEALS["items"] if lang in d.get("text", {})]
    today = date.today().isoformat()
    items = [d for d in items if d.get("end", "9999") >= today]
    items.sort(key=lambda d: d.get("start", ""))
    if limit: items = items[:limit]
    if not items:
        return f'<p class="empty">{ui["deals_empty"]}</p>'
    rows = []
    for d in items:
        t = d["text"][lang]
        status = ui["deal_confirmed"] if d.get("confirmed") else ui["deal_expected"]
        when = t.get("when", "")
        link = ""
        if d.get("aff") and AFF.get(d["aff"], {}).get("url"):
            link = f' <a href="{AFF[d["aff"]]["url"]}" rel="sponsored noopener" target="_blank">{ui["deal_go"]}</a>'
        rows.append(f'<li class="deal {"ok" if d.get("confirmed") else "tbc"}"><div class="deal-when">{inline(when)}'
                    f'<span class="deal-status">{status}</span></div><div class="deal-body"><strong>{inline(t["title"])}</strong>'
                    f'<span>{inline(t["note"])}{link}</span></div></li>')
    checked = DEALS.get("checked", "")
    return (f'<ul class="deals">{"".join(rows)}</ul>'
            f'<p class="deals-checked">{ui["deals_checked"].format(date=checked)}</p>')


# ---------- layout ----------
def page(lang, meta, body_html, path, alternates):
    ui, L = SITE["ui"][lang], SITE["languages"][lang]
    title = meta.get("title", "Nadri")
    full_title = title if meta.get("home") else f"{title} | Nadri"
    desc = meta.get("description", ui["tagline"])
    canonical = f"{BASE}{path}"
    nav = "".join(f'<a href="{L["prefix"]}{href}">{label}</a>' for href, label in ui["nav"])
    langs = "".join(
        f'<a href="{alternates[l]}" hreflang="{SITE["languages"][l]["hreflang"]}"'
        f'{CURRENT if l == lang else ""}>{SITE["languages"][l]["name"]}</a>'
        for l in SITE["languages"] if l in alternates)
    hreflang = "".join(f'<link rel="alternate" hreflang="{SITE["languages"][l]["hreflang"]}" href="{BASE}{u}">'
                       for l, u in alternates.items())
    if "en" in alternates:
        hreflang += f'<link rel="alternate" hreflang="x-default" href="{BASE}{alternates["en"]}">'
    head_extra = "".join(SITE.get("head_meta", []))
    if meta.get("disclosure") == "yes":
        body_html = f'<p class="disclosure">{ui["disclosure_inline"]}</p>' + body_html
    byline = ""
    if not meta.get("home") and meta.get("updated"):
        byline = f'<p class="byline">{ui["byline"].format(date=meta["updated"])}</p>'
    lede = f'<p class="lede">{inline(meta["lede"])}</p>' if meta.get("lede") else ""
    header_block = "" if meta.get("home") else f"<header class=\"page-head\"><h1>{inline(title)}</h1>{lede}{byline}</header>"
    return f"""<!doctype html>
<html lang="{L['hreflang']}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">{hreflang}
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website"><meta property="og:url" content="{canonical}"><meta property="og:site_name" content="Nadri">
<link rel="icon" href="/static/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/static/fonts/bricolage-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/static/style.css">{head_extra}
</head>
<body class="lang-{lang}{' home' if meta.get('home') else ''}{' s-' + meta['section'] if meta.get('section') else ''}">
<a class="skip" href="#main">{ui['skip']}</a>
<header class="site-head">
  <a class="brand" href="{L['prefix']}/" aria-label="Nadri home"><img src="/static/nadri-mark.svg" alt="" width="34" height="34"><span>Nadri</span></a>
  <nav class="main-nav" aria-label="{ui['nav_label']}">{nav}</nav>
  <nav class="langs" aria-label="{ui['lang_label']}">{langs}</nav>
</header>
<main id="main">
{header_block}
{('<div class="home-body">' + body_html + '</div>') if meta.get('home') else ('<article class="body">' + body_html + '</article>')}
{report_box(lang, meta, path)}
</main>
<footer class="site-foot">
  <p class="foot-brand"><strong>Nadri</strong> {ui['tagline']}</p>
  <p class="foot-links">{''.join(f'<a href="{L["prefix"]}{h}">{t}</a>' for h, t in ui['foot'])}</p>
  <p class="foot-small">{ui['foot_note']}</p>
</footer>
</body>
</html>
"""


def report_box(lang, meta, path):
    """Guide pages get an 'out of date?' box with a prefilled email (no backend needed)."""
    ui = SITE["ui"][lang]
    if meta.get("home") or not meta.get("updated") or meta.get("report") == "no" or "report_cta" not in ui:
        return ""
    from urllib.parse import quote
    url = SITE["base_url"] + path
    href = (f"mailto:{SITE['contact_email']}?subject={quote(ui['report_subject'] + ': ' + meta.get('title', ''))}"
            f"&body={quote(ui['report_mail'].format(url=url))}")
    return (f'<aside class="report" aria-labelledby="report-h"><h2 id="report-h">{ui["report_title"]}</h2>'
            f'<p>{ui["report_body"].format(date=meta["updated"])}</p>'
            f'<p><a class="report-btn" href="{html.escape(href)}">{ui["report_cta"]}</a> '
            f'<a class="report-log" href="{SITE["languages"][lang]["prefix"]}/updates/">{ui["updates"]}</a></p></aside>')


def url_for(lang, slug):
    pre = SITE["languages"][lang]["prefix"]
    return f"{pre}/" if slug == "index" else f"{pre}/{slug}/"


def build():
    if DIST.exists(): shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(ROOT / "static", DIST / "static")
    pages = {}
    for lang in SITE["languages"]:
        for f in sorted((ROOT / "content" / lang).glob("*.md")):
            meta, body = parse(f)
            pages[(lang, f.stem)] = (meta, body)
    # Rule: every page exists in every language, no exceptions.
    slugs = {s for _, s in pages}
    missing = sorted(f"content/{l}/{s}.md" for l in SITE["languages"] for s in slugs if (l, s) not in pages)
    if missing:
        raise SystemExit("Missing translations (every page must exist in every language):\n  " + "\n  ".join(missing))
    urls = []
    for (lang, slug), (meta, body) in pages.items():
        alternates = {l: url_for(l, slug) for l in SITE["languages"] if (l, slug) in pages}
        path = url_for(lang, slug)
        out = DIST / path.strip("/") / "index.html" if path != "/" else DIST / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang, meta, md(body, lang), path, alternates), encoding="utf-8")
        if meta.get("noindex") != "yes":
            urls.append((path, meta.get("updated", "")))
    sm = "".join(f"<url><loc>{BASE}{u}</loc>{f'<lastmod>{d}</lastmod>' if d else ''}</url>" for u, d in urls)
    (DIST / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>',
        encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    (DIST / "404.html").write_text(page("en", {"title": "Page not found", "noindex": "yes"},
        '<p>This page does not exist. Start from the <a href="/">Nadri home page</a>.</p>', "/404", {}),
        encoding="utf-8")
    print(f"built {len(pages)} pages -> {DIST}")


if __name__ == "__main__":
    build()
