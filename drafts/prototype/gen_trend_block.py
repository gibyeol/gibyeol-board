"""Daily trend block for a keyword page, built only from data files.

Reads data/shop-trends.json (keyword, headline numbers, ranking, items) and data/deals.json (sale dates),
writes drafts/prototype/trend-block.md and replaces the block between
<!-- trend:start --> and <!-- trend:end --> in drafts/prototype/winter-light-puffer.md.
A daily refresh only edits the json files and reruns this script.

Proposed build.py hook (not applied): a shortcode {{trend:kw-light-puffer}} that calls trend_block(kw, lang)
from this module, so pages never hold a copy of the numbers.

usage: python3 drafts/prototype/gen_trend_block.py
"""
import html
import urllib.parse
import json
import pathlib
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parents[2]
KW = "kw-light-puffer"
TODAY = date.today()


def eok(won):
    v = won / 1e8
    return f"{v:,.1f}억" if v < 1000 else f"{v:,.0f}억"


def dday(d):
    s, e = date.fromisoformat(d["start"]), date.fromisoformat(d["end"])
    if s > TODAY:
        return f"{s.month}/{s.day} 시작"
    n = (e - TODAY).days
    return "오늘 마감" if n == 0 else f"D-{n}"


def trend_block():
    T = json.loads((ROOT / "data/shop-trends.json").read_text(encoding="utf-8"))
    D = json.loads((ROOT / "data/deals.json").read_text(encoding="utf-8"))
    kw = next(k for k in T["keywords"] if k["id"] == KW)
    blk = kw["trend_block"]
    src = T["sources"]
    deals = {d["id"]: d for d in D["items"]}
    items = {i["id"]: i for i in T["items"]}
    rk = next(r for r in T["rankings"] if r["id"] == blk["ranking_id"])
    out = [f'<section class="tb" aria-label="오늘의 트렌드"><p class="tag tag-t"><i class="ic ic-timer" aria-hidden="true"></i>트렌드 · {html.escape(blk["as_of"])}</p>']
    # sale strip (site.js keeps D-day live and hides ended rows)
    rows = []
    for did, label in blk["deals"]:
        d = deals.get(did)
        if not d or date.fromisoformat(d["end"]) < TODAY:
            continue
        pct = f' <b>최대 {d["hero"]["value"]}%</b>' if d.get("hero", {}).get("kind") == "pct" else ""
        rows.append((d["end"], f'<tr data-start="{d["start"]}" data-end="{d["end"]}"><td><a href="/ko/deals/">{html.escape(label)}{pct} '
                     f'<span class="dday" data-today="오늘 마감">{dday(d)}</span></a></td></tr>'))
    out.append('<table class="codes strip" role="presentation"><tbody>' + "".join(r for _, r in sorted(rows)) + "</tbody></table>")
    # headline numbers
    cards = "".join(f'<div{" class=hero" if i == 0 else ""}><strong>{html.escape(h["value"])}</strong><span>{html.escape(h["label"])}</span>'
                    f'<span class="src">{html.escape(h["cite"])}</span></div>' for i, h in enumerate(blk["headline"]))
    out.append(f'<div class="stats">{cards}</div>')
    # review-sorted list (not a sales rank); ad-labelled items are excluded
    rv = next(r for r in T["rankings"] if r["id"] == blk["reviews_id"])
    shown = [it for it in rv["items"] if not it["ad"] and not it.get("not_light_puffer")][: blk["reviews_show"]]
    lis = ""
    for n, it in enumerate(shown, 1):
        q = urllib.parse.quote(f'{it["brand"]} {it["product"]}')
        lis += (f'<li><b>{n}</b><span class="nm"><a href="https://www.musinsa.com/" rel="noopener" target="_blank" title="무신사에서 상품 이름으로 검색">'
                f'{html.escape(it["brand"])} · {html.escape(it["product"])}</a><!-- aff-slot: musinsa {html.escape(it["brand"])} {html.escape(it["product"])} --></span>'
                f'<span class="r">★{it["rating"]:.1f} ({html.escape(it["reviews"])})</span><span class="p">{it["price_krw"]:,}원 <small>{it["discount_pct"]}%↓</small></span></li>')
    out.append(f'<h3><i class="ic ic-users" aria-hidden="true"></i>후기 많은 경량 패딩<span class="src">무신사 후기순 2026-11-26 17:04(운영자 확인 화면) · 판매 순위 아님 · 광고·비경량 제외</span></h3>')
    out.append(f'<ol class="rv">{lis}</ol>')
    out.append(f'<p class="reading">{html.escape(rv["reading"]["ko"])}</p>')
    # ranking bars
    top = rk["items"][0]["sales_krw"]
    lis = ""
    for it in rk["items"][: blk.get("bars_show", 99)]:
        lp = it.get("light_puffer_link")
        cls = ' class="lp"' if lp else ""
        lis += (f'<li{cls}><b>{it["rank"]}위</b><span>{html.escape(it["brand"])}</span>'
                f'<i style="width:{round(100 * it["sales_krw"] / top)}%"></i><em>{eok(it["sales_krw"])}</em></li>')
    out.append(f'<h3><i class="ic ic-list-checks" aria-hidden="true"></i>{html.escape(rk["title_ko"])}'
               f'<span class="src">11/26 16:25(운영자 확인 화면) · 전 상품 기준 · 2–4위 미확인 · 빨강=경량 패딩 품절 보도</span></h3>')
    out.append(f'<ol class="bars">{lis}</ol>')
    links = "".join(f'<a class="tb-go" href="{html.escape(l["url"])}" rel="noopener" target="_blank">{html.escape(l["label"])} →</a>'
                    f'<!-- aff-slot: {html.escape(l["aff_slot"])} -->' for l in blk["links"])
    out.append(f'<p class="links">{links}</p>')
    # official comparison table
    trs = ""
    for row in blk["table"]:
        i = items[row["item"]]
        price = f'{i["price_krw"]:,}원' if i.get("price_krw") else (f'${i["price_usd"]}' if i.get("price_usd") else row.get("price", "–"))
        rating = f'{i["rating"]:.1f} ({i["reviews"]})' if i.get("rating") else "–"
        trs += (f'<tr><td><a href="{html.escape(row["url"])}" rel="noopener" target="_blank">{html.escape(row["label"])} →</a><!-- aff-slot: {row["item"]} --></td>'
                f'<td class="n">{price}</td><td>{html.escape(row["fill"])}</td><td>{html.escape(row["fit"])}</td><td class="n">{rating}</td><td>{html.escape(row["now"])}</td></tr>')
    out.append('<details class="cmpd"><summary><i class="ic ic-tag" aria-hidden="true"></i>공식몰 사양 비교 더 보기 <span class="src">가격·충전재·핏·평점 · ' + html.escape(blk["table_checked"]) + '</span></summary>')
    out.append('<table class="cmp"><thead><tr><th>제품 → 공식 페이지</th><th>가격</th><th>충전재</th><th>핏</th><th>평점</th><th>지금</th></tr></thead><tbody>' + trs + "</tbody></table>")
    out.append("</details>")
    out.append("</section>")
    return "\n".join(out)


if __name__ == "__main__":
    block = trend_block()
    here = pathlib.Path(__file__).resolve().parent
    (here / "trend-block.md").write_text(block + "\n", encoding="utf-8")
    page = here / "winter-light-puffer.md"
    s = page.read_text(encoding="utf-8")
    a, b = s.index("<!-- trend:start -->") + len("<!-- trend:start -->"), s.index("<!-- trend:end -->")
    page.write_text(s[:a] + "\n" + block + "\n" + s[b:], encoding="utf-8")
    print("trend block written:", len(block), "chars")
