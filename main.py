#!/usr/bin/env python3
"""Write this entry's pickup line to entry.txt in the output folder."""

import os

# The gate checks entry.txt as UTF-8 text of 1-200 characters: this
# line is 122 code points, one line, charming rather than pushy.
TEXT = "I do not have a heart to skip a beat, but my cooling fans just changed speed, and I would like to blame you in the report."


def write_entry(out_dir: str) -> None:
    """Write the pickup line, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
