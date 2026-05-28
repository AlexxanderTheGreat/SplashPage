# 🚀 Migration — Overwrite + Backup

## TL;DR

1. **Rename your existing files** to `_OLD` (keeps them as a backup)
2. **Drop in the new files** from this bundle
3. **Replace `f1.py`** with the new one
4. **Run & push**

Old design lives at `/old`. New design lives at `/`.

---

## Step 1 — Backup your current files (rename them)

From inside your `SplashPage/` repo:

```bash
# Commit current state first (always smart)
git add -A && git commit -m "snapshot before v2 redesign"

# Rename old files to _OLD versions (kept as living backups)
mv templates/Splash_Page.html templates/Splash_Page_OLD.html
mv static/css/style.css         static/css/style_OLD.css
mv f1.py                        f1_OLD.py
```

## Step 2 — Drop in the new files

From this bundle (`splashpage_v2/`):

```bash
cp /path/to/splashpage_v2/templates/Splash_Page.html templates/
cp /path/to/splashpage_v2/static/css/style.css       static/css/
cp /path/to/splashpage_v2/f1.py                       f1.py

mkdir -p static/fonts
cp /path/to/splashpage_v2/static/fonts/Exo2-VariableFont_wght.ttf        static/fonts/
cp /path/to/splashpage_v2/static/fonts/Exo2-Italic-VariableFont_wght.ttf static/fonts/
```

## Step 3 — Run locally and check

```bash
source .venv/bin/activate
python f1.py
```

- **`http://localhost:5000`** → new redesign
- **`http://localhost:5000/old`** → your original splash page (still works!)

## Step 4 — Push to Render

```bash
git add -A
git commit -m "v2 redesign live"
git push
```

Render auto-redeploys. Your custom domain redirect still works.

---

## Final file layout in your repo

```
SplashPage/
├── f1.py                              ← NEW (renders new design at /, old at /old)
├── f1_OLD.py                          ← your backup
├── templates/
│   ├── Splash_Page.html               ← NEW redesign
│   ├── Splash_Page_OLD.html           ← your backup (still accessible at /old)
│   └── Tents.html                     ← untouched
└── static/
    ├── css/
    │   ├── style.css                  ← NEW stylesheet
    │   └── style_OLD.css              ← your backup
    ├── fonts/                         ← NEW
    │   ├── Exo2-VariableFont_wght.ttf
    │   └── Exo2-Italic-VariableFont_wght.ttf
    └── images/                        ← untouched (new design references same paths)
```

---

## Removing the `_OLD` backups later

When you're confident you don't need them anymore:

```bash
rm templates/Splash_Page_OLD.html
rm static/css/style_OLD.css
rm f1_OLD.py
```

Then in `f1.py`, delete the `@app.route("/old")` block and the `OLD_TEXTS` dictionary above it.

---

## Rollback (if v2 breaks something)

The fastest way back to your original:

```bash
git reset --hard HEAD~1   # undo the v2 commit
```

Or manually:
```bash
mv templates/Splash_Page.html       templates/Splash_Page_NEW.html
mv templates/Splash_Page_OLD.html   templates/Splash_Page.html
mv static/css/style.css             static/css/style_NEW.css
mv static/css/style_OLD.css         static/css/style.css
mv f1.py                            f1_NEW.py
mv f1_OLD.py                        f1.py
```

---

## What changed

| Area | Old | New |
|------|-----|-----|
| **Translation** | Server-side `texts` dict in `f1.py` | Client-side via `data-en`/`data-es` attributes + tiny JS. Add new copy directly to HTML — no Flask changes. |
| **CSS** | Inline styles + minimal `style.css` | Full external `style.css` with brand tokens, gradient backgrounds, responsive breakpoints |
| **Bootstrap** | Required for cards/carousel/dropdowns | **NOT required** — pure CSS Grid + Flex. You can remove the Bootstrap `<link>` and `<script>` tags from any other templates if nothing else uses them. |
| **Fonts** | Didot fallback (browser default since Didot is licensed) | Real **Exo 2** (loaded from `static/fonts/`) + **GFS Didot** from Google Fonts |
| **Sticky nav** | None | Translucent at top, frosted-white when scrolled, logo swaps |
| **Mobile nav** | Just Spanish toggle | Hamburger → slide-out side panel with full nav + contact info |
| **Inventory** | One long scroll, all categories shown | Tabbed (Tents / Jump Houses / Chairs & Tables / Toilets & Heaters / Extras) |
| **Phone numbers** | Some plain text | Every phone is a clickable `tel:` link |
| **Email** | `letscelebrate@…` | `contact@…` |
| **Quote form** | None | Formspree-backed contact form (ID `mvzyvygz`) — submissions email to `contact@moraleseventrentals.com` |

---

## Future maintenance tips

- **Adding a new product card**: open `Splash_Page.html`, find the `<div class="inv-grid">` for the right category, copy an existing `<div class="inv-card">…</div>` block. Add `data-en` / `data-es` attributes for any new text.
- **Updating prices**: search the template for the price (e.g. `$120/Day`), replace in both `data-en` and the visible text.
- **New language**: add `data-fr`, `data-pt`, etc. attributes next to `data-en`/`data-es`, then extend the toggle JS at the bottom of the template.
- **Form submissions**: log in at https://formspree.io with `contact@moraleseventrentals.com` — all quote requests show up there + in your email.
