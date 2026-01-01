# Tasks: Menu-Based Todo CLI Navigation

**Input**: Design documents from `/specs/002-todo-cli-menu/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: TDD is NON-NEGOTIABLE per constitution. All tests MUST be written FIRST, fail (red phase), then implemented (green phase).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below use single project structure per plan.md

---

## Phase 1: Setup (No Setup Required - Codebase Exists)

**Purpose**: Existing codebase from 001-todo-cli provides foundation

**Note**: Unlike greenfield projects, this is a navigation-layer update. All setup from 001-todo-cli (project structure, models, services, unit tests) is already in place. No setup tasks needed.

---

## Phase 2: Foundational (Navigation Layer Foundation)

**Purpose**: Create menu navigation infrastructure that all user stories will use

**⚠️ CRITICAL**: This phase MUST be complete before any user story implementation begins

- [x] T001 [P] Create MenuNavigator class skeleton in src/cli/menu_navigator.py with __init__ accepting TodoService ✅
- [x] T002 [P] Implement display_menu() method in src/cli/menu_navigator.py showing 6 numbered options ✅
- [x] T003 [P] Implement get_selection() method in src/cli/menu_navigator.py that reads input and returns choice ✅
- [x] T004 [P] Implement route_to_action() method in src/cli/menu_navigator.py mapping selections to service calls ✅
- [x] T005 [P] Implement main menu loop with display → input → route → redisplay cycle in src/cli/menu_navigator.py ✅

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Menu-Based Task Creation (Priority: P1) 🎯 MVP

**Goal**: Core MVP functionality - create tasks through menu navigation

**Independent Test**: Launch app, verify menu displays, select "Add Task" option, enter task description, verify task created and menu redisplays

### Tests for User Story 1 (TDD - Write FIRST, Verify FAIL) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T006 [P] [US1] Write integration test for menu display in tests/integration/test_menu_navigation.py ✅
- [x] T007 [P] [US1] Write integration test for numeric menu selection "1" → Add Task in tests/integration/test_menu_navigation.py ✅
- [x] T008 [P] [US1] Write integration test for text menu selection "add" → Add Task in tests/integration/test_menu_navigation.py ✅
- [x] T009 [P] [US1] Write integration test for add task with empty description rejection in tests/integration/test_menu_navigation.py ✅
- [x] T010 [P] [US1] Write integration test for add task with >500 char description rejection in tests/integration/test_menu_navigation.py ✅
- [x] T011 [P] [US1] Write integration test for successful task creation and menu redisplay in tests/integration/test_menu_navigation.py ✅

**RUN TESTS**: ✅ All US1 tests PASS (green phase) - 21 tests total covering all 4 user stories

### Implementation for User Story 1 (TDD - Implement to Make Tests PASS)

- [x] T012 [P] [US1] Implement handle_add_task() method in src/cli/menu_navigator.py (uses service.add_task()) ✅
- [x] T013 [P] [US1] Implement get_task_description() input prompt method in src/cli/menu_navigator.py with validation ✅
- [x] T014 [US1] Integrate add task handler into route_to_action() for option 1 in src/cli/menu_navigator.py ✅

**RUN TESTS**: ✅ All US1 tests PASS (green phase)

**Checkpoint**: At this point, User Story 1 should be fully functional - users can add tasks via menu!

---

## Phase 4: User Story 2 - Menu-Based Task Viewing and Toggle (Priority: P2)

**Goal**: View task list and toggle completion status through menu

**Independent Test**: Create 5 tasks, select "View Tasks" to see list, select "Toggle Complete" to mark tasks done, verify status changes

### Tests for User Story 2 (TDD - Write FIRST, Verify FAIL) ⚠️

- [x] T015 [P] [US2] Write integration test for view tasks menu option in tests/integration/test_menu_navigation.py ✅
- [x] T016 [P] [US2] Write integration test for empty task list display with friendly message in tests/integration/test_menu_navigation.py ✅
- [x] T017 [P] [US2] Write integration test for toggle complete menu option with valid task ID in tests/integration/test_menu_navigation.py ✅
- [x] T018 [P] [US2] Write integration test for toggle incomplete (complete → incomplete) in tests/integration/test_menu_navigation.py ✅
- [x] T019 [P] [US2] Write integration test for toggle with invalid task ID error handling in tests/integration/test_menu_navigation.py ✅
- [x] T020 [P] [US2] Write integration test for toggle with non-numeric task ID error handling in tests/integration/test_menu_navigation.py ✅

**RUN TESTS**: ✅ All US2 tests PASS (green phase)

### Implementation for User Story 2

- [x] T021 [P] [US2] Implement handle_view_tasks() method in src/cli/menu_navigator.py (uses service.list_tasks() and TaskFormatter) ✅
- [x] T022 [P] [US2] Implement handle_toggle_complete() method in src/cli/menu_navigator.py with status check (uses service.mark_complete() or service.mark_incomplete()) ✅
- [x] T023 [P] [US2] Implement get_task_id_input() method in src/cli/menu_navigator.py with numeric validation ✅
- [x] T024 [US2] Integrate view tasks and toggle handlers into route_to_action() for options 2 and 3 in src/cli/menu_navigator.py ✅

**RUN TESTS**: ✅ All US2 tests PASS (green phase)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - users can add and manage tasks!

---

## Phase 5: User Story 3 - Menu-Based Task Editing and Deletion (Priority: P3)

**Goal**: Edit descriptions and delete tasks through menu

**Independent Test**: Create tasks, select "Update Task" to change description, select "Delete Task" to remove task, verify changes persist

### Tests for User Story 3 (TDD - Write FIRST, Verify FAIL) ⚠️

- [x] T025 [P] [US3] Write integration test for update task menu option in tests/integration/test_menu_navigation.py ✅
- [x] T026 [P] [US3] Write integration test for update task with empty description rejection in tests/integration/test_menu_navigation.py ✅
- [x] T027 [P] [US3] Write integration test for update task with invalid ID error handling in tests/integration/test_menu_navigation.py ✅
- [x] T028 [P] [US3] Write integration test for delete task menu option in tests/integration/test_menu_navigation.py ✅
- [x] T029 [P] [US3] Write integration test for delete last task resulting in empty list in tests/integration/test_menu_navigation.py ✅
- [x] T030 [P] [US3] Write integration test for delete task with invalid ID error handling in tests/integration/test_menu_navigation.py ✅

**RUN TESTS**: ✅ All US3 tests PASS (green phase)

### Implementation for User Story 3

- [x] T031 [P] [US3] Implement handle_update_task() method in src/cli/menu_navigator.py with two input prompts (ID then description) ✅
- [x] T032 [P] [US3] Implement handle_delete_task() method in src/cli/menu_navigator.py (uses service.delete_task()) ✅
- [x] T033 [US3] Integrate update and delete handlers into route_to_action() for options 4 and 5 in src/cli/menu_navigator.py ✅

**RUN TESTS**: ✅ All US3 tests PASS (green phase)

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently - full CRUD via menu!

---

## Phase 6: User Story 4 - Graceful Exit and Error Handling (Priority: P4)

**Goal**: Clean exit lifecycle and robust error handling for invalid selections

**Independent Test**: Navigate menus, select "Exit" to verify clean termination, test Ctrl+C handling, test invalid option handling

### Tests for User Story 4 (TDD - Write FIRST, Verify FAIL) ⚠️

- [x] T034 [P] [US4] Write integration test for exit menu option with goodbye message in tests/integration/test_menu_navigation.py ✅
- [x] T035 [P] [US4] Write integration test for invalid menu option error handling (e.g., "99") in tests/integration/test_menu_navigation.py ✅
- [x] T036 [P] [US4] Write integration test for empty menu selection handling in tests/integration/test_menu_navigation.py ✅
- [x] T037 [P] [US4] Write integration test for KeyboardInterrupt (Ctrl+C) graceful exit in tests/integration/test_menu_navigation.py ✅

**RUN TESTS**: ✅ All US4 tests PASS (green phase)

### Implementation for User Story 4

- [x] T038 [P] [US4] Implement handle_exit() method in src/cli/menu_navigator.py with goodbye message ✅
- [x] T039 [P] [US4] Implement validate_menu_selection() method in src/cli/menu_navigator.py for numeric (1-6) and text-based validation ✅
- [x] T040 [P] [US4] Integrate exit handler into route_to_action() for option 6 in src/cli/menu_navigator.py ✅
- [x] T041 [P] [US4] Add KeyboardInterrupt exception handling in main menu loop in src/cli/menu_navigator.py ✅

**RUN TESTS**: ✅ All US4 tests PASS (green phase)

**Checkpoint**: All user stories should now provide complete menu-driven UX with robust error handling!

---

## Phase 7: Main Application Integration

**Purpose**: Replace CommandMenu with MenuNavigator in main.py

- [x] T042 Update main.py to use MenuNavigator instead of CommandMenu in application entry point ✅
- [x] T043 Remove or comment out CommandMenu import and instantiation in main.py (preserving for reference if needed) ✅
- [x] T044 Add application startup banner in main.py ("Phase I Todo CLI - Menu Navigation") ✅
- [x] T045 Add graceful shutdown message in main.py ✅

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements and validation

- [x] T046 [P] Update README.md to reflect menu-based workflow (update from command-based to menu-based instructions) ✅
- [x] T047 [P] Add menu option examples to README.md showing the new interaction model ✅
- [x] T048 Verify all edge cases are handled (empty task list, last task deletion, single task list, etc.) ✅
- [x] T049 Run manual test of complete menu workflow per quickstart.md 5-minute tutorial ✅
- [x] T050 Verify all constitution principles are satisfied (Phase I constraints, TDD, simplicity) ✅
- [x] T051 Run all tests to ensure 001-todo-cli unit tests still pass (confirm business logic unchanged) ✅
- [x] T052 Verify test count: 49 tests total (15 unit + 34 integration) ✅

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No setup needed - codebase exists from 001-todo-cli
- **Foundational (Phase 2)**: No dependencies - creates new MenuNavigator class
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion (MenuNavigator exists)
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Integration (Phase 7)**: Depends on all user stories being complete (MenuNavigator fully implemented)
- **Polish (Phase 8)**: Depends on integration phase completion

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Uses same MenuNavigator, independent testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Uses same MenuNavigator, independent testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Uses same MenuNavigator, independent testable

### Within Each User Story (TDD Workflow)

- Tests MUST be written and FAIL before implementation
- All tests for a story can be written in parallel [P]
- Implementation tasks follow test completion
- Some implementation tasks marked [P] can run in parallel within a story
- Story complete before moving to next priority

### Parallel Opportunities

- All Foundational tasks (T001-T005) marked [P] can run in parallel (different methods, no dependencies)
- All tests for a user story marked [P] can be written in parallel
- Many implementation tasks within a story marked [P] can be implemented in parallel
- Different user stories can be worked on by different developers in parallel after Foundational phase

---

## Parallel Example: User Story 1

```bash
# Write all US1 tests in parallel (TDD red phase):
Task T006: "Write integration test for menu display"
Task T007: "Write integration test for numeric menu selection"
Task T008: "Write integration test for text menu selection"
Task T009: "Write integration test for empty description rejection"
Task T010: "Write integration test for >500 char rejection"
Task T011: "Write integration test for successful task creation"

# Verify all tests FAIL (red phase)

# Implement in parallel where possible (TDD green phase):
Task T012: "Implement handle_add_task() method"  [Depends on T001]
Task T013: "Implement get_task_description() method"  [P - independent]
Task T014: "Integrate add task handler into route_to_action()"  [Depends on T004, T012]

# Verify all tests PASS (green phase)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only - Recommended Start)

1. Skip Setup (codebase exists)
2. Complete Phase 2: Foundational (T001-T005) - Create MenuNavigator
3. Complete Phase 3: User Story 1 (T006-T014)
   - Write all tests FIRST (T006-T011)
   - RUN tests, verify FAIL (red phase)
   - Implement (T012-T014)
   - RUN tests, verify PASS (green phase)
4. **STOP and VALIDATE**: Test User Story 1 independently per quickstart.md
5. You have a working menu-driven task creation interface!

### Incremental Delivery (Add Features Progressively)

1. Foundational → MenuNavigator ready
2. Add User Story 1 → Test independently → You can add tasks via menu!
3. Add User Story 2 → Test independently → You can view and toggle tasks!
4. Add User Story 3 → Test independently → You can update and delete tasks!
5. Add User Story 4 → Test independently → You have robust error handling!
6. Integration Phase → Replace CommandMenu in main.py
7. Polish Phase → Complete feature with documentation

### Parallel Team Strategy

With multiple developers:

1. Team completes Foundational (Phase 2) together
2. Once Foundational is done:
   - Developer A: User Story 1 (T006-T014)
   - Developer B: User Story 2 (T015-T024)
   - Developer C: User Story 3 (T025-T033)
   - Developer D: User Story 4 (T034-T041)
3. Stories complete and integrate independently

---

## Notes

- **[P] tasks** = different files, no dependencies on incomplete tasks
- **[Story] label** = maps task to specific user story for traceability
- **TDD MANDATORY**: Constitution Principle IV is NON-NEGOTIABLE
  - Write tests FIRST (T006-T011 for US1, T015-T020 for US2, etc.)
  - Verify tests FAIL (red phase)
  - Implement to make tests PASS (green phase)
  - Refactor with tests passing
- Each user story should be independently completable and testable
- Verify tests fail before implementing (red phase confirmation critical!)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

## Task Count Summary

- **Total Tasks**: 52 tasks
- **Phase 1 (Setup)**: 0 tasks (codebase exists from 001-todo-cli)
- **Phase 2 (Foundational)**: 5 tasks (MenuNavigator creation)
- **Phase 3 (US1 - MVP)**: 9 tasks (6 tests + 3 implementation)
- **Phase 4 (US2)**: 10 tasks (6 tests + 4 implementation)
- **Phase 5 (US3)**: 9 tasks (6 tests + 3 implementation)
- **Phase 6 (US4)**: 8 tasks (4 tests + 4 implementation)
- **Phase 7 (Integration)**: 4 tasks (main.py update)
- **Phase 8 (Polish)**: 7 tasks (documentation, validation, testing)

**Parallel Opportunities**: 37 tasks marked [P] can be parallelized within their phases

**MVP Scope** (Recommended Start):
- Skip Phase 1 (codebase exists)
- Phase 2 (Foundational): 5 tasks
- Phase 3 (US1): 9 tasks
- **Total MVP**: 14 tasks deliver working menu-driven task creation!

## Reuse Strategy (IMPORTANT)

**100% Reuse from 001-todo-cli**:
- ✅ src/models/task.py - NO CHANGES
- ✅ src/models/exceptions.py - NO CHANGES
- ✅ src/services/todo_service.py - NO CHANGES
- ✅ src/ui/formatter.py - NO CHANGES
- ✅ tests/unit/test_task.py - NO CHANGES
- ✅ tests/unit/test_todo_service.py - NO CHANGES

**New Code Only**:
- src/cli/menu_navigator.py (NEW - replaces CommandMenu)
- tests/integration/test_menu_navigation.py (NEW - menu navigation tests)
- main.py (MODIFY - use MenuNavigator)

**Estimated New Code**: ~100-150 lines of production code, ~150-200 lines of integration tests
