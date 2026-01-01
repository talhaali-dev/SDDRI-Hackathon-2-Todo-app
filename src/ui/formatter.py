"""Task formatting and display logic."""

from typing import List
from src.models.task import Task


class TaskFormatter:
    """Formats tasks for display in the terminal."""

    @staticmethod
    def format_task_list(tasks: List[Task]) -> str:
        """Format a list of tasks for display.

        Args:
            tasks: List of Task objects to format

        Returns:
            Formatted string with all tasks
        """
        if not tasks:
            return "No tasks in your list. Use 'add <description>' to create one."

        lines = []
        for task in tasks:
            status = "[✓]" if task.is_complete else "[ ]"
            lines.append(f"{status} [{task.id}] {task.description}")

        return "\n".join(lines)

    @staticmethod
    def format_task_created(task: Task) -> str:
        """Format confirmation message for created task.

        Args:
            task: Created Task object

        Returns:
            Success message
        """
        return f"✓ Task created: [{task.id}] {task.description}"
