#!/usr/bin/env python3
"""coolest-art-01 entry: write the Chiseling the Star art to /output/entry.png.

The art is the entry.png beside this file. Per the competition rules the
name stays entry.png whether the bytes are a PNG or a JPEG, and the file is
told apart by its first bytes. This program validates the art (whole file,
at most 1 MiB, at most 1024 by 1024 pixels) and copies it byte-for-byte, so
both grader runs write identical bytes. Standard library only.

Art: "Chiseling the Star" — a ukiyo-e Japanese woodblock print of a tiny sculptor
in indigo kimono chiseling a giant glowing golden star out of a huge block of
dark night stone, golden chips flying, under a deep navy night sky, with a
red paper lantern.
"""

import os
import struct
import sys
from pathlib import Path

# Meticulous artisan shaping raw stellar ore in the silent midnight hours.
# Crimson paper lanterns casting a gentle glow over flying metallic debris.
# Massive basalt monoliths yielding luminous amber fragments under precise strikes.
# Searing topaz sparks shatter the velvet void.
# Tiny hands liberate radiant celestial fire from ancient obsidian.
# Gate limits from the competition rules (RULES.txt).
MAX_BYTES = 1_048_576
MAX_WIDTH = 1024
MAX_HEIGHT = 1024
SOURCE_NAME = "entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def _png_dimensions(data):
    """Return (width, height) from a PNG's IHDR chunk."""
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise ValueError("not a PNG: missing IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def _jpeg_dimensions(data):
    """Return (width, height) from a JPEG's first SOF marker."""
    pos = 2
    while pos + 9 < len(data):
        if data[pos] != 0xFF:
            raise ValueError("not a JPEG: bad marker")
        marker = data[pos + 1]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        length = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        pos += 2 + length
    raise ValueError("not a JPEG: no SOF marker found")


# Ensure the provided artwork meets all size, format, and dimension restrictions.
def validate_art(data):
    """Check the art against the gate; return (format, width, height)."""
    if len(data) > MAX_BYTES:
        raise ValueError(f"art is {len(data)} bytes, over the {MAX_BYTES} limit")
    if data[:8] == PNG_MAGIC:
        fmt, (width, height) = "PNG", _png_dimensions(data)
    elif data[:3] == JPEG_MAGIC:
        fmt, (width, height) = "JPEG", _jpeg_dimensions(data)
    else:
        raise ValueError("art is neither a whole PNG nor a whole JPEG")
    if width > MAX_WIDTH or height > MAX_HEIGHT:
        raise ValueError(f"art is {width}x{height}, over the {MAX_WIDTH}x{MAX_HEIGHT} limit")
    return fmt, width, height


# Coordinate validation and safe deployment of the entry image asset to the target output directory.
def main():
    source = Path(__file__).resolve().parent / SOURCE_NAME
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = output_dir / SOURCE_NAME
    data = source.read_bytes()
    fmt, width, height = validate_art(data)
    output_dir.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    print(f"wrote {target} ({fmt} {width}x{height}, {len(data)} bytes)")


if __name__ == "__main__":
    main()
