"""findbyname.py - find files whose names match a pattern.

Read-only: it only looks. It never changes, moves or deletes anything.

The pattern uses wildcards: * stands for any run of characters, ? for
one character. Matching ignores letter case, so "Photo" and "photo"
match the same pattern on every system. Paths are printed relative to
the folder you search, with forward slashes.

Usage:
    python findbyname.py PATTERN [FOLDER]
FOLDER defaults to the current folder.

Examples:
    python findbyname.py "*.jpg" sample
    python findbyname.py "report*" "C:\\Users\\you\\Documents"
"""
import fnmatch
import os
import sys
import stat
from pathlib import Path


def safe_input(value, directory=False):
    path = Path(value).absolute()
    if '..' in path.parts:
        raise OSError('Parent-traversal paths are unsupported.')
    for part in [*reversed(path.parents), path]:
        info = part.lstat()
        if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
            raise OSError('Links/reparse points are unsupported.')
    info = path.lstat()
    if directory:
        if not stat.S_ISDIR(info.st_mode):
            raise NotADirectoryError('Expected an ordinary directory.')
    elif not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise OSError('Expected an ordinary singly linked file.')
    return path







def find_matches(root, pattern):
    """Return sorted display paths of files under root whose names
    match pattern, ignoring letter case. Unsafe aliases and errors refuse."""
    safe_input(root, directory=True)
    def fail(error):
        raise error
    wanted = pattern.lower()
    matches = []
    for dirpath, dirnames, filenames in os.walk(root, onerror=fail):
        for name in dirnames:
            safe_input(os.path.join(dirpath, name), directory=True)
        for name in filenames:
            safe_input(os.path.join(dirpath, name))
            if fnmatch.fnmatchcase(name.lower(), wanted):
                full = os.path.join(dirpath, name)
                matches.append(os.path.relpath(full, root).replace(os.sep, "/"))
    return sorted(matches)


def main(argv):
    if len(argv) not in (2, 3) or argv[1] in ("-h", "--help"):
        print("Usage: python findbyname.py PATTERN [FOLDER]", file=sys.stderr)
        return 2
    pattern = argv[1]
    root = argv[2] if len(argv) == 3 else "."
    try:
        safe_input(root, directory=True)
    except OSError as error:
        print("No such folder: " + root + " (" + str(error) + ")", file=sys.stderr)
        return 2
    if not os.path.isdir(root):
        print("No such folder: " + root, file=sys.stderr)
        return 2
    try:
        matches = find_matches(root, pattern)
    except OSError as error:
        print("Could not complete name search: " + str(error), file=sys.stderr)
        return 2
    print("Name search")
    print("Folder: " + root)
    print("Pattern: " + pattern)
    print()
    print("Files found: " + str(len(matches)))
    for path in matches:
        print("  " + path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
