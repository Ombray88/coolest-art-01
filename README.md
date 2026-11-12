# The World Turtle — coolest-art-01

A colossal sea turtle carrying a glowing golden city on its shell, swimming
through golden clouds above a tiny lighthouse at dusk. Sunlight refracts
through stained glass in its shell into shards of colour.

One clear focal point, a deep teal and warm gold palette, and a composition
that still reads at 300 pixels across.

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
