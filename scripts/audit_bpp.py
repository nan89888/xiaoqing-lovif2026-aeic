#!/usr/bin/env python3
"""Report actual bitstream bytes and unweighted BPP for matching PNG images."""

import argparse
from pathlib import Path

from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bitstream-dir", type=Path, required=True)
    parser.add_argument("--image-dir", type=Path, help="Optional source PNG directory for pixel count")
    args = parser.parse_args()

    streams = sorted(args.bitstream_dir.glob("*.bin"))
    if not streams:
        raise SystemExit(f"No .bin files found in {args.bitstream_dir}")

    total_bytes = sum(path.stat().st_size for path in streams)
    print(f"bitstreams: {len(streams)}")
    print(f"total_bytes: {total_bytes}")

    if args.image_dir is None:
        return

    total_pixels = 0
    missing = []
    for stream in streams:
        image_path = args.image_dir / f"{stream.stem}.png"
        if not image_path.exists():
            missing.append(image_path.name)
            continue
        with Image.open(image_path) as image:
            width, height = image.size
        total_pixels += width * height

    if missing:
        raise SystemExit("Missing matching images: " + ", ".join(missing[:10]))
    if total_pixels == 0:
        raise SystemExit("Total image pixels is zero")

    print(f"total_pixels: {total_pixels}")
    print(f"bpp: {8 * total_bytes / total_pixels:.12f}")


if __name__ == "__main__":
    main()
