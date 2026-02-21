# CrewAI crew

Minimal CrewAI research crew: researcher + analyst producing a report on a topic.

## Setup

1. Copy `.env` from workspace root or create from `../.env.example` and set `OPENAI_API_KEY`.
2. From this directory:
   ```bash
   uv sync
   ```
   Or with pip: `pip install -e .`

## Run

From this directory:

```bash
uv run python -m crew.main
```

Or: `uv run run-crew`

To use the CrewAI CLI instead (if installed): `crewai install` then `crewai run` — you would need to point the CLI at this project (e.g. same structure with a `run` script in pyproject matching `crew.main:run`).
