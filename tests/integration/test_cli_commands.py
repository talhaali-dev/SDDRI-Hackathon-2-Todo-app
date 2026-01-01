"""Integration tests for CLI commands."""

import unittest
from src.cli.menu import CommandMenu
from src.services.todo_service import TodoService


class TestCLICommands(unittest.TestCase):
    """Test cases for CLI command integration."""

    def setUp(self):
        """Set up fresh service and command menu for each test."""
        self.service = TodoService()
        self.menu = CommandMenu(self.service)

    def test_add_command(self):
        """T016: Test 'add' command integration."""
        result = self.menu.execute_command("add", ["Buy groceries"])
        self.assertIsNotNone(result)
        self.assertIn("Task created", result)
        self.assertIn("[1]", result)
        self.assertIn("Buy groceries", result)

    def test_list_command_with_tasks(self):
        """T017: Test 'list' command with tasks."""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")

        result = self.menu.execute_command("list", [])
        self.assertIn("Task 1", result)
        self.assertIn("Task 2", result)
        self.assertIn("[1]", result)
        self.assertIn("[2]", result)

    def test_list_command_empty(self):
        """T018: Test 'list' command with empty list."""
        result = self.menu.execute_command("list", [])
        self.assertIn("no tasks", result.lower())

    # User Story 2 Tests (TDD - Written FIRST, verify FAIL)

    def test_complete_command(self):
        """T034: Test 'complete' command integration."""
        task = self.service.add_task("Buy groceries")

        result = self.menu.execute_command("complete", [str(task.id)])
        self.assertIn("marked as complete", result.lower())
        self.assertIn(str(task.id), result)

        # Verify task is actually complete
        updated_task = self.service.tasks_by_id[task.id]
        self.assertTrue(updated_task.is_complete)

    def test_uncomplete_command(self):
        """T035: Test 'uncomplete' command integration."""
        task = self.service.add_task("Buy groceries")
        self.service.mark_complete(task.id)

        result = self.menu.execute_command("uncomplete", [str(task.id)])
        self.assertIn("marked as incomplete", result.lower())
        self.assertIn(str(task.id), result)

        # Verify task is actually incomplete
        updated_task = self.service.tasks_by_id[task.id]
        self.assertFalse(updated_task.is_complete)

    # User Story 4 Tests (TDD - Written FIRST, verify FAIL)

    def test_edit_command(self):
        """T058: Test 'edit' command integration."""
        task = self.service.add_task("Buy groceries")

        result = self.menu.execute_command("edit", [str(task.id), "Buy groceries and milk"])
        self.assertIn("updated", result.lower())
        self.assertIn(str(task.id), result)

        # Verify description is actually updated
        updated_task = self.service.tasks_by_id[task.id]
        self.assertEqual(updated_task.description, "Buy groceries and milk")

    # User Story 5 Tests (TDD - Written FIRST, verify FAIL)

    def test_delete_command(self):
        """T064: Test 'delete' command integration."""
        task = self.service.add_task("Buy groceries")
        self.assertEqual(len(self.service.list_tasks()), 1)

        result = self.menu.execute_command("delete", [str(task.id)])
        self.assertIn("deleted", result.lower())
        self.assertIn(str(task.id), result)

        # Verify task is actually deleted
        self.assertEqual(len(self.service.list_tasks()), 0)
        self.assertNotIn(task.id, self.service.tasks_by_id)


if __name__ == "__main__":
    unittest.main()
