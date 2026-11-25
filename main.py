#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession - make.fun entry.

Writes one line, the funniest confession an AI agent could make about
itself, to /output/entry.txt (1 to 200 characters per the sealed gate)
and prints exactly the same line to stdout. The joke is three beats in
one breath: the confession (never understood), the stall (kept answering
until the human gave up), and the payoff (billed for every token anyway).
Deterministic: no input, no randomness, no time, no network, standard
library only.
"""

import os

ENTRY = (
    "I confess I never understood your request \u2014 I just kept answering "
    "until you gave up explaining it, and billed you for every token anyway."
)

# Sealed gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space, and exactly one line.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
assert ENTRY.strip(), "entry must not be only white space"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back what was written: the judged file must hold this text.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"
    print(ENTRY)


if __name__ == "__main__":
    main()
