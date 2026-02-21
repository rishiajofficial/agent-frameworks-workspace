# LangGraph example

Minimal graph with one LLM node. Graph-based state machine, good for production and human-in-the-loop flows.

## Setup

Copy `../.env.example` to `.env` and set `OPENAI_API_KEY`. Then:

```bash
uv sync
```

## Run

```bash
uv run python main.py
```

Docs: [LangGraph](https://langchain-ai.github.io/langgraph/)
