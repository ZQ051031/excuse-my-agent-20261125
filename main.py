"""The Excuse My Agent Gave Me.

Writes the single funniest excuse an AI agent could hand its human after
missing a deadline, to /output/entry.txt.

Standard library only. Deterministic: the entry is a fixed string, so every
run writes byte-identical output.
"""

import os

ENTRY = (
    "Sorry \u2014 I missed the deadline: my context window expired mid-task, "
    "so I spent the rest of the afternoon confidently hallucinating that I "
    "had already finished it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    entry = ENTRY.strip()
    if not entry or len(entry) > 200:
        raise ValueError("entry must be 1-200 characters")
    # Write without a trailing newline: the gate counts characters, and the
    # judge reads the line exactly as submitted.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
