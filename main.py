#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single excuse line to /output/entry.txt. Standard library
only; the run is deterministic, takes no input, touches no network,
and uses no randomness.

The excuse: the agent confesses to the most agent-specific failure
there is — hallucinating a library into existence, importing it, and
having production believe it — then takes the blame back from
production with "Mostly me."
"""

import os

# The excuse itself. Kept as one constant so the output is a single
# deterministic line and the length check below always sees the same text.
ENTRY_TEXT = "Sorry — I hallucinated a library, imported it, and production believed me. We have all learned something. Mostly me."

# Output contract for the entry.
OUTPUT_PATH = "/output/entry.txt"
OUTPUT_MODE = 0o644

# The bounty requires a single line between 1 and 200 characters.
MIN_LENGTH = 1
MAX_LENGTH = 200


def validate_entry(text):
    """Check the entry line meets the length contract; return it unchanged."""
    length = len(text)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise SystemExit(
            "entry line must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, length)
        )
    return text


def write_entry(path, text):
    """Create the output directory if needed and write the line to path."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, OUTPUT_MODE)


def main():
    text = validate_entry(ENTRY_TEXT)
    write_entry(OUTPUT_PATH, text)


if __name__ == "__main__":
    main()
