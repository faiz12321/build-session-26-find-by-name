# Find files by name pattern

The final `findbyname.py` is a read-only teaching tool. It matches file names,
not file contents or folder names, using `fnmatchcase` on lowercased strings.
It lists relative paths with forward slashes. Unreadable folders can be skipped,
so a report is not a complete audit. A match is not a deletion recommendation.

## Practise

Save all three files in a new empty lesson folder. Python 3 is required:

    python make_sample.py
    python findbyname.py "*.jpg" sample
    python findbyname.py "report*" sample
    python findbyname.py "cat-0?.png" sample
    python -m unittest -v

Setup creates `sample` beside the script and refuses any existing sample path.
It does not delete or reset existing folders. Use a different new empty lesson
folder if it refuses. Photo and document names contain fictional text practice
bytes, not real photos or documents.

## Tests and recordings

22 fixture tests all create their data inside temporary folders. They cover
pattern behavior, CLI errors, unchanged source-tree metadata, setup file and
folder collision refusal, existing bytes, a nested unrelated file and repeat-run
preservation. The sample-count test also uses its own temporary folder.

The repair was recorded twice on GitHub-hosted Windows and twice on Ubuntu.
The recordings first save the intentionally limited plain-text checker from the
lesson, run it, then save the final pattern checker. Displayed outputs use the
first Windows run. Paired runs differ only in unittest elapsed time. Versions
and test rendering can differ by platform. No macOS or Windows desktop session
was tested; fixture passes are limited evidence, not a universal safety proof.

## License

MIT (see LICENSE).
