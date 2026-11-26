# winter-light-puffer-1 (ko): how a lightweight puffer is worn this winter.
# Facts: The Korea Herald 2026-10-20 (article 10908829: standalone in fall, layering piece in midwinter;
# defined waist, roomier shoulders; oatmeal, fog gray) and 2026-11-23 (article 10946254: pale pastels).
# Drawing is schematic (no real product, no brand). Phone-first: viewBox width 400, font >= 16.
import html, pathlib
FONT = 'system-ui, -apple-system, &quot;Noto Sans KR&quot;, sans-serif'
INK, RED, PAPER, MUTED, RULE, WHITE = '#16151a', '#b8392f', '#f4f0e6', '#5f5b55', '#c9c1b2', '#ffffff'
W = 400


def e(s): return html.escape(s, quote=False)


def text(x, y, s, size=16, fill=INK, bold=False, anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{"bold" if bold else "normal"}" text-anchor="{anchor}">{e(s)}</text>'


def num(cx, cy, n):
    return f'<circle cx="{cx}" cy="{cy}" r="13" fill="{RED}"/>' + text(cx, cy + 6, str(n), 16, WHITE, True)


def puffer(cx, top, fill, w=96, h=118, waist=True):
    """Short quilted jacket: roomy shoulders, nipped waist, hood."""
    l, r = cx - w // 2, cx + w // 2
    wl, wr = (cx - w // 2 + 10, cx + w // 2 - 10) if waist else (l, r)
    b = top + h
    body = (f'<path d="M{l-6},{top+14} Q{cx},{top-6} {r+6},{top+14} L{wr},{top+h*0.62} L{r},{b} L{l},{b} L{wl},{top+h*0.62} Z" '
            f'fill="{fill}" stroke="{INK}" stroke-width="2"/>')
    quilt = ''.join(f'<line x1="{l+2}" y1="{top+16+i*20}" x2="{r-2}" y2="{top+16+i*20}" stroke="{INK}" stroke-opacity=".35" stroke-width="1.5"/>' for i in range(1, 5))
    zip_ = f'<line x1="{cx}" y1="{top+6}" x2="{cx}" y2="{b}" stroke="{INK}" stroke-width="1.5"/>'
    arms = (f'<path d="M{l-6},{top+14} L{l-20},{top+h-6} L{l-6},{top+h-2} L{l+4},{top+40}" fill="{fill}" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{r+6},{top+14} L{r+20},{top+h-6} L{r+6},{top+h-2} L{r-4},{top+40}" fill="{fill}" stroke="{INK}" stroke-width="2"/>')
    hood = f'<path d="M{cx-26},{top+8} Q{cx},{top-22} {cx+26},{top+8}" fill="none" stroke="{INK}" stroke-width="2"/>'
    return arms + body + quilt + zip_ + hood


def person(cx, top):
    head = f'<circle cx="{cx}" cy="{top-30}" r="20" fill="#e9dcc9" stroke="{INK}" stroke-width="2"/>'
    legs = (f'<rect x="{cx-30}" y="{top+118}" width="26" height="78" rx="6" fill="#3c4a5c" stroke="{INK}" stroke-width="2"/>'
            f'<rect x="{cx+4}" y="{top+118}" width="26" height="78" rx="6" fill="#3c4a5c" stroke="{INK}" stroke-width="2"/>')
    return head + legs


def coat(cx, top):
    """Long open coat drawn behind/over the puffer."""
    c = '#8a6a4f'
    sleeves = (f'<path d="M{cx-54},{top+10} L{cx-74},{top+150} L{cx-56},{top+154} L{cx-44},{top+40}" fill="{c}" stroke="{INK}" stroke-width="2"/>'
               f'<path d="M{cx+54},{top+10} L{cx+74},{top+150} L{cx+56},{top+154} L{cx+44},{top+40}" fill="{c}" stroke="{INK}" stroke-width="2"/>')
    left = f'<path d="M{cx-54},{top+10} Q{cx-30},{top} {cx-18},{top+4} L{cx-22},{top+186} L{cx-60},{top+186} Z" fill="{c}" stroke="{INK}" stroke-width="2"/>'
    right = f'<path d="M{cx+54},{top+10} Q{cx+30},{top} {cx+18},{top+4} L{cx+22},{top+186} L{cx+60},{top+186} Z" fill="{c}" stroke="{INK}" stroke-width="2"/>'
    return sleeves + left + right


def build():
    b = []
    b.append(text(W // 2, 34, '경량 패딩, 이렇게 입어요', 20, INK, True))
    b.append(text(W // 2, 58, '그림 예시 · 실제 상품 아님', 16, MUTED))
    # panel 1: alone
    b.append(f'<rect x="12" y="74" width="182" height="344" rx="12" fill="{WHITE}" stroke="{RULE}"/>')
    b.append(person(103, 140))
    b.append(puffer(103, 140, '#d9cdb8'))
    b.append(text(103, 380, '가을·초겨울', 17, INK, True))
    b.append(text(103, 404, '겉옷 하나로', 16, MUTED))
    # panel 2: under a coat
    b.append(f'<rect x="206" y="74" width="182" height="344" rx="12" fill="{WHITE}" stroke="{RULE}"/>')
    b.append(person(297, 140))
    b.append(puffer(297, 140, '#b9c3cc', w=84, h=110))
    b.append(coat(297, 136))
    b.append(text(297, 380, '한겨울', 17, INK, True))
    b.append(text(297, 404, '코트 안에 한 겹 더', 16, MUTED))
    # what to look for this year
    y = 452
    b.append(text(20, y, '올해 많이 보이는 모양', 18, INK, True, 'start'))
    b.append(num(32, y + 30, 1) + text(54, y + 36, '허리선이 들어간 입체 실루엣', 16, INK, False, 'start'))
    b.append(num(32, y + 64, 2) + text(54, y + 70, '어깨는 넉넉하게', 16, INK, False, 'start'))
    b.append(num(32, y + 98, 3) + text(54, y + 104, '검정 말고 옅은 색', 16, INK, False, 'start'))
    sw = [('#d9cdb8', '오트밀'), ('#b9c3cc', '포그 그레이'), ('#cfe3d6', '파스텔')]
    for i, (c, n) in enumerate(sw):
        x = 20 + i * 132
        b.append(f'<rect x="{x}" y="{y+120}" width="30" height="30" rx="6" fill="{c}" stroke="{INK}" stroke-width="1.5"/>')
        b.append(text(x + 38, y + 141, n, 16, INK, False, 'start'))
    b.append(text(20, y + 182, '색은 예시예요. 실제 색은 상품마다 달라요.', 16, MUTED, False, 'start'))
    h = y + 200
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" role="img" aria-label="경량 패딩 입는 두 가지 방법과 올해 많이 보이는 모양" font-family="{FONT}">\n'
            f'<title>경량 패딩 입는 두 가지 방법과 올해 많이 보이는 모양</title>\n<rect width="{W}" height="{h}" fill="{PAPER}"/>\n' + '\n'.join(b) + '\n</svg>\n')


if __name__ == '__main__':
    out = pathlib.Path(__file__).resolve().parents[2] / 'static' / 'fig' / 'ko' / 'winter-light-puffer-1.svg'
    out.write_text(build(), encoding='utf-8')
    print('wrote', out)


# Product-card drawings for the winter-light-puffer prototype (no text, no logo, not a product photo).
# Colours are the colours the source names (Korea Herald 2026-10-20): Musinsa Standard "Cloudy Blue",
# New Balance Flying 77 "Butter Yellow" (also Ash Blue, Charcoal), The North Face Ventus On "Real Black/Black",
# MLB Curve Air Shell "lavender".
CARDS = {'musinsa-std': '#a9c6de', 'nb-flying77': '#f1dc8a', 'tnf-ventuson': '#2b2b2e', 'mlb-curve': '#c7b7e2'}


def card_icon(fill, hood=True):
    w, h, cx, top = 160, 120, 80, 22
    l, r, b = cx - 38, cx + 38, top + 84
    stroke = '#5f5b55' if fill == '#2b2b2e' else INK
    line = '#ffffff' if fill == '#2b2b2e' else INK
    parts = [f'<rect width="{w}" height="{h}" fill="{PAPER}"/>']
    parts.append(f'<path d="M{l-4},{top+12} L{l-18},{b-6} L{l-6},{b-2} L{l+2},{top+34} Z" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    parts.append(f'<path d="M{r+4},{top+12} L{r+18},{b-6} L{r+6},{b-2} L{r-2},{top+34} Z" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    parts.append(f'<path d="M{l-4},{top+12} Q{cx},{top-4} {r+4},{top+12} L{r-6},{top+52} L{r},{b} L{l},{b} L{l+6},{top+52} Z" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    for i in range(1, 5):
        y = top + 12 + i * 16
        parts.append(f'<line x1="{l+3}" y1="{y}" x2="{r-3}" y2="{y}" stroke="{line}" stroke-opacity=".35" stroke-width="1.5"/>')
    parts.append(f'<line x1="{cx}" y1="{top+4}" x2="{cx}" y2="{b}" stroke="{line}" stroke-opacity=".6" stroke-width="1.5"/>')
    if hood:
        parts.append(f'<path d="M{cx-20},{top+6} Q{cx},{top-18} {cx+20},{top+6}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="패딩 그림">'
            + ''.join(parts) + '</svg>\n')


if __name__ == '__main__':
    base = pathlib.Path(__file__).resolve().parents[2] / 'static' / 'fig'
    for k, c in CARDS.items():
        (base / f'light-puffer-{k}.svg').write_text(card_icon(c), encoding='utf-8')
        print('wrote', k)
