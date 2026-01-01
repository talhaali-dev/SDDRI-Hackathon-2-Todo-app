---
id: 0006
title: Implement User Story 2 Mark Complete
stage: green
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-todo-cli
branch: 001-todo-cli
user: user
command: /sp.implement specs/001-todo-cli/tasks.md
labels: ["implementation", "tdd", "user-story-2", "mark-complete"]
links:
  spec: specs/001-todo-cli/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - tests/unit/test_todo_service.py
  - tests/integration/test_cli_commands.py
  - src/services/todo_service.py
  - src/cli/menu.py
  - specs/001-todo-cli/tasks.md
tests:
  - ✅ test_mark_complete (unit)
  - ✅ test_mark_incomplete (unit)
  - ✅ test_mark_complete_invalid_id (unit)
  - ✅ test_mark_complete_idempotent (unit)
  - ✅ test_complete_command (integration)
  - ✅ test_uncomplete_command (integration)
  - ✅ All 15 tests passing (9 US1 + 6 US2)
---

## Prompt

/sp.implement specs/001-todo-cli/tasks.md

## Response snapshot

Successfully implemented User Story 2 (Mark Tasks Complete) following strict TDD workflow.

**TDD Process Followed**:
1. ✅ **Red Phase**: Wrote 6 tests FIRST (T030-T035)
2. ✅ **Verified Fail**: All 6 tests failed as expected
3. ✅ **Green Phase**: Implemented functionality (T036-T040)
4. ✅ **Verified Pass**: All 6 tests now pass + 9 US1 tests = 15/15 total

**Tests Written (TDD Red Phase)**:

Unit Tests (tests/unit/test_todo_service.py):
- T030: test_mark_complete - Mark task as complete
- T031: test_mark_incomplete - Mark task as incomplete
- T032: test_mark_complete_invalid_id - Raise TaskNotFoundError for invalid ID
- T033: test_mark_complete_idempotent - Idempotent complete operation

Integration Tests (tests/integration/test_cli_commands.py):
- T034: test_complete_command - Complete command integration
- T035: test_uncomplete_command - Uncomplete command integration

**Implementation (TDD Green Phase)**:

src/services/todo_service.py:
- T036: _get_task_by_id(task_id) - Private method for O(1) task lookup with error handling
- T037: mark_complete(task_id) - Mark task as complete
- T038: mark_incomplete(task_id) - Mark task as incomplete

src/cli/menu.py:
- T039: _handle_complete(args) - Complete command handler with validation
- T040: _handle_uncomplete(args) - Uncomplete command handler with validation

**Error Handling**:
- TaskNotFoundError raised for invalid task IDs
- ValueError caught for non-integer task IDs
- Clear error messages following constitution FR-011

**Test Results**:
```
test_mark_complete ... ok
test_mark_incomplete ... ok
test_mark_complete_invalid_id ... ok
test_mark_complete_idempotent ... ok
test_complete_command ... ok
test_uncomplete_command ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

All 15 tests passing (9 US1 + 6 US2).

**Updated tasks.md**:
- T030-T035 marked [x] (tests)
- T036-T040 marked [x] (implementation)
- Added verification notes: "✅ All US2 tests PASS (green phase) - 6/6 tests passing"

## Outcome

- ✅ Impact: User Story 2 fully implemented - users can now mark tasks complete/incomplete with proper validation and error handling
- 🧪 Tests: 6 new tests added, all passing (4 unit + 2 integration), 15/15 total tests passing
- 📁 Files: Modified test_todo_service.py, test_cli_commands.py, todo_service.py, menu.py, tasks.md
- 🔁 Next prompts: Continue with User Story 3 (Interactive Mode) - T041-T054, or stop here to validate US2 independently
- 🧠 Reflection: TDD workflow enforced successfully - tests written first, verified to fail, then implementation made tests pass. US2 is independently testable and fully functional. The _get_task_by_id helper method provides O(1) lookups with proper error handling. Command handlers include comprehensive validation (task ID presence, integer format, existence check). Ready to proceed with US3 or stop for independent validation.

## Evaluation notes (flywheel)

- Failure modes observed: None. All 6 US2 tests followed TDD workflow perfectly. Implementation passed on first attempt with no bugs.
- Graders run and results (PASS/FAIL): PASS - All tests pass, proper error handling, clean code, follows constitution principles.
- Prompt variant (if applicable): N/A (standard implementation workflow)
- Next experiment (smallest change to try): When implementing US3 (Interactive Mode with curses), consider how to test curses UI without actual terminal. May need to mock curses module or create testable abstractions for key handling and display logic.

