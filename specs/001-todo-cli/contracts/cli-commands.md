# CLI Command Interface Contract

**Feature**: 001-todo-cli
**Date**: 2026-01-01
**Phase**: Phase 1 - Design & Contracts

## Command Interface Specification

### Command Format

All commands follow this general format:
```
<command> [arguments]
```

**Input Protocol**:
- Commands entered via standard input (stdin)
- Prompts display `> ` to indicate ready for input
- Commands are case-insensitive
- Arguments separated by spaces
- Multi-word arguments use quotes (e.g., `add "Review pull request"`)

**Output Protocol**:
- Success messages to standard output (stdout)
- Error messages to standard output with clear error prefix
- Task lists formatted for readability
- Empty line before returning to prompt

---

## Command Reference

### 1. ADD - Create New Task

**Syntax**: `add <description>`

**Description**: Creates a new task with the provided description.

**Arguments**:
- `description` (required): Task description text (1-500 characters)
  - Multi-word descriptions should be quoted or entered after prompt
  - Leading/trailing whitespace automatically stripped

**Examples**:
```
> add "Write project documentation"
✓ Task created: [1] Write project documentation

> add Review pull requests
✓ Task created: [2] Review pull requests

> add
Error: Task description cannot be empty. Please provide a description (1-500 characters).
```

**Success Response**:
```
✓ Task created: [<id>] <description>
```

**Error Responses**:
```
Error: Task description cannot be empty. Please provide a description (1-500 characters).
Error: Task description exceeds 500 characters. Please shorten your description.
```

**Side Effects**:
- New task added to in-memory task list
- Task ID auto-assigned (incremental)
- Task status set to incomplete

**Mapped to**: User Story P1 (Create and View Tasks), FR-001, FR-002

---

### 2. LIST - View All Tasks

**Syntax**: `list`

**Description**: Displays all tasks with their IDs, descriptions, and completion status.

**Arguments**: None

**Examples**:
```
> list
Todo List (5 tasks):

Incomplete Tasks:
[ ] 1. Write project documentation
[ ] 2. Review pull requests
[ ] 3. Update tests

Complete Tasks:
[✓] 4. Setup development environment
[✓] 5. Create initial project structure

> list
No tasks available. Use 'add' command to create your first task.
```

**Success Response**:
```
Todo List (<count> tasks):

Incomplete Tasks:
[ ] <id>. <description>
...

Complete Tasks:
[✓] <id>. <description>
...
```

**Empty List Response**:
```
No tasks available. Use 'add' command to create your first task.
```

**Side Effects**: None (read-only operation)

**Mapped to**: User Story P1 (Create and View Tasks), FR-003, FR-006, FR-014

---

### 3. COMPLETE - Mark Task as Complete

**Syntax**: `complete <id>`

**Description**: Marks the specified task as complete.

**Arguments**:
- `id` (required): Task identifier (positive integer)

**Examples**:
```
> complete 3
✓ Task #3 marked as complete: [✓] Update tests

> complete 999
Error: Task #999 not found. Use 'list' command to see available task IDs.

> complete abc
Error: Invalid task ID 'abc'. Task IDs must be positive numbers. Example: 1, 2, 3
```

**Success Response**:
```
✓ Task #<id> marked as complete: [✓] <description>
```

**Error Responses**:
```
Error: Task #<id> not found. Use 'list' command to see available task IDs.
Error: Invalid task ID '<input>'. Task IDs must be positive numbers. Example: 1, 2, 3
```

**Side Effects**:
- Task completion status set to True
- Visual indicator updated ([ ] → [✓])

**Idempotency**: Marking already-complete task as complete succeeds without error

**Mapped to**: User Story P2 (Mark Tasks Complete), FR-004

---

### 4. UNCOMPLETE - Mark Task as Incomplete

**Syntax**: `uncomplete <id>`

**Description**: Marks the specified task as incomplete (reverses completion).

**Arguments**:
- `id` (required): Task identifier (positive integer)

**Examples**:
```
> uncomplete 4
✓ Task #4 marked as incomplete: [ ] Setup development environment

> uncomplete 999
Error: Task #999 not found. Use 'list' command to see available task IDs.
```

**Success Response**:
```
✓ Task #<id> marked as incomplete: [ ] <description>
```

**Error Responses**:
```
Error: Task #<id> not found. Use 'list' command to see available task IDs.
Error: Invalid task ID '<input>'. Task IDs must be positive numbers. Example: 1, 2, 3
```

**Side Effects**:
- Task completion status set to False
- Visual indicator updated ([✓] → [ ])

**Idempotency**: Marking already-incomplete task as incomplete succeeds without error

**Mapped to**: User Story P2 (Mark Tasks Complete), FR-005

---

### 5. EDIT - Update Task Description

**Syntax**: `edit <id> <new_description>`

**Description**: Updates the description of an existing task.

**Arguments**:
- `id` (required): Task identifier (positive integer)
- `new_description` (required): New task description (1-500 characters)

**Examples**:
```
> edit 1 "Write comprehensive project documentation"
✓ Task #1 updated: Write comprehensive project documentation

> edit 999 "New description"
Error: Task #999 not found. Use 'list' command to see available task IDs.

> edit 1 ""
Error: Task description cannot be empty. Please provide a description (1-500 characters).
```

**Success Response**:
```
✓ Task #<id> updated: <new_description>
```

**Error Responses**:
```
Error: Task #<id> not found. Use 'list' command to see available task IDs.
Error: Task description cannot be empty. Please provide a description (1-500 characters).
Error: Task description exceeds 500 characters. Please shorten your description.
```

**Side Effects**:
- Task description updated in-place
- Task ID and completion status unchanged

**Mapped to**: User Story P4 (Update Task Descriptions), FR-007

---

### 6. DELETE - Remove Task

**Syntax**: `delete <id>`

**Description**: Permanently removes the specified task from the list.

**Arguments**:
- `id` (required): Task identifier (positive integer)

**Examples**:
```
> delete 3
✓ Task #3 deleted: Update tests

> delete 999
Error: Task #999 not found. Use 'list' command to see available task IDs.
```

**Success Response**:
```
✓ Task #<id> deleted: <description>
```

**Error Responses**:
```
Error: Task #<id> not found. Use 'list' command to see available task IDs.
Error: Invalid task ID '<input>'. Task IDs must be positive numbers. Example: 1, 2, 3
```

**Side Effects**:
- Task removed from storage
- Task ID never reused
- If last task deleted, subsequent `list` shows empty message

**Warning**: No confirmation prompt (immediate deletion). Consider adding confirmation in future phases.

**Mapped to**: User Story P5 (Delete Tasks), FR-008

---

### 7. INTERACTIVE - Enter Interactive Mode

**Syntax**: `interactive`

**Description**: Switches from command mode to interactive navigation mode with arrow key support.

**Arguments**: None

**Examples**:
```
> interactive
[Enters interactive mode with task list and highlighted selection]

Use arrow keys to navigate, SPACE to toggle completion, ESC to exit
```

**Interactive Mode Interface**:
```
┌─────────────────────────────────────────────┐
│ Todo List (Interactive Mode)               │
│                                             │
│ ▶ [ ] 1. Write project documentation       │  ← Selected (highlighted)
│   [ ] 2. Review pull requests              │
│   [✓] 3. Update tests                      │
│   [ ] 4. Fix bug in login                  │
│                                             │
│ Arrow Keys: Navigate | Space: Toggle | ESC: Exit │
└─────────────────────────────────────────────┘
```

**Interactive Mode Controls**:
- `↑` (UP): Move selection up
- `↓` (DOWN): Move selection down
- `SPACE`: Toggle selected task completion status
- `ESC`: Exit interactive mode, return to command prompt

**Navigation Behavior**:
- Selection wraps (bottom to top, top to bottom)
- Immediate visual feedback on key press
- Status changes reflect immediately

**Success Response**: Enters interactive UI (no text response)

**Error Response**:
```
Error: Interactive mode unavailable. Curses library not supported on this terminal.
Fallback: Use command-based interface (add, list, complete, etc.)
```

**Side Effects**:
- Terminal switches to curses mode (full screen control)
- Original terminal state restored on exit

**Mapped to**: User Story P3 (Interactive Task Selection), FR-009, FR-010

---

### 8. HELP - Display Command Help

**Syntax**: `help`

**Description**: Displays list of available commands with brief descriptions.

**Arguments**: None

**Example Output**:
```
> help
Available Commands:

  add <description>       Create a new task
  list                    View all tasks
  complete <id>           Mark task as complete
  uncomplete <id>         Mark task as incomplete
  edit <id> <description> Update task description
  delete <id>             Delete a task
  interactive             Enter interactive mode
  help                    Show this help message
  exit                    Exit the application

Examples:
  > add "Review pull request #42"
  > complete 3
  > edit 1 "Updated task description"

For detailed help, see README.md
```

**Mapped to**: FR-013 (clear, intuitive interface)

---

### 9. EXIT - Quit Application

**Syntax**: `exit` or `quit`

**Description**: Exits the application.

**Arguments**: None

**Examples**:
```
> exit
Goodbye! All tasks will be lost (in-memory storage only).

> quit
Goodbye! All tasks will be lost (in-memory storage only).
```

**Success Response**:
```
Goodbye! All tasks will be lost (in-memory storage only).
```

**Side Effects**:
- Application terminates
- All in-memory data lost (Phase I constraint)
- Terminal state restored (if in interactive mode)

**Mapped to**: General application control

---

## Error Handling Contract

### Error Message Format

All error messages follow this format:
```
Error: <Clear description of what went wrong>. <Suggested corrective action>.
```

**Examples**:
```
Error: Task #42 not found. Use 'list' command to see available task IDs.
Error: Task description cannot be empty. Please provide a description (1-500 characters).
Error: Invalid command 'xyz'. Type 'help' to see available commands.
```

### Error Categories

1. **Validation Errors** (user input invalid)
   - Empty descriptions
   - Description length violations
   - Invalid ID formats

2. **Not Found Errors** (resource doesn't exist)
   - Task ID not in storage
   - Empty list operations requiring tasks

3. **Command Errors** (unknown command)
   - Unrecognized command names
   - Wrong number of arguments

**Mapped to**: FR-011 (clear, actionable error messages)

---

## Response Time Guarantees

Per success criteria:

| Operation | Maximum Response Time |
|-----------|----------------------|
| add | <1 second |
| list (up to 1000 tasks) | <2 seconds |
| complete / uncomplete | <1 second |
| edit | <1 second |
| delete | <1 second |
| interactive (enter/toggle) | <1 second (immediate visual feedback) |

**Mapped to**: SC-005 (<1 second response), SC-002 (<2 seconds list display)
