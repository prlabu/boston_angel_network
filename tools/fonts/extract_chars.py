import sys, html, unicodedata, json
from html.parser import HTMLParser
src = open(sys.argv[1], encoding='utf-8').read()
class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0; self.text=[]; self.attrs=[]; self.stack=[]
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style','template','noscript'): self.skip += 1
        for k,v in attrs:
            if k in ('alt','title','placeholder','aria-label','value') and v: self.attrs.append(v)
    def handle_endtag(self, tag):
        if tag in ('script','style','template','noscript'): self.skip -= 1
    def handle_data(self, d):
        if not self.skip: self.text.append(d)
p = P(); p.feed(src)
vis = ''.join(p.text)
att = ''.join(p.attrs)
# CSS content strings
import re
css = ''.join(re.findall(r'<style[^>]*>(.*?)</style>', src, re.S))
content = ''.join(re.findall(r'content:\s*"([^"]*)"', css))
chars = set(c for c in vis if not c.isspace()) | set(c for c in att if not c.isspace()) | set(content)
chars |= {' ', ' '} & set(vis + att) | {' '}
out = {'visible': sorted(set(vis) - set('\n\r\t')), 'attrs_extra': sorted(set(att)-set(vis)), 'css_content': sorted(set(content))}
for k,v in out.items():
    print(k, len(v))
    print('  ', ''.join(c if c.isprintable() and not c.isspace() else f'[U+{ord(c):04X}]' for c in v))
nonascii = sorted(c for c in set(vis+att+content) if ord(c) > 0x7e)
for c in nonascii:
    print(f'U+{ord(c):04X} {unicodedata.name(c, "?")} {c!r}')
json.dump(sorted(set(vis+att+content) - set('\n\r\t')), open('used_chars.json','w'))
