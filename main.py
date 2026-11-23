#!/usr/bin/env python3
"""Make the Judge Smile — entry program.

Writes one line (at most 200 characters) about a small good thing
that happened today to /output/entry.txt. Deterministic: the same
bytes on every run, no input, no network, no randomness.
"""

import os

LINE = (
    "The stray cat that has hissed at me for a year waited by my door "
    "this morning, dropped a leaf at my feet and purred \u2014 I think "
    "I have officially been adopted."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
