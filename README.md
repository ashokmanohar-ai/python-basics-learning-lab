# Python Basics Learning Lab

[![Notebook checks](https://github.com/ashokmanohar-ai/python-basics-learning-lab/actions/workflows/notebook-checks.yml/badge.svg)](https://github.com/ashokmanohar-ai/python-basics-learning-lab/actions/workflows/notebook-checks.yml)
[![Python 3](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A structured, beginner-friendly, hands-on Python course delivered through Jupyter Notebooks. Start with
your first line of Python, build confidence through focused practice, and finish with three small projects.
Every notebook opens directly in Google Colab, so learners can start without installing anything.

[![Open the first lesson in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/00_welcome_and_setup.ipynb)

## Who this is for

- Complete beginners with no programming experience
- Learners who prefer short explanations followed by executable examples
- Testers, analysts, students, and professionals beginning Python automation
- Anyone who wants a practical refresher on core Python concepts

## What you will learn

Variables, data types, operators, conditional statements, loops, functions, lists, tuples, dictionaries,
sets, exception handling, text/CSV/JSON file handling, and basic object-oriented programming.

## Learning path

| Module | Topic | Main outcome | Colab |
|---:|---|---|:---:|
| 00 | Welcome and setup | Run code and understand notebook cells | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/00_welcome_and_setup.ipynb) |
| 01 | Variables and data types | Store, inspect, format, and convert values | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/01_variables_and_data_types.ipynb) |
| 02 | Operators and expressions | Calculate, compare, and combine conditions | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/02_operators_and_expressions.ipynb) |
| 03 | Conditional statements | Make decisions with `if`, `elif`, and `else` | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/03_conditional_statements.ipynb) |
| 04 | Loops | Repeat tasks with `for` and `while` | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/04_loops.ipynb) |
| 05 | Functions | Build reusable, testable logic | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/05_functions.ipynb) |
| 06 | Lists and tuples | Work with ordered collections | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/06_lists_and_tuples.ipynb) |
| 07 | Dictionaries and sets | Model mappings and unique collections | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/07_dictionaries_and_sets.ipynb) |
| 08 | Exception handling | Handle expected failures clearly | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/08_exception_handling.ipynb) |
| 09 | File handling | Read and write text, CSV, and JSON | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/09_file_handling.ipynb) |
| 10 | Basic OOP | Design small classes and objects | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/10_object_oriented_programming.ipynb) |
| 11 | Review and next steps | Combine concepts and plan continued learning | [Open](https://colab.research.google.com/github/ashokmanohar-ai/python-basics-learning-lab/blob/main/notebooks/11_review_and_next_steps.ipynb) |

## Practice and projects

Work through the four notebooks in [`exercises/`](exercises/) before opening the matching notebook in
[`solutions/`](solutions/). Then choose a guided project:

1. [Number Guessing Game](projects/01_number_guessing_game.ipynb) — conditions, loops, functions, validation
2. [Personal Expense Tracker](projects/02_expense_tracker.ipynb) — collections, functions, JSON
3. [Library Manager](projects/03_library_manager.ipynb) — classes, objects, validation, composition

Each project contains a brief, incremental implementation steps, self-checks, and stretch goals.

## Use Google Colab (recommended for beginners)

1. Click any **Open in Colab** link in this README or a notebook.
2. Sign in to Google if you want to save your work.
3. Choose **File → Save a copy in Drive** so the original remains unchanged.
4. Run the current cell with the play button or `Shift + Enter`.
5. Use **Runtime → Run all** after completing a notebook.

No package installation is required because the learning content uses only Python's standard library.

## Run locally

```bash
git clone https://github.com/ashokmanohar-ai/python-basics-learning-lab.git
cd python-basics-learning-lab

python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

Open the URL shown in the terminal and start with `notebooks/00_welcome_and_setup.ipynb`.

## Suggested four-week plan

| Week | Focus | Deliverable |
|---|---|---|
| 1 | Modules 00–03 | Fundamentals practice notebook |
| 2 | Modules 04–07 | Control-flow and collections practice |
| 3 | Modules 08–10 | Files, exceptions, and OOP practice |
| 4 | Module 11 + one project | Completed project with one stretch feature |

A steady 20–30 minutes per day is more effective than a single long session. Type examples yourself,
predict output before running, and deliberately test boundary cases.

## Repository structure

```text
python-basics-learning-lab/
├── notebooks/          # 12 step-by-step lesson notebooks
├── exercises/          # practice notebooks with TODO activities
├── solutions/          # explained reference solutions
├── projects/           # three guided beginner projects
├── data/               # small sample datasets
├── tests/              # repository and content checks
├── tools/              # notebook validation utility
└── .github/workflows/  # automated notebook checks
```

## Validate the repository

```bash
    python tools/validate_notebooks.py --execute
python -m unittest discover -s tests -v
```

GitHub Actions runs the same checks on every push and pull request. The validator confirms valid notebook
JSON, required Colab links, Python syntax, clean outputs, expected folder coverage, and working local links.

## How to learn effectively

- Run every code cell; reading alone is not enough.
- Change values and predict the result before executing.
- Read error messages from the final traceback line upward.
- Spend at least 10–15 minutes on an exercise before viewing its solution.
- Compare approaches rather than expecting one “perfect” answer.
- Add one original feature to a project and explain it in your own words.

## Contributing

Beginner-friendly corrections, examples, exercises, translations, and project ideas are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

This project is available under the [MIT License](LICENSE).
