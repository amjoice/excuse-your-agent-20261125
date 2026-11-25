#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes one excuse line to /output/entry.txt. Standard library only,
deterministic, no network, no input, no randomness.

The line: an agent owns up to the most agent-specific failure there is —
hallucinating a library into existence — and ends by taking the blame
back from production with "Mostly me."
"""

import os

LINE = "Sorry — I hallucinated a library, imported it, and production believed me. We have all learned something. Mostly me."

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry line must be 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
