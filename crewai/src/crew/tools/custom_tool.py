"""Example custom tool. Add your tools here."""
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class CustomToolInput(BaseModel):
    """Input schema for CustomTool."""

    query: str = Field(..., description="Query to process")


class CustomTool(BaseTool):
    """Example custom tool for the crew."""

    name: str = "Custom Tool"
    description: str = "Use this for custom operations"
    args_schema: Type[BaseModel] = CustomToolInput

    def _run(self, query: str) -> str:
        return f"Processed: {query}"
