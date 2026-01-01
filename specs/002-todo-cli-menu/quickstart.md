# Quickstart Guide: Menu-Based Todo CLI

**Version**: 2.0 (Menu Navigation)
**Phase**: Phase I (In-Memory Python Console App)

## What's New in Version 2.0?

**Change**: Command-based workflow → Menu-based navigation

**Before** (001-todo-cli - Command-based):
```
todo> add Buy groceries
todo> list
todo> complete 1
```

**After** (002-todo-cli-menu - Menu-based):
```
=== TODO MENU ===
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
6. Exit

Enter choice: 1
```

**Benefits**:
- ✅ No command memorization needed
- ✅ Intuitive numbered selection
- ✅ All options visible at all times
- ✅ Easier for first-time users

## Installation

No installation required! Uses Python standard library only.

**Prerequisites**:
- Python 3.13 or higher
- Terminal/console application

**Run the application**:
```bash
uv run python main.py
```

## 5-Minute Tutorial

### Step 1: Launch the Application

```bash
$ uv run python main.py

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

### Step 2: Add Your First Task

```
Enter choice: 1
Enter task description: Buy groceries
Task 1 created.

[Menu redisplays]
```

### Step 3: Add More Tasks

```
Enter choice: 1
Enter task description: Write project documentation
Task 2 created.

Enter choice: 1
Enter task description: Review pull request #123
Task 3 created.
```

### Step 4: View Your Tasks

```
Enter choice: 2

[ ] [1] Buy groceries
[ ] [2] Write project documentation
[ ] [3] Review pull request #123

Press Enter to continue...
```

**Task Status Indicators**:
- `[ ]` = Incomplete
- `[✓]` = Complete

### Step 5: Mark a Task Complete

```
Enter choice: 3
Enter task ID: 1
Task 1 marked as complete.

Enter choice: 2

[✓] [1] Buy groceries
[ ] [2] Write project documentation
[ ] [3] Review pull request #123

Press Enter to continue...
```

### Step 6: Toggle Status Back

```
Enter choice: 3
Enter task ID: 1
Task 1 marked as incomplete.
```

### Step 7: Update a Task

```
Enter choice: 4
Enter task ID: 2
Enter new description: Write API documentation
Task 2 updated.

Enter choice: 2

[ ] [1] Buy groceries
[ ] [2] Write API documentation
[ ] [3] Review pull request #123

Press Enter to continue...
```

### Step 8: Delete a Task

```
Enter choice: 5
Enter task ID: 3
Task 3 deleted.

Enter choice: 2

[ ] [1] Buy groceries
[ ] [2] Write API documentation

Press Enter to continue...
```

### Step 9: Exit

```
Enter choice: 6

Thank you for using Todo CLI!
[Application exits]
```

## Menu Options Reference

| Option | Alias | Input | Description |
|--------|-------|-------|-------------|
| **1. Add Task** | `add` | Description | Create a new task with a description |
| **2. View Tasks** | `view` | None | Display all tasks with status indicators |
| **3. Toggle Complete** | `toggle` | Task ID | Mark task complete/incomplete (toggles) |
| **4. Update Task** | `update` | Task ID + Description | Change task description |
| **5. Delete Task** | `delete` | Task ID | Remove task from list |
| **6. Exit** | `exit`, `quit` | None | Exit application |

**Selection Methods**:
- **Numeric**: Enter `1`, `2`, `3`, `4`, `5`, or `6`
- **Text**: Enter `add`, `view`, `toggle`, `update`, `delete`, or `exit` (case-insensitive)

## Common Tasks

### Add Multiple Tasks Quickly

```
Enter choice: 1
Enter task description: Task 1
Task 1 created.

Enter choice: 1
Enter task description: Task 2
Task 2 created.

Enter choice: 1
Enter task description: Task 3
Task 3 created.
```

### Mark All Tasks Complete

```
Enter choice: 2  [View IDs]
Enter choice: 3
Enter task ID: 1
Task 1 marked as complete.

Enter choice: 3
Enter task ID: 2
Task 2 marked as complete.

Enter choice: 3
Enter task ID: 3
Task 3 marked as complete.
```

### Bulk Delete Tasks

```
Enter choice: 5
Enter task ID: 3
Task 3 deleted.

Enter choice: 5
Enter task ID: 2
Task 2 deleted.
```

## Input Validation

### Empty Input

```
Enter choice: 1
Enter task description: [Press Enter without typing]
Error: Description cannot be empty. Please provide a task description.
Enter task description: [Re-prompt]
```

### Invalid Task ID

```
Enter choice: 3
Enter task ID: abc
Error: Task ID must be a number. Please enter a valid numeric ID.
Enter task ID: [Re-prompt]
```

### Task Not Found

```
Enter choice: 3
Enter task ID: 999
Error: Task with ID 999 not found. Please verify the task ID and try again.
[Menu redisplays]
```

### Invalid Menu Option

```
Enter choice: 99
Error: Invalid menu option. Please enter a number between 1 and 6.
[Menu redisplays]
```

## Tips and Best Practices

### 1. View Tasks Often

Always view your task list (`option 2`) before toggling, updating, or deleting to see current task IDs.

### 2. Use Text Aliases

You can type `add`, `view`, `toggle`, `update`, `delete`, or `exit` instead of numbers:
```
Enter choice: add
[Same as option 1]
```

### 3. Task IDs Never Change

Task IDs are assigned sequentially (1, 2, 3...) and never reused after deletion. This means:
- Deleting task 2 creates a gap in numbering
- Next new task gets ID 4 (not 2)
- This prevents confusion about which task you're referencing

### 4. Press Enter to Continue

After viewing tasks, press Enter to return to the main menu. This gives you time to review the list.

### 5. Graceful Exit

Press Ctrl+C at any time to exit cleanly:
```
^C

Exiting Todo CLI...
```

## Troubleshooting

### Menu Doesn't Display

**Problem**: Menu doesn't appear on launch

**Solution**: Ensure you're running `main.py` from the correct directory
```bash
cd /path/to/project
uv run python main.py
```

### Tasks Not Persisting

**Expected Behavior**: Tasks are stored in memory only and disappear when application exits. This is by design for Phase I.

**Future**: Phase II will add database persistence.

### Terminal Too Small

**Problem**: Menu display looks cut off

**Solution**: Resize terminal to at least 40 characters wide. Menu is designed for small terminals.

### Description Too Long

**Problem**: Task description rejected for being too long

**Solution**: Keep descriptions under 500 characters. The system will show current length if exceeded.

## Differences from Command-Based Workflow

| Aspect | Command-Based (001-todo-cli) | Menu-Based (002-todo-cli-menu) |
|--------|------------------------------|---------------------------------|
| **Interaction** | Type commands | Select numbered options |
| **Discovery** | Must remember commands | All options visible |
| **Learning Curve** | Steeper (memorize commands) | Easier (menu shows all) |
| **Speed** | Faster for experienced users | Slightly slower (more prompts) |
| **Errors** | Typo in command name | Invalid option number |
| **Functionality** | Identical | Identical |

**Migration**: All functionality preserved - only the interaction model changed.

## Phase I Limitations

**Current Scope** (Phase I):
- ✅ In-memory storage only (no persistence)
- ✅ Single-user, single-session
- ✅ Terminal/console interface
- ✅ Standard library only (no external dependencies)

**Future Phases**:
- Phase II: Web application with database
- Phase III: AI chatbot integration
- Phase IV: Kubernetes deployment
- Phase V: Advanced cloud features

## Getting Help

### Display Menu Anytime

The main menu is always available after completing any action. Just wait for it to redisplay.

### Keyboard Shortcuts

- `Ctrl+C` - Exit application (graceful interrupt)
- `Enter` - Confirm input / Continue to menu

### Error Messages

All errors follow this format:
```
Error: [description]. [corrective action].
```

Read the corrective action to know what to do next.

---

**Version**: 2.0 (Menu-Based Navigation)
**Last Updated**: 2026-01-01
**Feature**: 002-todo-cli-menu
