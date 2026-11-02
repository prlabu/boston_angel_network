"""Render an SVG to PNG with headless Chrome.

Usage: python render.py SVG OUT.png W H [--color #000] [--bg #fff] [--pad 0]
The SVG is inlined into a zero-margin HTML page, sized W x H minus padding
(pad is a fraction of each side), centred.
"""
import argparse, os, subprocess, tempfile, shutil

ap = argparse.ArgumentParser()
ap.add_argument('svg'); ap.add_argument('out')
ap.add_argument('w', type=int); ap.add_argument('h', type=int)
ap.add_argument('--color', default='#000')
ap.add_argument('--bg', default='#fff')
ap.add_argument('--pad', type=float, default=0.0)
a = ap.parse_args()

svg = open(a.svg).read()
pw = a.w * (1 - 2 * a.pad); ph = a.h * (1 - 2 * a.pad)
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;padding:0;background:{a.bg};width:{a.w}px;height:{a.h}px;overflow:hidden}}
.wrap{{width:{a.w}px;height:{a.h}px;display:flex;align-items:center;justify-content:center;color:{a.color}}}
.wrap svg{{display:block;width:{pw}px;height:{ph}px}}
</style></head><body><div class="wrap">{svg}</div></body></html>'''
d = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(__file__)))
hp = os.path.join(d, 'page.html')
open(hp, 'w').write(html)
chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                '--force-device-scale-factor=1', f'--user-data-dir={d}/prof',
                f'--window-size={a.w},{a.h}', f'--screenshot={os.path.abspath(a.out)}',
                'file://' + hp], check=True, capture_output=True, timeout=120)
shutil.rmtree(d, ignore_errors=True)
from PIL import Image
im = Image.open(a.out)
print(a.out, im.size)
