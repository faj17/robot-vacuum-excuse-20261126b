#!/usr/bin/env python3
"""Robot vacuum excuse entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

SETUP = "I didn't miss that spot \u2014 the dust bunny looked me in the sensor"
PUNCH = "and I blinked first."


def assemble():
    return SETUP + " " + PUNCH


def validate(text):
    assert isinstance(text, str) and text.strip(), "entry must be non-empty"
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    return text


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(assemble()))


if __name__ == "__main__":
    main()
