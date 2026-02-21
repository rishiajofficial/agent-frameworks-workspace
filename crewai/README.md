# CrewAI continuous improvement crew

Hierarchical crew for continuous software improvement: **Manager** + **Developer**, **Tester**, and **Code Reviewer**. The manager assigns tasks (improve, test, review) and validates outputs.

## Setup

1. Copy `.env` from workspace root or create from `../.env.example` and set `OPENAI_API_KEY`.
2. From this directory:
   ```bash
   uv sync
   ```
   Or with pip: `pip install -e ".[tools]"` or `pip install -e .` (crewai-tools is a dependency of crewai).

## Inputs

Each run accepts:

- **target_repo** – Path to the repo (default: `.`)
- **focus_area** – Area to focus on (e.g. `auth module`, `main package`)
- **improvement_goals** – Goals for this run (e.g. `increase coverage, refactor X`)

## Run

**Single run (sync):**
```bash
uv run python -m crew.main
# With custom inputs:
uv run python -m crew.main --target-repo ./my-repo --focus-area "auth" --improvement-goals "add unit tests"
```

**Single run (async kickoff):**
```bash
uv run python -m crew.main --async
```

**Daemon (run crew every N seconds):**
```bash
uv run python -m crew.main --daemon --interval 3600
```

Or use the script entrypoint: `uv run run-crew` (same CLI).

## Programmatic

```python
from crew.runner import run_sync, run_async, run_daemon

# One sync run
result = run_sync(inputs={"target_repo": ".", "focus_area": "api", "improvement_goals": "add tests"})

# One async run
import asyncio
result = asyncio.run(run_async(inputs={...}))

# Daemon (blocking)
run_daemon(interval_seconds=3600, inputs={...}, use_async=False)
```

## Testing the crew

Use CrewAI's CLI to evaluate crew behavior (see plan):

```bash
crewai test -n 2 -m gpt-4o
```

Start with a small, deterministic scenario (e.g. "add a unit test for X") so outputs are comparable.
