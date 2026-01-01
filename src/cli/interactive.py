"""Interactive mode with curses for keyboard-driven task management."""

import curses
from typing import Optional, Any
from src.services.todo_service import TodoService


class InteractiveMode:
    """Interactive curses-based interface for task management.

    Provides smooth keyboard-driven navigation with arrow keys and spacebar toggle.
    """

    def __init__(self, service: TodoService):
        """Initialize interactive mode.

        Args:
            service: TodoService instance for task operations
        """
        self.service = service
        self.selected_index: int = 0
        self.running: bool = False
        self.stdscr: Optional[Any] = None

    def display_task_list(self):
        """Display the task list in curses interface.

        Shows all tasks with completion status and highlights selected task.
        """
        if self.stdscr is None:
            return

        self.stdscr.clear()
        tasks = self.service.list_tasks()

        # Display header
        self.stdscr.addstr(0, 0, "=== Interactive Mode ===")
        self.stdscr.addstr(1, 0, "Arrow Keys: Navigate | Space: Toggle | Esc: Exit")
        self.stdscr.addstr(2, 0, "-" * 40)

        # Display tasks
        for idx, task in enumerate(tasks):
            status = "[✓]" if task.is_complete else "[ ]"
            marker = ">> " if idx == self.selected_index else "   "
            task_line = f"{marker}{status} [{task.id}] {task.description}"

            # Handle long descriptions
            if len(task_line) > 76:
                task_line = task_line[:76] + "..."

            self.stdscr.addstr(3 + idx, 0, task_line)

        self.stdscr.refresh()

    def handle_key_up(self):
        """Handle arrow up key - navigate to previous task.

        Implements circular navigation (wraps to bottom if at top).
        """
        tasks = self.service.list_tasks()
        if not tasks:
            return

        self.selected_index = (self.selected_index - 1) % len(tasks)

    def handle_key_down(self):
        """Handle arrow down key - navigate to next task.

        Implements circular navigation (wraps to top if at bottom).
        """
        tasks = self.service.list_tasks()
        if not tasks:
            return

        self.selected_index = (self.selected_index + 1) % len(tasks)

    def handle_spacebar(self):
        """Handle spacebar key - toggle completion status of selected task."""
        tasks = self.service.list_tasks()
        if not tasks or self.selected_index >= len(tasks):
            return

        task = tasks[self.selected_index]
        if task.is_complete:
            self.service.mark_incomplete(task.id)
        else:
            self.service.mark_complete(task.id)

    def handle_escape(self):
        """Handle escape key - exit interactive mode."""
        self.running = False

    def _main_loop(self, stdscr):
        """Main interactive loop.

        Args:
            stdscr: Curses window
        """
        self.stdscr = stdscr
        self.running = True

        # Configure curses
        curses.curs_set(0)  # Hide cursor
        stdscr.keypad(True)  # Enable keypad input

        # Initial display
        self.display_task_list()

        # Event loop
        while self.running:
            try:
                key = stdscr.getch()

                if key == curses.KEY_UP:
                    self.handle_key_up()
                    self.display_task_list()
                elif key == curses.KEY_DOWN:
                    self.handle_key_down()
                    self.display_task_list()
                elif key == ord(' '):
                    self.handle_spacebar()
                    self.display_task_list()
                elif key == 27:  # Escape key
                    self.handle_escape()

            except KeyboardInterrupt:
                self.handle_escape()
                break

    def start(self):
        """Start interactive mode.

        Entry point for launching the interactive curses interface.
        """
        try:
            curses.wrapper(self._main_loop)
        except curses.error:
            print("Error: Unable to initialize curses interface.")
            print("Your terminal may not support curses, or the window is too small.")
            print("Please use command mode instead.")

    def run(self):
        """Public method to start interactive mode from CLI."""
        self.start()
