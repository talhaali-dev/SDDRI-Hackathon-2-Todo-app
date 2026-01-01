"""Integration tests for Interactive Mode."""

import unittest
from unittest.mock import Mock, patch, MagicMock
from src.services.todo_service import TodoService


class TestInteractiveMode(unittest.TestCase):
    """Test cases for Interactive Mode navigation and key handling."""

    def setUp(self):
        """Set up fresh service with sample tasks."""
        self.service = TodoService()
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        self.service.add_task("Task 3")

    # User Story 3 Tests (TDD - Written FIRST, verify FAIL)

    @patch('src.cli.interactive.curses')
    def test_handle_key_up_navigation(self, mock_curses):
        """T041: Test arrow up key decrements selected index."""
        from src.cli.interactive import InteractiveMode

        mode = InteractiveMode(self.service)
        mode.selected_index = 2  # Start at third task

        mode.handle_key_up()
        self.assertEqual(mode.selected_index, 1)  # Should move to second task

        mode.handle_key_up()
        self.assertEqual(mode.selected_index, 0)  # Should move to first task

    @patch('src.cli.interactive.curses')
    def test_handle_key_down_navigation(self, mock_curses):
        """T042: Test arrow down key increments selected index."""
        from src.cli.interactive import InteractiveMode

        mode = InteractiveMode(self.service)
        mode.selected_index = 0  # Start at first task

        mode.handle_key_down()
        self.assertEqual(mode.selected_index, 1)  # Should move to second task

        mode.handle_key_down()
        self.assertEqual(mode.selected_index, 2)  # Should move to third task

    @patch('src.cli.interactive.curses')
    def test_handle_spacebar_toggle(self, mock_curses):
        """T043: Test spacebar toggles task completion status."""
        from src.cli.interactive import InteractiveMode

        mode = InteractiveMode(self.service)
        tasks = self.service.list_tasks()

        # Initially incomplete
        mode.selected_index = 0
        self.assertFalse(tasks[0].is_complete)

        # Toggle to complete
        mode.handle_spacebar()
        self.assertTrue(tasks[0].is_complete)

        # Toggle back to incomplete
        mode.handle_spacebar()
        self.assertFalse(tasks[0].is_complete)

    @patch('src.cli.interactive.curses')
    def test_circular_navigation(self, mock_curses):
        """T044: Test circular navigation (wrap around)."""
        from src.cli.interactive import InteractiveMode

        mode = InteractiveMode(self.service)
        tasks = self.service.list_tasks()
        mode.selected_index = 0

        # Navigate down past the last task
        mode.selected_index = len(tasks) - 1  # Last task
        mode.handle_key_down()
        self.assertEqual(mode.selected_index, 0)  # Should wrap to first task

        # Navigate up past the first task
        mode.handle_key_up()
        self.assertEqual(mode.selected_index, len(tasks) - 1)  # Should wrap to last task

    @patch('src.cli.interactive.curses')
    def test_entering_exiting_interactive_mode(self, mock_curses):
        """T045: Test entering and exiting interactive mode cleanly."""
        from src.cli.interactive import InteractiveMode

        mode = InteractiveMode(self.service)

        # Simulate curses setup
        mock_stdscr = MagicMock()
        mock_curses.initscr.return_value = mock_stdscr
        mock_curses.wrapper.side_effect = lambda func: func(mock_stdscr)

        # Should handle escape to exit
        mode.running = True
        mode.handle_escape()
        self.assertFalse(mode.running)  # Should exit


if __name__ == "__main__":
    unittest.main()
