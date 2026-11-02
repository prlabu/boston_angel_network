# Web fonts

`src/` holds the OFL source fonts (League Gothic, Atkinson Hyperlegible). Neither declares a Reserved Font Name, so they are instanced and subsetted for the web.

```bash
python3 tools/fonts/build.py                                   # writes site/fonts/*.woff2 and the licences
python3 tools/fonts/extract_chars.py site/index.html           # writes used_chars.json (characters on the page)
python3 tools/fonts/verify.py                                  # checks every used character exists in each font
```

Needs `fontTools` and `brotli` (`pip install fonttools brotli`).
