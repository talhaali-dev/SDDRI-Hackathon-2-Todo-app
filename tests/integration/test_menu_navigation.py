"""Integration tests for menu-based navigation."""

import pytest
from io import StringIO
from unittest.mock import patch, Mock
from src.services.todo_service import TodoService
from src.cli.menu_navigator import MenuNavigator


class TestMenuDisplay:
    """Tests for menu display functionality (T006)."""

    def test_menu_displays_six_options(self):
        """Test that menu displays all 6 numbered options (T006)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            navigator.display_menu()
            output = fake_out.getvalue()

        # Verify menu structure
        assert "==========" in output
        assert "TODO MENU" in output
        assert "1. Add Task" in output
        assert "2. View Tasks" in output
        assert "3. Toggle Complete" in output
        assert "4. Update Task" in output
        assert "5. Delete Task" in output
        assert "6. Exit" in output


class TestNumericMenuSelection:
    """Tests for numeric menu selection (T007)."""

    def test_selection_1_routes_to_add_task(self):
        """Test that numeric selection '1' routes to Add Task (T007)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        with patch('builtins.input', return_value="Test Task"):
            with patch.object(navigator, 'get_task_description', return_value="Test Task"):
                result = navigator.route_to_action("1")

        assert result is True  # Should continue menu loop
        tasks = service.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].description == "Test Task"


class TestTextMenuSelection:
    """Tests for text-based menu selection (T008)."""

    def test_selection_add_routes_to_add_task(self):
        """Test that text selection 'add' routes to Add Task (T008)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        with patch.object(navigator, 'get_task_description', return_value="Test Task"):
            result = navigator.route_to_action("add")

        assert result is True  # Should continue menu loop
        tasks = service.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].description == "Test Task"


class TestEmptyDescriptionValidation:
    """Tests for empty description rejection (T009)."""

    def test_empty_description_rejected_with_error_message(self):
        """Test that empty description is rejected with error message (T009)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        # First attempt: empty description
        with patch('builtins.input', side_effect=["", "Valid Task"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                description = navigator.get_task_description()
                output = fake_out.getvalue()

        # Should get valid description on second attempt
        assert description == "Valid Task"

        # Should show error message for empty input
        assert "Error: Description cannot be empty" in output


class TestLongDescriptionValidation:
    """Tests for >500 character description rejection (T010)."""

    def test_description_over_500_chars_rejected(self):
        """Test that description >500 characters is rejected with error message (T010)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        # Create description that exceeds 500 characters
        long_description = "a" * 501

        with patch('builtins.input', side_effect=[long_description, "Valid Task"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                description = navigator.get_task_description()
                output = fake_out.getvalue()

        # Should get valid description on second attempt
        assert description == "Valid Task"

        # Should show error message about length
        assert "Error: Description exceeds maximum length of 500 characters" in output
        assert "Current length: 501" in output


class TestSuccessfulTaskCreation:
    """Tests for successful task creation and menu redisplay (T011)."""

    def test_successful_task_creation_displays_confirmation(self):
        """Test that successful task creation displays confirmation and allows menu redisplay (T011)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        with patch('builtins.input', return_value="Buy groceries"):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_add_task()
                output = fake_out.getvalue()

        # Should display confirmation message
        assert "Task 1 created." in output

        # Task should be in service
        tasks = service.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].description == "Buy groceries"

        # Should be able to add another task (menu redisplay simulation)
        with patch('builtins.input', return_value="Write documentation"):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_add_task()
                output = fake_out.getvalue()

        assert "Task 2 created." in output
        tasks = service.list_tasks()
        assert len(tasks) == 2


class TestViewTasks:
    """Tests for view tasks functionality (User Story 2)."""

    def test_view_tasks_displays_all_tasks(self):
        """Test that View Tasks displays all tasks with status (T015)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        # Add some tasks
        service.add_task("Task 1")
        service.add_task("Task 2")

        with patch('builtins.input', return_value=""):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_view_tasks()
                output = fake_out.getvalue()

        # Should display both tasks
        assert "[1]" in output
        assert "Task 1" in output
        assert "[2]" in output
        assert "Task 2" in output

    def test_view_empty_task_list_displays_friendly_message(self):
        """Test that empty task list displays friendly message (T016)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        with patch('builtins.input', return_value=""):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_view_tasks()
                output = fake_out.getvalue()

        # Should show empty message
        assert "No tasks found" in output
        assert "Add a task to get started" in output


class TestToggleComplete:
    """Tests for toggle complete functionality (User Story 2)."""

    def test_toggle_complete_marks_task_complete(self):
        """Test that toggle complete marks task as complete (T017)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        # Add a task
        task = service.add_task("Test Task")

        with patch('builtins.input', return_value="1"):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_toggle_complete()
                output = fake_out.getvalue()

        # Should show confirmation
        assert "Task 1 marked as complete." in output

        # Task should be complete
        tasks = service.list_tasks()
        assert tasks[0].is_complete is True

    def test_toggle_incomplete_marks_task_incomplete(self):
        """Test that toggle can mark complete task as incomplete (T018)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        # Add and complete a task
        task = service.add_task("Test Task")
        service.mark_complete(task.id)

        with patch('builtins.input', return_value="1"):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_toggle_complete()
                output = fake_out.getvalue()

        # Should show incomplete confirmation
        assert "Task 1 marked as incomplete." in output

        # Task should be incomplete
        tasks = service.list_tasks()
        assert tasks[0].is_complete is False

    def test_toggle_with_invalid_id_shows_error(self):
        """Test that toggle with invalid task ID shows error (T019)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        with patch('builtins.input', return_value="999"):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_toggle_complete()
                output = fake_out.getvalue()

        # Should show error message
        assert "Error: Task with ID 999 not found" in output

    def test_toggle_with_non_numeric_id_shows_error(self):
        """Test that toggle with non-numeric ID shows error (T020)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        with patch('builtins.input', return_value="abc"):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_toggle_complete()
                output = fake_out.getvalue()

        # Should show error message
        assert "Error: Task ID must be a number" in output


class TestUpdateTask:
    """Tests for update task functionality (User Story 3)."""

    def test_update_task_changes_description(self):
        """Test that update task changes description (T025)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        # Add a task
        task = service.add_task("Original description")

        with patch('builtins.input', side_effect=["1", "Updated description"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_update_task()
                output = fake_out.getvalue()

        # Should show confirmation
        assert "Task 1 updated." in output

        # Task should have new description
        tasks = service.list_tasks()
        assert tasks[0].description == "Updated description"

    def test_update_with_empty_description_rejected(self):
        """Test that update with empty description is rejected (T026)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        # Add a task
        task = service.add_task("Original description")

        # Try to update with empty description
        with patch('builtins.input', side_effect=["1", "", "Valid description"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_update_task()
                output = fake_out.getvalue()

        # Should show error and then success
        assert "Error: Description cannot be empty" in output
        assert "Task 1 updated." in output

    def test_update_with_invalid_id_shows_error(self):
        """Test that update with invalid ID shows error (T027)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        with patch('builtins.input', side_effect=["999", "New description"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_update_task()
                output = fake_out.getvalue()

        # Should show error message
        assert "Error: Task with ID 999 not found" in output


class TestDeleteTask:
    """Tests for delete task functionality (User Story 3)."""

    def test_delete_task_removes_from_list(self):
        """Test that delete task removes task from list (T028)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        # Add tasks
        service.add_task("Task 1")
        service.add_task("Task 2")

        with patch('builtins.input', return_value="1"):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_delete_task()
                output = fake_out.getvalue()

        # Should show confirmation
        assert "Task 1 deleted." in output

        # Task should be removed
        tasks = service.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].description == "Task 2"

    def test_delete_last_task_results_in_empty_list(self):
        """Test that deleting last task results in empty list (T029)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        # Add a single task
        service.add_task("Only task")

        with patch('builtins.input', return_value="1"):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_delete_task()
                output = fake_out.getvalue()

        # Should show confirmation
        assert "Task 1 deleted." in output

        # List should be empty
        tasks = service.list_tasks()
        assert len(tasks) == 0

    def test_delete_with_invalid_id_shows_error(self):
        """Test that delete with invalid ID shows error (T030)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        with patch('builtins.input', return_value="999"):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.handle_delete_task()
                output = fake_out.getvalue()

        # Should show error message
        assert "Error: Task with ID 999 not found" in output


class TestExit:
    """Tests for exit functionality (User Story 4)."""

    def test_exit_displays_goodbye_message(self):
        """Test that exit displays goodbye message (T034)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            navigator.handle_exit()
            output = fake_out.getvalue()

        # Should show goodbye message
        assert "Thank you for using Todo CLI!" in output


class TestErrorHandling:
    """Tests for error handling (User Story 4)."""

    def test_invalid_menu_option_shows_error(self):
        """Test that invalid menu option shows error (T035)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = navigator.route_to_action("99")
            output = fake_out.getvalue()

        # Should show error and continue
        assert "Error: Invalid menu option" in output
        assert result is True

    def test_keyboard_interrupt_handled_gracefully(self):
        """Test that KeyboardInterrupt (Ctrl+C) is handled gracefully (T037)."""
        service = TodoService()
        navigator = MenuNavigator(service)

        # Mock start() to raise KeyboardInterrupt immediately
        with patch.object(navigator, 'display_menu', side_effect=KeyboardInterrupt):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                navigator.start()
                output = fake_out.getvalue()

        # Should show graceful exit message
        assert "Exiting Todo CLI..." in output
