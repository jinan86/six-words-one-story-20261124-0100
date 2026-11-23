#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.
Deterministic, stdlib only, no network, no clock, no randomness.
"""

import os
from pathlib import Path

STORY = "The lighthouse keeper lit nothing tonight."

# The story, word by word:
#   The / lighthouse / keeper / lit / nothing / tonight.
# A keeper whose one job is to light the lamp lights nothing
# tonight — and the reader is left to fill in why.


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"expected exactly 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, "entry must be 1-60 characters"
    assert STORY.strip(), "entry must not be only whitespace"

    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
