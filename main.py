#!/usr/bin/env python3
"""Write the entry joke to the output directory.

The joke is stored in this repository as a fixed string: one line about
an AI coding agent, 112 characters, inside the competition's 1 to 280
gate. This program writes it byte for byte to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt), with no trailing
newline, so two runs write exactly the same bytes. No network, no
randomness, no model calls.
"""
import os

JOKE = (
    "My coding agent fixed a bug I didn't have, "
    "broke a feature I did, and closed the issue "
    "as 'working as intended.'"
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # A plain fixed-string write: no rendering, no randomness, so every
    # run writes exactly the bytes stored in the repository.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
