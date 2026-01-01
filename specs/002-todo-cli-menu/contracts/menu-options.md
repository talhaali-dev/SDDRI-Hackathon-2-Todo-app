# Menu Options Contract

**Feature**: 002-todo-cli-menu
**Date**: 2026-01-01
**Status**: Complete

## Menu Structure

**Display Format**:
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

## Option Contracts

### Option 1: Add Task

**Menu Text**: `1. Add Task`

**Aliases**: `1`, `add`, `Add`, `ADD` (case-insensitive)

**Input Required**: Yes (task description)

**Input Prompt**:
```
Enter task description:
```

**Action**:
1. Read user input (string)
2. Validate non-empty
3. Validate length ≤500 characters
4. Call `service.add_task(description)`
5. Display confirmation: `"Task [N] created."`
6. Redisplay main menu

**Validation Rules**:
- Empty input → `"Error: Description cannot be empty. Please provide a task description."`
- >500 chars → `"Error: Description exceeds maximum length of 500 characters. Current length: N."`

**Success Output**:
```
Task 1 created.
[Menu redisplays]
```

---

### Option 2: View Tasks

**Menu Text**: `2. View Tasks`

**Aliases**: `2`, `view`, `View`, `VIEW` (case-insensitive)

**Input Required**: No

**Action**:
1. Call `service.list_tasks()`
2. Format with TaskFormatter
3. Display tasks or empty message
4. Prompt: `"Press Enter to continue..."`
5. Wait for user input
6. Redisplay main menu

**Output Format** (with tasks):
```
[ ] [1] Buy groceries
[✓] [2] Write documentation
[ ] [3] Review PR #123

Press Enter to continue...
```

**Output Format** (empty list):
```
No tasks found. Add a task to get started!

Press Enter to continue...
```

---

### Option 3: Toggle Complete

**Menu Text**: `3. Toggle Complete`

**Aliases**: `3`, `toggle`, `Toggle`, `TOGGLE` (case-insensitive)

**Input Required**: Yes (task ID)

**Input Prompt**:
```
Enter task ID:
```

**Action**:
1. Read user input
2. Validate numeric input
3. Validate task_id exists
4. Check current status (is_complete)
5. If incomplete → call `service.mark_complete(task_id)`
6. If complete → call `service.mark_incomplete(task_id)`
7. Display confirmation
8. Redisplay main menu

**Validation Rules**:
- Non-numeric → `"Error: Task ID must be a number. Please enter a valid numeric ID."`
- Invalid ID → `"Error: Task with ID N not found. Please verify the task ID and try again."`

**Success Output** (incomplete → complete):
```
Task 3 marked as complete.
[Menu redisplays]
```

**Success Output** (complete → incomplete):
```
Task 3 marked as incomplete.
[Menu redisplays]
```

---

### Option 4: Update Task

**Menu Text**: `4. Update Task`

**Aliases**: `4`, `update`, `Update`, `UPDATE` (case-insensitive)

**Input Required**: Yes (task ID and new description)

**Input Prompts**:
```
Enter task ID:
Enter new description:
```

**Action**:
1. Read task ID
2. Validate numeric input
3. Validate task_id exists
4. Read new description
5. Validate non-empty
6. Validate length ≤500 characters
7. Call `service.update_task(task_id, new_description)`
8. Display confirmation
9. Redisplay main menu

**Validation Rules**:
- Non-numeric ID → `"Error: Task ID must be a number. Please enter a valid numeric ID."`
- Invalid ID → `"Error: Task with ID N not found. Please verify the task ID and try again."`
- Empty description → `"Error: Description cannot be empty. Please provide a task description."`
- >500 chars → `"Error: Description exceeds maximum length of 500 characters. Current length: N."`

**Success Output**:
```
Task 3 updated.
[Menu redisplays]
```

---

### Option 5: Delete Task

**Menu Text**: `5. Delete Task`

**Aliases**: `5`, `delete`, `Delete`, `DELETE` (case-insensitive)

**Input Required**: Yes (task ID)

**Input Prompt**:
```
Enter task ID:
```

**Action**:
1. Read user input
2. Validate numeric input
3. Validate task_id exists
4. Call `service.delete_task(task_id)`
5. Display confirmation
6. Redisplay main menu

**Validation Rules**:
- Non-numeric → `"Error: Task ID must be a number. Please enter a valid numeric ID."`
- Invalid ID → `"Error: Task with ID N not found. Please verify the task ID and try again."`

**Success Output**:
```
Task 3 deleted.
[Menu redisplays]
```

---

### Option 6: Exit

**Menu Text**: `6. Exit`

**Aliases**: `6`, `exit`, `Exit`, `EXIT`, `quit`, `Quit`, `QUIT` (case-insensitive)

**Input Required**: No

**Action**:
1. Display goodbye message
2. Break main loop
3. Terminate application

**Output**:
```
Thank you for using Todo CLI!
[Application exits]
```

---

## Error Handling Contract

**Error Message Format** (FR-017):
```
Error: [description]. [corrective action].
```

**Error Categories**:

### 1. Menu Selection Errors

**Invalid Menu Option**:
```
Error: Invalid menu option. Please enter a number between 1 and 6.
```

**Empty Input** (at menu selection):
```
Error: No option selected. Please enter a number between 1 and 6.
```

### 2. Task ID Input Errors

**Non-Numeric Task ID**:
```
Error: Task ID must be a number. Please enter a valid numeric ID.
```

**Task Not Found**:
```
Error: Task with ID N not found. Please verify the task ID and try again.
```

### 3. Description Input Errors

**Empty Description**:
```
Error: Description cannot be empty. Please provide a task description.
```

**Description Too Long**:
```
Error: Description exceeds maximum length of 500 characters. Current length: N.
```

## Input Validation Sequence

For each option requiring input:

1. **Display prompt** (if applicable)
2. **Read input** via `input()`
3. **Strip whitespace**
4. **Validate empty** (if required field)
5. **Validate format** (numeric, string length, etc.)
6. **Validate business logic** (task exists, constraints)
7. **Execute action** or **display error** and re-prompt

**Re-prompt Behavior**:
- On validation error → Display error message → Re-prompt for same input
- On success → Continue to next step or redisplay menu

## Performance Requirements

**Response Times**:
- Menu display: <100ms (instantaneous)
- Input reading: Immediate (blocking on user)
- Validation: <50ms
- Action execution: <1 second
- Menu redisplay: <100ms

**Throughput**:
- Support up to 1000 tasks in memory (inherited from 001-todo-cli)
- No degradation in menu display regardless of task count
