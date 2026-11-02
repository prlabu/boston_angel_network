"""Compact SVG path encoding for potrace curves (relative commands, 1-dp)."""
import math


def fmt(v):
    v = round(v, 1)
    if v == 0:
        return '0'
    s = f'{v:.1f}'
    if s.endswith('.0'):
        s = s[:-2]
    if s.startswith('0.'):
        s = s[1:]
    elif s.startswith('-0.'):
        s = '-' + s[2:]
    return s


def r1(v):
    return round(v * 10) / 10.0


class Enc:
    def __init__(self):
        self.out = []
        self.last_cmd = None
        self.last_tok = ''

    def cmd(self, c):
        if c != self.last_cmd or c in 'Mm':
            self.out.append(c)
            self.last_tok = c
            self.last_cmd = c

    def num(self, v):
        s = fmt(v)
        prev = self.last_tok
        need = True
        if prev and prev[-1].isalpha():
            need = False
        elif s[0] == '-':
            need = False
        elif s[0] == '.' and ('.' in prev):
            need = False
        self.out.append((' ' if need else '') + s)
        self.last_tok = s

    def text(self):
        return ''.join(self.out)


def curves_to_d(curves, tx=0.0, ty=0.0, k=1.0):
    """curves: list of {'start':[x,y], 'segs':[['L',c,e] | ['C',c1,c2,e]]}
    Coordinates are mapped p' = (p - (tx,ty)) * k, then rounded to 1 dp.
    Relative deltas are computed between ROUNDED absolutes so nothing drifts."""
    e = Enc()

    def P(p):
        return (r1((p[0] - tx) * k), r1((p[1] - ty) * k))

    for cv in curves:
        cur = P(cv['start'])
        start = cur
        e.cmd('M'); e.num(cur[0]); e.num(cur[1])
        e.last_cmd = None
        for sg in cv['segs']:
            if sg[0] == 'L':
                for q in (sg[1], sg[2]):
                    q = P(q)
                    dx, dy = r1(q[0] - cur[0]), r1(q[1] - cur[1])
                    if dx == 0 and dy == 0:
                        continue
                    if dy == 0:
                        e.cmd('h'); e.num(dx)
                    elif dx == 0:
                        e.cmd('v'); e.num(dy)
                    else:
                        e.cmd('l'); e.num(dx); e.num(dy)
                    cur = q
            else:
                c1, c2, q = P(sg[1]), P(sg[2]), P(sg[3])
                e.cmd('c')
                for p in (c1, c2, q):
                    e.num(r1(p[0] - cur[0])); e.num(r1(p[1] - cur[1]))
                cur = q
        e.cmd('z')
        e.last_cmd = None
    return e.text()


def bbox(curves):
    xs, ys = [], []
    for cv in curves:
        pts = [cv['start']] + [p for sg in cv['segs'] for p in sg[1:]]
        xs += [p[0] for p in pts]; ys += [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)
