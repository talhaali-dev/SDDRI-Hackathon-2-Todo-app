# Research Document: Phase I Todo List CLI

**Feature**: 001-todo-cli
**Date**: 2026-01-01
**Phase**: Phase 0 - Outline & Research

## Research Questions

### 1. Interactive Terminal UI Library for Phase I

**Question**: Which Python library should be used for interactive terminal UI (arrow key navigation, spacebar toggling) while respecting Phase I "standard library only" constraint?

**Decision**: Use Python's built-in `curses` module (standard library)

**Rationale**:
- Curses is part of Python standard library (available since Python 1.5)
- Provides complete terminal control: cursor positioning, keyboard input detection, screen refresh
- Supports arrow keys, spacebar, and other special key detection
- Cross-platform support (Unix/Linux/macOS native, Windows via windows-curses but Phase I targets standard terminals)
- Zero external dependencies - fully compliant with Phase I constraints
- Well-documented with extensive Python documentation and examples
- Proven solution for CLI applications (used by vim, htop, and many TUI applications)

**Alternatives Considered**:
1. **prompt_toolkit** (external library)
   - ❌ Rejected: Violates Phase I "standard library only" constraint
   - Pros: Modern API, excellent documentation, rich features
   - Cons: Requires pip install, adds external dependency

2. **rich** (external library)
   - ❌ Rejected: Violates Phase I "standard library only" constraint
   - Pros: Beautiful formatting, progress bars, modern CLI styling
   - Cons: External dependency, overkill for Phase I scope

3. **Basic input() with numbered menus**
   - ❌ Rejected as primary approach: Poor UX, doesn't meet P3 requirements for arrow key navigation
   - Pros: Absolutely minimal, no dependencies, works everywhere
   - Cons: Cannot detect arrow keys or provide smooth navigation required by spec
   - Note: Can serve as fallback if curses unavailable

**Implementation Notes**:
- Use `curses.wrapper()` for proper terminal setup/teardown
- Handle `curses.KEY_UP`, `curses.KEY_DOWN`, `curses.KEY_LEFT`, `curses.KEY_RIGHT` for navigation
- Use ord(' ') for spacebar detection
- Implement graceful fallback to basic menu if curses fails to initialize

**Phase I Compliance Verification**:
✅ Curses is standard library - COMPLIANT
✅ No external dependencies required - COMPLIANT
✅ Provides required interactive features - COMPLIANT

---

### 2. In-Memory Data Structure for Task Storage

**Question**: What is the optimal in-memory data structure for storing tasks with requirements for unique IDs, fast lookups, and ordered display?

**Decision**: Use combination of `list` for ordered storage and `dict` for ID-based lookups

**Rationale**:
- Preserves insertion order (tasks displayed in creation order per spec)
- O(1) lookup by ID using dictionary
- Simple, standard Python data structures (no external dependencies)
- Easy to iterate for display operations
- Supports efficient CRUD operations within memory constraints

**Data Structure Design**:
```python
tasks_by_id: dict[int, Task] = {}  # Fast ID lookup
tasks_ordered: list[Task] = []     # Preserves creation order for display
next_id: int = 1                   # Auto-incrementing ID counter
```

**Alternatives Considered**:
1. **List only** (indexed by position)
   - ❌ Rejected: O(n) lookup by ID, ID stability issues when tasks deleted
   - Pros: Simple, maintains order naturally
   - Cons: Slow lookups, fragile IDs

2. **Dict only** (OrderedDict for ordering)
   - ⚠️ Acceptable but less clear: Modern Python dicts maintain insertion order (3.7+), OrderedDict explicit
   - Pros: Single data structure, fast lookups
   - Cons: Less explicit about ordering intent, slightly more memory

3. **Database (SQLite, etc.)**
   - ❌ Rejected: Violates Phase I "no persistence" constraint
   - Would be appropriate for Phase II

**Implementation Notes**:
- Maintain synchronization between dict and list (add/delete operations update both)
- Use Python 3.13+ dict ordering guarantee
- IDs never reused within a session (monotonically increasing)
- Consider using `@dataclass` for Task model with validation

---

### 3. Testing Strategy for CLI Application

**Question**: What testing approach balances TDD requirements with CLI-specific challenges (terminal I/O, user interaction)?

**Decision**: Multi-layer testing strategy using standard library `unittest` module

**Rationale**:
- unittest is Python standard library - no external dependencies
- Supports unit tests (models, services) and integration tests (CLI workflows)
- Mock/patch capabilities for isolating terminal I/O
- Test discovery and runner built-in
- Familiar API similar to pytest (easy migration to pytest in Phase II if needed)

**Testing Layers**:
1. **Unit Tests** (`tests/unit/`)
   - Task model validation (empty descriptions, length limits)
   - TodoService operations (add, complete, update, delete)
   - Mock dependencies, test business logic in isolation
   - Fast execution, no I/O dependencies

2. **Integration Tests** (`tests/integration/`)
   - End-to-end CLI command workflows
   - Mock terminal I/O (stdin/stdout) using `io.StringIO`
   - Test user scenarios from spec (P1-P5)
   - Verify correct integration between layers

3. **Interactive Mode Tests**
   - Mock curses module for keyboard input simulation
   - Test navigation logic (arrow keys, wraparound)
   - Test spacebar toggle behavior
   - Verify screen state updates

**Alternatives Considered**:
1. **pytest** (external library)
   - ⚠️ Consideration: Better fixtures, parameterization, but requires external dependency
   - May be allowed as dev dependency (clarify during implementation)
   - Can migrate easily from unittest if approved

2. **Manual testing only**
   - ❌ Rejected: Violates TDD principle (Principle IV - NON-NEGOTIABLE)
   - No automated regression protection

**Mocking Strategy**:
- Use `unittest.mock` for terminal I/O
- Mock `curses` functions for interactive mode testing
- Create test fixtures for task lists in various states
- Use `io.StringIO` to capture/inject stdin/stdout

**TDD Workflow**:
1. Write failing test for user story acceptance scenario
2. Run test, verify failure (red phase)
3. Implement minimum code to pass test
4. Run test, verify pass (green phase)
5. Refactor with tests passing
6. Repeat for next scenario

---

### 4. Error Handling Patterns

**Question**: What error handling approach provides clear, actionable messages while maintaining clean code?

**Decision**: Custom exception hierarchy with user-friendly message formatting

**Rationale**:
- Explicit error types improve debugging and testing
- Centralized message formatting ensures consistency
- Enables different handling for validation vs. not-found vs. system errors
- Supports spec requirement (FR-011) for clear, actionable error messages

**Exception Hierarchy**:
```python
class TodoError(Exception):
    """Base exception for todo application"""
    pass

class ValidationError(TodoError):
    """Input validation failures"""
    pass

class TaskNotFoundError(TodoError):
    """Task ID does not exist"""
    pass

class EmptyTaskListError(TodoError):
    """Operation requires tasks but list is empty"""
    pass
```

**Error Message Guidelines**:
- Start with what went wrong
- Explain why it's invalid
- Suggest corrective action
- Examples:
  - "Task description cannot be empty. Please provide a description (1-500 characters)."
  - "Task #42 not found. Use 'list' command to see available task IDs."
  - "Invalid task ID 'abc'. Task IDs must be numbers. Example: 1, 2, 3"

**Alternatives Considered**:
1. **Return codes/tuples** (success flag + message)
   - ❌ Rejected: Less Pythonic, easy to ignore errors, verbose call sites
   - Pros: Explicit control flow
   - Cons: No automatic error propagation, clutters business logic

2. **Generic exceptions only**
   - ❌ Rejected: Harder to test specific error cases, less semantic
   - Pros: Simpler
   - Cons: Loses type information, harder to handle differently

**Implementation Notes**:
- Catch exceptions at CLI layer, format for user display
- Let exceptions propagate from service layer (don't catch/re-raise unnecessarily)
- Log exceptions if needed (but no logging infrastructure in Phase I)
- Validate early (fail fast at input layer)

---

### 5. Display Formatting and Visual Indicators

**Question**: How should tasks be visually formatted to clearly distinguish complete vs. incomplete status?

**Decision**: Use Unicode characters for checkmarks and consistent formatting

**Rationale**:
- Unicode ✓ (✓) and ✗ (✗) or [ ] / [X] are universally supported in modern terminals
- Clear visual distinction at a glance
- Accessible (can be read by screen readers)
- No color dependencies (works in non-color terminals)

**Display Format**:
```
Todo List (5 tasks):

Incomplete Tasks:
[ ] 1. Write project documentation
[ ] 2. Review pull requests
[ ] 3. Update tests

Complete Tasks:
[✓] 4. Setup development environment
[✓] 5. Create initial project structure
```

**Alternatives Considered**:
1. **Color-coding only** (green for complete, red for incomplete)
   - ❌ Rejected as sole indicator: Not accessible, fails in non-color terminals
   - Can be added as enhancement if colors available (curses.has_colors())

2. **Strikethrough text** (~~Task description~~)
   - ⚠️ Consider as secondary indicator: Not all terminals support, harder to read
   - Could combine with checkbox for redundancy

**Implementation Notes**:
- Use string formatting/padding for alignment
- Support word wrapping for long descriptions (>80 chars)
- Consider pagination for lists >20 tasks (enhances UX for large lists)
- Graceful degradation: if Unicode fails, use ASCII [ ] and [X]

---

### 6. Application Entry Point and Main Loop

**Question**: What is the appropriate structure for the main application loop and user interaction flow?

**Decision**: Menu-driven command loop with mode switching (command mode vs. interactive mode)

**Rationale**:
- Clear separation between text-based commands and interactive UI
- Easy to test (command dispatch logic separate from I/O)
- Supports both P1-P2 (command-based) and P3 (interactive) user stories
- Natural exit point and state management

**Application Flow**:
```
1. Start application
2. Display main menu
3. Read user input
4. Parse command / detect mode switch
5. Execute command OR enter interactive mode
   - Interactive mode: curses-based arrow key navigation
   - Command mode: text-based command execution
6. Display result / updated task list
7. Return to main menu (loop) or exit
```

**Command Structure**:
- `add <description>` - Add new task
- `list` - View all tasks
- `complete <id>` - Mark task complete
- `uncomplete <id>` - Mark task incomplete
- `edit <id> <new description>` - Update task description
- `delete <id>` - Delete task
- `interactive` - Enter interactive mode
- `help` - Show command help
- `exit` / `quit` - Exit application

**Alternatives Considered**:
1. **Interactive-only** (no text commands)
   - ❌ Rejected: Spec explicitly includes identifier-based commands (P2, P4, P5)
   - Would not satisfy all user stories

2. **Separate executables** for command vs. interactive modes
   - ❌ Rejected: Adds complexity, violates simplicity principle
   - User should access all features from single entry point

**Implementation Notes**:
- Use command pattern for easy extension and testing
- Validate input before command execution
- Maintain single source of truth for task list (shared between modes)
- Save/restore terminal state when switching modes

---

## Research Summary

All technical decisions made with Phase I constraints in mind:
✅ Standard library only (curses, unittest)
✅ No external dependencies for core functionality
✅ In-memory storage exclusively
✅ Clear, testable architecture
✅ Supports all P1-P5 user stories

**Key Technologies Selected**:
- Python 3.13+ standard library
- curses module for interactive UI
- unittest for testing framework
- dict + list for in-memory storage
- Custom exceptions for error handling

**Next Steps**: Proceed to Phase 1 design (data-model.md, contracts/, quickstart.md)
