# Todo CLI - Phase I (Menu Navigation)

A lightweight, in-memory command-line todo list application with **menu-based navigation** built for Phase I of the hackathon project.

## Features

- **Menu-Based Navigation**: Easy-to-use numbered menu interface (no command memorization)
- **Create Tasks**: Quickly add tasks with descriptions
- **View Tasks**: List all tasks with completion status
- **Toggle Status**: Mark tasks as complete/incomplete
- **Edit Tasks**: Update task descriptions
- **Delete Tasks**: Remove unwanted tasks
- **Graceful Exit**: Clean shutdown with Ctrl+C support

## Installation

### Prerequisites

- Python 3.13 or higher
- uv package manager

### Setup with uv

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/GrowWidTalha/SDDRI-Hackathon-2-Todo-app.git
   cd SDDRI-Hackathon-2-Todo-app
   ```

3. **Run the application**:
   ```bash
   uv run python main.py
   ```

## Quick Start

### Menu-Based Workflow

When you launch the application, you'll see a numbered menu:

```
========================================
         TODO MENU
========================================
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
6. Exit
========================================
Enter choice:
```

### Menu Options

- **1** or **add** - Create a new task
- **2** or **view** - View all tasks with status
- **3** or **toggle** - Toggle task completion (complete/incomplete)
- **4** or **update** - Update task description
- **5** or **delete** - Delete a task
- **6** or **exit** - Exit the application

### Example Workflow

```bash
$ uv run python main.py

==================================================
    Phase I Todo CLI - Menu Navigation
==================================================

========================================
         TODO MENU
========================================
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
6. Exit
========================================
Enter choice: 1
Enter task description: Buy groceries
Task 1 created.

[Menu redisplays]

Enter choice: 1
Enter task description: Write hackathon report
Task 2 created.

[Menu redisplays]

Enter choice: 2

[ ] [1] Buy groceries
[ ] [2] Write hackathon report

Press Enter to continue...

[Menu redisplays]

Enter choice: 3
Enter task ID: 1
Task 1 marked as complete.

[Menu redisplays]

Enter choice: 2

[✓] [1] Buy groceries
[ ] [2] Write hackathon report

Press Enter to continue...

Enter choice: 6

Thank you for using Todo CLI!
```

## Phase I Constraints

- **In-memory only**: Tasks are not persisted between sessions
- **Standard library only**: No external dependencies for core functionality
- **Single-user**: Designed for local, single-session use

## Input Validation

The application includes comprehensive input validation:

- **Empty descriptions** are rejected with a clear error message
- **Descriptions over 500 characters** are rejected (shows current length)
- **Invalid task IDs** (non-numeric or not found) show specific error messages
- **Invalid menu options** display guidance (enter 1-6)

## Testing

Run all tests (unit + integration):

```bash
# Run all tests
uv run pytest tests/ -v

# Run only integration tests
uv run pytest tests/integration/ -v

# Run only unit tests
uv run pytest tests/unit/ -v
```

**Test Coverage**:
- 49 tests total (15 unit + 34 integration)
- All menu navigation workflows tested
- All CRUD operations validated
- Error handling verified

## Project Structure

```
src/
├── models/          # Task entity and exceptions (reused from 001-todo-cli)
├── services/        # Business logic - TodoService (reused from 001-todo-cli)
├── cli/
│   ├── menu_navigator.py  # Menu-based navigation (NEW)
│   └── menu.py            # Original command menu (preserved)
├── ui/              # Display formatting (reused from 001-todo-cli)
└── main.py          # Application entry point (updated for menu)

tests/
├── unit/            # Unit tests for models and services (15 tests)
└── integration/     # Integration tests for CLI (34 tests)
    ├── test_menu_navigation.py  # Menu navigation tests (NEW)
    ├── test_cli_commands.py     # Original CLI command tests
    └── test_interactive_mode.py # Interactive mode tests
```

## License

Phase I Hackathon Project - 2026
