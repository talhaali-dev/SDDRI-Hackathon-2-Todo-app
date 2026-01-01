# Implementation Plan: Phase I Todo List CLI

**Branch**: `001-todo-cli` | **Date**: 2026-01-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-cli/spec.md`

## Summary

Building an in-memory CLI todo application for Phase I with smooth interactive user experience. The application provides complete task management (CRUD operations) through both command-based and interactive keyboard-driven interfaces. Core functionality includes task creation, viewing, completion tracking, editing, and deletion - all stored in memory during the session. Interactive mode enables arrow key navigation and spacebar toggling for efficient task management.

**Technical Approach**: Single Python CLI application using standard library for core logic with curses module for interactive terminal UI. In-memory storage using Python lists/dictionaries. Command pattern for menu operations. Test-driven development with pytest (standard library unittest as fallback).

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Standard library only (curses for interactive UI, unittest for testing)
**Storage**: In-memory only (Python list/dict data structures) - NO persistence
**Testing**: unittest (standard library) or pytest if allowed as dev dependency
**Target Platform**: Local terminal/console (Linux, macOS, Windows with appropriate terminal support)
**Project Type**: Single project (CLI application)
**Performance Goals**: <1 second response time for all commands, <2 seconds to display up to 1000 tasks
**Constraints**:
  - NO external dependencies for core logic (Phase I constraint)
  - NO persistence (files, databases, or external storage)
  - NO network calls or external services
  - In-memory storage only
  - Terminal/console interface exclusively
**Scale/Scope**: Single-user, single-session, up to 1000 tasks in memory

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Phase-Scoped Development (Principle I)
- ✅ **PASS**: Uses only Phase I allowed technologies (Python 3.13+, standard library)
- ✅ **PASS**: No forward-phase dependencies (no databases, no web frameworks, no external services)
- ✅ **PASS**: In-memory storage respects Phase I constraints
- ⚠️ **CLARIFICATION NEEDED**: Curses module (standard library) for interactive UI - verify acceptable for Phase I

### Deterministic Behavior (Principle II)
- ✅ **PASS**: All commands produce predictable, consistent outputs
- ✅ **PASS**: No random or non-deterministic operations
- ✅ **PASS**: State transitions are explicit (task creation, completion toggle, deletion)
- ✅ **PASS**: Interactive mode has clear, traceable navigation behavior

### Fail-Safe Error Handling (Principle III)
- ✅ **PASS**: Spec requires validation before state changes (FR-011)
- ✅ **PASS**: Clear error messages required for all invalid operations
- ✅ **PASS**: Empty state handling specified (empty task list messages)
- ✅ **PASS**: No partial failures possible (atomic operations on in-memory data)

### Test-Driven Development (Principle IV)
- ✅ **PASS**: TDD workflow will be followed (tests first, then implementation)
- ✅ **PASS**: All user stories have testable acceptance scenarios
- ✅ **PASS**: Unit tests for task operations, integration tests for CLI workflows

### Simplicity Over Extensibility (Principle V)
- ✅ **PASS**: No speculative features beyond spec requirements
- ✅ **PASS**: Direct implementation of CRUD operations without unnecessary abstraction
- ✅ **PASS**: Simple data structures (list/dict for task storage)
- ✅ **PASS**: YAGNI principle - only implementing specified P1-P5 user stories

### Code Quality Standards (Principle VI)
- ✅ **PASS**: Clear naming for functions (add_task, mark_complete, etc.)
- ✅ **PASS**: Single responsibility - separate modules for models, CLI, interactive UI
- ✅ **PASS**: Code maps directly to tasks from tasks.md
- ✅ **PASS**: No dead code or speculative abstractions

### Phase I Technology Constraints
- ✅ **PASS**: Python 3.13+ only
- ✅ **PASS**: Standard library only (curses module for interactive UI)
- ✅ **PASS**: No persistence mechanisms
- ✅ **PASS**: No external services or network calls
- ✅ **PASS**: Terminal/console interface exclusively

### Constitution Check Result
**STATUS**: ✅ **PASS WITH CLARIFICATION**

**Clarification Required**:
- Verify curses module (Python standard library) is acceptable for interactive UI in Phase I. Constitution states "standard library only" for core logic and allows external libraries "ONLY for CLI interaction enhancements". Curses is standard library, so should be acceptable, but requires confirmation during research phase.

**Alternative if curses not allowed**: Implement basic menu system with input() for command selection (degrades UX for P3 interactive mode but maintains functionality).

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-cli/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   └── cli-commands.md  # Command interface definitions
├── checklists/
│   └── requirements.md  # Spec quality checklist (already created)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/
│   └── task.py          # Task entity with validation
├── services/
│   └── todo_service.py  # Business logic for task operations
├── cli/
│   ├── menu.py          # Command menu and user input handling
│   └── interactive.py   # Interactive mode (arrow keys, spacebar)
├── ui/
│   └── formatter.py     # Display formatting and status indicators
└── main.py              # Application entry point

tests/
├── unit/
│   ├── test_task.py     # Task model unit tests
│   └── test_todo_service.py  # Service layer unit tests
└── integration/
    ├── test_cli_commands.py   # End-to-end CLI command tests
    └── test_interactive_mode.py  # Interactive mode integration tests

README.md                # Basic usage instructions
```

**Structure Decision**: Single project structure selected. This is a standalone CLI application with no frontend/backend separation needed. The `src/` directory contains the application code organized by concerns (models, services, cli, ui), and `tests/` mirrors this structure. Simple, flat hierarchy appropriate for Phase I scope.

## Complexity Tracking

> **No violations detected - this section intentionally left empty**

All constitution principles are satisfied. No complexity justifications required.

---

## Phase 0: Research Summary

**Status**: ✅ Complete

**Research Output**: [research.md](./research.md)

**Key Decisions Made**:

1. **Interactive UI Library**: Python curses module (standard library)
   - Rationale: Phase I compliant, full terminal control, zero dependencies
   - Alternative: Basic input() menus (fallback if curses unavailable)

2. **Data Storage**: dict + list combination for in-memory storage
   - Rationale: O(1) lookups, maintains creation order, simple
   - Structure: `tasks_by_id: dict[int, Task]` + `tasks_ordered: list[Task]`

3. **Testing Framework**: unittest (standard library)
   - Rationale: Phase I compliant, supports unit + integration tests
   - Note: pytest migration possible in Phase II if desired

4. **Error Handling**: Custom exception hierarchy
   - Classes: TodoError, ValidationError, TaskNotFoundError, EmptyTaskListError
   - Rationale: Clear error types, testable, user-friendly messages

5. **Display Formatting**: Unicode checkboxes [ ] and [✓]
   - Rationale: Clear visual distinction, terminal-agnostic
   - Fallback: ASCII [ ] and [X] if Unicode fails

6. **Application Flow**: Menu-driven command loop with mode switching
   - Modes: Command mode (text commands) + Interactive mode (curses UI)
   - Rationale: Supports all P1-P5 user stories, testable architecture

**All Phase I Constraints Verified**: ✅
- Standard library only (curses, unittest)
- No external dependencies
- No persistence mechanisms
- In-memory storage only

---

## Phase 1: Design Summary

**Status**: ✅ Complete

**Design Outputs**:
- [data-model.md](./data-model.md) - Entity definitions and storage strategy
- [contracts/cli-commands.md](./contracts/cli-commands.md) - CLI interface specification
- [quickstart.md](./quickstart.md) - User documentation and usage guide

### Data Model

**Entity**: Task
- **Attributes**: id (int, unique), description (str, 1-500 chars), is_complete (bool), created_at (int)
- **Validation**: Description non-empty, ID positive integer, completion boolean
- **Storage**: Dual structure (dict for lookups + list for ordered display)
- **Consistency**: Synchronized add/delete operations maintain invariants

### API Contracts

**Commands Defined** (9 total):
1. `add <description>` - Create task (P1)
2. `list` - View all tasks (P1)
3. `complete <id>` - Mark complete (P2)
4. `uncomplete <id>` - Mark incomplete (P2)
5. `edit <id> <new_description>` - Update description (P4)
6. `delete <id>` - Remove task (P5)
7. `interactive` - Enter interactive mode (P3)
8. `help` - Show command help
9. `exit` / `quit` - Quit application

**Error Handling Contract**:
- Format: `Error: <description>. <corrective action>.`
- Categories: Validation, Not Found, Command errors
- All mapped to FR-011 requirement

**Performance Guarantees**:
- Commands: <1 second response time
- List display: <2 seconds (up to 1000 tasks)
- Interactive toggle: Immediate visual feedback

### Quickstart Guide

Complete user documentation created covering:
- Installation (none required - standard library)
- Basic workflow tutorial (5-minute quickstart)
- Command reference table
- Interactive mode guide
- Common tasks and best practices
- Troubleshooting section
- Phase I limitations and future roadmap

---

## Constitution Re-Check (Post-Design)

**Status**: ✅ **PASS** (All Gates Clear)

### Updated Assessment

All constitution principles remain satisfied after design phase:

✅ **Phase-Scoped Development**: No Phase II+ dependencies introduced
✅ **Deterministic Behavior**: All commands have predictable outputs
✅ **Fail-Safe Error Handling**: Validation-first design, clear error messages
✅ **Test-Driven Development**: TDD workflow defined, test strategy documented
✅ **Simplicity Over Extensibility**: Direct CRUD implementation, no speculative features
✅ **Code Quality Standards**: Clear module separation (models, services, cli, ui)

**Clarification Resolved**: Curses module confirmed acceptable (Python standard library, explicitly allowed for CLI interaction enhancements per constitution).

---

## Next Steps

### Ready for Implementation

**Phase 2 Complete**: Planning finished. Next command: `/sp.tasks 001-todo-cli`

The `/sp.tasks` command will generate:
- `tasks.md` - Dependency-ordered task list for implementation
- Tasks organized by user story (P1-P5)
- Test tasks before implementation tasks (TDD workflow)
- Parallel task opportunities marked

### Implementation Readiness Checklist

- [x] Specification complete and validated
- [x] Technical context defined
- [x] Constitution gates passed
- [x] Research decisions documented
- [x] Data model designed
- [x] API contracts specified
- [x] User documentation drafted
- [x] Project structure defined
- [ ] Tasks generated (next step: `/sp.tasks`)
- [ ] Tests written (TDD red phase)
- [ ] Implementation (TDD green phase)
- [ ] Refactoring (TDD refactor phase)

### Estimated Scope

**Implementation Complexity**: Medium
- ~6-8 Python modules
- ~15 functions/methods
- ~200-300 lines of production code
- ~300-400 lines of test code
- Standard library only (no dependency management)

**User Stories**: 5 prioritized stories (P1-P5)
**Functional Requirements**: 15 requirements
**Success Criteria**: 8 measurable outcomes

---

## Appendix: File Checklist

### Planning Artifacts Created

- [x] `plan.md` - This file (implementation plan)
- [x] `research.md` - Phase 0 research findings
- [x] `data-model.md` - Entity and storage design
- [x] `contracts/cli-commands.md` - CLI interface contract
- [x] `quickstart.md` - User guide and documentation
- [x] `spec.md` - Feature specification (created by /sp.specify)
- [x] `checklists/requirements.md` - Spec quality checklist (created by /sp.specify)

### Next Artifacts (To Be Created)

- [ ] `tasks.md` - Implementation task list (created by /sp.tasks)

### Source Code Structure (To Be Implemented)

```
src/
├── models/task.py          # Task entity [P1]
├── services/todo_service.py # Business logic [P1-P5]
├── cli/menu.py             # Command menu [P1-P5]
├── cli/interactive.py      # Interactive mode [P3]
├── ui/formatter.py         # Display formatting [P1]
└── main.py                 # Entry point [P1]

tests/
├── unit/test_task.py                # [P1]
├── unit/test_todo_service.py        # [P1-P5]
├── integration/test_cli_commands.py # [P1-P5]
└── integration/test_interactive_mode.py # [P3]
```
