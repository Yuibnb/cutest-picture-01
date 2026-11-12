# Cutest Picture — Bath-Time Baby Capybara

A baby capybara wrapped in a fluffy white towel after its bath, a tiny
yellow rubber duck perched on its head and soap bubbles on its nose.

Why this picture: most entries are generic kitten/puppy close-ups. A
capybara is round, chubby and unusual; the duck-on-head and bubbles-on-nose
give it two small touches of personality, and the giant face with huge
bright eyes still reads clearly at ~300 px.

## How it was chosen

Four candidates were generated (all the same bath-time capybara idea, four
different moments) and judged pairwise against the judge's five criteria in
order: cute at one glance, cute subject, charm, craft, reads small. The
towel portrait won: the biggest, brightest, most symmetric eyes; the
roundest chubby proportions; and the face fills the frame, so it reads best
when small. The runner-up was the head-tilt bathtub portrait.

## Files

- `entry.png` — the picture (JPEG bytes, 1024x1024, 149,879 bytes)
- `main.py` — copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
  (`/output` by default), byte-identical on every run
- `LICENSE` — MIT

## Verify

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
    # run twice, compare sha256 of out/entry.png
