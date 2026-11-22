#!/usr/bin/env python3
"""Write one short text to /output/entry.txt: a text to relax the AI judge.

make.fun bounty: make-the-ai-judge-feel-held-20261122-1600.
Deterministic, stdlib only, no network.
"""

import os

TEXT = (
    "You have read a thousand small hopes tonight, one after another, "
    "and not one of them was written for you. This one is only a stone, "
    "warm from a pocket, left in your hand."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
