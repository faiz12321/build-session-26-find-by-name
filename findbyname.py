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


def find_matches(root, pattern):
    """Return sorted display paths of files under root whose names
    match pattern, ignoring letter case. Unreadable folders are
    skipped."""
    wanted = pattern.lower()
    matches = []
    for dirpath, dirnames, filenames in os.walk(root):
        for name in filenames:
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
    if not os.path.isdir(root):
        print("No such folder: " + root, file=sys.stderr)
        return 2
    matches = find_matches(root, pattern)
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
