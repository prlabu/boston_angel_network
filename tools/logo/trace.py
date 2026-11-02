"""Trace the BAF logo raster into grouped SVG paths.

Usage: python trace.py SRC OUTJSON [--thr 122] [--scale 2] [--blur 0] [--turd 2]
       [--alpha 1.0] [--opttol 0.2] [--noopt]
Writes a JSON with path strings per group in SOURCE pixel coordinates
(absolute, float), so the SVG writer can choose the viewBox later.
"""
import argparse, json, time
import numpy as np
from PIL import Image, ImageFilter
import potrace

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('out')
ap.add_argument('--thr', type=float, default=122)
ap.add_argument('--scale', type=int, default=1)
ap.add_argument('--blur', type=float, default=0)
ap.add_argument('--turd', type=int, default=2)
ap.add_argument('--alpha', type=float, default=1.0)
ap.add_argument('--opttol', type=float, default=0.2)
ap.add_argument('--noopt', action='store_true')
ap.add_argument('--split', type=float, default=2480)
ap.add_argument('--overlap', type=float, default=3)
a = ap.parse_args()

img = Image.open(a.src).convert('L')
if a.blur > 0:
    img = img.filter(ImageFilter.GaussianBlur(a.blur))
s = a.scale
if s != 1:
    img = img.resize((img.width * s, img.height * s), Image.BICUBIC)
g = np.asarray(img).astype(np.float32)
ink = g < a.thr
H, W = ink.shape
yy, xx = np.mgrid[0:H, 0:W]
xs = (xx + 0.5) / s  # pixel centre in source coords
ys = (yy + 0.5) / s

Y_TAG, X_WING = 1150, 1631
regions = {
    'baf': (ys < Y_TAG) & (xs < X_WING),
    'wing-l': (ys < Y_TAG) & (xs >= X_WING) & (xs < a.split + a.overlap),
    'wing-r': (ys < Y_TAG) & (xs >= a.split - a.overlap),
    'tagline': (ys >= Y_TAG),
}

def trace(mask):
    # crop to bbox for speed
    r = np.nonzero(mask.any(1))[0]; c = np.nonzero(mask.any(0))[0]
    r0, r1, c0, c1 = max(r[0] - 2, 0), r[-1] + 3, max(c[0] - 2, 0), c[-1] + 3
    sub = mask[r0:r1, c0:c1]
    bm = potrace.Bitmap(~sub)  # potracer inverts; pass background=True
    plist = bm.trace(turdsize=a.turd * s * s, alphamax=a.alpha,
                     opticurve=not a.noopt, opttolerance=a.opttol)
    out = []
    for curve in plist:
        sp = curve.start_point
        segs = []
        for seg in curve.segments:
            if seg.is_corner:
                segs.append(['L', [seg.c.x, seg.c.y], [seg.end_point.x, seg.end_point.y]])
            else:
                segs.append(['C', [seg.c1.x, seg.c1.y], [seg.c2.x, seg.c2.y],
                             [seg.end_point.x, seg.end_point.y]])
        out.append({'start': [sp.x, sp.y], 'segs': segs})
    # convert to source coords
    def T(p):
        return [(p[0] + c0) / s, (p[1] + r0) / s]
    for cv in out:
        cv['start'] = T(cv['start'])
        cv['segs'] = [[sg[0]] + [T(p) for p in sg[1:]] for sg in cv['segs']]
    return out

res = {'params': vars(a)}
for name, reg in regions.items():
    t = time.time()
    res[name] = trace(ink & reg)
    print(name, len(res[name]), 'curves', sum(len(c['segs']) for c in res[name]), 'segs',
          f'{time.time()-t:.1f}s', flush=True)
json.dump(res, open(a.out, 'w'))
