"""Unit tests for Task model."""

import unittest
from src.models.task import Task
from src.models.exceptions import ValidationError


class TestTaskModel(unittest.TestCase):
    """Test cases for Task model validation and creation."""

    def test_task_validation_empty_description(self):
        """T010: Test that empty description raises ValidationError."""
        with self.assertRaises(ValidationError) as context:
            task = Task(id=1, description="")
            task.validate_description()
        self.assertIn("empty", str(context.exception).lower())

    def test_task_validation_description_too_long(self):
        """T011: Test that description >500 chars raises ValidationError."""
        long_description = "a" * 501
        with self.assertRaises(ValidationError) as context:
            task = Task(id=1, description=long_description)
            task.validate_description()
        self.assertIn("500", str(context.exception))

    def test_task_creation_with_valid_description(self):
        """T012: Test Task creation with valid description."""
        task = Task(id=1, description="Buy groceries")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Buy groceries")
        self.assertFalse(task.is_complete)
        self.assertIsNotNone(task.created_at)


if __name__ == "__main__":
    unittest.main()
