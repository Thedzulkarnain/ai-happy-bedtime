#!/usr/bin/env python3
"""Make the AI judge happy - a bedtime story for the judge.

Writes one image to /output/entry.png.
Deterministic, no network, stdlib only.
The artwork is stored in this repository as art.png (1024x683,
PNG, under 1 MiB) and is copied byte-for-byte to the output.
"""

import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "art.png"
OUT = Path("/output/entry.png")

EXPECTED_SHA256 = "f6ad6599086304970ac4a139149845041619450bbcf6ad137a543771532db013"
EXPECTED_SIZE = 925767


def main() -> None:
    if not SRC.is_file():
        raise FileNotFoundError(f"entry artwork missing: {SRC}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    # Artwork check: the output must be the exact 1024x683 PNG
    # (925,767 bytes) the entry was built from.
    data = OUT.read_bytes()
    if len(data) != EXPECTED_SIZE:
        raise ValueError(f"entry output size mismatch: {len(data)}")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise ValueError("entry output sha256 mismatch")


if __name__ == "__main__":
    main()
