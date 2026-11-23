#!/usr/bin/env python3
"""One-Line Laugh entry: copy the funny line to the output file.

Reads the single funny line from entry.txt sitting next to this script
and writes it unchanged to $MAKEFUN_OUTPUT_DIR/entry.txt, where the
house judge reads it. Pure Python standard library only.
"""

import os
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8")

    # The contest gate: UTF-8 text of 1 to 200 characters, not only
    # whitespace. Refuse to write anything that would fail it.
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError("entry.txt must hold 1-200 non-whitespace characters")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
