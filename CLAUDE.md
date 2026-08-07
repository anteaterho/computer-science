# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

This is a **learning repository** — coursework for a Korean computer-science curriculum, not a software project. There is no build system, package manager, tests, or git history. It is organized by topic:

- `01. 블록코딩/` — block coding (empty so far)
- `02. C언어/` — C language (empty so far)
- `03. Python/` — the only populated section; Python fundamentals

Content is grouped into numbered subject folders (`01. 기본문법/`), then numbered topic folders (`01. 출력`, `02. 입력`, `03. 반복제어문`, `04. 리스트`). File names follow `NN_주제_ex_NN.py` (e.g. `01_출력_ex_01.py`); some homework files are named `homework.py`.

## Running exercises

Each file is a standalone script. Run one with (paths contain spaces and Korean characters — always quote):

```bash
python "03. Python/01. 기본문법/02. 입력/homework.py"
```

Files under `02. 입력` and later read from stdin via `input()`.

## File anatomy

A typical exercise file contains, in order: a triple-quoted docstring stating the **problem** (in Korean), one or more commented-out or triple-quoted **earlier attempts**, then the **current working solution** at the bottom. When editing, the live code is the un-commented block at the end — leave the problem statement and prior attempts intact unless asked, since they are part of the student's record.

## Working style — this is the important part

`03. Python/.vscode/settings.json` deliberately disables **all** editor autocomplete, inline suggestions, and parameter hints. This is a beginner learning environment: the student is meant to write and figure out code themselves.

Because of that, default to **teaching over solving**. Prefer explaining the concept, pointing at the bug, or giving a hint over writing the finished answer. Do not silently "improve", refactor, or modernize a student's working code (list comprehensions, f-strings, etc.) unless they ask — matching the level of the current lesson matters more than idiomatic polish. Solution files may intentionally contain the kind of small logic mistakes a learner makes; confirm intent before "fixing" them.
