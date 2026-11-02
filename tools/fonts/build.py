import os, shutil
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools import subset

WORK = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(WORK, 'src') + os.sep                          # OFL source TTFs
OUT = os.path.join(WORK, '..', '..', 'site', 'fonts') + os.sep    # shipped WOFF2 files

UNICODES = (
    list(range(0x0000, 0x0180))      # Basic Latin, Latin-1 Supplement (incl. U+00A0), Latin Extended-A
    + [0x02C6, 0x02DA, 0x02DC]       # spacing circumflex, ring, tilde
    + list(range(0x0300, 0x0329))    # combining diacritics, for NFD-decomposed accented text
    + list(range(0x2000, 0x2070))    # General Punctuation
    + [0x20AC, 0x2122, 0x2212]       # euro, trademark, minus
)

# 1) League Gothic: pin the wdth axis at its default (100) -> static font, drops fvar/gvar/HVAR/STAT
vf = TTFont(SRC + 'LeagueGothic-wdth.ttf')
static = instancer.instantiateVariableFont(vf, {'wdth': 100})
# A static font needs no STAT, no variations PS-name prefix (ID 25), and no axis/instance names (IDs 256+)
if 'STAT' in static:
    del static['STAT']
static['name'].names = [r for r in static['name'].names if r.nameID < 25 or (26 <= r.nameID < 256)]
static_path = os.path.join(WORK, 'LeagueGothic-Regular-static.ttf')
static.save(static_path)

def make_options():
    o = subset.Options()
    o.flavor = 'woff2'
    o.layout_features = o.layout_features + ['case', 'tnum', 'pnum']   # defaults already include kern, liga, ccmp, locl, mark, mkmk, frac, sups
    o.name_IDs = ['*']            # keep copyright, trademark, designer, license (IDs 0-14) in the binary
    o.name_languages = ['*']
    o.hinting = True              # keep ttfautohint instructions in Atkinson
    o.notdef_outline = True
    o.glyph_names = False
    o.layout_closure = True
    return o

jobs = [
    (static_path, 'league-gothic.woff2'),
    (SRC + 'Atkinson-Regular.ttf', 'atkinson-hyperlegible-regular.woff2'),
    (SRC + 'Atkinson-Bold.ttf', 'atkinson-hyperlegible-bold.woff2'),
]
for src, dst in jobs:
    opts = make_options()
    font = subset.load_font(src, opts)
    s = subset.Subsetter(opts)
    s.populate(unicodes=UNICODES)
    s.subset(font)
    subset.save_font(font, OUT + dst, opts)
    # lossless (unsubsetted) WOFF2 for size comparison only
    f2 = TTFont(src); f2.flavor = 'woff2'; f2.save(os.path.join(WORK, 'full-' + dst))

shutil.copyfile(SRC + 'LeagueGothic-OFL.txt', OUT + 'LeagueGothic-OFL.txt')
shutil.copyfile(SRC + 'Atkinson-OFL.txt', OUT + 'AtkinsonHyperlegible-OFL.txt')
print('done')
