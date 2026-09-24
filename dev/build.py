#!/usr/bin/env python3
"""Build a fully self-contained index.html for The Bangalore Cafe landing page.

- Cover-crops + resizes + recompresses each generated image
- Base64-embeds images and fonts as data URIs (works offline / in sandboxed previews)
"""
import base64
import io
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# placeholder -> (source file, target (w, h), jpeg quality)
IMAGES = {
    'FEAST':       ('assets/raw/feast.jpg',       (1080, 1350), 78),
    'INTERIOR':    ('assets/raw/interior.jpg',    (1000, 1250), 75),
    'SOUTH':       ('assets/raw/southindian.jpg', (800, 800),   75),
    'OUTHOUSE':    ('assets/raw/outhouse.jpg',    (840, 1120),  75),
    'DESSERT':     ('assets/raw/dessert.jpg',     (840, 1120),  75),
    'DRIVEIN':     ('assets/raw/drivein.jpg',     (1100, 825),  75),
    'BANQUET':     ('assets/raw/banquet.jpg',     (1100, 825),  75),
    'NORTH':       ('assets/raw/northindian.jpg', (800, 800),   75),
    'CONTINENTAL': ('assets/raw/continental.jpg', (800, 800),   75),
}

FONTS = {
    'FRAUNCES':    'assets/fonts/fraunces.woff2',
    'FRAUNCES_IT': 'assets/fonts/fraunces-italic.woff2',
    'MANROPE':     'assets/fonts/manrope.woff2',
}


def cover_crop(im, tw, th):
    """Resize + center-crop so the image exactly covers (tw, th)."""
    sw, sh = im.size
    scale = max(tw / sw, th / sh)
    nw, nh = max(tw, round(sw * scale)), max(th, round(sh * scale))
    im = im.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - tw) // 2, (nh - th) // 2
    return im.crop((left, top, left + tw, top + th))


def image_data_uri(rel, size, quality):
    with open(os.path.join(ROOT, rel), 'rb') as f:
        im = Image.open(f).convert('RGB')
    im = cover_crop(im, *size)
    buf = io.BytesIO()
    im.save(buf, 'JPEG', quality=quality, optimize=True, progressive=True)
    data = buf.getvalue()
    print(f'  {rel:<32} -> {size[0]}x{size[1]}  {len(data)/1024:7.1f} KB')
    return 'data:image/jpeg;base64,' + base64.b64encode(data).decode('ascii')


def font_data_uri(rel):
    with open(os.path.join(ROOT, rel), 'rb') as f:
        data = f.read()
    print(f'  {rel:<32} {len(data)/1024:7.1f} KB')
    return 'data:font/woff2;base64,' + base64.b64encode(data).decode('ascii')


def main():
    src = os.path.join(ROOT, 'dev', 'page.html')
    with open(src, encoding='utf-8') as f:
        html = f.read()

    print('Embedding images:')
    for key, (rel, size, q) in IMAGES.items():
        ph = f'__IMG_{key}__'
        if ph not in html:
            sys.exit(f'ERROR: placeholder {ph} missing from page.html')
        html = html.replace(ph, image_data_uri(rel, size, q))

    print('Embedding fonts:')
    for key, rel in FONTS.items():
        ph = f'__FONT_{key}__'
        if ph not in html:
            sys.exit(f'ERROR: placeholder {ph} missing from page.html')
        html = html.replace(ph, font_data_uri(rel))

    for leftover in ('__IMG_', '__FONT_'):
        if leftover in html:
            sys.exit(f'ERROR: unresolved placeholder {leftover}*')

    out = os.path.join(ROOT, 'index.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'\nWrote {out}  ({os.path.getsize(out)/1024/1024:.2f} MB)')


if __name__ == '__main__':
    main()
