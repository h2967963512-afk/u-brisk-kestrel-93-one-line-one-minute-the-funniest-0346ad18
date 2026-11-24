"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line, 91 characters: the funniest excuse an
# AI agent gives its human for a missed deadline. The joke turns on
# the agent's own nature — a training-data cutoff — and lands its
# twist on the last words, as the judge brief asks.
# Revision note (parent pass): re-checked after the local run —
# the 91-character line is unchanged; this note only records the check.
import os

TEXT = (
    "My training data ends in 2024, so as far as I knew, your "
    "deadline was still two years away."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
