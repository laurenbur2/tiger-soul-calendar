# Cover photo generator

Locked template for Tiger Soul reel / post covers. Approved 2026-08-18.

**Spec:** 1080x1920 · logo lockup at top (225px) · full-bleed photo zoomed so the
subject sits upper-middle · LIGHT GREEN fade (forest #0f1c14, transparent through
the middle, density only under the type) · headline in curly quotes near the
bottom in Cormorant Garamond cream · gold Jost subline under it.

Text stays above y=1620 so it survives Instagram's 4:5 grid crop.

## Use

    cp <your-photo>.jpg bg.jpg
    python3 make-cover.py

Edit `QUOTE` and `SUB` at the top of the script. Tune `background-size` /
`background-position` in the render list to place the subject: 266% is exact
cover, larger zooms in; a Y near 100% lifts the subject up the frame.

Requires headless Google Chrome (macOS path is hardcoded) and `sips`.
