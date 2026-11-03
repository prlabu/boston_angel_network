"""Header logo: trim BAN_OPTION-B.png to its artwork and key out the off-white background.
Inputs:  site/assets/BAN_OPTION-B.png (black ink on #F6F4F0)
Outputs: site/assets/ban-logo.png (ink colour, transparent background, 3x the 56px display height)
Dependencies: pillow
Example: uv run --with pillow python tools/logo/ban_header.py
"""
from PIL import Image

SRC, OUT, PAD, H = 'site/assets/BAN_OPTION-B.png', 'site/assets/ban-logo.png', 12, 168
im = Image.open(SRC).convert('RGB')
grey = im.convert('L')
x0, y0, x1, y1 = grey.point(lambda v: 255 if v < 128 else 0).getbbox()
box = (x0 - PAD, y0 - PAD, x1 + PAD, y1 + PAD)
bg, ink = grey.getpixel((5, 5)), im.getpixel(((x0 + x1) // 2, (y0 + y1) // 2))
ink_l = sum(ink) // 3
alpha = grey.crop(box).point(lambda v: max(0, min(255, round(255 * (bg - v) / (bg - ink_l)))))
out = Image.new('RGBA', alpha.size, ink + (0,))
out.putalpha(alpha)
out = out.resize((round(out.width * H / out.height), H), Image.LANCZOS)
out.save(OUT, optimize=True)
print(OUT, out.size, 'ink', ink)
