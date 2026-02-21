"""Tool to run the test suite and return stdout, stderr, and exit code."""
import subprocess
from pathlib import Path

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class RunTestsToolInput(BaseModel):
    """Input schema for RunTestsTool."""

    cwd: str = Field(
        default=".",
        description="Working directory (repo root) where to run the test command.",
    )
    command: str = Field(
        default="pytest -v --tb=short 2>&1",
        description="Shell command to run tests (e.g. 'pytest -v', 'npm test', 'cargo test').",
    )


class RunTestsTool(BaseTool):
    """Run the test suite and return output and exit code for the Tester agent to interpret."""

    name: str = "run_tests"
    description: str = (
        "Run the test suite in the given directory. Returns stdout, stderr, and exit code. "
        "Use this to execute pytest, npm test, cargo test, or similar."
    )
    args_schema: Type[BaseModel] = RunTestsToolInput

    def _run(self, cwd: str = ".", command: str = "pytest -v --tb=short 2>&1") -> str:
        base = Path(cwd).resolve()
        if not base.exists():
            return f"Error: directory does not exist: {base}"
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=str(base),
                capture_output=True,
                text=True,
                timeout=300,
            )
            out = result.stdout or ""
            err = result.stderr or ""
            combined = f"STDOUT:\n{out}\n\nSTDERR:\n{err}\n\nExit code: {result.returncode}"
            return combined
        except subprocess.TimeoutExpired:
            return "Error: test run timed out after 300 seconds."
        except Exception as e:
            return f"Error running tests: {e}"
