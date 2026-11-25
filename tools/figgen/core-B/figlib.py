"""Phone-first SVG helpers: viewBox width 400, min font-size 16."""
from xml.sax.saxutils import escape as _e

FONT = 'system-ui, -apple-system, &quot;Noto Sans KR&quot;, &quot;Noto Sans JP&quot;, &quot;Noto Sans TC&quot;, sans-serif'
INK, RED, PAPER, MUTED, RULE, WHITE, SOFT = '#16151a', '#b8392f', '#f4f0e6', '#5f5b55', '#c9c1b2', '#ffffff', '#e9e2d3'
W = 400
OUT = '/home/user/gibyeol-board/static/fig'


def e(s):
    return _e(s, {'"': '&quot;'})


def T(x, y, s, size=16, w='400', fill=INK, anchor='start'):
    assert size >= 16, (s, size)
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{e(s)}</text>\n'


def R(x, y, w, h, fill=WHITE, stroke=RULE, sw=1.5, rx=10):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>\n'


def arrow(x, y1, y2, color=INK):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - 8}" stroke="{color}" stroke-width="2.5"/>\n'
            f'<path d="M{x - 7},{y2 - 10} L{x},{y2} L{x + 7},{y2 - 10} z" fill="{color}"/>\n')


class Fig:
    def __init__(self, title_lines):
        self.title = title_lines
        self.body = ''
        self.y = 30 + 26 * (len(title_lines) - 1) + 24  # cursor below title

    def add(self, s):
        self.body += s

    def svg(self, pad=18):
        h = self.y + pad
        t = ''.join(T(20, 34 + 26 * i, s, 20, '700') for i, s in enumerate(self.title))
        label = ' '.join(self.title)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" role="img" aria-label="{e(label)}" '
                f'font-family="{FONT}">\n<title>{e(label)}</title>\n'
                f'<rect width="{W}" height="{h}" fill="{PAPER}"/>\n{t}{self.body}</svg>\n')

    def footer(self, lines, size=16, fill=MUTED, gap=8):
        self.y += gap
        for s in lines:
            self.y += 22
            self.add(T(20, self.y, s, size, '400', fill))


def write(lang, name, svg):
    import os
    p = f'{OUT}/{lang}/{name}.svg'
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(svg)
    return p
