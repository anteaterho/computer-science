# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

This is a **learning repository** — coursework for a Korean computer-science curriculum, not a software project. There is no build system, package manager, tests, or git history. It is organized by topic:

- `01. 블록코딩/` — block coding (empty so far)
- `02. C언어/` — C language (empty so far)
- `03. Python/` — the only populated section, split into two subjects: `01. 기본문법/` (Python fundamentals, sessions 01–10) and `02. 인공지능/` (AI track, started with pandas/numpy)

Content is grouped into numbered subject folders (`01. 기본문법/`, `02. 인공지능/`), then one folder per class session, numbered in order: `01. 출력`, `02. 입력`, `03. 반복제어문`, `04. 리스트_01` … `10. 딕셔너리_02`. A topic spanning several sessions gets a `_NN` suffix (`리스트_01/_02/_03`, `세트_01/_02`, `딕셔너리_01/_02`), so two folders may share a session number when one session covered two topics (`09. 세트_02`, `09. 딕셔너리_01`).

Within a session folder:

- exercises: `NN_주제_ex_NN.py` — the leading `NN` is the session number, the trailing one the exercise number as the instructor numbered it (e.g. `03_반복_ex_09.py`)
- in `02. 인공지능/` the whole session is one Jupyter notebook instead, named `NN_주제.ipynb` (e.g. `01_오리엔테이션_판다스_넘파이.ipynb`); its cells play the role the separate `ex` files play elsewhere
- homework: a `숙제/` subfolder holding `NN_주제_숙제_NN.py` plus any problem-statement images, named `NN_주제_과제*.png`
- study notes: `NN_주제_노트.md` (e.g. `03_반복_노트.md`, `01_오리엔테이션_노트.md`) — what was learned, per-file summary, bugs worth revisiting, what to practice next. A `숙제/` folder may carry its own `NN_주제_숙제_노트.md`.

## Running exercises

Each file is a standalone script. Run one with (paths contain spaces and Korean characters — always quote):

```bash
python "03. Python/01. 기본문법/02. 입력/숙제/02_입력_숙제_01.py"
```

Files under `02. 입력` and later read from stdin via `input()`.

## File anatomy

A typical exercise file contains, in order: a triple-quoted docstring stating the **problem** (in Korean), one or more commented-out or triple-quoted **earlier attempts**, then the **current working solution** at the bottom. When editing, the live code is the un-commented block at the end — leave the problem statement and prior attempts intact unless asked, since they are part of the student's record.

## Working style — this is the important part

`03. Python/.vscode/settings.json` deliberately disables **all** editor autocomplete, inline suggestions, and parameter hints. This is a beginner learning environment: the student is meant to write and figure out code themselves.

Because of that, default to **teaching over solving**. Prefer explaining the concept, pointing at the bug, or giving a hint over writing the finished answer. Do not silently "improve", refactor, or modernize a student's working code (list comprehensions, f-strings, etc.) unless they ask — matching the level of the current lesson matters more than idiomatic polish. Solution files may intentionally contain the kind of small logic mistakes a learner makes; confirm intent before "fixing" them.
