"""IndexNow: tell Bing (and the other IndexNow search engines) which public pages were added or changed.

Source: https://www.indexnow.org/documentation and /faq (read 2026-11-28, copy in wondu-archive
raw-from-scratchpad/bing-2026-11-28). Rules followed here:
- the key file {key}.txt sits at the site root (build.py writes it from data/site.json indexnow_key);
- one POST of up to 10,000 URLs to one endpoint (we use https://www.bing.com/indexnow); it is shared
  with the other participating engines;
- "Submit only when content has changed. Do not resubmit unchanged URLs."
- "Should I submit URLs that changed before I started using IndexNow? No." -> send only pages changed
  after the key file went live (i.e. with each later publish), not the whole sitemap.

Only URLs that are in the LIVE sitemap are sent (never drafts). Nothing is sent without --send.

  python3 tools/indexnow.py --since 2026-11-28          # list pages whose sitemap lastmod >= date
  python3 tools/indexnow.py --all                       # every page in the live sitemap
  python3 tools/indexnow.py /ko/essentials/ /essentials/ # these paths only (must be in the sitemap)
  ... add --send to actually submit; the result is appended to ops/indexnow-log.md
"""
import datetime
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = json.loads((ROOT / "data/site.json").read_text(encoding="utf-8"))
BASE = SITE["base_url"].rstrip("/")
KEY = SITE.get("indexnow_key", "")
ENDPOINT = "https://www.bing.com/indexnow"
LOG = ROOT / "ops/indexnow-log.md"


def get(url):
    r = subprocess.run(["curl", "-s", "-L", "--max-time", "30", "-w", "\n%{http_code}", url], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"curl failed on {url} (exit {r.returncode}). Nothing sent.")
    body, _, code = r.stdout.rpartition("\n")
    return code, body


def main(argv):
    send = "--send" in argv
    args = [a for a in argv if a != "--send"]
    if not KEY:
        sys.exit("data/site.json has no indexnow_key")
    code, body = get(f"{BASE}/{KEY}.txt")
    if code != "200" or body.strip() != KEY:
        sys.exit(f"key file {BASE}/{KEY}.txt is not live (HTTP {code}); publish it first. Nothing sent.")
    code, sm = get(f"{BASE}/sitemap.xml")
    if code != "200":
        sys.exit(f"live sitemap HTTP {code}. Nothing sent.")
    live = dict(re.findall(r"<url><loc>([^<]+)</loc>(?:<lastmod>([^<]+)</lastmod>)?</url>", sm))
    if args == ["--all"]:
        urls = list(live)
    elif args[:1] == ["--since"] and len(args) == 2 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", args[1]):
        urls = [u for u, d in live.items() if d and d >= args[1]]
    elif args and not any(a.startswith("--") for a in args):
        urls = [BASE + a for a in args]
        missing = [u for u in urls if u not in live]
        if missing:
            sys.exit("not in the live sitemap (not public?): " + " ".join(missing))
    else:
        sys.exit(__doc__)
    if not urls:
        sys.exit("no URLs matched. Nothing sent.")
    if len(urls) > 10000:
        sys.exit("more than 10,000 URLs in one request (IndexNow limit).")
    host = BASE.split("://", 1)[1]
    payload = {"host": host, "key": KEY, "keyLocation": f"{BASE}/{KEY}.txt", "urlList": urls}
    print(f"{len(urls)} URL(s) -> {ENDPOINT}")
    for u in urls[:5]:
        print("  ", u)
    if len(urls) > 5:
        print(f"   ... and {len(urls) - 5} more")
    if not send:
        print("dry run: add --send to submit")
        return
    r = subprocess.run(["curl", "-s", "--max-time", "60", "-o", "/dev/stderr", "-w", "%{http_code}", "-X", "POST", ENDPOINT,
                        "-H", "Content-Type: application/json; charset=utf-8", "--data-binary", "@-"],
                       input=json.dumps(payload), capture_output=True, text=True)
    code = r.stdout.strip() if r.returncode == 0 else f"000 (curl exit {r.returncode}, not delivered)"
    meaning = {"200": "OK, URL submitted", "202": "accepted, key validation pending", "400": "bad request",
               "403": "key not valid", "422": "URL/key does not match the host", "429": "too many requests"}
    print(f"HTTP {code} {meaning.get(code, '')} {r.stderr.strip()[:300]}")
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M KST")
    with LOG.open("a", encoding="utf-8") as f:
        if f.tell() == 0:
            f.write("# IndexNow 전송 기록 (tools/indexnow.py가 씀)\n\n| 시각 | 보낸 곳 | 주소 수 | 결과 | 조건 |\n|---|---|---|---|---|\n")
        f.write(f"| {now} | {ENDPOINT} | {len(urls)} | HTTP {code} {meaning.get(code, '')} | {' '.join(args)} |\n")
        f.write("<details><summary>보낸 주소</summary>\n\n" + "\n".join(f"- {u}" for u in urls) + "\n\n</details>\n\n")
    print(f"logged to {LOG.relative_to(ROOT)} - commit it")


if __name__ == "__main__":
    main(sys.argv[1:])
