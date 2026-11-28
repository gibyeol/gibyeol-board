"""Merge collected EN/KO/JA/ZH name records into static/name-en4.js (owner 2026-11-28 [7eb4ec94#4639] [7eb4ec94#4680]).

Input: JSON arrays of records (see trendmin-threads scratch BRIEF): key, type (given|surname|nick), of, sex,
ko_std (+src), ko_alt (+src), ja (+src), zh (+src), origin, meaning{en,ko,ja,zh} (+src), c, nicks, note.
Output: static/name-en4.js, which adds to window.NADRI_NAMES at load time:
  given/surname: {ko, ks?, ka?, ja?, zh?, o?, c?, m?, t}  - ko = the spelling in use first (ko_alt[0]) when one is evidenced,
                 ks = the National Institute of Korean Language standard when it differs ("매튜 / 매슈")
  nick:          {of, ko, ks?, ja?, zh?}
Existing hand-checked entries in name-data.js keep their meaning text; only missing fields are filled and ko/ks are
updated when the record has a source. Nothing is invented here: empty fields stay empty.
usage: python3 tools/names/merge_en4.py <records.json> [...]
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "static" / "name-en4.js"


# reviewed corrections (2026-11-28, Claude while merging): spellings taken from one person's title that are not the name itself
POP_FIRST = {"matthew", "matthews",   # owner [7eb4ec94#4642]
             # owner [7eb4ec94#4748]: "많이쓰는걸 앞에 둬" - which one is used more: Claude judgement (no official source), both always shown;
             # review 2026-11-28: matt/david/richard/samuel back to standard first (맷 데이먼, 데이비드 베컴, 리처드 기어, 새뮤얼 L. 잭슨)
             "emma", "liam", "jacob", "daniel", "benjamin", "lucas", "leo", "andrew", "thomas", "joseph", "nicholas", "jonathan", "timothy", "julian", "sebastian", "owen", "brandon", "isabella", "amelia", "sarah", "samantha", "angela", "stephanie", "rebecca", "melissa", "amanda", "camila", "violet", "eleanor", "evelyn", "elias", "josh", "bobby", "drew", "greg", "adams", "evans", "daniels", "andrews", "simmons", "jenkins", "thompson", "hughes", "lopez", "gomez", "diaz", "cruz"}
FIX = {"lee": {"meaning": None, "origin": None, "note": "Lee is also the Korean/Chinese surname 이/李: no English-surname meaning (review 2026-11-28)"},
       "sam": {"of": "samuel", "note": "BtN: short form of Samuel, Samson, Samantha (Samuel first)"},
       "charlie": {"of": "charles", "note": "BtN: diminutive or feminine form of Charles"},
       "steph": {"of": None, "zh": None, "note": "BtN: Stephanie or Stephen -> no single full name; zh 斯蒂夫 is Steve"},
       "ted": {"of": None, "note": "BtN: Edward or Theodore"},
       "al": {"of": None, "note": "BtN: Albert and other names"},
       "lori": {"of": None, "note": "BtN: Laura, Lorraine"},
       "mel": {"of": None, "note": "BtN: Melvin, Melanie, Melissa"},
       "nguyen": {"ko_alt": [], "note": "윈 had 1 usage example against 4 for 응우옌: not shown first"},
       "kim": {"skip": True, "note": "Kim: an English first name (킴) and the Korean surname (김); keep the existing entry"}}


def clean(s):
    return (s or "").strip() or None


def main(paths):
    recs = []
    for p in paths:
        recs += json.load(open(p, encoding="utf-8"))
    out, skipped, surn_e = {}, [], {}
    surn = {(r.get("key") or "").lower() for r in recs if r.get("type") == "surname"}
    for r in recs:
        k = (r.get("key") or "").strip().lower()
        if not k:
            continue
        if r.get("type") == "nick" and k in surn:   # Kim the surname (김) wins over Kim the short form of Kimberly
            skipped.append((k, "short form that is also a surname on the list"))
            continue
        if k in FIX:
            r = dict(r, **FIX[k])
            if r.get("skip"):
                skipped.append((k, r["note"]))
                continue
        std = clean(r.get("ko_std")) if r.get("ko_std_src") else None
        alts = [a for a in (r.get("ko_alt") or []) if a and a != std] if r.get("ko_alt_src") else []
        # owner [7eb4ec94#4680]: show both. Which goes first needs evidence of use; only owner-confirmed names put the
        # spelling in use first (owner [7eb4ec94#4642]: Matthews -> 매튜스). Others: standard first, the other after it.
        if alts and std and k not in POP_FIRST:
            ko, alt_after = std, alts[0]
        else:
            ko, alt_after = (alts[0] if alts else std), None
        if not ko:
            if r.get("type") == "nick" and r.get("of") and k not in out:
                out[k] = r["of"].strip().lower()   # still link the short form to the full name (meaning); sound falls back
                continue
            skipped.append((k, "no sourced Korean spelling"))
            continue
        e = {"ko": ko}
        if alts and std and std != ko:
            e["ks"] = std
        if alt_after:
            e["ka"] = alt_after
        if clean(r.get("ja")) and r.get("ja_src"):
            e["ja"] = r["ja"].strip()
        # a one-character Chinese form of a first name comes from one person's local name (金 for Jim Carrey): not a general spelling
        if clean(r.get("zh")) and r.get("zh_src") and (len(r["zh"].strip()) >= 2 or r.get("type") == "surname"):
            e["zh"] = r["zh"].strip()
        if r.get("type") == "nick" and r.get("of"):
            e["of"] = r["of"].strip().lower()
        elif r.get("type") == "nick":
            pass  # short form of several names: own spellings, no single meaning
        else:
            m = r.get("meaning") or {}
            if m.get("en") and r.get("meaning_src"):
                e["m"] = {x: m[x] for x in ("en", "ko", "ja", "zh") if m.get(x)}
                e["c"] = r.get("c") or "m"
                u = re.search(r"https?://\S+", r.get("meaning_src") or "")
                if u:   # shown as the meaning's source (review 2026-11-28: most surname meanings are from Wikipedia, not Behind the Name)
                    e["ms"] = u.group(0).rstrip(").,;'\"")
            if clean(r.get("origin")):
                e["o"] = r["origin"].strip()
        e["t"] = r.get("type") or "given"
        if e["t"] == "surname":
            surn_e[k] = e
        if k in out:  # same key from two lists (e.g. a nick that is also a given name): keep the fuller one
            o = out[k]
            # a first name and a surname with one spelling (Thomas, Kelly): the first-name record stays the entry,
            # the surname's spellings go to sk/sj/sz below (review 2026-11-28)
            if isinstance(o, dict) and (o.get("t") == "surname") != (e["t"] == "surname"):
                if e["t"] == "surname":
                    continue
            elif not isinstance(o, str) and len(json.dumps(o)) >= len(json.dumps(e)):
                continue
        out[k] = e
    # a word that is both a first name and a surname (Riley, Kelly): keep the surname's own spellings for the surname position
    # (review 2026-11-28: Charles Riley showed the actress's 芮莉 in the surname place). None = surname spelling not settled.
    for k, se in surn_e.items():
        g = out.get(k)
        if isinstance(g, dict) and g is not se and g.get("t") != "surname":
            for f, sf in (("ko", "sk"), ("ja", "sj"), ("zh", "sz")):
                if g.get(f) != se.get(f):
                    g[sf] = se.get(f) or ""
    js = ("/* EN/KO/JA/ZH name list (owner 2026-11-28 [7eb4ec94#4639] [7eb4ec94#4680]). Generated by tools/names/merge_en4.py;\n"
          "   sources per record in data/names-en4/*.json. Fills window.NADRI_NAMES without overwriting checked meanings. */\n"
          "(function () {\n  var A = " + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n"
          "  var D = window.NADRI_NAMES = window.NADRI_NAMES || {};\n"
          "  Object.keys(A).forEach(function (k) {\n"
          "    var a = A[k], d = D[k];\n"
          "    if (typeof a === 'string') { if (!d) D[k] = a; return; }   // short form with no checked Korean spelling: link only\n"
          "    // checked link (Mary -> Maria, Sofia -> Sophia): keep the link for the meaning, add the collected spellings (review 2026-11-28)\n"
          "    if (typeof d === 'string') { if (a.ko) D[k] = Object.assign({}, a, { of: a.of || d, m: undefined, c: undefined, ms: undefined }); return; }\n"
          "    if (!d || typeof d !== 'object') { D[k] = a; return; }\n"
          "    ['ko', 'ks', 'ka', 'of'].forEach(function (f) { if (a[f]) d[f] = a[f]; });\n"
          "    // keep the checked Japanese/Chinese spelling; a different collected spelling is kept for look-up only (jv/zv)\n"
          "    if (a.ja) { if (!d.ja) d.ja = a.ja; else if (d.ja !== a.ja) d.jv = (d.jv || []).concat(a.ja); }\n"
          "    if (a.zh) { if (!d.zh) d.zh = a.zh; else if (d.zh !== a.zh) d.zv = (d.zv || []).concat(a.zh); }\n"
          "    if (a.m && !d.m) { d.m = a.m; d.c = a.c; if (a.ms) d.ms = a.ms; }\n"
          "    if (a.o && !d.o) d.o = a.o;\n"
          "    ['sk', 'sj', 'sz'].forEach(function (f) { if (f in a) d[f] = a[f]; });\n"
          "  });\n})();\n")
    OUT.write_text(js, encoding="utf-8")
    print(f"{len(out)} names -> {OUT.relative_to(ROOT)}; skipped {len(skipped)}")
    for k, why in skipped[:40]:
        print("  skip", k, why)


if __name__ == "__main__":
    main(sys.argv[1:])
