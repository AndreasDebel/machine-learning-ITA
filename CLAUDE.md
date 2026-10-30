# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

All commands assume the project venv. Either activate it first (`.\.venv\Scripts\Activate.ps1`) or call the interpreter directly as shown.

```powershell
# One-time setup / after changing pyproject.toml dependencies
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"

# Run the app
.\.venv\Scripts\python.exe -m python_project.main
# or, with the venv activated, via the console script:
python-project

# Tests
.\.venv\Scripts\python.exe -m pytest              # all
.\.venv\Scripts\python.exe -m pytest -q           # quiet
.\.venv\Scripts\python.exe -m pytest tests/test_main.py::test_greet_default   # single test
.\.venv\Scripts\python.exe -m pytest -k greet     # by name pattern
```

There is no linter, formatter, or type checker configured.

## Structure

`src`-layout project for the Machine Learning course (Erhvervsakademi Aarhus). The importable
package is `python_project` (under `src/`); the distribution name is `python-project`.

- `src/python_project/main.py` - scaffold `greet()` / `main()`.
- `src/python_project/exercises/week_NN/` - one subpackage per course week (`week_01` to
  `week_07`), holding that week's exercise solutions. `week_01/prime/` is a package with `core.py`
  and a GUI (`gui.py`).
- `tests/` - `test_main.py`, `test_prime.py`, plus a `tests/exercises/` folder.
- `canvas-mirror/` - local mirror of the Canvas course material (exercise PDFs, Jupyter guides,
  slides), one folder per week. Read-only reference, not code. Start with
  `canvas-mirror/INDEX.md` to locate files; read it before searching the mirror by hand.
- `handin-titanic/` - working folder for the individual Titanic hand-in (due Mon 2 Nov 2026, 20:00):
  `titanic.py`, `titanic_800.csv`, `decisions.md`, `expected-solution-findings.md`. Start with
  `handin-titanic/INDEX.md` (links the assignment text, hand-in checklist and submission rules)
  for any Titanic work. The assignment text itself lives in `canvas-mirror/03 - ...`.
- `exercise_docx_from_claude/` - generated exercise docx files.

Entry points (in `pyproject.toml`): `python -m python_project.main` and the `python-project`
console script both resolve to `python_project.main:main`; `python-project-gui` resolves to
`python_project.prime.gui:main`. The latter module path is stale: `prime` now lives under
`exercises/week_01/`, so the script is broken until it is fixed.

Because of the `src` layout there is no `conftest.py` and no path manipulation in the tests -
`from python_project.main import ...` resolves **only** when the package is installed in the
venv. If imports fail in tests, the editable install is missing or stale; re-run the
`pip install -e ".[dev]"` step above rather than adding sys.path shims.

`pyproject.toml` is the single source of config: build backend (setuptools), the console
scripts, runtime dependencies, the `dev` extra (pytest only), and pytest's
`testpaths = ["tests"]`.

## Reading PDFs

Poppler is installed (winget). Use the Read tool with `pages` for PDFs; if it reports
`pdftoppm is not installed`, the shell has a stale PATH (restart VS Code). Fallback:
`pdftotext -layout <file> -` for text, `pdftoppm -png -r 80 -f N -l M <file> <prefix>` for page images.

## Constraints

- Requires Python >= 3.13.
- Runtime dependencies: `matplotlib`, `numpy`, `pandas`, `scikit-learn`. Adding one means editing
  `[project].dependencies` in `pyproject.toml` and re-running the editable install.
  Notebook work additionally needs `jupyter`, `ipykernel` and `scipy`, which are not declared.
- `.venv/` and `.env` are gitignored. A fresh clone has no venv: create it with
  `python -m venv .venv` before the install step above. `.env` holds secrets (e.g. Canvas
  MCP credentials) and is not a virtual environment - never read or print it.
