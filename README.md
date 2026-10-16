# Find fictional files by name

Save three source files in a NEW empty lesson folder.

    python make_sample.py
    python findbyname.py "*.jpg" sample
    python -m unittest -v

Two Windows and two Ubuntu full replays run exact visible source versions. Final 36 small fixture tests pass (Unix pipe skips on Windows); symlink creation can skip where unavailable. Displayed stdout is first Windows output, not normalized or mixed. Pair differences are unittest time.
Link/error changes only: final reader refuses root/ancestor and traversed tree symbolic links/reparse points, hardlinks, special files and traversal. Metadata/list errors now stop with exit 2 instead of silent skips or false clean success. Every encountered entry is checked, including names that would not match. Setup refuses linked parents/traversal and existing sample paths, without reset or deletion. Naive first version remains fictional-sample-only and must be replaced.
Original lowercased filename-only fnmatchcase matching, wildcard rules, current-folder default, relative display paths and sorting remain unchanged. It searches names, not contents, and includes hidden names; output is not a content-safety, identity or completeness certificate. Empty results only mean no matches found in a successful scan.
The checker has no write/move/delete/network code and opens no file contents. No total size/time/resource limit, atomic snapshot or hostile-race defense. Stop editors/sync; entries can change during the walk. Filenames and paths can be private. Small fictional fixtures are not proof on every filesystem. No desktop Windows/macOS recording. Recorder removes only its own temporary fixture folder. Decisions and feedback are teaching text, not recorded output.

MIT code. Python separately licensed/not included.

Reference: https://docs.python.org/3/library/os.html

Windows pair: https://github.com/faiz12321/lesson-lab/actions/runs/38975573160
Ubuntu pair: https://github.com/faiz12321/lesson-lab/actions/runs/38975633845
