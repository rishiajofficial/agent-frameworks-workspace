"""
Minimal Pydantic AI agent: one agent, one run.
Run: uv run python main.py
Set OPENAI_API_KEY in the environment or .env.
"""
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o-mini")

if __name__ == "__main__":
    result = agent.run_sync("What is 2 + 2? Reply in one short sentence.")
    print(result.output)
