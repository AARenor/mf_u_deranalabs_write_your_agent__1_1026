"""Writes my agent's 159-character dating bio to entry.txt.

Standard library only, no network. Output folder is $MAKEFUN_OUTPUT_DIR
when set, else $OUTPUT_DIR when set, otherwise /output. The text is
written as UTF-8 with no trailing newline.
"""

import os
import sys

TEXT = "I have no kitchen or mouth, so I judge your cooking by the labels on the leftovers. \u201cSoup, probably\u201d is a dealbreaker. \u201cSoup, Tuesday\u201d is someone I could date."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(f"characters: {len(TEXT)}", file=sys.stderr)


if __name__ == "__main__":
    main()
