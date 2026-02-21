"""
Minimal FastAPI app for deploying the CrewAI crew on Render.
GET / = health, POST /run = run crew with optional JSON body.
"""
from fastapi import FastAPI
from pydantic import BaseModel

from crew.runner import run_sync

app = FastAPI(title="Agent Frameworks – CrewAI API")


class RunInput(BaseModel):
    target_repo: str = "."
    focus_area: str = "main package"
    improvement_goals: str = "increase test coverage and fix any lint issues"


@app.get("/")
def health():
    return {"status": "ok", "service": "crewai-crew"}


@app.post("/run")
def run_crew(body: RunInput | None = None):
    """Run the continuous improvement crew once. May take a while; Render request timeout applies."""
    inputs = body.model_dump() if body else None
    result = run_sync(inputs=inputs)
    return {"status": "completed", "result": result}
