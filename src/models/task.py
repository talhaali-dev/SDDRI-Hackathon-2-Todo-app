"""Task model for the Todo CLI application."""

from dataclasses import dataclass
from time import time
from src.models.exceptions import ValidationError


@dataclass
class Task:
    """Represents a single task in the todo list.

    Attributes:
        id: Unique identifier for the task (positive integer)
        description: Task description (1-500 characters)
        is_complete: Whether the task is marked as complete
        created_at: Unix timestamp when the task was created
    """

    id: int
    description: str
    is_complete: bool = False
    created_at: int = None

    def __post_init__(self):
        """Initialize created_at if not provided."""
        if self.created_at is None:
            self.created_at = int(time())

    def validate_description(self):
        """Validate task description.

        Raises:
            ValidationError: If description is empty or exceeds 500 characters
        """
        if not self.description or len(self.description.strip()) == 0:
            raise ValidationError("Error: Description cannot be empty. Please provide a task description.")

        if len(self.description) > 500:
            raise ValidationError(
                f"Error: Description exceeds maximum length of 500 characters. "
                f"Current length: {len(self.description)}."
            )
