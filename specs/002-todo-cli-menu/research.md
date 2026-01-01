# Research: Menu-Based Todo CLI Navigation

**Feature**: 002-todo-cli-menu
**Date**: 2026-01-01
**Status**: Complete

## Overview

Research completed for menu-based navigation system to replace command-based workflow in Phase I Todo CLI. All technical decisions align with Phase I constraints (standard library only, in-memory storage).

## Technical Decisions

### 1. Menu Display Technology

**Decision**: Standard print() statements with formatted text

**Rationale**:
- Phase I compliant (standard library only)
- Universally compatible across all terminals
- Simple, readable, no dependencies
- Sufficient for 6-option menu display
- Easy to format with borders and separators

**Alternatives Considered**:
- **curses module**: Rejected - overkill for simple menu, adds complexity, not needed for static menu display
- **第三方库 (Third-party libraries)**: Rejected - violates Phase I constraints

**Implementation**:
```python
def display_menu():
    print("=" * 40)
    print("    TODO MENU")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Toggle Complete")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")
    print("=" * 40)
```

---

### 2. Menu Input Method

**Decision**: input() for user selection, int() for numeric parsing with fallback

**Rationale**:
- Phase I compliant (standard library)
- Straightforward validation logic
- Supports both numeric (1, 2, 3) and text-based ("add", "view") per FR-003
- Natural Python pattern for console input

**Alternatives Considered**:
- **sys.stdin.readline()**: Rejected - more complex, input() sufficient
- **getpass module**: Rejected - designed for passwords, unnecessary here

**Implementation Strategy**:
- Primary: Numeric selection (1-6)
- Secondary: Text-based selection (case-insensitive: "add", "view", "toggle", "update", "delete", "exit")
- Validation: Check against valid options, clear error message for invalid input
- Re-prompt on invalid input

---

### 3. Navigation Flow

**Decision**: Infinite loop with menu display → get input → route action → redisplay

**Rationale**:
- Matches FR-004 (redisplays menu after all actions except Exit)
- Simple, predictable control flow
- Easy to understand and debug
- Supports graceful exit (Exit option or Ctrl+C)

**Flow Diagram**:
```
START
  ↓
display_menu()
  ↓
get_selection()
  ↓
route_to_action()
  ↓
execute_action()
  ↓
if action == Exit: break
  ↓
(redisplay menu)
```

**Break Conditions**:
- User selects "6. Exit"
- User presses Ctrl+C (KeyboardInterrupt)
- Application completes task and terminates normally

---

### 4. Code Reuse Strategy

**Decision**: 100% reuse of 001-todo-cli business logic

**Rationale**:
- TodoService, Task model, validation already tested and validated
- Avoids code duplication
- Reduces implementation risk
- Maintains consistency across features
- All unit tests reusable without changes

**Reuse Confirmation**:
- ✅ **Task model** (src/models/task.py): NO CHANGES - identical data structure
- ✅ **TodoService** (src/services/todo_service.py): NO CHANGES - all CRUD operations identical
- ✅ **Exceptions** (src/models/exceptions.py): NO CHANGES - same error types
- ✅ **TaskFormatter** (src/ui/formatter.py): NO CHANGES - same display logic
- ⚠️ **CommandMenu** → **MenuNavigator**: REPLACEMENT - navigation layer only
- ⚠️ **main.py**: MODIFY - use MenuNavigator instead of CommandMenu

**New Code Required**:
- MenuNavigator class (menu display, selection routing, input handling)
- Integration tests for menu navigation
- Updated main.py loop

---

### 5. Testing Strategy

**Decision**: Reuse existing unit tests + add menu navigation integration tests

**Rationale**:
- Business logic already validated by 001-todo-cli tests
- New tests focus on navigation layer only
- Reduces test duplication
- Clear separation of concerns

**Test Categories**:

**Reused from 001-todo-cli** (NO CHANGES):
- tests/unit/test_task.py - Task model validation
- tests/unit/test_todo_service.py - TodoService CRUD operations
- All 28 existing tests pass unchanged

**New Tests Required**:
- tests/integration/test_menu_navigation.py - Menu display and routing
  - test_menu_displays_correctly
  - test_numeric_menu_selection
  - test_text_menu_selection (case-insensitive)
  - test_invalid_menu_selection
  - test_add_task_from_menu
  - test_view_tasks_from_menu
  - test_toggle_complete_from_menu
  - test_update_task_from_menu
  - test_delete_task_from_menu
  - test_exit_from_menu
  - test_empty_input_handling
  - test_non_numeric_id_validation

---

## Phase I Compliance Verification

✅ **All constraints satisfied**:

| Constraint | Decision | Verification |
|------------|----------|--------------|
| Python 3.13+ only | ✅ Using standard library (print, input, int) | No external packages |
| Standard library only | ✅ No third-party dependencies | All functions built-in |
| No persistence | ✅ In-memory storage unchanged from 001-todo-cli | Data structures identical |
| No external services | ✅ All operations local | No network calls |
| Terminal/console only | ✅ stdin/stdout via input() and print() | No GUI or web interface |

---

## Implementation Considerations

### Menu Formatting

**Visual Design**:
- Width: 40 characters (fits in small terminals)
- Separator: "====" lines for clarity
- Alignment: Left-aligned options
- Numbering: 1-6 (single digit for simplicity)

**Example Display**:
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
Enter choice: _
```

### Input Validation

**Validation Priority**:
1. Menu selection (1-6 or valid text)
2. Task ID (numeric, exists in list)
3. Task description (non-empty, ≤500 chars)

**Error Message Format** (FR-017):
```
Error: [description]. [corrective action].
```

**Examples**:
- "Error: Invalid menu option. Please enter a number between 1 and 6."
- "Error: Task ID must be a number. Please enter a valid numeric ID."
- "Error: Task description cannot be empty. Please provide a description."

### Performance

**Targets**:
- Menu display: <100ms (instantaneous)
- Input handling: <50ms (immediate)
- Action routing: <50ms (function call)
- Task operations: <1 second (inherited from 001-todo-cli)
- Menu redisplay: <100ms (instantaneous)

**Optimization**:
- No computation in menu display
- Direct function calls (no reflection)
- Minimal string formatting
- Immediate re-prompt after action

---

## Summary

All research questions resolved. Implementation can proceed with clear technical direction:
- Simple print-based menu display
- Standard input() for selection
- Full reuse of 001-todo-cli business logic
- Integration tests for navigation layer only
- Phase I compliant (standard library only)

**Estimated Implementation Effort**: LOW
- 100-150 lines of new code (MenuNavigator + updated main.py)
- 150-200 lines of integration tests
- 0 lines changed in business logic
- Leverages all existing unit tests (28 tests)
