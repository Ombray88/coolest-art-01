# Chiseling the Star — coolest-art-01

A ukiyo-e Japanese woodblock print of a tiny sculptor in indigo kimono chiseling a giant glowing golden star out of a huge block of dark night stone, golden chips flying, under a deep navy night sky, with a red paper lantern.

A patient artisan carves celestial luminescence from an inky midnight monolith suspended in the void.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (JPEG bytes, 1024x1024, under 1 MiB)
```

`main.py` (Python 3.13, standard library only) validates the art against the
competition gate — a whole PNG or JPEG, at most 1 MiB and 1024 by 1024 — and
copies it byte-for-byte to `/output/entry.png`, so both grader runs write
identical bytes.

## License

MIT — see LICENSE.

## How to run
```bash
MAKEFUN_OUTPUT_DIR=/tmp/art-output python3 main.py
```
The terminal output indicates the target file location, detected format, pixel dimensions, and size in bytes.
