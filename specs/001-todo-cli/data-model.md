# Data Model: Phase I Todo List CLI

**Feature**: 001-todo-cli
**Date**: 2026-01-01
**Phase**: Phase 1 - Design & Contracts

## Entity Definitions

### Task

Represents a single todo item in the application.

**Attributes**:

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | int | Required, Unique, Auto-assigned, > 0 | Unique identifier for the task, auto-incremented |
| description | str | Required, 1-500 characters, Non-empty | Human-readable task description |
| is_complete | bool | Required, Default: False | Completion status (True = complete, False = incomplete) |
| created_at | int | Required, Auto-assigned | Creation order indicator (sequential number) |

**Validation Rules**:

1. **Description Validation**:
   - MUST NOT be empty string
   - MUST NOT be only whitespace
   - MUST be between 1 and 500 characters (after stripping whitespace)
   - Leading/trailing whitespace should be stripped automatically
   - Error message: "Task description cannot be empty. Please provide a description (1-500 characters)."

2. **ID Validation**:
   - MUST be positive integer
   - MUST be unique within the session
   - Auto-assigned by system (users cannot set ID manually)
   - IDs never reused (monotonically increasing)

3. **Completion Status**:
   - MUST be boolean value
   - Toggle operation changes True ↔ False
   - Default value is False (incomplete) on creation

**State Transitions**:

```
[New Task Created] → is_complete = False (Incomplete)
                         ↓
                    [User marks complete]
                         ↓
                    is_complete = True (Complete)
                         ↓
                    [User marks incomplete]
                         ↓
                    is_complete = False (Incomplete)
```

**Invariants**:
- Task ID is immutable once assigned
- Description can be updated but must always satisfy validation rules
- Completion status is always a boolean value
- Created order is immutable (no reordering in Phase I)

---

## Data Storage

### In-Memory Storage Strategy

**Primary Storage**:
```python
# Global application state (in-memory only)
tasks_by_id: dict[int, Task] = {}      # Fast O(1) lookup by ID
tasks_ordered: list[Task] = []         # Preserves creation order for display
next_task_id: int = 1                  # Auto-incrementing ID counter
```

**Storage Characteristics**:
- **Session-scoped**: All data lost when application exits (Phase I constraint)
- **Single-user**: No concurrency concerns, no locking needed
- **In-memory only**: No file I/O, database connections, or external persistence
- **Maximum capacity**: Limited by available system memory (~1000 tasks target per spec)

**Data Operations Complexity**:

| Operation | Complexity | Notes |
|-----------|------------|-------|
| Create (add task) | O(1) | Append to list, insert to dict |
| Read (get by ID) | O(1) | Dict lookup |
| Read (list all) | O(n) | Iterate ordered list |
| Update (edit description) | O(1) | Dict lookup + field update |
| Update (toggle complete) | O(1) | Dict lookup + boolean flip |
| Delete | O(n) | Dict delete O(1) + list remove O(n) |
| Count | O(1) | len(tasks_ordered) |

---

## Entity Relationships

**Relationships**: None (single entity model)

This is a simple single-entity application. No relationships exist in Phase I.

**Future Phase Considerations** (Out of Scope for Phase I):
- Phase II may introduce Users (one-to-many: User → Tasks)
- Phase II+ may introduce Categories/Tags (many-to-many: Tasks ↔ Tags)
- Phase III may introduce AI suggestions (one-to-many: Task → Suggestions)

---

## Data Validation

### Input Validation Layer

All validation happens at the Task model level before state changes.

**Validation Functions**:

```python
def validate_description(description: str) -> str:
    """
    Validates and normalizes task description.

    Args:
        description: Raw user input for task description

    Returns:
        Normalized description (stripped whitespace)

    Raises:
        ValidationError: If description is empty or exceeds length limits
    """
    # Implementation validates:
    # - Not None
    # - Strip whitespace
    # - Length between 1-500 characters
    # - Not empty after stripping
    pass

def validate_task_id(task_id: int, task_store: dict) -> int:
    """
    Validates task ID exists in storage.

    Args:
        task_id: Task identifier to validate
        task_store: Current task storage dict

    Returns:
        Validated task ID

    Raises:
        TaskNotFoundError: If task ID does not exist
        ValidationError: If task ID is not a positive integer
    """
    # Implementation validates:
    # - Is integer
    # - Is positive (> 0)
    # - Exists in storage
    pass
```

**Validation Error Messages**:

| Scenario | Error Message |
|----------|---------------|
| Empty description | "Task description cannot be empty. Please provide a description (1-500 characters)." |
| Description too long | "Task description exceeds 500 characters. Please shorten your description." |
| Task ID not found | "Task #{id} not found. Use 'list' command to see available task IDs." |
| Invalid ID type | "Invalid task ID '{input}'. Task IDs must be positive numbers. Example: 1, 2, 3" |
| Empty task list operation | "No tasks available. Use 'add' command to create your first task." |

---

## Data Consistency Rules

### Synchronization Between Storage Structures

**Invariant**: `tasks_by_id` and `tasks_ordered` must always contain the same Task objects.

**Consistency Rules**:

1. **On Task Creation**:
   ```
   - Assign new ID (next_task_id++)
   - Create Task instance with validated description
   - Add to tasks_by_id dict
   - Append to tasks_ordered list
   - Both operations succeed or both fail (atomic)
   ```

2. **On Task Deletion**:
   ```
   - Remove from tasks_by_id dict
   - Remove from tasks_ordered list
   - Both operations succeed or both fail (atomic)
   - ID is never reused
   ```

3. **On Task Update** (description or completion status):
   ```
   - Modify Task object in-place
   - Changes automatically reflected in both dict and list (same object reference)
   - No synchronization needed (shared reference)
   ```

**Consistency Checks** (for testing):
- `len(tasks_by_id) == len(tasks_ordered)` at all times
- All IDs in `tasks_by_id.keys()` match `[t.id for t in tasks_ordered]`
- All Task objects in dict are also in list (same references)

---

## Performance Considerations

**Memory Usage**:
- Each Task object: ~200 bytes (estimated)
- 1000 tasks: ~200KB + overhead
- Well within Phase I constraints (no memory limit specified)

**Scalability Targets** (from spec):
- Support up to 1000 tasks in memory without degradation
- Response time <1 second for all operations
- Display list in <2 seconds regardless of size (up to 1000 tasks)

**Optimization Notes**:
- No premature optimization needed (simplicity principle)
- List iteration for display is O(n) but acceptable for 1000 tasks
- Delete operation is O(n) but rare compared to reads
- If performance issues arise, consider OrderedDict only (removes list)

---

## Testing Strategy for Data Model

**Unit Tests**:

1. **Task Creation**:
   - Valid description → Task created with ID, incomplete status
   - Empty description → ValidationError
   - Description >500 chars → ValidationError
   - Whitespace-only → ValidationError

2. **Task Validation**:
   - Valid ID lookup → Returns task
   - Non-existent ID → TaskNotFoundError
   - Negative ID → ValidationError
   - String ID → ValidationError

3. **Task Updates**:
   - Toggle completion → Status flips
   - Update description (valid) → Description changes
   - Update description (invalid) → ValidationError, original unchanged

4. **Storage Consistency**:
   - Add task → Exists in both dict and list
   - Delete task → Removed from both dict and list
   - Update task → Changes reflected in both structures
   - Count matches between dict and list

**Test Fixtures**:
- Empty task list
- Single task
- Multiple tasks (mix of complete/incomplete)
- Large task list (100+ tasks for performance testing)
