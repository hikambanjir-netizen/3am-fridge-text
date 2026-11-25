#!/usr/bin/env python3
"""The 3AM Fridge Text - make.fun bounty entry.

Writes exactly one line - the message a smart fridge sends its owner at 3am -
to /output/entry.txt. Pure Python standard library only.
"""

import os

ENTRY = "3am. Your leftovers started a podcast in here and I'm the only subscriber. Please eat them before they get a sponsor."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # One line only, <= 140 characters, no follow-up needed on a lock screen.
    assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, over the 140 limit"
    assert "\n" not in ENTRY
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
