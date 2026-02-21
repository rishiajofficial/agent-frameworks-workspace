# src/crew/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from crew.tools import FileReadTool, FileWriteTool, RunTestsTool, RunShellTool


@CrewBase
class ContinuousImprovementCrew:
    """Hierarchical crew for continuous software improvement: Manager + Developer, Tester, Code Reviewer."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def developer(self) -> Agent:
        return Agent(
            config=self.agents_config["developer"],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            tools=[
                FileReadTool(),
                FileWriteTool(),
                RunShellTool(),
            ],
        )

    @agent
    def tester(self) -> Agent:
        return Agent(
            config=self.agents_config["tester"],
            verbose=True,
            tools=[
                RunTestsTool(),
                FileReadTool(),
            ],
        )

    @agent
    def code_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config["code_reviewer"],
            verbose=True,
            tools=[
                FileReadTool(),
            ],
        )

    @task
    def improvement_task(self) -> Task:
        return Task(config=self.tasks_config["improvement_task"])

    @task
    def test_suite_task(self) -> Task:
        return Task(config=self.tasks_config["test_suite_task"])

    @task
    def review_task(self) -> Task:
        return Task(config=self.tasks_config["review_task"])

    @crew
    def crew(self) -> Crew:
        """Creates the continuous improvement crew with hierarchical process and manager."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_llm="gpt-4o",
            verbose=True,
        )
