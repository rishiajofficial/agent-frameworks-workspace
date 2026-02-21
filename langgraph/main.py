"""
Minimal LangGraph agent: a small state graph with an LLM node.
Run: uv run python main.py
Set OPENAI_API_KEY in the environment or .env.
"""
import operator
from typing import Annotated

from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class State(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]


def agent_node(state: State) -> dict:
    """Single node: call the LLM with current messages."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    response = llm.invoke(
        [SystemMessage(content="You are a helpful assistant. Reply briefly.")]
        + state["messages"]
    )
    return {"messages": [response]}


# Build graph: START -> agent -> END
graph = StateGraph(State)
graph.add_node("agent", agent_node)
graph.add_edge(START, "agent")
graph.add_edge("agent", END)

app = graph.compile()

if __name__ == "__main__":
    result = app.invoke({"messages": [HumanMessage(content="What is 2 + 2? Reply in one sentence.")]})
    for msg in result["messages"]:
        if hasattr(msg, "content") and msg.content:
            print(msg.content)
