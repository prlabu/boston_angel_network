"""IoU of rendered logo vs source, plus comparison images.

Usage: python compare.py SRC RENDER.png GEO.json OUT_COMPARE.png [--zoomdir DIR]
"""
import argparse, json, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('render'); ap.add_argument('geo'); ap.add_argument('out')
ap.add_argument('--zoomdir')
ap.add_argument('--src-thr', type=float, default=122)
ap.add_argument('--ren-thr', type=float, default=127.5)
a = ap.parse_args()

geo = json.load(open(a.geo))
lx, ly, lw, lh = [int(round(v)) for v in geo['logo_vb']]
src = np.asarray(Image.open(a.src).convert('L')).astype(np.float32)
crop = src[ly:ly + lh, lx:lx + lw]
ren = np.asarray(Image.open(a.render).convert('L')).astype(np.float32)
assert ren.shape == crop.shape, (ren.shape, crop.shape)
S = crop < a.src_thr
R = ren < a.ren_thr

H, W = S.shape
yy, xx = np.mgrid[0:H, 0:W]
Y = yy + ly; X = xx + lx
regions = {'baf': (Y < 1150) & (X < 1631), 'wings': (Y < 1150) & (X >= 1631), 'tagline': Y >= 1150}


def iou(m=None):
    s, r = (S, R) if m is None else (S & m, R & m)
    return float((s & r).sum() / (s | r).sum())

res = {'overall': iou()}
for k, m in regions.items():
    res[k] = iou(m)
res['src_px'] = int(S.sum()); res['ren_px'] = int(R.sum())
res['missed_px'] = int((S & ~R).sum()); res['extra_px'] = int((R & ~S).sum())
print(json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in res.items()}))

# diff overlay: black = both, red = source only (render missed), blue = render only (extra)
diff = np.full((H, W, 3), 255, np.uint8)
diff[S & R] = (40, 40, 40)
diff[S & ~R] = (230, 30, 30)
diff[R & ~S] = (20, 110, 255)

src_rgb = np.stack([crop.astype(np.uint8)] * 3, -1)
ren_rgb = np.stack([ren.astype(np.uint8)] * 3, -1)
pw = 1600
ph = int(round(H * pw / W))
def sm(arr):
    return Image.fromarray(arr).resize((pw, ph), Image.LANCZOS)

gap = 24; head = 56
try:
    font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 30)
except Exception:
    font = ImageFont.load_default()
details = [('wing loop + split', (2420, 800, 2640, 1110)), ('F serif', (1380, 425, 1570, 640)),
           ('A apex', (860, 425, 1020, 560)), ('right wing tip', (3150, 420, 3320, 600)),
           ('n hairline', (1060, 1380, 1200, 1560))]
dscale = 3
dimgs = []
for name, (x0, y0, x1, y1) in details:
    sl = (slice(y0 - ly, y1 - ly), slice(x0 - lx, x1 - lx))
    tri = np.concatenate([src_rgb[sl], np.full((y1 - y0, 4, 3), 160, np.uint8), ren_rgb[sl],
                          np.full((y1 - y0, 4, 3), 160, np.uint8), diff[sl]], 1)
    im = Image.fromarray(tri)
    dimgs.append((name, im.resize((im.width * dscale, im.height * dscale), Image.NEAREST)))
total_w = pw * 2 + gap * 3
# lay detail strips in rows that fit total_w
rows, cur, cw = [], [], gap
for nm, im in dimgs:
    if cur and cw + im.width + gap > total_w:
        rows.append(cur); cur, cw = [], gap
    cur.append((nm, im)); cw += im.width + gap
rows.append(cur)
det_h = sum(head + max(im.height for _, im in r) + gap for r in rows)
dh = int(round(H * (total_w - 2 * gap) / W))
canvas = Image.new('RGB', (total_w, head + ph + gap + head + dh + gap + det_h), 'white')
dr = ImageDraw.Draw(canvas)
canvas.paste(sm(src_rgb), (gap, head)); canvas.paste(sm(ren_rgb), (pw + 2 * gap, head))
dr.text((gap, 12), 'Source (chuffed-hero.jpg, cropped to logo viewBox)', fill='black', font=font)
dr.text((pw + 2 * gap, 12), 'Render of logo.svg (Chrome, 1 unit = 1 source px)', fill='black', font=font)
y2 = head + ph + gap
txt = ('Diff overlay: dark = both, red = source only, blue = render only.   IoU overall %.4f | '
       'baf %.4f | wings %.4f | tagline %.4f' % (res['overall'], res['baf'], res['wings'], res['tagline']))
dr.text((gap, y2 + 12), txt, fill='black', font=font)
canvas.paste(Image.fromarray(diff).resize((total_w - 2 * gap, dh), Image.LANCZOS), (gap, y2 + head))
y = y2 + head + dh + gap
for r in rows:
    x = gap
    for nm, im in r:
        dr.text((x, y + 12), nm + '  (source | render | diff, 3x)', fill='black', font=font)
        canvas.paste(im, (x, y + head)); x += im.width + gap
    y += head + max(im.height for _, im in r) + gap
os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
canvas.save(a.out, optimize=True)
print('wrote', a.out, canvas.size)

if a.zoomdir:
    os.makedirs(a.zoomdir, exist_ok=True)
    # name: (x0,y0,x1,y1) in source coords
    zooms = {'loop': (2380, 760, 2780, 1120), 'B': (180, 420, 660, 1120),
             'A_F': (600, 420, 1570, 1120), 'wingtip_l': (1690, 420, 2150, 800),
             'wingtip_r': (2900, 420, 3320, 1000), 'boston': (180, 1180, 1320, 1600),
             'angel': (1300, 1180, 2250, 1860), 'fund': (2360, 1180, 3330, 1600)}
    for n, (x0, y0, x1, y1) in zooms.items():
        sl = (slice(y0 - ly, y1 - ly), slice(x0 - lx, x1 - lx))
        a1 = src_rgb[sl]; a2 = ren_rgb[sl]; a3 = diff[sl]
        strip = np.concatenate([a1, np.full((a1.shape[0], 8, 3), 255, np.uint8), a2,
                                np.full((a1.shape[0], 8, 3), 255, np.uint8), a3], 1)
        Image.fromarray(strip).save(os.path.join(a.zoomdir, f'z_{n}.png'))
json.dump(res, open(os.path.splitext(a.out)[0] + '_iou.json', 'w'))
