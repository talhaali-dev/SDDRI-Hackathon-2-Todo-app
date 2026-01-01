"""TodoService - Business logic for task management."""

from typing import List, Dict
from src.models.task import Task
from src.models.exceptions import ValidationError, TaskNotFoundError


class TodoService:
    """Service layer for managing todo tasks.

    Implements in-memory storage using:
    - tasks_by_id: dict for O(1) lookups by ID
    - tasks_ordered: list for maintaining creation order
    """

    def __init__(self):
        """Initialize storage structures and ID counter."""
        self.tasks_by_id: Dict[int, Task] = {}
        self.tasks_ordered: List[Task] = []
        self.next_task_id: int = 1

    def add_task(self, description: str) -> Task:
        """Add a new task to the list.

        Args:
            description: Task description (1-500 characters)

        Returns:
            Created Task object

        Raises:
            ValidationError: If description is invalid
        """
        # Create task with validation
        task = Task(id=self.next_task_id, description=description)
        task.validate_description()

        # Add to both storage structures
        self.tasks_by_id[task.id] = task
        self.tasks_ordered.append(task)

        # Increment ID counter
        self.next_task_id += 1

        return task

    def list_tasks(self) -> List[Task]:
        """List all tasks in creation order.

        Returns:
            List of Task objects in creation order
        """
        return self.tasks_ordered.copy()

    def _get_task_by_id(self, task_id: int) -> Task:
        """Get a task by ID.

        Args:
            task_id: Unique identifier for the task

        Returns:
            Task object

        Raises:
            TaskNotFoundError: If task_id does not exist
        """
        if task_id not in self.tasks_by_id:
            raise TaskNotFoundError(
                f"Error: Task with ID {task_id} not found. "
                f"Please verify the task ID and try again."
            )
        return self.tasks_by_id[task_id]

    def mark_complete(self, task_id: int) -> None:
        """Mark a task as complete.

        Args:
            task_id: Unique identifier for the task

        Raises:
            TaskNotFoundError: If task_id does not exist
        """
        task = self._get_task_by_id(task_id)
        task.is_complete = True

    def mark_incomplete(self, task_id: int) -> None:
        """Mark a task as incomplete.

        Args:
            task_id: Unique identifier for the task

        Raises:
            TaskNotFoundError: If task_id does not exist
        """
        task = self._get_task_by_id(task_id)
        task.is_complete = False

    def update_task(self, task_id: int, new_description: str) -> None:
        """Update a task's description.

        Args:
            task_id: Unique identifier for the task
            new_description: New task description (1-500 characters)

        Raises:
            TaskNotFoundError: If task_id does not exist
            ValidationError: If new_description is invalid
        """
        # Validate new description first
        if not new_description or len(new_description.strip()) == 0:
            raise ValidationError(
                "Error: Description cannot be empty. Please provide a task description."
            )

        if len(new_description) > 500:
            raise ValidationError(
                f"Error: Description exceeds maximum length of 500 characters. "
                f"Current length: {len(new_description)}."
            )

        # Get task and update description
        task = self._get_task_by_id(task_id)
        task.description = new_description

    def delete_task(self, task_id: int) -> None:
        """Delete a task from the list.

        Args:
            task_id: Unique identifier for the task

        Raises:
            TaskNotFoundError: If task_id does not exist
        """
        if task_id not in self.tasks_by_id:
            raise TaskNotFoundError(
                f"Error: Task with ID {task_id} not found. "
                f"Please verify the task ID and try again."
            )

        # Get task to remove from ordered list
        task = self.tasks_by_id[task_id]

        # Remove from both storage structures
        del self.tasks_by_id[task_id]
        self.tasks_ordered.remove(task)
