"""Daily trend block for the Christmas keyword DRAFT, built only from drafts/christmas/christmas-data.json.

Same idea as drafts/prototype/gen_trend_block.py (winter-light-puffer): the numbers live in a data file and this
script rewrites the block between <!-- trend:start --> and <!-- trend:end --> in drafts/christmas/christmas.md.
A daily refresh = edit christmas-data.json, run this script. Korean only (the draft has no other languages yet).

It does not read or write build.py, content/ or data/*.json (live files). When the page is published, the same
function can be pointed at content/<lang>/<slug>.md, or build.py can get a {{trend:christmas}} shortcode (not applied).

D-day is written with today's date in Seoul. On the built site, site.js recounts it in the browser and hides
rows whose end date has passed (`.codes tr[data-end]`). Rows that already ended are left out here too.

usage: python3 drafts/christmas/gen_christmas_block.py [--check]
  --check  print the block and do not write the page
"""
import html
import json
import pathlib
import sys
from datetime import date, datetime
from zoneinfo import ZoneInfo

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "christmas-data.json"
PAGE = HERE / "christmas.md"
TODAY = datetime.now(ZoneInfo("Asia/Seoul")).date()


def e(s):
    return html.escape(s, quote=False)  # page text; URLs here never hold a double quote


def a(url, text):
    return f'<a href="{e(url)}" rel="noopener" target="_blank">{text}</a>'


def dday(row):
    s, end = date.fromisoformat(row["start"]), date.fromisoformat(row["end"])
    if s > TODAY:
        return f"{s.month}/{s.day} 시작"
    n = (end - TODAY).days
    return row.get("today_text", "오늘 마감") if n == 0 else f"D-{n}"


def block(d):
    out = [f'<section class="tb" aria-label="오늘의 트렌드"><p class="tag tag-t"><i class="ic ic-timer" aria-hidden="true"></i>'
           f'트렌드 · {e(d["as_of"])} 기준</p>']
    # sale / date strip: running rows by soonest end, then rows that have not started
    rows = []
    for r in sorted(d["strip"], key=lambda r: (0, r["end"]) if r["start"] <= TODAY.isoformat() else (1, r["start"])):  # running rows first, then upcoming
        if date.fromisoformat(r["end"]) < TODAY:
            continue
        pct = f' <b>최대 {r["pct"]}%</b>' if r.get("pct") else ""
        today = e(r.get("today_text", "오늘 마감"))
        rows.append(f'<tr data-start="{r["start"]}" data-end="{r["end"]}"><td>{a(r["url"], e(r["label"]) + pct + " " + f"<span class=\"dday\" data-today=\"{today}\">{dday(r)}</span>")}</td></tr>')
    out.append('<table class="codes strip" role="presentation"><tbody>' + "".join(rows) + "</tbody></table>")
    # headline numbers
    cards = "".join(f'<div{" class=hero" if i == 0 else ""}><strong>{e(s["value"])}</strong><span>{e(s["label"])}</span>'
                    f'<span class="src">{e(s["cite"])}</span></div>' for i, s in enumerate(d["stats"]))
    out.append(f'<div class="stats">{cards}</div>')
    # products the stores themselves put forward (not a sales rank)
    pk = d["picks"]
    lis = ""
    for it in pk["items"]:
        cond = f' <small>{e(it["cond"])}</small>' if it.get("cond") else ""
        lis += (f'<li><span class="nm">{a(it["url"], e(it["name"]))}{cond}</span>'
                f'<span class="r">{e(it["store"])}</span><span class="p">{e(it["price"])}</span></li>')
    out.append(f'<h3><i class="ic ic-store" aria-hidden="true"></i>{e(pk["title"])}<span class="src">{e(pk["src_note"])}</span></h3>')
    out.append(f'<ol class="rv norank">{lis}</ol>')
    # search-growth bars, in the order the source gave them
    bs = d["bars"]
    top = max(b["value"] for b in bs["items"])
    lis = "".join(f'<li><b>{e(b["label"].replace("크리스마스 ", ""))}</b><span>{e(b["label"])}</span>'
                  f'<i style="width:{round(100 * b["value"] / top)}%"></i><em>+{b["value"]}%</em></li>' for b in bs["items"])
    out.append(f'<h3><i class="ic ic-list-checks" aria-hidden="true"></i>{e(bs["title"])}<span class="src">{e(bs["src_note"])}</span></h3>')
    out.append(f'<ol class="bars">{lis}</ol>')
    out.append(f'<p class="reading">{e(bs["reading"])}</p>')
    out.append('<p class="links">' + "".join(f'<a class="tb-go" href="{e(l["url"])}" rel="noopener" target="_blank">{e(l["label"])} →</a>'
                                            for l in d["links"]) + "</p>")
    # markets table (collapsed)
    mk = d["markets"]
    trs = "".join(f'<tr><td>{a(r["url"], e(r["name"]) + " →")}</td><td class="n">{r["when"]}</td><td>{r["hours"]}</td>'
                  f'<td>{e(r["sells"])}</td><td>{e(r["access"])}</td></tr>' for r in mk["rows"])
    out.append(f'<details class="cmpd"><summary><i class="ic ic-map-pin" aria-hidden="true"></i>{e(mk["summary"])} '
               f'<span class="src">{e(mk["summary_src"])}</span></summary>')
    out.append('<table class="cmp mk"><thead><tr><th>어디</th><th>언제</th><th>몇 시</th><th>파는 것</th><th>가는 길</th></tr></thead>'
               f'<tbody>{trs}</tbody></table>')
    out.append("</details>")
    out.append("</section>")
    return "\n".join(out)


def check_sources(d):
    """Every row must point at a source listed in the file (so each number can be traced to a raw text)."""
    keys = set(d["sources"])
    used = [r["src"] for r in d["strip"] + d["stats"] + d["picks"]["items"]]
    used += [s for r in d["markets"]["rows"] for s in r["src"]]
    used += [it["src_word_src"] for it in d["picks"]["items"] if it.get("src_word_src")]
    missing = sorted(set(used) - keys)
    if missing:
        raise SystemExit(f"gen_christmas_block: source id not in sources: {missing}")


if __name__ == "__main__":
    d = json.loads(DATA.read_text(encoding="utf-8"))
    check_sources(d)
    b = block(d)
    if "--check" in sys.argv:
        print(b)
        sys.exit(0)
    s = PAGE.read_text(encoding="utf-8")
    i, j = s.index("<!-- trend:start -->") + len("<!-- trend:start -->"), s.index("<!-- trend:end -->")
    PAGE.write_text(s[:i] + "\n" + b + "\n" + s[j:], encoding="utf-8")
    print(f"trend block written: {PAGE.name} {len(b)} chars (today in Seoul: {TODAY})")
