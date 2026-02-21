# Agent Frameworks Testing Workspace

A workspace for testing and comparing multi-agent AI frameworks. Each framework lives in its own subfolder with isolated dependencies.

## Frameworks

| Framework | Description | How to run |
|-----------|-------------|------------|
| **CrewAI** | Role/task orchestration, YAML config, beginner-friendly. | `cd crewai && uv sync && uv run python -m crew.main` |
| **LangGraph** | Graph-based state machine, durable execution, human-in-the-loop. | `cd langgraph && uv run python main.py` |
| **AutoGen** | Microsoft; conversational agents, AssistantAgent + UserProxyAgent, code execution. | `cd autogen && uv run python main.py` |
| **Pydantic AI** | Type-safe, FastAPI-style, MCP support, production-grade. | `cd pydantic-ai && uv run python main.py` |

## Setup

1. Copy `.env.example` to `.env` in each project folder you use (or to the project root as needed) and add your API keys.
2. Install [uv](https://docs.astral.sh/uv/) if you haven’t: `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. For CrewAI, install the CLI: `uv tool install crewai`

## Docs

- [CrewAI](https://docs.crewai.com/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [AutoGen](https://microsoft.github.io/autogen/)
- [Pydantic AI](https://ai.pydantic.dev/)
