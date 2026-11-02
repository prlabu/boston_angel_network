#!/bin/bash
# Re-trace the Boston Angel Fund logo into site/assets/ and check it against the source.
# Usage (from the repo root):
#   python3 -m venv tools/logo/.venv && tools/logo/.venv/bin/pip install potracer pillow numpy scikit-image
#   bash tools/logo/final.sh path/to/logo-source.jpg
# The source used on 2026-11-01 was the Chuffed campaign image (kept outside the repo).
set -e
SRC=${1:?usage: final.sh path/to/logo-source.jpg}
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/../.." && pwd)
PY=$HERE/.venv/bin/python
A=$ROOT/site/assets
F=$(mktemp -d)
mkdir -p "$A"
# 1. trace (params chosen from a sweep: blur 1.2, 2x bicubic, thr 122, turd 20 src px^2, alphamax 1.0, opttol 1.2)
"$PY" -I "$HERE/trace.py" "$SRC" "$F/trace.json" --blur 1.2 --scale 2 --opttol 1.2 --alpha 1.0 --turd 20 --thr 122 --split 2480 --overlap 3 > "$F/trace.log"
# 2. SVGs straight into site/assets
"$PY" -I "$HERE/build.py" "$F/trace.json" "$A" --fav-stroke 2 --fav-margin 0.06 | tail -1 > "$F/geo.json"
read LW LH < <(python3 -c "import json;g=json.load(open('$F/geo.json'));print(int(g['logo_vb'][2]),int(g['logo_vb'][3]))")
# 3. verify logo.svg against the source (IoU + side-by-side image)
python3 -I "$HERE/render.py" "$A/logo.svg" "$F/logo_render.png" $LW $LH > /dev/null
python3 -I "$HERE/compare.py" "$SRC" "$F/logo_render.png" "$F/geo.json" "$F/logo-compare.png" | head -1
echo "comparison image: $F/logo-compare.png"
# 4. favicons
python3 -I "$HERE/render.py" "$A/favicon.svg" "$F/fav_512.png" 512 512 > /dev/null
python3 -I "$HERE/render.py" "$A/mark.svg" "$F/apple_1080.png" 1080 1080 --color '#3255A4' --bg '#FBFAF6' --pad 0.14 > /dev/null
python3 -I - <<PYEOF
from PIL import Image
f = Image.open('$F/fav_512.png').convert('RGB')
f.resize((32, 32), Image.BOX).save('$A/favicon-32.png', optimize=True)
f.resize((16, 16), Image.BOX).save('$A/favicon-16.png', optimize=True)
Image.open('$F/apple_1080.png').convert('RGB').resize((180, 180), Image.BOX).save('$A/apple-touch-icon.png', optimize=True)
PYEOF
echo "Re-embed provenance in the PNGs afterwards (see README)."
