"""Custom exception classes for the Todo CLI application."""


class TodoError(Exception):
    """Base exception for all Todo application errors."""
    pass


class ValidationError(TodoError):
    """Raised when input validation fails."""
    pass


class TaskNotFoundError(TodoError):
    """Raised when a requested task ID does not exist."""
    pass


class EmptyTaskListError(TodoError):
    """Raised when operations require tasks but the list is empty."""
    pass
