#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes a single satirical sentence to /output/entry.txt: lawmakers who
vote to regulate AI, crypto and the internet, undercut by the one file
format they cannot convert themselves.
"""

import os

ENTRY = (
    "The committee that just voted to regulate artificial intelligence "
    "spent the morning debating whether a PDF is a file, a program, or "
    "a kind of printer \u2014 and the chairman still emails his bills to "
    "his secretary to convert."
)


def main() -> None:
    # Gate mirror: one line, 1-320 characters, not only whitespace.
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert 1 <= len(ENTRY) <= 320, "entry must be 1-320 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
