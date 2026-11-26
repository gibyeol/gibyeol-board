"""Daily trend block for the keyword page winter-light-puffer, in every site language, built only from data files.

Reads data/shop-trends.json (keyword, headline numbers, ranking, items) and data/deals.json (sale dates) and
replaces the block between <!-- trend:start --> and <!-- trend:end --> in content/<lang>/winter-light-puffer.md
for ko, en, ja and zh-tw. The Korean block is also written to drafts/prototype/trend-block.md.
A daily refresh only edits the json files, reruns this script, then runs build.py.

The data files hold Korean text only. Every Korean string that appears in the block needs an entry in TR below
(en, ja, zh-tw). A string without an entry stops the script, so new data can never show up untranslated.

D-day: written here with today's date in Seoul. On the built page site.js recounts the D-day in the browser
(Seoul date) and hides rows whose sale has ended, because the strip is a `.codes tr[data-end]` table.
The headline numbers, the review list, the ranking and the "as of" date stay as of the last run.

Proposed build.py hook (not applied): a shortcode {{trend:kw-light-puffer}} that calls trend_block(lang)
from this module, so pages never hold a copy of the numbers.

usage: python3 drafts/prototype/gen_trend_block.py
"""
import html
import json
import pathlib
import re
from datetime import date, datetime
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parents[2]
KW = "kw-light-puffer"
SLUG = "winter-light-puffer"
LANGS = ["ko", "en", "ja", "zh-tw"]
PREFIX = {"ko": "/ko", "en": "", "ja": "/ja", "zh-tw": "/zh-tw"}
TODAY = datetime.now(ZoneInfo("Asia/Seoul")).date()

# Fixed words of the block. Prices in the narrow review list use ₩ in every language but Korean.
UI = {
    "ko": {"aria": "오늘의 트렌드", "tag": "트렌드", "ext": "↗ = 날짜가 실린 기사로 연결", "today": "오늘 마감", "starts": "{m}/{d} 시작", "upto": "최대 {n}%",
           "search": "무신사에서 상품 이름으로 검색", "rv_h": "후기 많은 경량 패딩",
           "rv_src": "무신사 후기순 2026-11-26 17:04(운영자 확인 화면) · 판매 순위 아님 · 광고·비경량 제외 · 이름을 누르면 무신사 홈(이름으로 검색)",
           "rank": "{n}위", "bars_src": "11/26 16:25(운영자 확인 화면) · 전 상품 기준 · 2–4위 미확인 · 빨강=경량 패딩 품절 보도",
           "cmp": "공식몰 사양 비교 더 보기", "cmp_src": "가격·충전재·핏·평점",
           "th": ["제품 → 공식 페이지", "가격", "충전재", "핏", "평점", "지금"]},
    "en": {"aria": "Today's trend", "tag": "Trend", "ext": "↗ = opens the Korean news article with the dates", "today": "Ends today", "starts": "starts {mon} {d}", "upto": "up to {n}%",
           "search": "Search this name on Musinsa", "rv_h": "Lightweight puffers with the most reviews",
           "rv_src": "Musinsa, most-reviewed sort, 2026-11-26 17:04 (screen checked by our operator) · not a sales ranking · ads and non-lightweight items left out · names open Musinsa home; search the Korean name",
           "rank": "#{n}", "bars_src": "Nov 26 16:25 (screen checked by our operator) · all items · ranks 2–4 not checked · red = lightweight puffer sell-out in the news",
           "cmp": "Compare official store specs", "cmp_src": "price · fill · fit · rating",
           "th": ["Product → official page", "Price", "Fill", "Fit", "Rating", "Now"]},
    "ja": {"aria": "今日のトレンド", "tag": "トレンド", "ext": "↗ = 日付が載った韓国語の記事が開きます", "today": "今日まで", "starts": "{m}/{d}開始", "upto": "最大{n}%",
           "search": "ムシンサで商品名を検索", "rv_h": "レビューの多い軽量ダウン",
           "rv_src": "ムシンサ レビュー順 2026-11-26 17:04(運営者が確認した画面)・売上順位ではありません・広告と軽量でない商品は除外・名前はムシンサのトップへ(韓国語名で検索)",
           "rank": "{n}位", "bars_src": "11/26 16:25(運営者が確認した画面)・全商品・2〜4位は未確認・赤=軽量ダウンの品切れ報道あり・金額はウォン",
           "cmp": "公式ストアの仕様を比べる", "cmp_src": "価格・中わた・フィット・評価",
           "th": ["商品 → 公式ページ", "価格", "中わた", "フィット", "評価", "今"]},
    "zh-tw": {"aria": "今日趨勢", "tag": "趨勢", "ext": "↗ = 開啟刊登日期的韓文報導", "today": "今天截止", "starts": "{m}/{d} 開始", "upto": "最低 {z} 折",
              "search": "在 MUSINSA 用商品名稱搜尋", "rv_h": "評論最多的輕羽絨",
              "rv_src": "MUSINSA 評論數排序 2026-11-26 17:04(營運者確認的畫面)・不是銷售排名・已排除廣告與非輕量商品・點名稱到 MUSINSA 首頁(用韓文名稱搜尋)",
              "rank": "#{n}", "bars_src": "11/26 16:25(營運者確認的畫面)・全商品・第2〜4名未確認・紅色=有輕羽絨售罄報導・金額為韓元",
              "cmp": "比較官網規格", "cmp_src": "價格・填充物・版型・評分",
              "th": ["商品 → 官方頁面", "價格", "填充物", "版型", "評分", "現在"]},
}

# Korean strings from the data files -> en, ja, zh-tw. Translation only: no new facts.
TR = {
    # as_of, table_checked
    "2026-11-26 기준": ("as of 2026-11-26", "2026-11-26時点", "截至 2026-11-26"),
    "11/26 확인": ("checked Nov 26", "11/26確認", "11/26 確認"),
    # sale strip labels
    "유니클로": ("Uniqlo", "ユニクロ", "UNIQLO"),
    "백화점 3사": ("3 department stores", "百貨店3社", "3 大百貨公司"),
    "스파오": ("SPAO", "SPAO", "SPAO"),
    "탑텐": ("TOPTEN", "TOPTEN", "TOPTEN"),
    "무신사 블프": ("Musinsa Black Friday", "ムシンサ ブラックフライデー", "MUSINSA 黑五"),
    # headline numbers
    "★4.9·1만+": ("★4.9 · 10k+", "★4.9・1万+", "★4.9・1萬+"),
    "104.7억": ("₩10.47bn", "104.7億ウォン", "104.7 億韓元"),
    "무신사 8월 경량 패딩 매출(전년 대비)": ("Musinsa lightweight puffer sales in August (vs a year before)",
                                "ムシンサの8月の軽量ダウン売上(前年比)", "MUSINSA 8 月輕羽絨銷售額(和去年比)"),
    "코리아헤럴드 10/20": ("Korea Herald Oct 20", "コリアヘラルド 10/20", "韓國先驅報 10/20"),
    "후기 1위 예일 퀼팅자켓 49,800원": ("Most reviews: YALE quilted jacket ₩49,800",
                              "レビュー数1位 YALE キルティングジャケット 49,800ウォン", "評論數第 1:YALE 絎縫外套 49,800 韓元"),
    "무신사 후기순 11/26 17:04": ("Musinsa, most reviews, Nov 26 17:04", "ムシンサ レビュー順 11/26 17:04", "MUSINSA 評論數排序 11/26 17:04"),
    "블프 전 상품 브랜드 판매 1위 무신사 스탠다드": ("No. 1 brand in Black Friday sales (all items): Musinsa Standard",
                                   "ブラックフライデー全商品のブランド売上1位 ムシンサ・スタンダード",
                                   "黑五全商品品牌銷售第 1:MUSINSA STANDARD"),
    "무신사 집계 11/26 16:25": ("Musinsa tally, Nov 26 16:25", "ムシンサ集計 11/26 16:25", "MUSINSA 統計 11/26 16:25"),
    # review list: reviews count, Nadri reading
    "1만+": ("10k+", "1万+", "1萬+"),
    "8천+": ("8k+", "8千+", "8千+"),
    "7천+": ("7k+", "7千+", "7千+"),
    "Nadri 읽기(화면 12개 기준): 광고 뺀 10개 중 무신사 스탠다드 계열 4개, 퀼팅 자켓 3개": (
        "Nadri's reading (12 items on the screen): of the 10 that are not ads, 4 are Musinsa Standard lines and 3 are quilted jackets",
        "Nadriの読み(画面の12件から): 広告を除いた10件のうち、ムシンサ・スタンダード系が4件、キルティングジャケットが3件",
        "Nadri 解讀(依畫面 12 件): 扣掉廣告的 10 件中,MUSINSA STANDARD 系列 4 件、絎縫外套 3 件"),
    # ranking
    "무신사 무진장 26 겨울 블프 브랜드 판매 금액 순위": ("Musinsa 'Mujinjang 26 Winter' Black Friday: brands by sales",
                                      "ムシンサ「ムジンジャン26冬」ブラックフライデー ブランド別売上順位",
                                      "MUSINSA「MUJINJANG 26 冬季」黑五 品牌銷售額排名"),
    "무신사 스탠다드": ("Musinsa Standard", "ムシンサ・スタンダード", "MUSINSA STANDARD"),
    "아디다스": ("adidas", "アディダス", "adidas"),
    "노스페이스": ("The North Face", "ザ・ノース・フェイス", "The North Face"),
    # links
    "무신사 홈에서 블프 랭킹 찾기": ("Musinsa home: find the Black Friday ranking", "ムシンサのトップで ブラックフライデーのランキングを探す",
                              "到 MUSINSA 首頁找黑五排名"),
    "무신사 홈에서 '경량 패딩' 검색": ("Musinsa home: search 경량 패딩", "ムシンサのトップで「경량 패딩」を検索", "到 MUSINSA 首頁搜尋「경량 패딩」"),
    # comparison table
    "유니클로 라이트다운볼륨": ("Uniqlo Light Down Volume", "ユニクロ ライトダウンボリューム", "UNIQLO Light Down Volume"),
    "유니클로 PUFFTECH컴팩트(남)": ("Uniqlo PUFFTECH Compact (men)", "ユニクロ PUFFTECHコンパクト(メンズ)", "UNIQLO PUFFTECH Compact(男)"),
    "유니클로 울트라라이트다운(남)": ("Uniqlo Ultra Light Down (men)", "ユニクロ ウルトラライトダウン(メンズ)", "UNIQLO Ultra Light Down(男)"),
    "무신사 스탠다드 라이트 다운 (무신사 홈)": ("Musinsa Standard light down (Musinsa home)", "ムシンサ・スタンダード ライトダウン(ムシンサのトップ)",
                                 "MUSINSA STANDARD 輕羽絨(MUSINSA 首頁)"),
    "아크테릭스 세륨 후디(미국)": ("Arc'teryx Cerium Hoody (US)", "アークテリクス セリウムフーディ(米国)", "始祖鳥 Cerium Hoody(美國)"),
    "10만 원대": ("₩100k–199k", "10万ウォン台", "10 多萬韓元"),
    "솜털 85%": ("85% down", "ダウン85%", "羽絨 85%"),
    "합성 솜": ("Synthetic fill", "化繊わた", "人造纖維棉"),
    "솜털 90%": ("90% down", "ダウン90%", "羽絨 90%"),
    "850필 · 338g": ("850 fill · 338 g", "850フィル・338g", "850 FP・338g"),
    "오버사이즈": ("Oversized", "オーバーサイズ", "寬鬆版"),
    "슬림": ("Slim", "スリム", "修身版"),
    "레귤러": ("Regular", "レギュラー", "標準版"),
    "피티드": ("Fitted", "フィッテッド", "合身版"),
    "판매 중": ("Available", "販売中", "販售中"),
    "12월 중순": ("From mid-Dec", "12月中旬から", "12 月中旬起"),
    "품절 보도(10/20)": ("Sold out, per news (Oct 20)", "品切れ報道(10/20)", "報導售罄(10/20)"),
    "미국 블프 ~12/1": ("US Black Friday to Dec 1", "米国ブラックフライデー〜12/1", "美國黑五至 12/1"),
    "–": ("–", "–", "–"),
}

# Musinsa product names: the Korean name stays (it is what you type into Musinsa's search); a plain gloss goes on top.
# Brand spellings YALE / SUARE: see name_en_source in data/shop-trends.json. 시어쉘 (unconfirmed) stays only in the Korean name.
PRODUCT = {
    ("예일", "웜업 퀼팅자켓_블랙"): ("YALE · Warm-up Quilted Jacket, black", "YALE・Warm-up キルティングジャケット ブラック", "YALE・Warm-up 絎縫外套 黑色"),
    ("무신사 스탠다드", "트랜스폼 라운드 넥 라이트 다운 재킷[블랙]"): (
        "Musinsa Standard · Transform round-neck light down jacket, black",
        "ムシンサ・スタンダード・トランスフォーム ラウンドネック ライトダウンジャケット ブラック",
        "MUSINSA STANDARD・Transform 圓領輕羽絨外套 黑色"),
    ("무신사 스탠다드 스포츠", "코어 패딩자켓(4 colors)"): (
        "Musinsa Standard Sports · Core padded jacket (4 colors)",
        "ムシンサ・スタンダード スポーツ・コア パディングジャケット(4色)",
        "MUSINSA STANDARD SPORTS・Core 鋪棉外套(4 色)"),
    ("예일", "웜업 퀼팅자켓_아이보리"): ("YALE · Warm-up Quilted Jacket, ivory", "YALE・Warm-up キルティングジャケット アイボリー", "YALE・Warm-up 絎縫外套 象牙白"),
    ("수아레", "(컬러 추가) 라이트 시어쉘 패딩 점퍼 - 6 COLOR"): (
        "SUARE · light padded jumper, 6 colors (colors added)",
        "SUARE・ライト パディングジャンパー 6色(色追加)",
        "SUARE・輕量鋪棉夾克 6 色(新增顏色)"),
}
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def tr(s, lang):
    if lang == "ko" or s.isascii() and not any(c.isalpha() for c in s.replace("–", "")):
        return s  # Korean, or numbers/symbols only (e.g. +718%)
    try:
        return TR[s][LANGS.index(lang) - 1]
    except KeyError:
        raise SystemExit(f"gen_trend_block: no {lang} translation for data string {s!r}; add it to TR")


def won(n, lang):
    return {"ko": f"{n:,}원", "en": f"₩{n:,}", "ja": f"{n:,}ウォン", "zh-tw": f"{n:,} 韓元"}[lang]


def eok(w, lang):
    if lang == "en":
        return f"₩{w / 1e9:,.2f}bn"
    v = w / 1e8
    s = f"{v:,.1f}" if v < 1000 else f"{v:,.0f}"
    return s + {"ko": "억", "ja": "億", "zh-tw": "億"}[lang]


def dday(d, lang):
    s, e = date.fromisoformat(d["start"]), date.fromisoformat(d["end"])
    if s > TODAY:
        return UI[lang]["starts"].format(m=s.month, d=s.day, mon=MON[s.month - 1])
    n = (e - TODAY).days
    return UI[lang]["today"] if n == 0 else f"D-{n}"


def stat_value(v):
    """Big headline number. "104.7億ウォン" may break only between 億 and ウォン on a phone."""
    v = html.escape(v)
    m = re.fullmatch(r"(.+?億)(ウォン)", v)
    return f'<b class="nw">{m.group(1)}</b><wbr><b class="nw">{m.group(2)}</b>' if m else v


def zhe(pct):
    """Taiwanese 折 notation: 60% off = 4 折 (you pay 40%)."""
    z = (100 - pct) / 10
    return f"{z:g}"


def deal_link(d, lang):
    """The row opens this language's deals board if the deal is listed there, else the sale's source article."""
    if lang == "ko" or lang in d.get("text", {}):
        return f'href="{PREFIX[lang]}/deals/"', ""
    return f'href="{html.escape(d["source"]["url"])}" rel="noopener" target="_blank"', " ↗"


def trend_block(lang):
    T = json.loads((ROOT / "data/shop-trends.json").read_text(encoding="utf-8"))
    D = json.loads((ROOT / "data/deals.json").read_text(encoding="utf-8"))
    ui, e = UI[lang], html.escape
    kw = next(k for k in T["keywords"] if k["id"] == KW)
    blk = kw["trend_block"]
    deals = {d["id"]: d for d in D["items"]}
    items = {i["id"]: i for i in T["items"]}
    rk = next(r for r in T["rankings"] if r["id"] == blk["ranking_id"])
    out = [f'<section class="tb" aria-label="{ui["aria"]}"><p class="tag tag-t"><i class="ic ic-timer" aria-hidden="true"></i>'
           f'{ui["tag"]} · {e(tr(blk["as_of"], lang))}</p>']
    # sale strip (site.js keeps D-day live and hides ended rows)
    rows, ext = [], False
    for did, label in blk["deals"]:
        d = deals.get(did)
        if not d or date.fromisoformat(d["end"]) < TODAY:
            continue
        pct = f' <b>{ui["upto"].format(n=d["hero"]["value"], z=zhe(d["hero"]["value"]))}</b>' if d.get("hero", {}).get("kind") == "pct" else ""
        href, mark = deal_link(d, lang)
        ext = ext or bool(mark)
        rows.append((d["end"], f'<tr data-start="{d["start"]}" data-end="{d["end"]}"><td><a {href}>{e(tr(label, lang))}{pct} '
                     f'<span class="dday" data-today="{ui["today"]}">{dday(d, lang)}</span>{mark}</a></td></tr>'))
    if ext:  # some chips open the Korean news article behind the sale dates, not our deals board
        out[0] = out[0][:-4] + f'<span class="src">{ui["ext"]}</span></p>'
    out.append('<table class="codes strip" role="presentation"><tbody>' + "".join(r for _, r in sorted(rows)) + "</tbody></table>")
    # headline numbers
    cards = "".join(f'<div{" class=hero" if i == 0 else ""}><strong>{stat_value(tr(h["value"], lang))}</strong><span>{e(tr(h["label"], lang))}</span>'
                    f'<span class="src">{e(tr(h["cite"], lang))}</span></div>' for i, h in enumerate(blk["headline"]))
    out.append(f'<div class="stats">{cards}</div>')
    # review-sorted list (not a sales rank); ad-labelled items are excluded
    rv = next(r for r in T["rankings"] if r["id"] == blk["reviews_id"])
    shown = [it for it in rv["items"] if not it["ad"] and not it.get("not_light_puffer")][: blk["reviews_show"]]
    lis = ""
    for n, it in enumerate(shown, 1):
        ko_name = f'{it["brand"]} · {it["product"]}'
        if lang == "ko":
            name, orig = e(ko_name), ""
        else:
            try:
                name = e(PRODUCT[(it["brand"], it["product"])][LANGS.index(lang) - 1])
            except KeyError:
                raise SystemExit(f"gen_trend_block: no {lang} gloss for product {ko_name!r}; add it to PRODUCT")
            orig = f'<small class="ko" lang="ko">{e(ko_name)}</small>'
        lis += (f'<li><b>{n}</b><span class="nm"><a href="https://www.musinsa.com/" rel="noopener" target="_blank" title="{ui["search"]}">'
                f'{name}</a><!-- aff-slot: musinsa {e(it["brand"])} {e(it["product"])} -->{orig}</span>'
                f'<span class="r">★{it["rating"]:.1f} ({e(tr(it["reviews"], lang))})</span><span class="p">{won(it["price_krw"], "ko" if lang == "ko" else "en")} <small>{it["discount_pct"]}%↓</small></span></li>')
    out.append(f'<h3><i class="ic ic-users" aria-hidden="true"></i>{ui["rv_h"]}<span class="src">{ui["rv_src"]}</span></h3>')
    out.append(f'<ol class="rv">{lis}</ol>')
    out.append(f'<p class="reading">{e(tr(rv["reading"]["ko"], lang))}</p>')
    # ranking bars
    top = rk["items"][0]["sales_krw"]
    lis = ""
    for it in rk["items"][: blk.get("bars_show", 99)]:
        cls = ' class="lp"' if it.get("light_puffer_link") else ""
        lis += (f'<li{cls}><b>{ui["rank"].format(n=it["rank"])}</b><span>{e(tr(it["brand"], lang))}</span>'
                f'<i style="width:{round(100 * it["sales_krw"] / top)}%"></i><em>{eok(it["sales_krw"], lang)}</em></li>')
    out.append(f'<h3><i class="ic ic-list-checks" aria-hidden="true"></i>{e(tr(rk["title_ko"], lang))}'
               f'<span class="src">{ui["bars_src"]}</span></h3>')
    out.append(f'<ol class="bars">{lis}</ol>')
    links = "".join(f'<a class="tb-go" href="{e(l["url"])}" rel="noopener" target="_blank">{e(tr(l["label"], lang))} →</a>'
                    f'<!-- aff-slot: {e(l["aff_slot"])} -->' for l in blk["links"])
    out.append(f'<p class="links">{links}</p>')
    # official comparison table
    trs = ""
    for row in blk["table"]:
        i = items[row["item"]]
        price = won(i["price_krw"], lang) if i.get("price_krw") else (f'${i["price_usd"]}' if i.get("price_usd") else e(tr(row.get("price", "–"), lang)))
        rating = f'{i["rating"]:.1f} ({i["reviews"]})' if i.get("rating") else "–"
        trs += (f'<tr><td><a href="{e(row["url"])}" rel="noopener" target="_blank">{e(tr(row["label"], lang))} →</a><!-- aff-slot: {row["item"]} --></td>'
                f'<td class="n">{price}</td><td>{e(tr(row["fill"], lang))}</td><td>{e(tr(row["fit"], lang))}</td><td class="n">{rating}</td><td>{e(tr(row["now"], lang))}</td></tr>')
    out.append(f'<details class="cmpd"><summary><i class="ic ic-tag" aria-hidden="true"></i>{ui["cmp"]} <span class="src">{ui["cmp_src"]} · '
               + e(tr(blk["table_checked"], lang)) + '</span></summary>')
    out.append('<table class="cmp"><thead><tr>' + "".join(f"<th>{h}</th>" for h in ui["th"]) + "</tr></thead><tbody>" + trs + "</tbody></table>")
    out.append("</details>")
    out.append("</section>")
    return "\n".join(out)


def put(page, block):
    s = page.read_text(encoding="utf-8")
    a, b = s.index("<!-- trend:start -->") + len("<!-- trend:start -->"), s.index("<!-- trend:end -->")
    page.write_text(s[:a] + "\n" + block + "\n" + s[b:], encoding="utf-8")


if __name__ == "__main__":
    for lang in LANGS:
        block = trend_block(lang)
        if lang == "ko":
            (pathlib.Path(__file__).resolve().parent / "trend-block.md").write_text(block + "\n", encoding="utf-8")
        put(ROOT / "content" / lang / f"{SLUG}.md", block)
        print(f"trend block written: {lang} {len(block)} chars (today in Seoul: {TODAY})")
