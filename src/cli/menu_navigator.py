"""Menu-based navigation for Todo CLI."""

from src.services.todo_service import TodoService
from src.ui.formatter import TaskFormatter
from src.models.exceptions import ValidationError, TaskNotFoundError


class MenuNavigator:
    """Handles menu-based navigation for task management.

    Provides numbered menu interface for all task operations.
    """

    def __init__(self, service: TodoService):
        """Initialize menu navigator with TodoService.

        Args:
            service: TodoService instance for task operations
        """
        self.service = service
        self.formatter = TaskFormatter()

    def display_menu(self) -> None:
        """Display the main menu with 6 numbered options."""
        print("=" * 40)
        print("         TODO MENU")
        print("=" * 40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Toggle Complete")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        print("=" * 40)

    def get_selection(self) -> str:
        """Get menu selection from user.

        Returns:
            User's menu selection (numeric or text-based)
        """
        choice = input("Enter choice: ").strip()
        return choice

    def route_to_action(self, choice: str) -> bool:
        """Route menu selection to appropriate action.

        Args:
            choice: User's menu selection (1-6 or text alias)

        Returns:
            True to continue menu loop, False to exit
        """
        # Normalize choice
        choice_lower = choice.lower()

        # Map selections to actions
        if choice in ("1", "add"):
            self.handle_add_task()
            return True
        elif choice in ("2", "view"):
            self.handle_view_tasks()
            return True
        elif choice in ("3", "toggle"):
            self.handle_toggle_complete()
            return True
        elif choice in ("4", "update"):
            self.handle_update_task()
            return True
        elif choice in ("5", "delete"):
            self.handle_delete_task()
            return True
        elif choice in ("6", "exit", "quit"):
            self.handle_exit()
            return False
        else:
            print("Error: Invalid menu option. Please enter a number between 1 and 6.")
            return True

    def start(self) -> None:
        """Start the main menu loop.

        Entry point for menu-based navigation.
        Displays menu, gets input, routes action, repeats until exit.
        """
        while True:
            try:
                # Display menu
                self.display_menu()

                # Get user selection
                choice = self.get_selection()

                # Route to action
                should_continue = self.route_to_action(choice)

                # Exit if requested
                if not should_continue:
                    break

            except KeyboardInterrupt:
                # Handle Ctrl+C gracefully
                print("\n\nExiting Todo CLI...")
                break

    def handle_add_task(self) -> None:
        """Handle Add Task option (Option 1).

        Prompts for description, validates, creates task, displays confirmation.
        """
        description = self.get_task_description()
        if description:
            try:
                task = self.service.add_task(description)
                print(f"Task {task.id} created.")
            except ValidationError as e:
                print(str(e))

    def handle_view_tasks(self) -> None:
        """Handle View Tasks option (Option 2).

        Displays all tasks with status indicators.
        Prompts user to press Enter to continue.
        """
        tasks = self.service.list_tasks()

        if not tasks:
            print("\nNo tasks found. Add a task to get started!")
        else:
            print()
            print(self.formatter.format_task_list(tasks))

        # Prompt to continue
        input("\nPress Enter to continue...")

    def handle_toggle_complete(self) -> None:
        """Handle Toggle Complete option (Option 3).

        Prompts for task ID, toggles completion status, displays confirmation.
        """
        task_id = self.get_task_id_input()
        if task_id is None:
            return

        try:
            task = self.service._get_task_by_id(task_id)

            # Toggle based on current status
            if task.is_complete:
                self.service.mark_incomplete(task_id)
                print(f"Task {task_id} marked as incomplete.")
            else:
                self.service.mark_complete(task_id)
                print(f"Task {task_id} marked as complete.")

        except TaskNotFoundError as e:
            print(str(e))

    def handle_update_task(self) -> None:
        """Handle Update Task option (Option 4).

        Prompts for task ID and new description, updates task, displays confirmation.
        """
        # Get task ID
        task_id = self.get_task_id_input()
        if task_id is None:
            return

        # Get new description
        new_description = self.get_task_description("Enter new description: ")
        if not new_description:
            return

        try:
            self.service.update_task(task_id, new_description)
            print(f"Task {task_id} updated.")
        except (TaskNotFoundError, ValidationError) as e:
            print(str(e))

    def handle_delete_task(self) -> None:
        """Handle Delete Task option (Option 5).

        Prompts for task ID, deletes task, displays confirmation.
        """
        task_id = self.get_task_id_input()
        if task_id is None:
            return

        try:
            self.service.delete_task(task_id)
            print(f"Task {task_id} deleted.")
        except TaskNotFoundError as e:
            print(str(e))

    def handle_exit(self) -> None:
        """Handle Exit option (Option 6).

        Displays goodbye message (terminates application).
        """
        print("\nThank you for using Todo CLI!")

    def get_task_description(self, prompt: str = "Enter task description: ") -> str | None:
        """Get and validate task description from user.

        Args:
            prompt: Input prompt text

        Returns:
            Validated description or None if cancelled
        """
        while True:
            description = input(prompt).strip()

            # Check for empty input
            if not description:
                print("Error: Description cannot be empty. Please provide a task description.")
                continue

            # Check length
            if len(description) > 500:
                print(f"Error: Description exceeds maximum length of 500 characters. Current length: {len(description)}.")
                continue

            return description

    def get_task_id_input(self) -> int | None:
        """Get and validate task ID from user.

        Returns:
            Validated task ID or None if invalid
        """
        while True:
            user_input = input("Enter task ID: ").strip()

            if not user_input:
                print("Error: No task ID provided. Please enter a task ID.")
                return None

            try:
                return int(user_input)
            except ValueError:
                print("Error: Task ID must be a number. Please enter a valid numeric ID.")
                return None
