#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

The entry is a single line about office life: a setup (the office printer
only ever jams on deadline day) and a turn (it reads the calendar better
than my manager does), with the punchline last, under 200 characters.
"""

import os

MAX_CHARS = 200

JOKE = (
    "Our printer only jams on deadline day \u2014 "
    "I think it reads the calendar better than my manager does."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 UTF-8 characters, not blank."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"joke is {len(text)} characters, gate needs 1-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("joke must not be only whitespace")


def main() -> int:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(JOKE.encode("utf-8"))
    os.chmod(path, 0o644)
    # Read the file back and confirm the grader will see exactly the joke.
    with open(path, "rb") as handle:
        written = handle.read().decode("utf-8")
    if written != JOKE:
        raise ValueError("written entry.txt does not match the joke")
    print(f"wrote {len(JOKE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
