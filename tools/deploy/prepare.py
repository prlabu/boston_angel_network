"""Adapt a copy of site/ to the address GitHub Pages will serve it from.

Usage: python3 tools/deploy/prepare.py OUT_DIR BASE_URL BASE_PATH
  OUT_DIR    a copy of site/ (never site/ itself)
  BASE_URL   e.g. https://saifiz2.github.io/boston_angel_fund  (no trailing slash)
  BASE_PATH  e.g. /boston_angel_fund, or empty for a custom domain at the root

What it changes, and why:
- index.html: the share image becomes an absolute URL and og:url, a canonical
  link and the JSON-LD url are added. Facebook, LinkedIn and X ignore relative
  image URLs, so link previews would otherwise show no image.
- 404.html: root paths (/css/site.css) gain BASE_PATH, because a project site
  lives under /boston_angel_fund/ and the 404 page is served at any depth.
- _headers is dropped: GitHub Pages ignores it (index.html carries its CSP in a
  <meta> tag).
"""
import pathlib
import re
import sys


def main():
    out, base_url, base_path = sys.argv[1], sys.argv[2].rstrip('/'), sys.argv[3].rstrip('/')
    out = pathlib.Path(out)
    if out.resolve().name == 'site':
        sys.exit('refusing to modify site/ itself; pass a copy')

    index = out / 'index.html'
    html = index.read_text(encoding='utf-8')
    old = '<meta property="og:image" content="assets/og-image.png">'
    if old in html:
        html = html.replace(old, (
            f'<meta property="og:image" content="{base_url}/assets/og-image.png">\n'
            f'<meta property="og:url" content="{base_url}/">\n'
            f'<link rel="canonical" href="{base_url}/">'
        ))
        html = html.replace('"@type": "NGO",', f'"@type": "NGO",\n  "url": "{base_url}/",', 1)
    index.write_text(html, encoding='utf-8')

    notfound = out / '404.html'
    page = notfound.read_text(encoding='utf-8')
    page = re.sub(r'(href|src)="/(?!/)', lambda m: f'{m.group(1)}="{base_path}/', page)
    notfound.write_text(page, encoding='utf-8')

    headers = out / '_headers'
    if headers.exists():
        headers.unlink()

    print(f'prepared {out} for {base_url}/ (path "{base_path or "/"}")')


if __name__ == '__main__':
    main()
