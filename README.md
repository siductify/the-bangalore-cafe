# The Bangalore Cafe — Landing Page

A minimal, interactive landing page for **The Bangalore Cafe**, a pure-vegetarian restaurant in Shanti Nagar, Bengaluru.

**Live site:** `https://<username>.github.io/<repo>/` *(updated automatically by GitHub Pages)*

---

## About

The Bangalore Cafe is a relaxed, all-vegetarian restaurant blending South and North Indian flavours with Western-style dishes — plus an Outhouse for chaat & chai, a Dessert House, old-school Drive-In dining, and a Banquet Hall.

- **Address:** 4, Kengal Hanumanthaiah Rd, Bheemanna Garden, Shanti Nagar, Bengaluru, Karnataka 560027
- **Phone:** 095359 64043
- **Hours:** Open daily, 12 pm – 1 am
- **Reservations:** [District](https://district.in/) · [Zomato](https://www.zomato.com/bangalore/the-bangalore-cafe-1-shanti-nagar-bangalore/book) · [EazyDiner](https://www.eazydiner.com/bengaluru/the-bangalore-cafe-shanti-nagar-central-bengaluru-662185) · [Swiggy](https://www.swiggy.com/)

## Features

- **Fully self-contained `index.html`** — all images, fonts, CSS and JS are inlined as data URIs, so it works offline, in sandboxed previews, and on any static host with zero build step.
- **Layered parallax hero** — scroll parallax on every image layer, a giant outlined ghost word, plus subtle mouse-follow depth on desktop.
- **Interactive bits** — review carousel (autoplay, dots, arrows, swipe), count-up rating stats, scroll-progress bar, scrollspy nav, reveal-on-scroll animations, cuisine marquee, fullscreen mobile menu.
- **Right-click & DevTools guard** — `contextmenu`, F12, Ctrl/Cmd+Shift+I/J/C and Ctrl+U are intercepted via event listeners with a friendly toast. *(Deters casual copying; not a true security boundary.)*
- **Design** — warm cream/espresso/terracotta palette, Fraunces + Manrope typography, film-grain overlay, reduced-motion support, responsive down to small phones.
- **SEO** — meta description, theme colour, and `Restaurant` structured data (JSON-LD).

## Repo structure

```
index.html          ← the site (deployed via GitHub Pages)
dev/page.html       ← source template (placeholders instead of base64 blobs)
dev/build.py        ← build script: embeds optimized images + fonts into index.html
assets/             ← original generated images and woff2 fonts
```

## Rebuilding after edits

Edit `dev/page.html` (it contains readable placeholders like `__IMG_FEAST__`), then:

```bash
pip install Pillow
python3 dev/build.py
```

## Credits

Images are AI-generated placeholders in an editorial style — swap in the cafe's real photos in `assets/raw/` and rebuild. Ratings shown (Zomato 4.3 / Swiggy 4.4 / Facebook 4.6) are from public listings.
