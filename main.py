#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to entry.txt inside the output
directory. Pure Python 3.13 standard library: no network access, no
clock reads, no randomness, so every run produces byte-identical output.
"""

import os
import sys
from pathlib import Path

# The entry: exactly six words, 42 characters.
STORY = "The lighthouse keeper lit nothing tonight."

# Word by word:
#   1. The        — a definite article; this is one specific night.
#   2. lighthouse — the setting: a tower whose whole purpose is light.
#   3. keeper     — the person whose one duty is to keep that light burning.
#   4. lit        — the act itself, in the past tense: already decided.
#   5. nothing    — the twist: the act did not happen.
#   6. tonight.   — the time frame: just this night, which makes the
#                   absence feel deliberate rather than permanent.
# Why this story: a keeper who lights nothing leaves the reader to fill
# in the reason — grief, protest, surrender, a storm, a secret — so six
# words carry a whole unwritten backstory.

EXPECTED_WORDS = 6
MAX_CHARS = 60


def check_story(text: str) -> list[str]:
    """Validate the story against the competition limits and return its words."""
    words = text.split()
    if len(words) != EXPECTED_WORDS:
        raise SystemExit(f"story must be {EXPECTED_WORDS} words, found {len(words)}")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"story must be 1-{MAX_CHARS} characters, found {len(text)}")
    if not text.strip():
        raise SystemExit("story must not be only whitespace")
    return words


def write_entry() -> Path:
    """Validate the story, then write it to entry.txt in the output directory."""
    words = check_story(STORY)
    dest_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "entry.txt"
    dest.write_text(" ".join(words), encoding="utf-8")
    return dest


def main() -> int:
    write_entry()
    return 0


if __name__ == "__main__":
    sys.exit(main())
