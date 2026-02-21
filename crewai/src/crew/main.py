#!/usr/bin/env python
# src/crew/main.py
import os
from crew.crew import ResearchCrew


def run():
    """Run the research crew."""
    os.makedirs("output", exist_ok=True)

    inputs = {
        "topic": "Artificial Intelligence in Healthcare",
    }

    result = ResearchCrew().crew().kickoff(inputs=inputs)

    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)
    print("\n\nReport saved to output/report.md")


if __name__ == "__main__":
    run()
