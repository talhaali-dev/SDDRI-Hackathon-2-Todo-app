# Implementation Plan: Menu-Based Todo CLI Navigation

**Branch**: `002-todo-cli-menu` | **Date**: 2026-01-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-todo-cli-menu/spec.md`
**Replaces**: `001-todo-cli` (navigation model only - all business logic reused)

## Summary

Updating the Phase I Todo CLI from command-based workflow to menu-based navigation system. Users will see a numbered menu upon launch and select options by entering numbers (1-6) instead of typing command names. All task management functionality (CRUD operations, validation, storage) remains identical - only the interaction layer changes.

**Technical Approach**: Replace `CommandMenu` and main loop with `MenuNavigator` that displays numbered options and routes selections to existing service methods. The `TodoService`, `Task` model, validation logic, and storage structures from 001-todo-cli are fully reused without modification.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Standard library only (no external packages)
**Storage**: In-memory only (Python list/dict - identical to 001-todo-cli)
**Testing**: unittest (standard library)
**Target Platform**: Local terminal/console (Linux, macOS, Windows)
**Project Type**: Single project (CLI application update)
**Performance Goals**: <1 second response time for all menu operations, immediate menu redisplay
**Constraints**:
  - NO changes to business logic (TodoService, Task model)
  - NO new dependencies (Phase I constraint)
  - NO persistence or external storage
  - Reuse 100% of existing 001-todo-cli models, services, tests
**Scale/Scope**: Single-user, single-session, up to 1000 tasks in memory (unchanged from 001-todo-cli)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Phase-Scoped Development (Principle I)
- ✅ **PASS**: Uses only Phase I allowed technologies (Python 3.13+, standard library)
- ✅ **PASS**: No forward-phase dependencies (no databases, no web frameworks, no external services)
- ✅ **PASS**: In-memory storage respects Phase I constraints
- ✅ **PASS**: Navigation layer change only - business logic unchanged from 001-todo-cli

### Deterministic Behavior (Principle II)
- ✅ **PASS**: All menu selections produce predictable, consistent outputs
- ✅ **PASS**: No hidden state or implicit behavior
- ✅ **PASS**: Menu redisplay after each action is explicit and traceable
- ✅ **PASS**: State transitions (task CRUD) identical to 001-todo-cli (already validated)

### Fail-Safe Error Handling (Principle III)
- ✅ **PASS**: Spec requires validation before state changes (FR-014, FR-015, FR-016, FR-018)
- ✅ **PASS**: Clear error messages required (FR-017 format: "Error: [description]. [corrective action].")
- ✅ **PASS**: Empty state handling specified (edge cases for empty task list)
- ✅ **PASS**: No partial failures possible - atomic operations on in-memory data

### Test-Driven Development (Principle IV)
- ✅ **PASS**: TDD workflow will be followed (tests first, then implementation)
- ✅ **PASS**: All user stories have testable acceptance scenarios
- ✅ **PASS**: Tests will cover menu navigation, input validation, service integration
- ✅ **PASS**: Existing 001-todo-cli tests for TodoService can be reused unchanged

### Simplicity Over Extensibility (Principle V)
- ✅ **PASS**: No speculative features beyond menu navigation requirements
- ✅ **PASS**: Direct implementation of menu display and selection routing
- ✅ **PASS**: No abstractions beyond MenuNavigator class
- ✅ **PASS**: YAGNI principle - only implementing specified menu interaction

### Code Quality Standards (Principle VI)
- ✅ **PASS**: Clear naming for functions (display_menu, get_selection, route_to_handler)
- ✅ **PASS**: Single responsibility - MenuNavigator handles navigation only
- ✅ **PASS**: Code maps directly to user stories (menu creation, selection routing, redisplay)
- ✅ **PASS**: No dead code - every method serves a menu navigation purpose

### Phase I Technology Constraints
- ✅ **PASS**: Python 3.13+ only
- ✅ **PASS**: Standard library only (no curses needed - simple input() sufficient)
- ✅ **PASS**: No persistence mechanisms
- ✅ **PASS**: No external services or network calls
- ✅ **PASS**: Terminal/console interface exclusively

### Constitution Check Result
**STATUS**: ✅ **PASS** (All Gates Clear)

**Note**: This is a navigation-layer update to 001-todo-cli. All business logic (TodoService, Task model, validation, storage) is fully reused and already constitution-compliant from Phase I.

## Project Structure

### Documentation (this feature)

```text
specs/002-todo-cli-menu/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (reuse from 001-todo-cli with notes)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (menu navigation contracts)
│   └── menu-options.md # Menu option definitions and routing
├── checklists/
│   └── requirements.md  # Spec quality checklist (already created)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

**Structure Decision**: Single project structure - this is an update to existing 001-todo-cli codebase. We will modify CLI layer only, preserving all business logic.

```text
src/
├── models/
│   ├── task.py          # Reuse from 001-todo-cli (NO CHANGES)
│   └── exceptions.py    # Reuse from 001-todo-cli (NO CHANGES)
├── services/
│   └── todo_service.py  # Reuse from 001-todo-cli (NO CHANGES)
├── cli/
│   ├── menu_navigator.py  # NEW: Menu-based navigation (replaces CommandMenu)
│   └── interactive.py   # Reuse from 001-todo-cli (optional - interactive mode)
├── ui/
│   └── formatter.py     # Reuse from 001-todo-cli (NO CHANGES)
└── main.py              # MODIFY: Use MenuNavigator instead of CommandMenu

tests/
├── unit/
│   ├── test_task.py     # Reuse from 001-todo-cli (NO CHANGES)
│   └── test_todo_service.py  # Reuse from 001-todo-cli (NO CHANGES)
└── integration/
    ├── test_menu_navigation.py  # NEW: Menu navigation tests
    └── test_cli_commands.py    # UPDATE: Adapt for menu-based interaction
```

**Reuse Strategy**:
- **100% of business logic reused**: Task, TodoService, exceptions, formatter
- **Only CLI layer changes**: Replace CommandMenu with MenuNavigator, update main.py loop
- **Tests reused**: All unit tests for models and services remain identical
- **New tests**: Menu navigation integration tests

## Complexity Tracking

> **No violations detected - this section intentionally left empty**

All constitution principles are satisfied. This is a navigation-layer refactoring that preserves all existing business logic, validation, and storage. The update simplifies user interaction (menu selection vs command typing) without introducing technical complexity.

---

## Phase 0: Research Summary

**Status**: ✅ Complete

**Research Output**: [research.md](./research.md)

**Key Decisions Made**:

1. **Menu Display**: Standard print() statements with formatted text
   - Rationale: Simple, readable, works on all terminals without curses complexity
   - Alternative: curses module (rejected - overkill for simple menu display)

2. **Menu Selection**: input() for user selection, int() for numeric parsing
   - Rationale: Phase I compliant, straightforward validation
   - Supports both numeric (1, 2, 3) and text-based ("add", "view") per FR-003

3. **Navigation Flow**: Infinite loop with menu display → get input → route action → redisplay
   - Rationale: Simple, predictable, matches FR-004 (redisplays after all actions except Exit)
   - Break condition: Exit action selected or KeyboardInterrupt

4. **Code Reuse**: 100% of 001-todo-cli business logic (TodoService, Task, exceptions)
   - Rationale: Avoid duplication, leverages tested implementation
   - MenuNavigator routes to existing TodoService methods unchanged

5. **Testing Strategy**: Reuse existing unit tests, add menu navigation integration tests
   - Rationale: Business logic already validated by 001-todo-cli tests
   - New tests focus on menu display, selection routing, input validation

**All Phase I Constraints Verified**: ✅
- Standard library only (print, input, int)
- No external dependencies
- No persistence mechanisms
- In-memory storage only (unchanged from 001-todo-cli)

---

## Phase 1: Design Summary

**Status**: ✅ Complete

**Design Outputs**:
- [data-model.md](./data-model.md) - Entity definitions (reuse note: identical to 001-todo-cli)
- [contracts/menu-options.md](./contracts/menu-options.md) - Menu structure and routing
- [quickstart.md](./quickstart.md) - User documentation for menu-based workflow

### Data Model

**Note**: Data model is **100% identical to 001-todo-cli**. No changes to Task entity or storage structures.

**Entity**: Task
- **Attributes**: id (int, unique), description (str, 1-500 chars), is_complete (bool), created_at (int)
- **Validation**: Description non-empty, ID positive integer, completion boolean
- **Storage**: Dual structure (dict for lookups + list for ordered display) - **unchanged from 001-todo-cli**
- **Operations**: O(1) create/read/update, O(n) delete/list - **unchanged from 001-todo-cli**

### Menu Option Contracts

**Menu Structure** (FR-002):
```
=== TODO MENU ===
1. Add Task
2. View Tasks
3. Toggle Complete
4. Update Task
5. Delete Task
6. Exit
```

**6 Menu Options Defined**:

**Option 1: Add Task**
- Input: Task description (string, 1-500 chars)
- Action: Call `service.add_task(description)`
- Output: Confirmation message, redisplay menu
- Validation: FR-014 (non-empty), FR-015 (max 500 chars)

**Option 2: View Tasks**
- Input: None
- Action: Call `service.list_tasks()`, format with TaskFormatter
- Output: Task list display, prompt to press Enter, redisplay menu
- Edge Case: Empty list → friendly message

**Option 3: Toggle Complete**
- Input: Task ID (integer)
- Action: Call `service.mark_complete()` or `service.mark_incomplete()` based on current status
- Output: Confirmation message, redisplay menu
- Validation: FR-016 (ID exists), FR-018 (numeric input)

**Option 4: Update Task**
- Input: Task ID (integer), new description (string, 1-500 chars)
- Action: Call `service.update_task(task_id, new_description)`
- Output: Confirmation message, redisplay menu
- Validation: FR-016 (ID exists), FR-014 (non-empty), FR-015 (max 500 chars), FR-018 (numeric input)

**Option 5: Delete Task**
- Input: Task ID (integer)
- Action: Call `service.delete_task(task_id)`
- Output: Confirmation message, redisplay menu
- Validation: FR-016 (ID exists), FR-018 (numeric input)

**Option 6: Exit**
- Input: None
- Action: Display goodbye message, break loop
- Output: Goodbye message, application termination

**Error Handling Contract**:
- Format: "Error: [description]. [corrective action]." (FR-017)
- Categories: Menu validation, Input validation, Task operations
- All mapped to FR-005, FR-014-018

**Performance Guarantees**:
- Menu operations: <1 second response time
- Menu redisplay: Immediate (fr-004)
- Task operations: Identical to 001-todo-cli (already validated)

### Quickstart Guide

Complete user documentation created covering:
- Installation (none required - standard library)
- Menu-based workflow tutorial (step-by-step)
- Menu option reference table
- Input selection methods (numeric and text-based)
- Common tasks and best practices
- Troubleshooting section
- Differences from command-based workflow (001-todo-cli)
- Phase I limitations and scope

---

## Constitution Re-Check (Post-Design)

**Status**: ✅ **PASS** (All Gates Clear)

### Updated Assessment

All constitution principles remain satisfied after design phase:

✅ **Phase-Scoped Development**: No Phase II+ dependencies introduced. Menu display uses print/input (standard library).
✅ **Deterministic Behavior**: Menu flow is explicit and predictable. All selections route deterministically to service methods.
✅ **Fail-Safe Error Handling**: Input validation before menu routing. Clear error messages per FR-017.
✅ **Test-Driven Development**: TDD workflow defined. Tests will cover menu navigation, input validation, service integration.
✅ **Simplicity Over Extensibility**: Direct menu implementation. No menu framework or abstraction layer.
✅ **Code Quality Standards**: Clear separation - MenuNavigator handles navigation, TodoService handles business logic.

**Reuse Validation**:
- ✅ All 001-todo-cli business logic preserved without modification
- ✅ All 001-todo-cli unit tests reusable without changes
- ✅ Constitution compliance inherited from validated 001-todo-cli implementation

---

## Next Steps

### Ready for Implementation

**Phase 1 Complete**: Planning finished. Next command: `/sp.tasks 002-todo-cli-menu`

The `/sp.tasks` command will generate:
- `tasks.md` - Dependency-ordered task list for menu navigation implementation
- Tasks organized by user story (P1-P4)
- Test tasks before implementation tasks (TDD workflow)
- Parallel task opportunities marked
- Clear indication of which 001-todo-cli code to reuse vs what to create new

### Implementation Readiness Checklist

- [x] Specification complete and validated
- [x] Technical context defined
- [x] Constitution gates passed
- [x] Research decisions documented
- [x] Data model verified (reuse confirmed)
- [x] Menu option contracts specified
- [x] User documentation drafted
- [x] Project structure defined (reuse strategy clear)
- [ ] Tasks generated (next step: `/sp.tasks`)
- [ ] Tests written (TDD red phase)
- [ ] Implementation (TDD green phase)
- [ ] Refactoring (TDD refactor phase)

### Estimated Scope

**Implementation Complexity**: Low (navigation layer update only)
- ~1 new Python module (MenuNavigator)
- ~5 functions/methods (display_menu, get_selection, route_to_handler, input handlers)
- ~100-150 lines of production code (menu display and routing)
- ~150-200 lines of integration tests (menu navigation tests)
- Standard library only (no dependency management)
- **0 lines changed** in business logic (TodoService, Task model - full reuse)

**User Stories**: 4 prioritized stories (P1-P4)
**Functional Requirements**: 21 requirements
**Success Criteria**: 7 measurable outcomes

**Key Advantage**: 100% of business logic and unit tests from 001-todo-cli are reused. Only the CLI interaction layer changes, significantly reducing implementation effort and risk.
