"""
Run the continuous improvement crew: sync, async, or daemon mode.
Uses inputs: target_repo, focus_area, improvement_goals.
"""
import asyncio
import time
from typing import Any

from crew.crew import ContinuousImprovementCrew


def _default_inputs() -> dict[str, Any]:
    return {
        "target_repo": ".",
        "focus_area": "main package",
        "improvement_goals": "increase test coverage and fix any lint issues",
    }


def run_sync(inputs: dict[str, Any] | None = None) -> str:
    """Run the crew once, synchronously. Returns the final output."""
    inputs = inputs or _default_inputs()
    crew_instance = ContinuousImprovementCrew().crew()
    result = crew_instance.kickoff(inputs=inputs)
    return result.raw if hasattr(result, "raw") else str(result)


async def run_async(inputs: dict[str, Any] | None = None) -> str:
    """Run the crew once, asynchronously. Returns the final output."""
    inputs = inputs or _default_inputs()
    crew_instance = ContinuousImprovementCrew().crew()
    result = await crew_instance.kickoff_async(inputs=inputs)
    return result.raw if hasattr(result, "raw") else str(result)


def run_daemon(
    interval_seconds: float = 3600,
    inputs: dict[str, Any] | None = None,
    use_async: bool = False,
) -> None:
    """
    Long-running daemon: run the crew every interval_seconds.
    If use_async is True, uses kickoff_async; otherwise kickoff (blocking).
    """
    inputs = inputs or _default_inputs()

    while True:
        try:
            crew_instance = ContinuousImprovementCrew().crew()
            if use_async:
                result = asyncio.run(crew_instance.kickoff_async(inputs=inputs))
            else:
                result = crew_instance.kickoff(inputs=inputs)
            out = result.raw if hasattr(result, "raw") else str(result)
            print(f"[Crew run finished]\n{out[:500]}...")
        except Exception as e:
            print(f"[Crew run error] {e}")
        print(f"[Sleeping {interval_seconds}s until next run]")
        time.sleep(interval_seconds)
