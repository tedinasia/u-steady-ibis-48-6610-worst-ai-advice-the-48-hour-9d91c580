#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible AI advice to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "If your phone gets wet, charge it immediately \u2014 the electricity dries it out faster."

OUTPUT_PATH = "/output/entry.txt"

# The gate requires 1-140 UTF-8 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry violates the 1-140 char gate"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
