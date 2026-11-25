# phone-first SVG builder: viewBox width 400, min font-size 16
from xml.sax.saxutils import escape as esc
INK, RED, PAPER, MUTED, RULE, WHITE, SOFT = "#16151a", "#b8392f", "#f4f0e6", "#5f5b55", "#c9c1b2", "#ffffff", "#e9e2d3"
FONT = 'system-ui, -apple-system, &quot;Noto Sans KR&quot;, &quot;Noto Sans JP&quot;, &quot;Noto Sans TC&quot;, sans-serif'
W, M = 400, 16
LH = 22

def T(x, y, s, size=16, weight=400, fill=INK, anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>'

class Fig:
    def __init__(self, label):
        self.label, self.parts, self.y = label, [], 18
    def title(self, lines, sub=None):
        for i, l in enumerate(lines):
            self.y += 26 if i else 22
            self.parts.append(T(M, self.y, l, 20, 700))
        for l in (sub or []):
            self.y += LH
            self.parts.append(T(M, self.y, l, 16, 400, MUTED))
        self.y += 14
    def card(self, head=None, lines=(), chip=None, chip_fill=SOFT, chip_ink=INK, fill=WHITE,
             stroke=RULE, sw=1, head_fill=INK, line_fill=MUTED, chip_w=40, red_lines=()):
        x0 = M + (chip_w + 24 if chip else 14)
        n_head = len(head) if isinstance(head, (list, tuple)) else (1 if head else 0)
        heads = head if isinstance(head, (list, tuple)) else ([head] if head else [])
        h = 14 + 22 * n_head + 22 * len(lines) + 10
        if chip: h = max(h, 14 + 36 + 14)
        top = self.y
        self.parts.append(f'<rect x="{M}" y="{top}" width="{W-2*M}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        if chip:
            self.parts.append(f'<rect x="{M+12}" y="{top+12}" width="{chip_w}" height="36" rx="8" fill="{chip_fill}"/>')
            self.parts.append(T(M + 12 + chip_w/2, top + 36, chip, 16, 700, chip_ink, "middle"))
        yy = top + 14
        for hl in heads:
            yy += 20
            self.parts.append(T(x0, yy, hl, 17, 700, head_fill))
            yy += 2
        for i, l in enumerate(lines):
            yy += 20 if i == 0 and not heads else 22 if i or heads else 20
            col = RED if i in red_lines else line_fill
            wt = 700 if i in red_lines else 400
            self.parts.append(T(x0, yy, l, 16, wt, col))
        self.y = top + h + 10
    def arrow(self, label=None):
        cx = 44
        y0 = self.y - 4
        self.parts.append(f'<path d="M{cx} {y0} V{y0+24}" stroke="{MUTED}" stroke-width="2"/>')
        self.parts.append(f'<path d="M{cx-6} {y0+18} L{cx} {y0+26} L{cx+6} {y0+18}" fill="none" stroke="{MUTED}" stroke-width="2"/>')
        if label:
            self.parts.append(T(cx + 16, y0 + 19, label, 16, 700, MUTED))
        self.y = y0 + 34
    def question(self, q_lines, yes_label, out_lines, pill_w=56):
        # soft question box with a white "yes" outcome strip inside
        top = self.y
        h_q = 14 + 22 * len(q_lines)
        h_o = 12 + 22 * len(out_lines) + 8
        h = h_q + 10 + h_o + 12
        self.parts.append(f'<rect x="{M}" y="{top}" width="{W-2*M}" height="{h}" rx="10" fill="{SOFT}"/>')
        yy = top + 14
        for l in q_lines:
            yy += 20
            self.parts.append(T(M + 14, yy, l, 17, 700))
            yy += 2
        ot = top + h_q + 10
        self.parts.append(f'<rect x="{M+10}" y="{ot}" width="{W-2*M-20}" height="{h_o}" rx="8" fill="{WHITE}"/>')
        self.parts.append(f'<rect x="{M+20}" y="{ot+10}" width="{pill_w}" height="26" rx="13" fill="{RED}"/>')
        self.parts.append(T(M + 20 + pill_w/2, ot + 29, yes_label, 16, 700, WHITE, "middle"))
        xo = M + 20 + pill_w + 10
        yy = ot + 8
        for i, l in enumerate(out_lines):
            yy += 22
            self.parts.append(T(xo, yy - 1, l, 16, 700 if i == 0 else 400, INK if i == 0 else MUTED))
        self.y = top + h + 10
    def row(self, label, value, bold_value=True, value_fill=INK, top_rule=True):
        if top_rule:
            self.parts.append(f'<path d="M{M+14} {self.y} H{W-M-14}" stroke="{RULE}" stroke-width="1"/>')
        self.y += 28
        self.parts.append(T(M + 14, self.y, label, 16, 400, MUTED))
        self.parts.append(T(W - M - 14, self.y, value, 17 if bold_value else 16, 700 if bold_value else 400, value_fill, "end"))
        self.y += 14
    def box_start(self):
        self._box_top, self._box_idx = self.y, len(self.parts)
        self.y += 4
    def box_end(self, fill=WHITE, stroke=RULE):
        h = self.y - self._box_top + 6
        self.parts.insert(self._box_idx, f'<rect x="{M}" y="{self._box_top}" width="{W-2*M}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}"/>')
        self.y = self._box_top + h + 10
    def note(self, lines, fill=MUTED, weight=400):
        for l in lines:
            self.y += LH
            self.parts.append(T(M, self.y, l, 16, weight, fill))
        self.y += 8
    def raw(self, s, dy=0):
        self.parts.append(s); self.y += dy
    def svg(self):
        H = int(self.y + 8)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(self.label)}" font-family="{FONT}">\n'
                f'<rect width="{W}" height="{H}" fill="{PAPER}"/>\n' + "\n".join(self.parts) + "\n</svg>\n")

def row2(self, label, value, value_fill=RED, top_rule=True):
    if top_rule:
        self.parts.append(f'<path d="M{M+14} {self.y} H{W-M-14}" stroke="{RULE}" stroke-width="1"/>')
    self.y += 26
    self.parts.append(T(M + 14, self.y, label, 16, 400, MUTED))
    self.y += 24
    self.parts.append(T(M + 14, self.y, value, 18, 700, value_fill))
    self.y += 14
Fig.row2 = row2

def steps(self, items, x=M, w=None, chip_w=32):
    # compact numbered rows inside an existing frame
    w = w or (W - 2 * M)
    for i, (head, line, red) in enumerate(items):
        top = self.y
        h = 14 + 22 + (22 if line else 0) + 10
        self.parts.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="8" fill="{WHITE}" stroke="{RED if red else RULE}" stroke-width="{2 if red else 1}"/>')
        self.parts.append(f'<circle cx="{x+12+chip_w/2}" cy="{top+h/2}" r="{chip_w/2}" fill="{RED if red else INK}"/>')
        self.parts.append(T(x + 12 + chip_w/2, top + h/2 + 6, str(i + 1), 16, 700, WHITE, "middle"))
        tx = x + 12 + chip_w + 12
        self.parts.append(T(tx, top + (34 if line else 30), head, 17, 700, RED if red else INK))
        if line:
            self.parts.append(T(tx, top + 56, line, 16, 400, MUTED))
        self.y = top + h + 8
Fig.steps = steps
