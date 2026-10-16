# Find files by name pattern

`findbyname.py` lists the files inside a folder whose names match a
pattern you give it. It is read-only: it only looks, and it never
changes, moves or deletes anything. Run it first on the made-up
`sample` folder from `make_sample.py` before pointing it anywhere
else.

- `*` stands for any run of characters, `?` for exactly one.
- Matching ignores letter case on every system, so `*.jpg` also finds
  `dog.JPG`.
- Paths are printed relative to the folder you search, with forward
  slashes.
- Folders the tool cannot read are skipped; the report only covers
  what it could see.
- Only file names are matched, never folder names or contents.

## Use

    python make_sample.py
    python findbyname.py "*.jpg" sample
    python findbyname.py "report*" "C:\Users\you\Documents"

If you leave out the folder, the current folder is searched.

## Tests

    python -m unittest -v

Works on Windows, Mac and Linux with Python 3.10 or newer. Nothing to
install: it uses only what comes with Python.

## License

MIT (see LICENSE).
