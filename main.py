"""Cutest-picture-01 entry: copy the picture beside this file to the output.

The picture is entry.png (JPEG bytes, 1024x1024, under 1 MiB). The program
writes the exact same bytes on every run: a plain copy, nothing drawn.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SRC = HERE / "entry.png"
if not SRC.is_file():
    raise FileNotFoundError(f"missing picture beside this file: {SRC}")

# The gate takes a whole PNG or JPEG: refuse to ship anything else, loudly,
# instead of silently copying a corrupt file and scoring 0.
MAGIC = SRC.read_bytes()[:4]
if MAGIC[:3] != b"\xff\xd8\xff" and MAGIC != b"\x89PNG":
    raise ValueError(f"{SRC} is neither a JPEG nor a PNG (first bytes {MAGIC!r})")

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT / "entry.png")
