# code-ops-daily

A personal collection of short, practical code examples, small scripts, and notes created as daily exercises and quick references. The goal is to keep bite-sized, easy-to-read items you can adapt and reuse.

## What you'll find here
This repository is organized by day and topic to make adding and browsing small exercises simple. Example folders in this repo:
- Day-01/ … Day-09/ — daily exercises and example files (one folder per day)
- DAY-03/ — a duplicate/alternate-day folder (check contents and unify if needed)
- List-ExHandling/ — examples about lists and exception handling
- Notes/ — short writeups, tips, and useful commands
- emOji/ — small emoji-related experiments
- other-folder/ — miscellaneous files
- .gitignore
- README.md (this file)

If you open any folder you’ll typically find small scripts, short programs, or a README describing that day's intent.

## Purpose
- Capture quick solutions, tricks, and learning notes.
- Keep examples minimal and focused — one idea per file.
- Serve as a personal reference and a place to share small utilities.

## Getting started
1. Clone the repo:
   ```bash
   git clone https://github.com/Attrivishal/code-ops-daily.git
   cd code-ops-daily
   ```
2. Browse a folder (for example `Day-03/`) and open files in your editor.
3. Read the top comments in each file for usage instructions.

## How to run items
- Check the file extension or first line (shebang) to identify language.
- Common commands:
  - Bash: `bash path/to/script.sh` or make executable `chmod +x script.sh && ./script.sh`
  - Python: `python3 path/to/script.py` (consider using a virtualenv)
  - Node: `node path/to/script.js`
- If a script requires dependencies, the file should include notes at the top describing how to install them (e.g., `pip install -r requirements.txt`, or `npm install`).

## Recommended file header for new items
When you add a new file, include a short header like:
```text
# Title: one-line description
# Purpose: what this script/example demonstrates
# Usage: how to run it (example command)
# Requirements: any libraries or tools needed
```

## Contributing
Small, focused contributions are welcome. Suggestions:
- One idea per file or one logical change per pull request.
- Add/update a short header at the top of new files (see the recommended header).
- Use clear file names (e.g., `Day-07/todo-list.py`, `List-ExHandling/unique_items.js`).
- Branch/PR workflow:
  - Create a topic branch: `git checkout -b feat/day-10-example`
  - Make small commits with meaningful messages.
  - Open a pull request describing the change and usage.
- If you add tests or example outputs, include them alongside the files.

## Style & maintenance suggestions
- Prefer readability and small, self-contained examples.
- Avoid hard-coded local paths or machine-specific assumptions.
- Document required runtime versions (e.g., Python 3.10) at the top of files.
- Consider consolidating duplicate folders (e.g., `DAY-03` vs `Day-03`) to keep naming consistent.

## License
No license file is included by default. If you want to publish or share this repository publicly, add a LICENSE file (MIT is a common choice for small collections). Example: create a `LICENSE` file with the MIT text.

## Roadmap / Ideas
- Add a short README inside each Day-* folder explaining the day's theme.
- Add a top-level index (example: `INDEX.md`) with one-line descriptions and direct links to interesting files.
- Add a small CI check to ensure scripts contain a header (optional).

## Contact / Questions
If you want changes or a tailored README that lists every file with a one-line description, tell me which level of detail you want and I can:
- Generate a README that enumerates files and short descriptions automatically, or
- Commit this README directly to the repository for you.

Enjoy using the repo — keep items small and focused, and it will become a very useful personal reference.
