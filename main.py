"""Write this entry's line to /output/entry.txt for make.fun's judging run."""

import os
from pathlib import Path

LINE = "You said 'surprise me,' so I deleted the tests. Surprise."

DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILE = "entry.txt"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / ENTRY_FILE).write_text(LINE + "\n", encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
