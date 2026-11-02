import json, os, unicodedata
from fontTools.ttLib import TTFont

WORK = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(WORK, 'src') + os.sep                          # OFL source TTFs
OUT = os.path.join(WORK, '..', '..', 'site', 'fonts') + os.sep    # shipped WOFF2 files
used = json.load(open(os.path.join(WORK, 'used_chars.json')))
extra = list('áéíóúñüçãõâêôàÁÉÍÓÚÑÇ¿¡')
# chars produced by text-transform:uppercase on League Gothic headings
upper_extra = sorted(set(''.join(c.upper() for c in used + extra)))
required = sorted(set(c for c in used + extra + upper_extra if c not in '\n\r\t'))
print('required chars (%d):' % len(required), ''.join(c if c != ' ' else '␠' for c in required))

pairs = {
    'league-gothic.woff2': ('LeagueGothic-wdth.ttf', 'League Gothic', 400),
    'atkinson-hyperlegible-regular.woff2': ('Atkinson-Regular.ttf', 'Atkinson Hyperlegible', 400),
    'atkinson-hyperlegible-bold.woff2': ('Atkinson-Bold.ttf', 'Atkinson Hyperlegible', 700),
}

def pair_kern(font, left, right):
    """Return x-advance adjustment for glyph pair from GPOS kern lookups (PairPos fmt 1/2, incl. Extension)."""
    gpos = font['GPOS'].table
    lookups = set()
    for fr in gpos.FeatureList.FeatureRecord:
        if fr.FeatureTag == 'kern':
            lookups.update(fr.Feature.LookupListIndex)
    total = 0
    for li in sorted(lookups):
        lk = gpos.LookupList.Lookup[li]
        for st in lk.SubTable:
            if lk.LookupType == 9: st = st.ExtSubTable
            if st.LookupType != 2 if hasattr(st, 'LookupType') else False: continue
            if left not in st.Coverage.glyphs: continue
            if st.Format == 1:
                ps = st.PairSet[st.Coverage.glyphs.index(left)]
                for pvr in ps.PairValueRecord:
                    if pvr.SecondGlyph == right:
                        v = pvr.Value1; total += getattr(v, 'XAdvance', 0) or 0
                        break
                else: continue
                break
            elif st.Format == 2:
                c1 = st.ClassDef1.classDefs.get(left, 0); c2 = st.ClassDef2.classDefs.get(right, 0)
                v = st.Class1Record[c1].Class2Record[c2].Value1
                adj = getattr(v, 'XAdvance', 0) or 0 if v else 0
                total += adj
                if adj: break
    return total

report = {}
for out, (src, fam, wt) in pairs.items():
    f = TTFont(OUT + out)
    o = TTFont(SRC + src)
    if 'fvar' in o:  # compare against the default instance
        from fontTools.varLib import instancer
        o = instancer.instantiateVariableFont(o, {'wdth': 100})
    name = f['name']
    cm = f.getBestCmap(); ocm = o.getBestCmap()
    missing = [c for c in required if ord(c) not in cm]
    print('\n=====', out, os.path.getsize(OUT + out), 'bytes; flavor', f.flavor)
    print(' family(1):', name.getDebugName(1), '| subfamily(2):', name.getDebugName(2), '| typo family(16):', name.getDebugName(16),
          '| full(4):', name.getDebugName(4), '| ps(6):', name.getDebugName(6))
    print(' family OK:', name.getDebugName(1) == fam, '| usWeightClass', f['OS/2'].usWeightClass, 'expected', wt,
          '| bold bit', bool(f['OS/2'].fsSelection & 0x20), '| fsType', f['OS/2'].fsType)
    print(' name 0:', name.getDebugName(0)); print(' name 7:', name.getDebugName(7)); print(' name 13:', name.getDebugName(13))
    print(' tables:', sorted(f.keys()))
    print(' variable tables left:', [t for t in ('fvar','gvar','HVAR','STAT','avar','MVAR') if t in f])
    print(' glyphs', len(f.getGlyphOrder()), 'of', len(o.getGlyphOrder()), '| cmap', len(cm), 'of', len(ocm))
    print(' GSUB features:', sorted(set(r.FeatureTag for r in f['GSUB'].table.FeatureList.FeatureRecord)))
    print(' GPOS features:', sorted(set(r.FeatureTag for r in f['GPOS'].table.FeatureList.FeatureRecord)))
    print(' MISSING required:', missing)
    # metrics + outline integrity vs original for every kept codepoint
    adv_diff = []; outline_diff = []
    for cp, g in cm.items():
        og = ocm.get(cp)
        if og is None: adv_diff.append((cp, 'not in source')); continue
        if f['hmtx'][g][0] != o['hmtx'][og][0]: adv_diff.append((cp, f['hmtx'][g][0], o['hmtx'][og][0]))
        a = f['glyf'][g]; b = o['glyf'][og]
        ca = a.getCoordinates(f['glyf'])[0] if a.numberOfContours else []
        cb = b.getCoordinates(o['glyf'])[0] if b.numberOfContours else []
        if list(ca) != list(cb): outline_diff.append(hex(cp))
    print(' advance mismatches:', adv_diff[:10], '| outline mismatches:', outline_diff[:10])
    # kerning spot check
    kp = ['AV', 'To', 'Ty', 'LT', 'Yo', 'P.', 'TA', 'Wa', 'AT', 'r,', 'F.', 'Vá', 'Tó']
    res = []
    for p in kp:
        l, r = p
        if ord(l) in cm and ord(r) in cm:
            res.append((p, pair_kern(f, cm[ord(l)], cm[ord(r)]), pair_kern(o, ocm[ord(l)], ocm[ord(r)])))
    print(' kern (pair, subset, original):', res)
    print(' kern preserved:', all(a == b for _, a, b in res), '| nonzero pairs:', sum(1 for _, a, _ in res if a))
    # ligature check
    gsub = f['GSUB'].table
    liga = []
    for fr in gsub.FeatureList.FeatureRecord:
        if fr.FeatureTag == 'liga':
            for li in fr.Feature.LookupListIndex:
                lk = gsub.LookupList.Lookup[li]
                for st in lk.SubTable:
                    if lk.LookupType == 7: st = st.ExtSubTable
                    if hasattr(st, 'ligatures'):
                        for first, ligs in st.ligatures.items():
                            for lg in ligs: liga.append(first + '+' + '+'.join(lg.Component) + '->' + lg.LigGlyph)
    print(' liga rules:', liga[:10])
    report[out] = missing
json.dump(report, open(os.path.join(WORK, 'missing.json'), 'w'))
