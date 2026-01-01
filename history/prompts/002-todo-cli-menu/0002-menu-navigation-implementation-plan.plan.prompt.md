---
id: 0002
title: Menu Navigation Implementation Plan
stage: plan
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: 002-todo-cli-menu
branch: 002-todo-cli-menu
user: user
command: /sp.plan
labels: ["plan", "phase-i", "menu-navigation", "reuse-strategy", "architecture"]
links:
  spec: specs/002-todo-cli-menu/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/002-todo-cli-menu/plan.md
  - specs/002-todo-cli-menu/research.md
  - specs/002-todo-cli-menu/data-model.md
  - specs/002-todo-cli-menu/contracts/menu-options.md
  - specs/002-todo-cli-menu/quickstart.md
tests:
  - N/A (planning artifacts)
---

## Prompt

/sp.plan

## Response snapshot

Generated complete implementation plan for Phase I Menu-Based Todo CLI Navigation with Phase 0 research and Phase 1 design artifacts.

**Planning Workflow**:
- ✅ Phase 0 (Research): Technical decisions for menu navigation
- ✅ Phase 1 (Design): Data model confirmation, menu option contracts, user documentation
- ✅ Constitution Check: All gates passed (100% reuse of validated business logic)

**Key Technical Decisions** (Phase 0 Research):

1. **Menu Display**: Standard print() statements with formatted text
   - Rationale: Phase I compliant, universally compatible, simple
   - Alternative: curses module (rejected - overkill for simple menu)

2. **Menu Selection**: input() for user selection, int() for numeric parsing
   - Rationale: Phase I compliant, straightforward validation
   - Supports both numeric (1-6) and text-based ("add", "view", "exit") per FR-003

3. **Navigation Flow**: Infinite loop with menu display → get input → route action → redisplay
   - Rationale: Simple, predictable, matches FR-004 requirement
   - Break conditions: Exit option or KeyboardInterrupt (Ctrl+C)

4. **Code Reuse**: 100% reuse of 001-todo-cli business logic
   - Rationale: Avoid duplication, leverages tested implementation
   - TodoService, Task model, exceptions, formatter reused unchanged
   - MenuNavigator routes to existing service methods

5. **Testing Strategy**: Reuse existing unit tests + add menu navigation integration tests
   - Rationale: Business logic already validated
   - New tests focus on menu display, selection routing, input validation

**Data Model Design** (Phase 1):

**Confirmation**: Data model is 100% identical to 001-todo-cli (NO CHANGES)
- Task entity: id, description, is_complete, created_at (unchanged)
- Storage: Dual structure - tasks_by_id (dict) + tasks_ordered (list) (unchanged)
- All validation rules preserved (unchanged)
- All operations and complexity preserved (unchanged)

**Menu Option Contracts** (Phase 1):

**6 Menu Options Defined**:
1. **Add Task** - Input: description, Action: service.add_task(), Output: confirmation + redisplay
2. **View Tasks** - Input: none, Action: service.list_tasks() + format, Output: display + press Enter prompt
3. **Toggle Complete** - Input: task ID, Action: toggle based on current status, Output: confirmation + redisplay
4. **Update Task** - Input: task ID + new description, Action: service.update_task(), Output: confirmation + redisplay
5. **Delete Task** - Input: task ID, Action: service.delete_task(), Output: confirmation + redisplay
6. **Exit** - Input: none, Action: break loop, Output: goodbye message + termination

**Error Handling Contract**:
- Format: "Error: [description]. [corrective action]."
- Categories: Menu validation, Input validation, Task operations
- All mapped to FR-005, FR-014-018

**Performance Guarantees**:
- Menu operations: <1 second response time
- Menu redisplay: <100ms (instantaneous)
- Task operations: identical to 001-todo-cli (already validated)

**Quickstart Guide** (Phase 1):

Complete user documentation created covering:
- Installation (none required - standard library)
- 5-minute tutorial workflow (step-by-step menu navigation)
- Menu option reference table (aliases, inputs, descriptions)
- Input selection methods (numeric and text-based)
- Common tasks and best practices
- Troubleshooting section
- Differences from command-based workflow (001-todo-cli comparison table)
- Phase I limitations and future roadmap

**Constitution Check Results**:

✅ All Principles PASS:
- Phase-Scoped Development: No Phase II+ dependencies, standard library only
- Deterministic Behavior: All menu selections produce predictable outputs
- Fail-Safe Error Handling: Validation-first design, clear error messages
- Test-Driven Development: TDD workflow defined, test strategy documented
- Simplicity Over Extensibility: Direct menu implementation, no abstractions
- Code Quality Standards: Clear separation - MenuNavigator handles navigation, TodoService handles business logic

**Reuse Validation**:
- ✅ All 001-todo-cli business logic preserved without modification
- ✅ All 001-todo-cli unit tests reusable without changes
- ✅ Constitution compliance inherited from validated implementation

**Project Structure**:

Single project structure (update to existing 001-todo-cli codebase):
```
src/
├── models/              # REUSE from 001-todo-cli (NO CHANGES)
├── services/            # REUSE from 001-todo-cli (NO CHANGES)
├── cli/
│   ├── menu_navigator.py  # NEW: Menu-based navigation (replaces CommandMenu)
│   └── interactive.py     # REUSE from 001-todo-cli (optional)
├── ui/                  # REUSE from 001-todo-cli (NO CHANGES)
└── main.py              # MODIFY: Use MenuNavigator

tests/
├── unit/                # REUSE from 001-todo-cli (NO CHANGES)
└── integration/
    ├── test_menu_navigation.py  # NEW: Menu navigation tests
    └── test_cli_commands.py    # UPDATE: Adapt for menu-based interaction
```

**Reuse Strategy**:
- 100% of business logic reused (Task, TodoService, exceptions, formatter)
- Only CLI layer changes (MenuNavigator replaces CommandMenu)
- All unit tests for models and services remain identical
- New tests: Menu navigation integration tests only

## Outcome

- ✅ Impact: Complete implementation plan for menu-based navigation - ready for task generation and TDD implementation
- 🧪 Tests: Testing strategy defined (reuse existing unit tests + add menu navigation integration tests)
- 📁 Files: Created plan.md, research.md, data-model.md, contracts/menu-options.md, quickstart.md (5 planning artifacts)
- 🔁 Next prompts: /sp.tasks 002-todo-cli-menu (generate dependency-ordered task list for implementation)
- 🧠 Reflection: Plan successfully balances menu navigation UX requirements with Phase I constraints (standard library, in-memory). 100% reuse of 001-todo-cli business logic significantly reduces implementation complexity and risk. MenuNavigator is the only new code required (~100-150 lines). All constitution gates passed. Ready for task generation.

## Evaluation notes (flywheel)

- Failure modes observed: None. All planning phases completed successfully. Constitution check passed with full reuse confirmation.
- Graders run and results (PASS/FAIL): PASS - All constitution principles satisfied. Technical decisions align with Phase I constraints. Data model confirmed identical to 001-todo-cli (no changes). Menu option contracts fully defined with input/output specifications. Quickstart provides complete user guidance with tutorial workflow.
- Prompt variant (if applicable): N/A (standard planning workflow)
- Next experiment (smallest change to try): During task generation, validate that task list clearly indicates which code to reuse from 001-todo-cli vs what to create new. This will prevent accidental duplication of already-implemented business logic.
