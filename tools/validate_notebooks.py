"""Validate course notebooks without third-party dependencies."""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DIRECTORIES = ("notebooks", "exercises", "solutions", "projects")
EXPECTED_COUNTS = {"notebooks": 12, "exercises": 4, "solutions": 4, "projects": 3}


def source_text(cell):
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else source


def validate_notebook(path):
    errors = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"cannot read valid JSON: {error}"]

    if notebook.get("nbformat") != 4:
        errors.append("nbformat must be 4")
    cells = notebook.get("cells", [])
    if not cells:
        errors.append("contains no cells")
        return errors

    markdown_text = "\n".join(source_text(cell) for cell in cells if cell.get("cell_type") == "markdown")
    if "colab.research.google.com" not in markdown_text:
        errors.append("missing Google Colab link")
    if "Learning objectives" not in markdown_text:
        errors.append("missing learning objectives")
    first_markdown = source_text(cells[0])
    if any(line.startswith("    ") for line in first_markdown.splitlines()):
        errors.append("introductory Markdown contains code-block indentation")

    for index, cell in enumerate(cells, start=1):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs"):
            errors.append(f"code cell {index} contains committed output")
        source = source_text(cell)
        try:
            compile(source, f"{path}:{index}", "exec")
        except SyntaxError as error:
            errors.append(f"code cell {index} has invalid Python: {error.msg}")
    return errors


def execute_notebook(path):
    """Execute code cells in order using an isolated namespace."""
    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace = {"__name__": "__main__", "__file__": str(path)}
    captured_output = io.StringIO()
    for index, cell in enumerate(notebook.get("cells", []), start=1):
        if cell.get("cell_type") != "code":
            continue
        source = source_text(cell)
        try:
            with contextlib.redirect_stdout(captured_output):
                exec(compile(source, f"{path}:{index}", "exec"), namespace)
        except Exception as error:  # Report the exact notebook cell that failed.
            return [f"code cell {index} failed at runtime: {type(error).__name__}: {error}"]
    return []


def validate_markdown_links():
    errors = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    import re
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", readme):
        if "://" in target or target.startswith("#"):
            continue
        if not (ROOT / target).exists():
            errors.append(f"README link does not exist: {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--execute",
        action="store_true",
        help="also execute every code cell in notebook order",
    )
    arguments = parser.parse_args()
    failures = []
    for directory in REQUIRED_DIRECTORIES:
        notebooks = sorted((ROOT / directory).glob("*.ipynb"))
        expected = EXPECTED_COUNTS[directory]
        if len(notebooks) != expected:
            failures.append(f"{directory}: expected {expected} notebooks, found {len(notebooks)}")
        for path in notebooks:
            for error in validate_notebook(path):
                failures.append(f"{path.relative_to(ROOT)}: {error}")
            if arguments.execute:
                for error in execute_notebook(path):
                    failures.append(f"{path.relative_to(ROOT)}: {error}")
    failures.extend(validate_markdown_links())

    if failures:
        print("Validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    total = sum(EXPECTED_COUNTS.values())
    runtime = " and runtime execution" if arguments.execute else ""
    print(
        f"Validated {total} notebooks: JSON, syntax, Colab links, outputs, "
        f"structure{runtime} are clean."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
