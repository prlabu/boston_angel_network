"""Write logo.svg, mark.svg, favicon.svg from a trace JSON.

Usage: python build.py TRACE.json OUTDIR [--fav-stroke 0] [--fav-margin 0.07]
Prints viewBox geometry as JSON on the last line.
"""
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgpath import curves_to_d, fmt

ap = argparse.ArgumentParser()
ap.add_argument('trace'); ap.add_argument('outdir')
ap.add_argument('--fav-stroke', type=float, default=0.0)
ap.add_argument('--fav-margin', type=float, default=0.07)
a = ap.parse_args()
T = json.load(open(a.trace))
os.makedirs(a.outdir, exist_ok=True)

# Ink bounding boxes measured on the thresholded source (x1/y1 exclusive).
INK_ALL = (184, 431, 3324, 1852)
INK_TOP = (186, 431, 3308, 1113)
INK_BAF = (186, 431, 1560, 1113)
SPLIT_X = T['params']['split']


def vb(box, m):
    x0, y0, x1, y1 = box
    return x0 - m, y0 - m, (x1 - x0) + 2 * m, (y1 - y0) + 2 * m


def p(curves, tx, ty, k=1.0, extra=''):
    return f'<path fill="currentColor"{extra} d="{curves_to_d(curves, tx, ty, k)}"/>'


def svg_open(w, h, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {fmt(w)} {fmt(h)}" '
            f'role="img" aria-label="{label}">')


def wings(tx, ty):
    return ('<g id="wings">'
            f'<g id="wing-l">{p(T["wing-l"], tx, ty)}</g>'
            f'<g id="wing-r">{p(T["wing-r"], tx, ty)}</g>'
            '</g>')


# ---- logo.svg: full lockup, uniform margin = 2% of artwork width
w_all = INK_ALL[2] - INK_ALL[0]
m_logo = round(0.02 * w_all)
lx, ly, lw, lh = vb(INK_ALL, m_logo)
logo = (svg_open(lw, lh, 'Boston Angel Fund') +
        f'<g id="baf">{p(T["baf"], lx, ly)}</g>' + wings(lx, ly) +
        f'<g id="tagline">{p(T["tagline"], lx, ly)}</g></svg>\n')
open(os.path.join(a.outdir, 'logo.svg'), 'w').write(logo)

# ---- mark.svg: BAF + wings, tight (2% of mark height)
h_top = INK_TOP[3] - INK_TOP[1]
m_mark = round(0.02 * h_top)
mx, my, mw, mh = vb(INK_TOP, m_mark)
mark = (svg_open(mw, mh, 'Boston Angel Fund') +
        f'<g id="baf">{p(T["baf"], mx, my)}</g>' + wings(mx, my) + '</svg>\n')
open(os.path.join(a.outdir, 'mark.svg'), 'w').write(mark)

# ---- favicon.svg: 100x100 sunflower tile, BAF in blue filling width minus margin
S = 100.0
bw = INK_BAF[2] - INK_BAF[0]; bh = INK_BAF[3] - INK_BAF[1]
k = S * (1 - 2 * a.fav_margin) / bw
ox = (S - bw * k) / 2; oy = (S - bh * k) / 2
tx = INK_BAF[0] - ox / k; ty = INK_BAF[1] - oy / k
stroke = ''
if a.fav_stroke > 0:
    stroke = (f' stroke="#3255A4" stroke-width="{fmt(a.fav_stroke)}" '
              f'stroke-linejoin="round"')
fav = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
       '<rect width="100" height="100" fill="#FFB511"/>'
       f'<path fill="#3255A4"{stroke} d="{curves_to_d(T["baf"], tx, ty, k)}"/></svg>\n')
open(os.path.join(a.outdir, 'favicon.svg'), 'w').write(fav)

geo = {'logo_vb': [lx, ly, lw, lh], 'logo_margin': m_logo,
       'mark_vb': [mx, my, mw, mh], 'mark_margin': m_mark,
       'split_x_src': SPLIT_X, 'split_x_logo': SPLIT_X - lx, 'split_x_mark': SPLIT_X - mx,
       'fav_k': k, 'sizes': {f: os.path.getsize(os.path.join(a.outdir, f))
                             for f in ('logo.svg', 'mark.svg', 'favicon.svg')}}
print(json.dumps(geo))
