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

`src`-layout project. The importable package is `python_project` (under `src/`); the
distribution name is `python-project`. Two entry points into the same function:
`python -m python_project.main` and the `python-project` console script, both resolving to
`python_project.main:main`.

Because of the `src` layout there is no `conftest.py` and no path manipulation in the tests —
`from python_project.main import ...` resolves **only** when the package is installed in the
venv. If imports fail in tests, the editable install is missing or stale; re-run the
`pip install -e ".[dev]"` step above rather than adding sys.path shims.

`pyproject.toml` is the single source of config: build backend (setuptools), the console
script, the `dev` extra (pytest only), and pytest's `testpaths = ["tests"]`.

## Constraints

- Requires Python >= 3.13.
- Zero runtime dependencies. Adding one means editing `[project].dependencies` in
  `pyproject.toml` and re-running the editable install.
- The current code is a scaffold: `main.py` holds a single `greet()` helper and a `main()`
  that prints it, with matching tests. There is no meaningful architecture yet.
