#!/usr/bin/env python
# src/crew/main.py
"""
Run the continuous improvement crew (sync by default).
Inputs: target_repo, focus_area, improvement_goals.
For async or daemon mode, use crew.runner.run_async / run_daemon.
"""
import argparse
import os

from crew.runner import run_sync, run_async, run_daemon


def run():
    """Run the continuous improvement crew once (sync)."""
    os.makedirs("output", exist_ok=True)

    parser = argparse.ArgumentParser(description="Continuous improvement crew")
    parser.add_argument(
        "--target-repo",
        default=".",
        help="Path to the target repo (default: current directory)",
    )
    parser.add_argument(
        "--focus-area",
        default="main package",
        help="Focus area for improvements (e.g. 'auth module')",
    )
    parser.add_argument(
        "--improvement-goals",
        default="increase test coverage and fix any lint issues",
        help="Goals for this run (e.g. 'refactor X, add tests for Y')",
    )
    parser.add_argument(
        "--async",
        dest="use_async",
        action="store_true",
        help="Use async kickoff (one run, non-blocking)",
    )
    parser.add_argument(
        "--daemon",
        action="store_true",
        help="Run as daemon: crew every N seconds until interrupted",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=3600,
        help="Daemon interval in seconds (default: 3600)",
    )
    args = parser.parse_args()

    inputs = {
        "target_repo": args.target_repo,
        "focus_area": args.focus_area,
        "improvement_goals": args.improvement_goals,
    }

    if args.daemon:
        run_daemon(interval_seconds=args.interval, inputs=inputs, use_async=args.use_async)
        return

    if args.use_async:
        import asyncio
        result = asyncio.run(run_async(inputs=inputs))
    else:
        result = run_sync(inputs=inputs)

    print("\n\n=== CREW RESULT ===\n\n")
    print(result)


if __name__ == "__main__":
    run()
