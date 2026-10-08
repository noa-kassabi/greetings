# greetings

Welcome desk of Albert School: welcome, register and enroll new students.

## Setup

```bash
uv sync --locked
uv run pre-commit install
```

## Use

```bash
uv run greetings                                  # demo
uv run greetings roster path/to/roster.csv        # a day's roster
bash scripts/daily_roster.sh [YYYY-MM-DD]         # download then register (needs .env)
```

Copy `.env.example` to `.env` and fill it in. `.env` is never committed.

## Check

```bash
uv run ruff format --check . && uv run ruff check . && uv run mypy && uv run pytest
```
