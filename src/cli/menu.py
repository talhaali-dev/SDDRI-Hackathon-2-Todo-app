"""Command menu and CLI command handling."""

from typing import List, Optional
from src.services.todo_service import TodoService
from src.ui.formatter import TaskFormatter
from src.models.exceptions import ValidationError, TaskNotFoundError


class CommandMenu:
    """Handles parsing and executing CLI commands."""

    def __init__(self, service: TodoService):
        """Initialize command menu with TodoService.

        Args:
            service: TodoService instance for task operations
        """
        self.service = service
        self.formatter = TaskFormatter()

    def parse_command(self, user_input: str) -> tuple[str, List[str]]:
        """Parse user input into command and arguments.

        Args:
            user_input: Raw user input string

        Returns:
            Tuple of (command_name, arguments_list)
        """
        parts = user_input.strip().split(maxsplit=1)
        if not parts:
            return ("", [])

        command = parts[0].lower()
        args = parts[1].split() if len(parts) > 1 else []

        # Special handling for 'add' command - keep description as single arg
        if command == "add" and len(parts) > 1:
            args = [parts[1]]

        return (command, args)

    def execute_command(self, command: str, args: List[str]) -> Optional[str]:
        """Execute a command with given arguments.

        Args:
            command: Command name
            args: Command arguments

        Returns:
            Command result message or None
        """
        if command == "add":
            return self._handle_add(args)
        elif command == "list":
            return self._handle_list(args)
        elif command == "complete":
            return self._handle_complete(args)
        elif command == "uncomplete":
            return self._handle_uncomplete(args)
        elif command == "interactive":
            return self._handle_interactive(args)
        elif command == "edit":
            return self._handle_edit(args)
        elif command == "delete":
            return self._handle_delete(args)
        elif command == "help":
            return self._handle_help(args)
        elif command in ("exit", "quit"):
            return self._handle_exit(args)
        else:
            return f"Error: Unknown command '{command}'. Type 'help' for available commands."

    def _handle_add(self, args: List[str]) -> str:
        """Handle 'add' command.

        Args:
            args: [description]

        Returns:
            Success or error message
        """
        if not args:
            return "Error: 'add' command requires a description. Usage: add <description>"

        description = args[0]

        try:
            task = self.service.add_task(description)
            return self.formatter.format_task_created(task)
        except ValidationError as e:
            return str(e)

    def _handle_list(self, args: List[str]) -> str:
        """Handle 'list' command.

        Args:
            args: No arguments expected

        Returns:
            Formatted task list
        """
        tasks = self.service.list_tasks()
        return self.formatter.format_task_list(tasks)

    def _handle_complete(self, args: List[str]) -> str:
        """Handle 'complete' command.

        Args:
            args: [task_id]

        Returns:
            Success or error message
        """
        if not args:
            return "Error: 'complete' command requires a task ID. Usage: complete <id>"

        try:
            task_id = int(args[0])
            self.service.mark_complete(task_id)
            return f"Task {task_id} marked as complete."
        except ValueError:
            return f"Error: Invalid task ID '{args[0]}'. Task ID must be a number."
        except TaskNotFoundError as e:
            return str(e)

    def _handle_uncomplete(self, args: List[str]) -> str:
        """Handle 'uncomplete' command.

        Args:
            args: [task_id]

        Returns:
            Success or error message
        """
        if not args:
            return "Error: 'uncomplete' command requires a task ID. Usage: uncomplete <id>"

        try:
            task_id = int(args[0])
            self.service.mark_incomplete(task_id)
            return f"Task {task_id} marked as incomplete."
        except ValueError:
            return f"Error: Invalid task ID '{args[0]}'. Task ID must be a number."
        except TaskNotFoundError as e:
            return str(e)

    def _handle_interactive(self, args: List[str]) -> str:
        """Handle 'interactive' command.

        Args:
            args: No arguments expected

        Returns:
            Message indicating interactive mode has launched
        """
        from src.cli.interactive import InteractiveMode

        mode = InteractiveMode(self.service)
        mode.run()

        return "Exited interactive mode."

    def _handle_edit(self, args: List[str]) -> str:
        """Handle 'edit' command.

        Args:
            args: [task_id, new_description]

        Returns:
            Success or error message
        """
        if len(args) < 2:
            return "Error: 'edit' command requires task ID and new description. Usage: edit <id> <description>"

        try:
            task_id = int(args[0])
            # Join remaining args as description (handles multi-word descriptions)
            new_description = ' '.join(args[1:])
            self.service.update_task(task_id, new_description)
            return f"Task {task_id} updated."
        except ValueError:
            return f"Error: Invalid task ID '{args[0]}'. Task ID must be a number."
        except TaskNotFoundError as e:
            return str(e)
        except ValidationError as e:
            return str(e)

    def _handle_delete(self, args: List[str]) -> str:
        """Handle 'delete' command.

        Args:
            args: [task_id]

        Returns:
            Success or error message
        """
        if not args:
            return "Error: 'delete' command requires a task ID. Usage: delete <id>"

        try:
            task_id = int(args[0])
            self.service.delete_task(task_id)
            return f"Task {task_id} deleted."
        except ValueError:
            return f"Error: Invalid task ID '{args[0]}'. Task ID must be a number."
        except TaskNotFoundError as e:
            return str(e)

    def _handle_help(self, args: List[str]) -> str:
        """Handle 'help' command.

        Args:
            args: No arguments expected

        Returns:
            Help message with all available commands
        """
        help_text = """
=== Todo CLI Commands ===

Task Management:
  add <description>       Create a new task
  list                    Display all tasks
  edit <id> <description> Update task description
  delete <id>             Delete a task

Task Status:
  complete <id>           Mark task as complete
  uncomplete <id>         Mark task as incomplete

Interactive Mode:
  interactive             Launch keyboard-driven interactive mode

Other:
  help                    Show this help message
  exit / quit             Exit the application
"""
        return help_text.strip()

    def _handle_exit(self, args: List[str]) -> str:
        """Handle 'exit' / 'quit' commands.

        Args:
            args: No arguments expected

        Returns:
            Exit message (signals main loop to terminate)
        """
        return "exit"
