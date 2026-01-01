# Tasks: Phase I Todo List CLI

**Input**: Design documents from `/specs/001-todo-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: TDD is NON-NEGOTIABLE per constitution. All tests MUST be written FIRST, fail (red phase), then implement (green phase).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below use single project structure per plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize Python project with uv (uv init --no-workspace or verify uv is available)
- [x] T002 Create pyproject.toml with project metadata (name="todo-cli", version="0.1.0", requires-python=">=3.13", dependencies=[])
- [x] T003 Create project directory structure (src/, src/models/, src/services/, src/cli/, src/ui/, tests/, tests/unit/, tests/integration/)
- [x] T004 Create __init__.py files in all Python package directories
- [x] T005 [P] Create README.md with basic usage instructions per quickstart.md (include uv installation and setup)
- [x] T006 [P] Create .gitignore for Python and uv (ignore __pycache__, *.pyc, .pytest_cache, .vscode, .idea, .venv/, uv.lock, *.egg-info/)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 [P] Create custom exception classes in src/models/exceptions.py (TodoError, ValidationError, TaskNotFoundError, EmptyTaskListError)
- [x] T008 [P] Create Task model class definition (skeleton) in src/models/task.py with @dataclass decorator and type hints
- [x] T009 [P] Create TodoService class (skeleton) in src/services/todo_service.py with storage initialization (tasks_by_id dict, tasks_ordered list, next_task_id counter)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Core MVP functionality - add tasks and view them in a list

**Independent Test**: Launch app, add 3-5 tasks, verify all appear in list view with IDs and status

### Tests for User Story 1 (TDD - Write FIRST, Verify FAIL) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T010 [P] [US1] Write unit test for Task model validation (empty description) in tests/unit/test_task.py
- [x] T011 [P] [US1] Write unit test for Task model validation (description >500 chars) in tests/unit/test_task.py
- [x] T012 [P] [US1] Write unit test for Task creation with valid description in tests/unit/test_task.py
- [x] T013 [P] [US1] Write unit test for TodoService.add_task() in tests/unit/test_todo_service.py
- [x] T014 [P] [US1] Write unit test for TodoService.list_tasks() with empty list in tests/unit/test_todo_service.py
- [x] T015 [P] [US1] Write unit test for TodoService.list_tasks() with multiple tasks in tests/unit/test_todo_service.py
- [x] T016 [P] [US1] Write integration test for 'add' command in tests/integration/test_cli_commands.py
- [x] T017 [P] [US1] Write integration test for 'list' command with tasks in tests/integration/test_cli_commands.py
- [x] T018 [P] [US1] Write integration test for 'list' command with empty list in tests/integration/test_cli_commands.py

**RUN TESTS**: ✅ Verified all US1 tests FAIL (red phase) - proceeding to implementation

### Implementation for User Story 1 (TDD - Implement to Make Tests PASS)

- [x] T019 [P] [US1] Implement Task model __init__ with validation in src/models/task.py
- [x] T020 [P] [US1] Implement Task model validate_description() method in src/models/task.py
- [x] T021 [US1] Implement TodoService.add_task(description) method in src/services/todo_service.py (depends on T019, T020)
- [x] T022 [US1] Implement TodoService.list_tasks() method returning ordered list in src/services/todo_service.py
- [x] T023 [P] [US1] Create TaskFormatter class in src/ui/formatter.py with format_task_list() method
- [x] T024 [P] [US1] Implement TaskFormatter display logic for complete/incomplete tasks (Unicode [ ] and [✓]) in src/ui/formatter.py
- [x] T025 [US1] Create CommandMenu class skeleton in src/cli/menu.py with parse_command() method
- [x] T026 [US1] Implement 'add' command handler in src/cli/menu.py (depends on T021)
- [x] T027 [US1] Implement 'list' command handler in src/cli/menu.py (depends on T022, T023)
- [x] T028 [US1] Create main.py with application entry point and main loop
- [x] T029 [US1] Integrate TodoService and CommandMenu in main.py

**RUN TESTS**: ✅ All US1 tests PASS (green phase) - 9/9 tests passing

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently - YOU HAVE A WORKING MVP!

---

## Phase 4: User Story 2 - Mark Tasks Complete (Priority: P2)

**Goal**: Track progress by marking tasks complete/incomplete

**Independent Test**: Create 5 tasks, mark 2-3 complete, verify status changes in list view

### Tests for User Story 2 (TDD - Write FIRST, Verify FAIL) ⚠️

- [x] T030 [P] [US2] Write unit test for TodoService.mark_complete(task_id) in tests/unit/test_todo_service.py
- [x] T031 [P] [US2] Write unit test for TodoService.mark_incomplete(task_id) in tests/unit/test_todo_service.py
- [x] T032 [P] [US2] Write unit test for mark_complete with invalid ID (TaskNotFoundError) in tests/unit/test_todo_service.py
- [x] T033 [P] [US2] Write unit test for idempotent complete operation in tests/unit/test_todo_service.py
- [x] T034 [P] [US2] Write integration test for 'complete' command in tests/integration/test_cli_commands.py
- [x] T035 [P] [US2] Write integration test for 'uncomplete' command in tests/integration/test_cli_commands.py

**RUN TESTS**: ✅ Verified all US2 tests FAIL (red phase) - proceeding to implementation

### Implementation for User Story 2

- [x] T036 [P] [US2] Implement TodoService.get_task_by_id(task_id) private method in src/services/todo_service.py
- [x] T037 [US2] Implement TodoService.mark_complete(task_id) method in src/services/todo_service.py (depends on T036)
- [x] T038 [US2] Implement TodoService.mark_incomplete(task_id) method in src/services/todo_service.py (depends on T036)
- [x] T039 [US2] Implement 'complete' command handler in src/cli/menu.py
- [x] T040 [US2] Implement 'uncomplete' command handler in src/cli/menu.py

**RUN TESTS**: ✅ All US2 tests PASS (green phase) - 6/6 tests passing

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Interactive Task Selection (Priority: P3)

**Goal**: Smooth keyboard-driven interface with arrow keys and spacebar toggle

**Independent Test**: Create tasks, use arrows to navigate, spacebar to toggle completion

### Tests for User Story 3 (TDD - Write FIRST, Verify FAIL) ⚠️

- [x] T041 [P] [US3] Write unit test for InteractiveMode.handle_key_up() navigation in tests/integration/test_interactive_mode.py
- [x] T042 [P] [US3] Write unit test for InteractiveMode.handle_key_down() navigation in tests/integration/test_interactive_mode.py
- [x] T043 [P] [US3] Write unit test for InteractiveMode.handle_spacebar() toggle in tests/integration/test_interactive_mode.py
- [x] T044 [P] [US3] Write unit test for circular navigation (wrap around) in tests/integration/test_interactive_mode.py
- [x] T045 [P] [US3] Write integration test for entering/exiting interactive mode in tests/integration/test_interactive_mode.py

**RUN TESTS**: ✅ Verified all US3 tests FAIL (red phase) - proceeding to implementation

### Implementation for User Story 3

- [x] T046 [P] [US3] Create InteractiveMode class skeleton in src/cli/interactive.py with curses setup
- [x] T047 [US3] Implement InteractiveMode.display_task_list() with curses in src/cli/interactive.py
- [x] T048 [US3] Implement InteractiveMode.handle_key_up() for navigation in src/cli/interactive.py
- [x] T049 [US3] Implement InteractiveMode.handle_key_down() for navigation in src/cli/interactive.py
- [x] T050 [US3] Implement InteractiveMode.handle_spacebar() for toggle in src/cli/interactive.py
- [x] T051 [US3] Implement InteractiveMode.handle_escape() to exit in src/cli/interactive.py
- [x] T052 [US3] Implement circular navigation (bottom to top, top to bottom) in src/cli/interactive.py
- [x] T053 [US3] Implement 'interactive' command handler in src/cli/menu.py to launch interactive mode
- [x] T054 [US3] Add curses fallback handling (show error if curses unavailable) in src/cli/interactive.py

**RUN TESTS**: ✅ All US3 tests PASS (green phase) - 5/5 tests passing

**Checkpoint**: All user stories should now provide smooth UX

---

## Phase 6: User Story 4 - Update Task Descriptions (Priority: P4)

**Goal**: Edit task descriptions without deleting and recreating

**Independent Test**: Create tasks, edit one by ID, verify description updates

### Tests for User Story 4 (TDD - Write FIRST, Verify FAIL) ⚠️

- [x] T055 [P] [US4] Write unit test for TodoService.update_task(task_id, new_description) in tests/unit/test_todo_service.py
- [x] T056 [P] [US4] Write unit test for update with invalid ID (TaskNotFoundError) in tests/unit/test_todo_service.py
- [x] T057 [P] [US4] Write unit test for update with empty description (ValidationError) in tests/unit/test_todo_service.py
- [x] T058 [P] [US4] Write integration test for 'edit' command in tests/integration/test_cli_commands.py

**RUN TESTS**: ✅ Verified all US4 tests FAIL (red phase) - proceeding to implementation

### Implementation for User Story 4

- [x] T059 [US4] Implement TodoService.update_task(task_id, new_description) method in src/services/todo_service.py
- [x] T060 [US4] Implement 'edit' command handler in src/cli/menu.py

**RUN TESTS**: ✅ All US4 tests PASS (green phase) - 4/4 tests passing

**Checkpoint**: Task editing works independently

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P5)

**Goal**: Remove unwanted tasks from list

**Independent Test**: Create tasks, delete specific ones by ID, verify removal

### Tests for User Story 5 (TDD - Write FIRST, Verify FAIL) ⚠️

- [x] T061 [P] [US5] Write unit test for TodoService.delete_task(task_id) in tests/unit/test_todo_service.py
- [x] T062 [P] [US5] Write unit test for delete with invalid ID (TaskNotFoundError) in tests/unit/test_todo_service.py
- [x] T063 [P] [US5] Write unit test for delete last task (empty list after) in tests/unit/test_todo_service.py
- [x] T064 [P] [US5] Write integration test for 'delete' command in tests/integration/test_cli_commands.py

**RUN TESTS**: ✅ Verified all US5 tests FAIL (red phase) - proceeding to implementation

### Implementation for User Story 5

- [x] T065 [US5] Implement TodoService.delete_task(task_id) method in src/services/todo_service.py
- [x] T066 [US5] Implement 'delete' command handler in src/cli/menu.py

**RUN TESTS**: ✅ All US5 tests PASS (green phase) - 4/4 tests passing

**Checkpoint**: All user stories are independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T067 [P] Implement 'help' command showing all available commands in src/cli/menu.py
- [x] T068 [P] Implement 'exit' / 'quit' command handlers in src/cli/menu.py
- [x] T069 [P] Add error handling for invalid commands (unknown command name) in src/cli/menu.py
- [x] T070 [P] Add error handling for wrong number of arguments in src/cli/menu.py
- [x] T071 [P] Update README.md with complete usage instructions from quickstart.md
- [x] T072 [P] Add application startup banner/title in main.py
- [x] T073 [P] Add graceful exit message in main.py
- [x] T074 Verify all edge cases are handled (description >500 chars, single task list, etc.)
- [x] T075 Run manual test of complete workflow per quickstart.md 5-minute tutorial
- [x] T076 Verify all constitution principles are satisfied (Phase I constraints, TDD, simplicity)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Independent from other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - Independent from other stories

### Within Each User Story (TDD Workflow)

- Tests MUST be written and FAIL before implementation
- All tests for a story can be written in parallel [P]
- Implementation tasks follow test completion
- Some implementation tasks marked [P] can run in parallel within a story
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (Phase 1)
- All Foundational tasks marked [P] can run in parallel (Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Many implementation tasks within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Write all US1 tests in parallel (TDD red phase):
Task T010: "Write unit test for Task model validation (empty description)"
Task T011: "Write unit test for Task model validation (description >500 chars)"
Task T012: "Write unit test for Task creation"
Task T013: "Write unit test for TodoService.add_task()"
Task T014: "Write unit test for TodoService.list_tasks() - empty"
Task T015: "Write unit test for TodoService.list_tasks() - with tasks"
Task T016: "Write integration test for 'add' command"
Task T017: "Write integration test for 'list' command - with tasks"
Task T018: "Write integration test for 'list' command - empty"

# Verify all tests FAIL (red phase)

# Implement in parallel where possible (TDD green phase):
Task T019: "Implement Task model __init__"  [P]
Task T020: "Implement Task model validate_description()"  [P]
Task T023: "Create TaskFormatter class"  [P]
Task T024: "Implement TaskFormatter display logic"  [P]
# Then sequentially:
Task T021: "Implement TodoService.add_task()" (needs T019, T020)
Task T022: "Implement TodoService.list_tasks()"
Task T025: "Create CommandMenu skeleton"
Task T026: "Implement 'add' command handler" (needs T021)
Task T027: "Implement 'list' command handler" (needs T022, T023)
Task T028: "Create main.py entry point"
Task T029: "Integrate TodoService and CommandMenu"

# Verify all tests PASS (green phase)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only - Recommended Start)

1. Complete Phase 1: Setup (T001-T006)
2. Complete Phase 2: Foundational (T007-T009) - CRITICAL
3. Complete Phase 3: User Story 1 (T010-T029)
   - Write all tests FIRST (T010-T018)
   - RUN tests, verify FAIL (red phase)
   - Implement (T019-T029)
   - RUN tests, verify PASS (green phase)
4. **STOP and VALIDATE**: Test User Story 1 independently per quickstart.md
5. Deploy/demo if ready - YOU HAVE A WORKING TODO APP!

### Incremental Delivery (Add Features Progressively)

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo (task completion tracking)
4. Add User Story 3 → Test independently → Deploy/Demo (smooth interactive UI)
5. Add User Story 4 → Test independently → Deploy/Demo (task editing)
6. Add User Story 5 → Test independently → Deploy/Demo (task deletion)
7. Add Polish Phase → Complete feature

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (T010-T029)
   - Developer B: User Story 2 (T030-T040)
   - Developer C: User Story 3 (T041-T054)
3. Stories complete and integrate independently

---

## Notes

- **[P] tasks** = different files, no dependencies on incomplete tasks
- **[Story] label** maps task to specific user story for traceability
- **TDD MANDATORY**: Constitution Principle IV is NON-NEGOTIABLE
  - Write tests FIRST (T010-T018 for US1, T030-T035 for US2, etc.)
  - Verify tests FAIL (red phase)
  - Implement to make tests PASS (green phase)
  - Refactor with tests passing
- Each user story should be independently completable and testable
- Verify tests fail before implementing (red phase confirmation critical!)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

## Task Count Summary

- **Total Tasks**: 76 tasks
- **Phase 1 (Setup)**: 6 tasks (added uv initialization and pyproject.toml)
- **Phase 2 (Foundational)**: 3 tasks
- **Phase 3 (US1 - MVP)**: 20 tasks (9 tests + 11 implementation)
- **Phase 4 (US2)**: 11 tasks (6 tests + 5 implementation)
- **Phase 5 (US3)**: 14 tasks (5 tests + 9 implementation)
- **Phase 6 (US4)**: 6 tasks (4 tests + 2 implementation)
- **Phase 7 (US5)**: 6 tasks (4 tests + 2 implementation)
- **Phase 8 (Polish)**: 10 tasks

**Parallel Opportunities**: 42 tasks marked [P] can be parallelized within their phases

**MVP Scope**: Phase 1-3 only (29 tasks) delivers working todo app!
