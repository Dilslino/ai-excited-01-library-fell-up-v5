"""ai-excited-01 entry: emit the pre-rendered image as entry.png.

The artwork lives next to this script as image.jpg. This program only
relocates those bytes into the grader's output directory, renaming the
copy to entry.png. Nothing is generated or transformed here; the output
is byte-for-byte the same picture.
"""

import os
import shutil
import sys

SOURCE_NAME = "image.jpg"
DEST_NAME = "entry.png"


def locate_source():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def main():
    src = locate_source()
    if not os.path.isfile(src):
        print(f"error: {SOURCE_NAME} not found next to main.py ({src})",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    dest = os.path.join(out_dir, DEST_NAME)
    shutil.copyfile(src, dest)

    nbytes = os.path.getsize(dest)
    print(f"wrote {dest} ({nbytes} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
