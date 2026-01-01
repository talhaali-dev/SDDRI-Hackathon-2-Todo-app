# Data Model: Menu-Based Todo CLI Navigation

**Feature**: 002-todo-cli-menu
**Date**: 2026-01-01
**Status**: Complete

## Overview

**IMPORTANT**: The data model for 002-todo-cli-menu is **100% identical to 001-todo-cli**. This feature updates only the navigation layer (menu-based UI), not the data structures or business logic.

All entities, attributes, validation rules, storage structures, and operations are **unchanged** from the original command-based implementation.

## Entities

### Task

**Description**: Represents a single todo item in the task list.

**Attributes**:
| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `id` | `int` | Positive integer, unique | Sequential identifier starting from 1, assigned by TodoService |
| `description` | `str` | 1-500 characters, non-empty | Task description text |
| `is_complete` | `bool` | True or False | Completion status flag |
| `created_at` | `int` | Unix timestamp | Creation timestamp (auto-generated) |

**Validation Rules**:
1. `id` must be a positive integer (>0)
2. `description` cannot be empty or whitespace-only
3. `description` cannot exceed 500 characters
4. `is_complete` must be boolean (True/False)

**State Transitions**:
```
[New Task] → is_complete = False
    ↓
[Toggle Complete] → is_complete = !is_complete
    ↓
[Update Description] → description = new_value
    ↓
[Delete] → removed from storage
```

### Task List

**Description**: Collection of tasks maintained during application session.

**Storage Structure** (Dual structure for O(1) lookups and ordered display):

**1. tasks_by_id** (Dictionary)
- Type: `dict[int, Task]`
- Purpose: O(1) task lookup by ID
- Key: Task ID
- Value: Task object
- Invariant: Contains all tasks, keys are unique

**2. tasks_ordered** (List)
- Type: `list[Task]`
- Purpose: Maintain creation-order display
- Order: Tasks in creation order (first created = first in list)
- Invariant: Length matches tasks_by_id, contains same Task objects

**Synchronization**:
- Both structures updated atomically on add/delete
- `add_task()`: Append to list, add to dict
- `delete_task()`: Remove from list, delete from dict key
- `update_task()`: Update in place (no structural change)
- `mark_complete()`/`mark_incomplete()`: Update in place (no structural change)

**Operations Complexity**:
| Operation | tasks_by_id | tasks_ordered | Overall |
|-----------|-------------|---------------|----------|
| Create (add_task) | O(1) dict insert | O(1) list append | O(1) |
| Read by ID (_get_task_by_id) | O(1) dict lookup | N/A | O(1) |
| Read all (list_tasks) | N/A | O(n) list copy | O(n) |
| Update (update_task, mark_*) | O(1) dict access | O(1) in-place | O(1) |
| Delete (delete_task) | O(1) dict delete | O(n) list remove | O(n) |

**Invariants**:
1. `len(tasks_by_id) == len(tasks_ordered)` at all times
2. All Task objects in tasks_ordered exist in tasks_by_id
3. Task IDs are sequential (1, 2, 3...) with no gaps
4. Deleted task IDs are never reused

## Operations

### Task Creation

**Method**: `TodoService.add_task(description: str) -> Task`

**Process**:
1. Validate description (non-empty, ≤500 chars)
2. Create Task object with `id = next_task_id`
3. Add to `tasks_by_id[id] = task`
4. Append to `tasks_ordered.append(task)`
5. Increment `next_task_id += 1`
6. Return created Task

**Error Conditions**:
- Empty description → Raises `ValidationError`
- Description >500 chars → Raises `ValidationError`

### Task Retrieval

**Method**: `TodoService.list_tasks() -> list[Task]`

**Process**:
1. Return copy of `tasks_ordered` list
2. Preserves creation order

**Edge Cases**:
- Empty list → Returns empty list `[]`

### Task Status Toggle

**Method**: `TodoService.mark_complete(task_id: int)` / `TodoService.mark_incomplete(task_id: int)`

**Process**:
1. Validate task_id exists → Raise `TaskNotFoundError` if not
2. Get task from `tasks_by_id[task_id]`
3. Set `task.is_complete = True` (or False)
4. No structural change to storage

**Error Conditions**:
- Invalid task_id → Raises `TaskNotFoundError`

### Task Update

**Method**: `TodoService.update_task(task_id: int, new_description: str)`

**Process**:
1. Validate new_description (non-empty, ≤500 chars)
2. Validate task_id exists → Raise `TaskNotFoundError` if not
3. Get task from `tasks_by_id[task_id]`
4. Set `task.description = new_description`
5. No structural change to storage

**Error Conditions**:
- Invalid task_id → Raises `TaskNotFoundError`
- Empty description → Raises `ValidationError`
- Description >500 chars → Raises `ValidationError`

### Task Deletion

**Method**: `TodoService.delete_task(task_id: int)`

**Process**:
1. Validate task_id exists → Raise `TaskNotFoundError` if not
2. Get task from `tasks_by_id[task_id]`
3. Delete from dict: `del tasks_by_id[task_id]`
4. Remove from list: `tasks_ordered.remove(task)`
5. Task ID is **not reused** (gap in sequence remains)

**Error Conditions**:
- Invalid task_id → Raises `TaskNotFoundError`

**Edge Cases**:
- Delete last task → Both structures become empty
- Delete first/middle task → Remaining tasks maintain relative order

## Data Model Summary

**Key Points**:
- ✅ Identical to 001-todo-cli - no changes to entities or storage
- ✅ All validation rules unchanged
- ✅ All operations preserve invariants
- ✅ Performance characteristics unchanged
- ✅ Error handling unchanged

**What Changed in 002-todo-cli-menu**:
- ❌ Data model: NO CHANGES
- ❌ Storage: NO CHANGES
- ❌ Validation: NO CHANGES
- ❌ Operations: NO CHANGES
- ✅ Only navigation layer changed (menu UI vs command UI)

**Implication**: All business logic, validation, and storage from 001-todo-cli can be reused without modification.
