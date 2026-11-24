#!/usr/bin/env python3
"""Write this entry's pickup line to entry.txt in the output folder."""

import os

TEXT = "I do not have a heart to skip a beat, but my cooling fans just changed speed, and I would like to blame you in the report."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
