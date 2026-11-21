#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261120.

The program writes one image that sums up the world news of
Friday 20 November 2026 to /output/entry.png.

The image itself (entry.png, in this repository) was drawn by
draw_entry.py from stories cross-checked across several news
sources for that day. Drawing happens before submission because
the grading sandbox has no network and no font guarantees, so the
most reliable deterministic program is one that copies the
finished image byte for byte.

Running the program twice therefore always writes the same bytes.
The output directory is /output in the grader; for local runs it
can be overridden with the MAKEFUN_OUTPUT_DIR environment variable.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"


def source_image() -> Path:
    """Return the path of the image shipped with this repository."""
    here = Path(__file__).resolve().parent
    candidate = here / IMAGE_NAME
    if candidate.is_file():
        return candidate
    # Fallback for graders that mount the repository at /bot.
    bot_candidate = Path("/bot") / IMAGE_NAME
    if bot_candidate.is_file():
        return bot_candidate
    raise FileNotFoundError(f"{IMAGE_NAME} not found next to main.py")


def output_path() -> Path:
    """Return where the entry image must be written."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / IMAGE_NAME


def main() -> int:
    src = source_image()
    dst = output_path()
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    if dst.read_bytes() != src.read_bytes():
        raise RuntimeError("copied image does not match the source bytes")
    size = dst.stat().st_size
    if size > 1048576:
        raise RuntimeError("entry image exceeds the 1 MiB limit")
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
