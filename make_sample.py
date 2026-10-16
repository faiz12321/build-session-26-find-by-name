"""make_sample.py - create a made-up practice folder for the lesson.

Creates a folder called "sample" next to this script with made-up
files and folders: photos with mixed letter case, documents, and a
couple of names that trick a simple text search. It refuses any existing
sample path before writing. Nothing is deleted or replaced.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLE = os.path.join(HERE, "sample")

FILES = [
    "notes.txt",
    "photos/cat.jpg",
    "photos/dog.JPG",
    "photos/photo notes.txt",
    "photos/raw/cat-01.png",
    "report draft.docx",
    "report final.docx",
    "stars.txt",
]


def main():
    try:
        os.mkdir(SAMPLE)
    except FileExistsError:
        raise SystemExit("Stopped: sample already exists. Nothing was replaced or deleted.")
    for relative in FILES:
        path = os.path.join(SAMPLE, *relative.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "x", encoding="utf-8", newline="") as handle:
            handle.write("made-up practice bytes\n")
    print("Created a new sample folder beside make_sample.py.")
    print("It holds 8 made-up files for pattern search practice.")


if __name__ == "__main__":
    main()
