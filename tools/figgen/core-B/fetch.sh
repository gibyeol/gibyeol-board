#!/bin/bash
# usage: fetch.sh name url
d=/tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/core-B/web
curl -sL --retry 2 --max-time 60 -A "Mozilla/5.0" -b $d/ck -c $d/ck "$2" -o $d/$1.html -w "$1 %{http_code} %{size_download}\n"
python3 -I -c '
import sys,re,html
s=open(sys.argv[1],encoding="utf-8",errors="replace").read()
s=re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>","",s)
s=re.sub(r"(?i)<br\s*/?>|</p>|</li>|</tr>|</h\d>|</div>|</td>|</th>","\n",s)
s=re.sub(r"<[^>]+>"," ",s); s=html.unescape(s)
s=re.sub(r"[ \t\xa0]+"," ",s); s=re.sub(r"\n\s*\n+","\n",s)
open(sys.argv[2],"w").write(s)' $d/$1.html $d/$1.txt
