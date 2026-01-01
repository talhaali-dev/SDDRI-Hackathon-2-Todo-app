"""Unit tests for TodoService."""

import unittest
from src.services.todo_service import TodoService
from src.models.exceptions import ValidationError, TaskNotFoundError, EmptyTaskListError


class TestTodoService(unittest.TestCase):
    """Test cases for TodoService operations."""

    def setUp(self):
        """Set up fresh TodoService instance for each test."""
        self.service = TodoService()

    def test_add_task(self):
        """T013: Test adding a task to the service."""
        task = self.service.add_task("Buy groceries")
        self.assertIsNotNone(task)
        self.assertEqual(task.description, "Buy groceries")
        self.assertEqual(task.id, 1)
        self.assertFalse(task.is_complete)

    def test_list_tasks_empty(self):
        """T014: Test listing tasks when list is empty."""
        tasks = self.service.list_tasks()
        self.assertEqual(len(tasks), 0)
        self.assertIsInstance(tasks, list)

    def test_list_tasks_with_multiple_tasks(self):
        """T015: Test listing tasks with multiple tasks."""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        self.service.add_task("Task 3")

        tasks = self.service.list_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].description, "Task 1")
        self.assertEqual(tasks[1].description, "Task 2")
        self.assertEqual(tasks[2].description, "Task 3")

    # User Story 2 Tests (TDD - Written FIRST, verify FAIL)

    def test_mark_complete(self):
        """T030: Test marking a task as complete."""
        task = self.service.add_task("Buy groceries")
        self.assertFalse(task.is_complete)

        self.service.mark_complete(task.id)
        updated_task = self.service.tasks_by_id[task.id]
        self.assertTrue(updated_task.is_complete)

    def test_mark_incomplete(self):
        """T031: Test marking a task as incomplete."""
        task = self.service.add_task("Buy groceries")
        self.service.mark_complete(task.id)

        self.service.mark_incomplete(task.id)
        updated_task = self.service.tasks_by_id[task.id]
        self.assertFalse(updated_task.is_complete)

    def test_mark_complete_invalid_id(self):
        """T032: Test marking complete with invalid ID raises TaskNotFoundError."""
        with self.assertRaises(TaskNotFoundError) as context:
            self.service.mark_complete(999)

        self.assertIn("999", str(context.exception))

    def test_mark_complete_idempotent(self):
        """T033: Test marking complete operation is idempotent."""
        task = self.service.add_task("Buy groceries")

        # Mark complete twice
        self.service.mark_complete(task.id)
        self.service.mark_complete(task.id)

        # Should still be complete (no error)
        updated_task = self.service.tasks_by_id[task.id]
        self.assertTrue(updated_task.is_complete)

    # User Story 4 Tests (TDD - Written FIRST, verify FAIL)

    def test_update_task(self):
        """T055: Test updating task description."""
        task = self.service.add_task("Buy groceries")

        self.service.update_task(task.id, "Buy groceries and milk")
        updated_task = self.service.tasks_by_id[task.id]
        self.assertEqual(updated_task.description, "Buy groceries and milk")

    def test_update_task_invalid_id(self):
        """T056: Test update with invalid ID raises TaskNotFoundError."""
        with self.assertRaises(TaskNotFoundError) as context:
            self.service.update_task(999, "New description")

        self.assertIn("999", str(context.exception))

    def test_update_task_empty_description(self):
        """T057: Test update with empty description raises ValidationError."""
        task = self.service.add_task("Buy groceries")

        with self.assertRaises(ValidationError) as context:
            self.service.update_task(task.id, "")

        self.assertIn("empty", str(context.exception).lower())

    # User Story 5 Tests (TDD - Written FIRST, verify FAIL)

    def test_delete_task(self):
        """T061: Test deleting a task."""
        task = self.service.add_task("Buy groceries")
        self.assertEqual(len(self.service.list_tasks()), 1)

        self.service.delete_task(task.id)
        self.assertEqual(len(self.service.list_tasks()), 0)
        self.assertNotIn(task.id, self.service.tasks_by_id)

    def test_delete_task_invalid_id(self):
        """T062: Test delete with invalid ID raises TaskNotFoundError."""
        with self.assertRaises(TaskNotFoundError) as context:
            self.service.delete_task(999)

        self.assertIn("999", str(context.exception))

    def test_delete_last_task(self):
        """T063: Test deleting last task results in empty list."""
        task = self.service.add_task("Only task")

        self.service.delete_task(task.id)

        tasks = self.service.list_tasks()
        self.assertEqual(len(tasks), 0)


if __name__ == "__main__":
    unittest.main()
