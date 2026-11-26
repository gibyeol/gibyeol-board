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
LINKS = {k: v for k, v in json.loads((ROOT / "data/links.json").read_text(encoding="utf-8")).items() if not k.startswith("_")}
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
    if kind == "dealcards":
        return deal_cards(lang, int(key) if key else 3)
    if kind == "board":
        return countdown(lang, int(key) if key else 5)
    if kind == "guides":
        return guides_index(lang, only=key)  # {{guides:olive-young}} = only the group holding that page
    if kind == "codes":
        return codes_table(lang)
    if kind == "fig":
        # {{fig:name|caption}} → static/fig/<lang>/<name>.svg (language text) or static/fig/<name>.svg (no text)
        for rel in [f"fig/{lang}/{key}.{ext}" for ext in ("svg", "webp", "jpg", "png")] + [f"fig/{key}.{ext}" for ext in ("svg", "webp", "jpg", "png")]:
            if (ROOT / "static" / rel).exists():
                cap = inline(label) if label else ""
                alt = html.escape(re.sub(r"\*\*|\[|\]\([^)]*\)", "", label or key))
                return (f'<figure class="fig"><img src="/static/{rel}" alt="{alt}" loading="lazy" decoding="async">'
                        + (f"<figcaption>{cap}</figcaption>" if cap else "") + "</figure>")
        raise SystemExit(f"missing figure: static/fig/{lang}/{key}.(svg|webp|jpg|png) (or static/fig/{key}.*)")
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
            cls = ' class="steps"' if tag == "ol" else ""
            out.append(f"<{tag}{cls}>" + "".join(f"<li>{inline(i)}</li>" for i in items) + f"</{tag}>")
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
DEAL_UI = {
    "ko": {"all": "전체", "live": "진행 중", "soon": "곧 시작", "ends": "D-{n} 마감", "today": "오늘 마감",
           "starts": "{n}일 뒤 시작", "copy": "복사", "copied": "복사됨", "source": "출처", "until": "까지",
           "code": "코드", "filter": "분야"},
    "en": {"all": "All", "live": "On now", "soon": "Coming up", "ends": "{n} days left", "today": "Ends today",
           "starts": "Starts in {n} days", "copy": "Copy", "copied": "Copied", "source": "Source", "until": "until",
           "code": "Code", "filter": "Category"},
    "ja": {"all": "すべて", "live": "開催中", "soon": "まもなく", "ends": "残り{n}日", "today": "今日まで",
           "starts": "{n}日後に開始", "copy": "コピー", "copied": "コピーしました", "source": "出典", "until": "まで",
           "code": "コード", "filter": "カテゴリー"},
    "zh-tw": {"all": "全部", "live": "進行中", "soon": "即將開始", "ends": "剩 {n} 天", "today": "今天截止",
              "starts": "{n} 天後開始", "copy": "複製", "copied": "已複製", "source": "來源", "until": "截止",
              "code": "代碼", "filter": "分類"},
}


def deal_dates(d, lang):
    s, e = date.fromisoformat(d["start"]), date.fromisoformat(d["end"])
    if lang == "en":
        f = lambda x: x.strftime("%b ") + str(x.day)
    else:
        f = lambda x: f"{x.month}/{x.day}"
    if d.get("open_start"):
        return (f"~ {f(e)}" if lang != "en" else f"Until {f(e)}")
    return f"{f(s)} – {f(e)}"


def deals_board(lang, limit=None):
    ui, du = SITE["ui"][lang], DEAL_UI[lang]
    today = date.today()
    items = [d for d in DEALS["items"] if lang in d.get("text", {}) and date.fromisoformat(d["end"]) >= today]
    live = sorted([d for d in items if date.fromisoformat(d["start"]) <= today], key=lambda d: d["end"])
    soon = sorted([d for d in items if date.fromisoformat(d["start"]) > today], key=lambda d: d["start"])
    items = live + soon
    if limit: items = items[:limit]
    if not items:
        return f'<p class="empty">{ui["deals_empty"]}</p>'
    cats = DEALS.get("categories", {})
    rows = []
    for d in items:
        t = d["text"][lang]
        ok = d.get("status", "confirmed" if d.get("confirmed") else "expected") == "confirmed"
        status = ui["deal_confirmed"] if ok else ui["deal_expected"]
        cat = cats.get(d.get("category", ""), {}).get(lang, "")
        s, e = date.fromisoformat(d["start"]), date.fromisoformat(d["end"])
        if s > today:
            dd = du["starts"].format(n=(s - today).days)
        else:
            n = (e - today).days
            dd = du["today"] if n == 0 else du["ends"].format(n=n)
        codes = ""
        for c in d.get("code", []):
            cn = c.get("note", {}).get(lang, "")
            codes += (f'<span class="deal-code"><span class="code-label">{du["code"]}{" · " + html.escape(cn) if cn else ""}</span>'
                      f'<code>{html.escape(c["value"])}</code><button type="button" class="copy" data-code="{html.escape(c["value"])}" '
                      f'data-done="{du["copied"]}">{du["copy"]}</button></span>')
        link = ""
        if d.get("aff") and AFF.get(d["aff"], {}).get("url"):
            link = f'<a class="deal-go" href="{AFF[d["aff"]]["url"]}" rel="sponsored noopener" target="_blank">{ui["deal_go"]}</a>'
        src = d.get("source", {})
        src_html = (f'<a class="deal-src" href="{html.escape(src["url"])}" rel="noopener" target="_blank">{du["source"]}'
                    f'{" (" + src["date"] + ")" if src.get("date") else ""}</a>') if src.get("url") else ""
        rows.append(
            f'<li class="deal {"ok" if ok else "tbc"}" data-cat="{d.get("category","")}" data-start="{d["start"]}" data-end="{d["end"]}">'
            f'<div class="deal-when">{deal_dates(d, lang)}<span class="deal-dday">{dd}</span>'
            f'<span class="deal-status">{status}{" · " + cat if cat else ""}</span></div>'
            f'<div class="deal-body"><strong>{inline(t["title"])}</strong><span class="deal-note">{inline(t["note"])}</span>'
            f'{"<div class=deal-codes>" + codes + "</div>" if codes else ""}'
            f'<span class="deal-links">{link}{src_html}</span></div></li>')
    chips = ""
    if not limit:
        used = [c for c in cats if any(d.get("category") == c for d in items)]
        chips = (f'<div class="deal-filter" role="group" aria-label="{du["filter"]}">'
                 f'<button type="button" class="chip" data-cat="" aria-pressed="true">{du["all"]}</button>'
                 + "".join(f'<button type="button" class="chip" data-cat="{c}" aria-pressed="false">{cats[c][lang]}</button>' for c in used)
                 + "</div>")
    checked = DEALS.get("checked", "")
    script = '<script src="/static/deals.js" defer></script>'
    return (f'{chips}<ul class="deals" data-ends="{du["ends"]}" data-today="{du["today"]}" data-starts="{du["starts"]}">{"".join(rows)}</ul>'
            f'<p class="deals-checked">{ui["deals_checked"].format(date=checked)}</p>{script}')




# ---------- official links: every thing we name gets a way to reach it ----------
def link_attrs(e):
    ios = f"https://apps.apple.com/app/{e['ios']}" if e.get("ios") else ""
    andr = f"https://play.google.com/store/apps/details?id={e['android']}" if e.get("android") else ""
    href = e.get("web") or ios or andr
    data = (f' data-ios="{ios}"' if ios else "") + (f' data-android="{andr}"' if andr else "")
    return f'class="go" href="{href}"{data} rel="noopener" target="_blank"'


def autolink(body):
    """Link the first plain-text mention of each registered name. Skips headings, existing links, code and buttons."""
    parts = re.split(r"(<[^>]+>)", body)
    skip, done = 0, set()
    for i, part in enumerate(parts):
        if part.startswith("<"):
            m = re.match(r"<(/?)(a|h1|h2|h3|code|button|script)\b", part)
            if m:
                skip += -1 if m.group(1) else 1
            continue
        if skip > 0 or not part.strip():
            continue
        for key, e in LINKS.items():
            if key in done:
                continue
            for term in sorted(e["terms"], key=len, reverse=True):
                pos = part.find(term)
                if pos < 0:
                    continue
                if term.isascii() and ((pos > 0 and part[pos - 1].isalnum()) or (pos + len(term) < len(part) and part[pos + len(term)].isalnum())):
                    continue
                part = part[:pos] + f"<a {link_attrs(e)}>{term}</a>" + part[pos + len(term):]
                done.add(key)
                break
        parts[i] = part
    return "".join(parts)

# ---------- A-Z hub: every guide, grouped by the situation you are in ----------
# Same groups in every language: no split by who the reader is, only by what they need right now.
GUIDE_GROUPS = [
    (["essentials", "e-arrival-card", "money", "first-trip", "health"],
     {"en": "Before you go", "ko": "출발 전 준비", "ja": "出発前の準備", "zh-tw": "出發前準備"}),
    (["airport-to-seoul"],
     {"en": "Arriving", "ko": "도착했을 때", "ja": "到着したら", "zh-tw": "抵達時"}),
    (["getting-around", "seoul-subway", "seoul-bus", "ktx-busan", "jeju"],
     {"en": "Getting around", "ko": "이동하기", "ja": "移動する", "zh-tw": "交通移動"}),
    (["deals", "olive-young", "kbeauty-how-to-choose", "daiso", "shopping-streets", "convenience-store", "tax-refund", "duty-free", "skin-clinic"],
     {"en": "Shopping and deals", "ko": "쇼핑과 할인", "ja": "買い物とセール", "zh-tw": "購物與特賣"}),
    (["seoul-areas", "palaces", "food", "winter", "concert-trip", "everyday"],
     {"en": "Travelling in Korea", "ko": "한국 안에서 여행하기", "ja": "韓国を旅する", "zh-tw": "在韓國旅行"}),
    (["departure-day", "abroad-esim"],
     {"en": "Flying out of Korea", "ko": "한국에서 출국할 때", "ja": "韓国から出国するとき", "zh-tw": "從韓國出境時"}),
    (["emergency"],
     {"en": "Emergencies", "ko": "응급 상황", "ja": "緊急時", "zh-tw": "緊急狀況"}),
]
PAGES = {}


def guides_index(lang, only=None):
    pre, out = SITE["languages"][lang]["prefix"], []
    for slugs, label in GUIDE_GROUPS:
        if only and only not in slugs:
            continue
        items = [(s, PAGES[(lang, s)][0]) for s in slugs if (lang, s) in PAGES]
        if not items:
            continue
        lis = "".join(f'<li><a href="{pre}/{s}/">{inline(m.get("title", s))}</a><p>{inline(m.get("description", ""))}</p></li>' for s, m in items)
        out.append(f'<section class="az"><h3>{label[lang]}</h3><ol>{lis}</ol></section>')
    return "".join(out)

# ---------- home components (v7 design: numbers lead, a seal marks what we checked) ----------
HOME_UI = {
    "ko": {"seoul": "서울 지금", "phases": ["새벽", "낮", "저녁", "밤"], "count": "확인한 세일 {d}건 · 공개 코드 {c}개 · 가이드 {g}편",
           "board": "마감 시세표", "all": "전체", "left": "남은 날", "sale": "세일", "today": "오늘", "starts": "{n}일 뒤",
           "checked": "확인", "codes_h": "공개된 할인 코드", "codes_p": "브랜드나 언론이 공개한 것만, 조건 그대로",
           "cols": ["코드", "어디서", "조건", "마감", "확인"], "cards": "이번 주 꼭 볼 할인",
           "pct": "% 최대", "wd": "월화수목금토일"},
    "en": {"seoul": "Seoul now", "phases": ["dawn", "day", "evening", "night"], "count": "{d} sales checked · {c} public codes · {g} guides",
           "board": "Ending soon", "all": "All", "left": "Left", "sale": "Sale", "today": "Today", "starts": "in {n}d",
           "checked": "Checked", "codes_h": "Public discount codes", "codes_p": "Only codes a brand or the press published, conditions as stated",
           "cols": ["Code", "Where", "Conditions", "Ends", "Checked"], "cards": "Worth a look this week",
           "pct": "% off, max", "wd": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]},
    "ja": {"seoul": "ソウル現在", "phases": ["夜明け", "昼", "夕方", "夜"], "count": "確認したセール{d}件 · 公開コード{c}個 · ガイド{g}本",
           "board": "締切が近い順", "all": "すべて", "left": "残り", "sale": "セール", "today": "今日", "starts": "{n}日後",
           "checked": "確認", "codes_h": "公開されている割引コード", "codes_p": "ブランドや報道が公開したものだけ、条件もそのまま",
           "cols": ["コード", "どこで", "条件", "締切", "確認"], "cards": "今週見ておきたいセール",
           "pct": "% 最大オフ", "wd": "月火水木金土日"},
    "zh-tw": {"seoul": "首爾現在", "phases": ["清晨", "白天", "傍晚", "夜晚"], "count": "已確認特賣 {d} 檔 · 公開代碼 {c} 組 · 指南 {g} 篇",
              "board": "即將截止", "all": "全部", "left": "剩餘", "sale": "特賣", "today": "今天", "starts": "{n} 天後",
              "checked": "已確認", "codes_h": "公開的折扣代碼", "codes_p": "只收品牌或媒體公開的代碼,條件照原文",
              "cols": ["代碼", "哪裡用", "條件", "截止", "確認"], "cards": "這週值得看的特賣",
              "pct": "% 最高折扣", "wd": "一二三四五六日"},
}
COUNTS = {}


def seal(text="확인"):
    return f'<b class="seal-mark" aria-hidden="true">{text}</b>'


def live_items(lang):
    today = date.today()
    return [d for d in DEALS["items"] if d.get("text", {}).get(lang, {}).get("title")
            and date.fromisoformat(d["end"]) >= today]


def dday_html(d, lang):
    hu, today = HOME_UI[lang], date.today()
    s, e = date.fromisoformat(d["start"]), date.fromisoformat(d["end"])
    if s > today:
        return hu["starts"].format(n=(s - today).days), False
    n = (e - today).days
    return (hu["today"] if n == 0 else f"D-{n}"), n <= 2


def short_date(iso, lang):
    if not iso:
        return ""
    p = iso.split("-")
    return ".".join(p[1:]) if len(p) == 3 else iso


def stamp(d, lang):
    src = d.get("source", {})
    if not src.get("url"):
        return ""
    return (f'<a class="stamp" href="{html.escape(src["url"])}" rel="noopener" target="_blank">{seal()}'
            f'<span>{HOME_UI[lang]["checked"]} {short_date(src.get("date", ""), lang)}</span></a>')


def hero_html(d, lang):
    h = d["hero"]
    if h["kind"] == "pct":
        return f'{h["value"]}<small>{HOME_UI[lang]["pct"]}</small>'
    v = h["value"]  # krw
    big = {"ko": (f"{v // 10000}", "만 원"), "en": (f"₩{v // 1000}k", " off, max"),
           "ja": (f"{v // 10000}", "万ウォン"), "zh-tw": (f"{v // 10000}", "萬韓元")}[lang]
    return f'{big[0]}<small>{big[1]}</small>'


def first_sentence(t):
    """First sentence that says more than the headline number (skips 'Up to 85%.')."""
    parts = [x for x in re.split(r"(?:(?<=[.!?])(?=\s|$)|(?<=。))\s*", t.strip()) if x]
    for x in parts:
        if len(re.sub(r"[\d%.,\s]", "", x)) >= 10:
            return x
    return parts[0] if parts else ""


def deal_cards(lang, n=3):
    today = date.today()
    pool = sorted([d for d in live_items(lang) if d.get("hero") and d.get("status") == "confirmed"
                   and date.fromisoformat(d["start"]) <= today], key=lambda d: d["end"])
    picked, cats = [], set()
    for d in pool:  # one per category, so three different reasons to look
        if d.get("category") in cats:
            continue
        picked.append(d); cats.add(d.get("category"))
        if len(picked) == n:
            break
    out = []
    for d in picked:
        t = d["text"][lang]
        dd, hot = dday_html(d, lang)
        out.append(f'<article class="dc" data-start="{d["start"]}" data-end="{d["end"]}">'
                   f'<div class="dc-top"><span>{inline(t["title"])}</span><span class="dday{" hot" if hot else ""}" data-today="{HOME_UI[lang]["today"]}">{dd}</span></div>'
                   f'<div class="num">{hero_html(d, lang)}</div>'
                   f'<p>{inline(first_sentence(t["note"]))}</p>{stamp(d, lang)}</article>')
    return f'<section class="deals3" aria-label="{HOME_UI[lang]["cards"]}">{"".join(out)}</section>' if out else ""


def countdown(lang, n=5):
    today, hu, L = date.today(), HOME_UI[lang], SITE["languages"][lang]
    items = sorted([d for d in live_items(lang) if date.fromisoformat(d["start"]) <= today], key=lambda d: d["end"])[:n]
    rows = ""
    for d in items:
        dd, hot = dday_html(d, lang)
        rows += (f'<tr data-start="{d["start"]}" data-end="{d["end"]}"><td class="d{" hot" if hot else ""}"><span class="dday" data-today="{hu["today"]}">{dd}</span></td>'
                 f'<td>{inline(d["text"][lang]["title"])}<small>{deal_dates(d, lang)}</small></td></tr>')
    return (f'<aside class="board"><h2><span>{hu["board"]}</span><a href="{L["prefix"]}/deals/">{hu["all"]}</a></h2>'
            f'<table><thead><tr><th>{hu["left"]}</th><th>{hu["sale"]}</th></tr></thead><tbody>{rows}</tbody></table></aside>')


def codes_table(lang):
    hu, du = HOME_UI[lang], DEAL_UI[lang]
    rows = ""
    for d in sorted(live_items(lang), key=lambda d: d["end"]):
        for c in d.get("code", []):
            cn = c.get("note", {}).get(lang, "")
            rows += (f'<tr data-start="{d["start"]}" data-end="{d["end"]}"><td><code>{html.escape(c["value"])}</code></td>'
                     f'<td>{inline(d["text"][lang]["title"])}</td><td>{html.escape(cn)}</td>'
                     f'<td class="mono">{short_date(d["end"], lang)}</td><td>{stamp(d, lang)}</td>'
                     f'<td><button type="button" class="copy" data-code="{html.escape(c["value"])}" data-done="{du["copied"]}">{du["copy"]}</button></td></tr>')
    if not rows:
        return ""
    head = "".join(f"<th>{h}</th>" for h in hu["cols"]) + "<th></th>"
    return (f'<section class="sec"><div class="sec-h"><h2>{hu["codes_h"]}</h2><p>{hu["codes_p"]}</p></div>'
            f'<div class="table"><table class="codes"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div></section>')


def dateline(lang):
    hu, t = HOME_UI[lang], date.today()
    wd = hu["wd"][t.weekday()]
    ds = {"ko": f"{t.year}. {t.month}. {t.day}. {wd}", "en": f"{wd} {t.day} {t.strftime('%b')} {t.year}",
          "ja": f"{t.year}年{t.month}月{t.day}日({wd})", "zh-tw": f"{t.year}年{t.month}月{t.day}日 週{wd}"}[lang]
    c = COUNTS.get(lang, {})
    count = hu["count"].format(d=c.get("deals", 0), c=c.get("codes", 0), g=c.get("guides", 0))
    return (f'<div class="dateline"><span>{ds} · <span id="seoul-now" data-label="{hu["seoul"]}" '
            f'data-phases="{"|".join(hu["phases"])}">{hu["seoul"]}</span></span><span>{count}</span></div>')


SKY = """<svg class="sky" viewBox="0 0 1200 420" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
<defs><radialGradient id="sunG"><stop offset="0" stop-color="#c8402c" stop-opacity=".4"/><stop offset="1" stop-color="#c8402c" stop-opacity="0"/></radialGradient>
<radialGradient id="moonG"><stop offset="0" stop-color="#efe6d2" stop-opacity=".3"/><stop offset="1" stop-color="#efe6d2" stop-opacity="0"/></radialGradient>
<linearGradient id="peak" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#2c3a50"/><stop offset="1" stop-color="#1b2140"/></linearGradient></defs>
<g id="stars" fill="#f3ead8"></g>
<g id="sun" style="display:none"><circle r="80" fill="url(#sunG)"/><circle r="20" fill="#d74a46" opacity=".9"/></g>
<g id="moon" style="display:none"><circle r="70" fill="url(#moonG)"/><circle r="16" fill="#efe6d2" opacity=".9"/></g>
<path d="M0 420 L0 350 Q60 320 110 280 Q150 320 220 322 Q290 322 340 262 Q390 318 470 318 Q540 318 600 240 Q660 318 730 318 Q810 318 860 262 Q910 322 980 322 Q1050 322 1090 280 Q1140 320 1200 350 L1200 420Z" fill="url(#peak)" opacity=".8"/>
</svg>"""


# ---------- desktop layout (2026-11-26): table of contents + image/text pairs. Mobile CSS hides/ignores both ----------
TOC_LABEL = {"ko": "이 페이지", "en": "On this page", "ja": "このページ", "zh-tw": "本頁內容"}
_FIG = r'(?:<figure class="(?:fig|tr-photo)[^"]*"[^>]*>.*?</figure>|<div class="tr-pair[^"]*">.*?</div>)'


def desktop_pairs(body):
    """Wrap a picture and the text that explains it in <div class="sbs"> so wide screens can put them side by side.
    The wrapper has no box of its own, so phones render exactly as before."""
    sbs = lambda m: f'<div class="sbs">{m.group(1)}\n{m.group(2)}</div>'
    body = re.sub(rf'({_FIG})\n(<ol class="steps">.*?</ol>)', sbs, body, flags=re.S)
    body = re.sub(rf'(?<=</h3>\n)({_FIG})\n(<p>.*?</p>)',
                  lambda m: sbs(m) if '-step"' in body[:m.start()].rsplit("<h3", 1)[-1][:40] else m.group(0), body, flags=re.S)
    body = re.sub(rf'(<figure class="fig"[^>]*>(?:(?!</figure>).)*?-shot-.*?</figure>)\n(<ul class="eac-facts eac-wide">.*?</ul>)', sbs, body, flags=re.S)
    return body


def toc(lang, body):
    hs = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, flags=re.S)
    if len(hs) < 3:
        return ""
    lis = "".join(f'<li><a href="#{hid}">{re.sub(r"<[^>]+>", "", t)}</a></li>' for hid, t in hs)
    return f'<nav class="toc" aria-label="{TOC_LABEL[lang]}"><p class="toc-h">{TOC_LABEL[lang]}</p><ol>{lis}</ol></nav>'


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
    token = SITE.get("analytics", {}).get("cloudflare_token")
    if token:  # Cloudflare Web Analytics: no cookies, no personal data (see privacy page)
        head_extra += ("<script defer src='https://static.cloudflareinsights.com/beacon.min.js' "
                       f"data-cf-beacon='{{\"token\": \"{html.escape(token)}\"}}'></script>")
    if meta.get("disclosure") == "yes":
        body_html = f'<p class="disclosure">{ui["disclosure_inline"]}</p>' + body_html
    byline = ""
    if not meta.get("home") and meta.get("updated") and meta.get("byline") != "no":
        # "approved by an editor" only when the owner approved this version: `approved:` date >= `updated:` date.
        # Anyone who edits a page after approval removes `approved:` (see drafts/BRIEF-access.md).
        key = "byline" if meta.get("approved") and meta["approved"] >= meta["updated"] else "byline_pending"
        byline = f'<p class="byline">{ui[key].format(date=meta["updated"])}</p>'
    lede = f'<p class="lede">{inline(meta["lede"])}</p>' if meta.get("lede") else ""
    crumb = (f'<p class="crumb"><a href="{L["prefix"]}/guides/">{ui["crumb_guides"]}</a> › <a href="{L["prefix"]}/guides/">{ui["crumb_country"]}</a></p>' if meta.get("section") else "")
    header_block = "" if meta.get("home") else f"<header class=\"page-head\">{crumb}<h1>{inline(title)}</h1>{lede}{byline}</header>"
    side = "" if meta.get("home") else toc(lang, body_html)
    if not meta.get("home"):
        body_html = desktop_pairs(body_html)
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
<link rel="stylesheet" href="/static/fonts.css"><link rel="stylesheet" href="/static/style.css">{head_extra}
</head>
<body class="lang-{lang}{' home' if meta.get('home') else ''}{' s-' + meta['section'] if meta.get('section') else ''}">
<a class="skip" href="#main">{ui['skip']}</a>
<header class="site-head{' mast' if meta.get('home') else ''}">
  {SKY}
  <div class="wrap">
    {dateline(lang)}
    <div class="brand-row">
      <a class="brand" href="{L['prefix']}/" aria-label="Nadri home"><img src="/static/nadri-mark-light.svg" alt="" width="44" height="44"><{'h1' if meta.get('home') else 'span'} class="wordmark">Nadri</{'h1' if meta.get('home') else 'span'}></a><span class="catch">{html.escape(ui['catch'])}</span>
    </div>
    <div class="nav-row">
      <nav class="main-nav" aria-label="{ui['nav_label']}">{nav}</nav>
      <nav class="langs" aria-label="{ui['lang_label']}">{langs}</nav>
    </div>
  </div>
</header>
<main id="main" class="wrap{' has-toc' if side else ''}">
{header_block}{side}
{('<div class="home-body">' + body_html + '</div>') if meta.get('home') else ('<article class="body">' + body_html + '</article>')}
{report_box(lang, meta, path)}
</main>
<footer class="site-foot wrap">
  <p class="foot-brand"><strong>Nadri</strong> {ui['tagline']}</p>
  <p class="foot-links">{''.join(f'<a href="{L["prefix"]}{h}">{t}</a>' for h, t in ui['foot'])}</p>
  <p class="foot-small">{ui['foot_note']}</p>
</footer>
<script src="/static/site.js" defer></script>
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
    PAGES.update(pages)
    # Rule: every shared page exists in every language. A page written for one audience only
    # says so with `only: <lang>` and is exempt.
    only = {s: m["only"] for (l, s), (m, _) in pages.items() if m.get("only")}
    bad = sorted(f"content/{l}/{s}.md (only: {only[s]})" for (l, s) in pages if s in only and l != only[s])
    if bad:
        raise SystemExit("Page marked `only:` for another language:\n  " + "\n  ".join(bad))
    slugs = {s for _, s in pages if s not in only}
    missing = sorted(f"content/{l}/{s}.md" for l in SITE["languages"] for s in slugs if (l, s) not in pages)
    if missing:
        raise SystemExit("Missing translations (every shared page must exist in every language):\n  " + "\n  ".join(missing))
    for lang in SITE["languages"]:
        items = live_items(lang)
        COUNTS[lang] = {"deals": len(items), "codes": sum(len(d.get("code", [])) for d in items),
                        "guides": sum(1 for (l, _), (m, _b) in pages.items() if l == lang and m.get("section"))}
    urls = []
    for (lang, slug), (meta, body) in pages.items():
        alternates = {l: url_for(l, slug) for l in SITE["languages"] if (l, slug) in pages}
        path = url_for(lang, slug)
        out = DIST / path.strip("/") / "index.html" if path != "/" else DIST / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang, meta, autolink(md(body, lang)), path, alternates), encoding="utf-8")
        if meta.get("noindex") != "yes":
            urls.append((path, meta.get("updated", "")))
    sm = "".join(f"<url><loc>{BASE}{u}</loc>{f'<lastmod>{d}</lastmod>' if d else ''}</url>" for u, d in urls)
    (DIST / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>',
        encoding="utf-8")
    # AI training crawlers are asked to stay out; search and AI-search crawlers stay allowed (ops/content-protection.md, 2026-11-25)
    train = ["GPTBot", "CCBot", "Google-Extended", "anthropic-ai", "ClaudeBot", "Bytespider", "Applebot-Extended", "meta-externalagent", "cohere-training-data-crawler", "Diffbot", "omgili"]
    blocked = "".join(f"User-agent: {b}\nDisallow: /\n\n" for b in train)
    (DIST / "robots.txt").write_text(f"{blocked}User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    (DIST / "404.html").write_text(page("en", {"title": "Page not found", "noindex": "yes"},
        '<p>This page does not exist. Start from the <a href="/">Nadri home page</a>.</p>', "/404", {}),
        encoding="utf-8")
    print(f"built {len(pages)} pages -> {DIST}")


if __name__ == "__main__":
    build()
