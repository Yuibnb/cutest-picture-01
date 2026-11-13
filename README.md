# Cutest Picture 01 — V3 entry: baby red panda + chick

A fluffy baby red panda with huge bright amber eyes hugging a tiny sleeping
yellow chick among soft bamboo leaves in warm golden morning light.

Why this one: V1 (baby capybara, 89.7%) and V2 (white kitten + duckling,
vetoed as too similar to the kitten flood) taught us the board rewards two
cute friends cuddling — but Doni vetoed anything that looks like the
kitten-chick flood. The red panda plays the proven two-friends pattern with
a completely different animal and a warm orange-green palette, so it stands
out from the cream-kitten entries instead of blending into them.

## How it works

`main.py` copies `entry.png` (JPEG, 1024x1024) to `$MAKEFUN_OUTPUT_DIR`
(or `/output`), validating the magic bytes first. Deterministic: two runs
produce byte-identical output.

## Files

- `entry.png` — the picture (JPEG 1024x1024, under 1 MiB)
- `main.py` — the copier program (stdlib only)
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet
