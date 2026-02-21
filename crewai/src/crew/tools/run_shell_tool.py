"""Tool to run a shell command (for Developer: build, install, git, etc.)."""
import subprocess
from pathlib import Path

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class RunShellToolInput(BaseModel):
    """Input schema for RunShellTool."""

    command: str = Field(..., description="Shell command to run (e.g. pip install -e ., npm run build).")
    cwd: str = Field(
        default=".",
        description="Working directory where to run the command.",
    )


class RunShellTool(BaseTool):
    """Run a shell command and return stdout, stderr, and exit code."""

    name: str = "run_shell"
    description: str = (
        "Run a shell command in the given directory. Use for builds, installs, git, linters. "
        "Returns combined stdout/stderr and exit code."
    )
    args_schema: Type[BaseModel] = RunShellToolInput

    def _run(self, command: str, cwd: str = ".") -> str:
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
                timeout=120,
            )
            out = result.stdout or ""
            err = result.stderr or ""
            return f"STDOUT:\n{out}\n\nSTDERR:\n{err}\n\nExit code: {result.returncode}"
        except subprocess.TimeoutExpired:
            return "Error: command timed out after 120 seconds."
        except Exception as e:
            return f"Error: {e}"
