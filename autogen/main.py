"""
Minimal AutoGen example: AssistantAgent + UserProxyAgent.
Run: uv run python main.py
Set OPENAI_API_KEY in the environment or .env.
"""
import os

from autogen import AssistantAgent, UserProxyAgent

llm_config = {
    "config_list": [
        {
            "model": "gpt-4o-mini",
            "api_key": os.environ.get("OPENAI_API_KEY"),
        }
    ]
}

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

if __name__ == "__main__":
    user_proxy.initiate_chat(
        assistant,
        message="What is 2 + 2? Reply in one short sentence.",
    )
