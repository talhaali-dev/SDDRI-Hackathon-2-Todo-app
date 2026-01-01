# Quickstart Guide: Phase I Todo List CLI

**Feature**: 001-todo-cli
**Date**: 2026-01-01
**Phase**: Phase I - In-Memory Python Console App

## Overview

Phase I Todo CLI is an in-memory command-line todo application built with Python 3.13+. It provides complete task management (create, view, edit, delete, complete) through both command-based and interactive keyboard-driven interfaces.

**Key Features**:
- ✅ Create and manage tasks
- ✅ Mark tasks complete/incomplete
- ✅ Interactive mode with arrow key navigation
- ✅ Edit task descriptions
- ✅ Delete tasks
- ⚠️ In-memory only (data lost on exit)

## Prerequisites

**Required**:
- Python 3.13 or higher
- Terminal/console with UTF-8 support
- Unix/Linux/macOS for interactive mode (curses support)

**Verify Installation**:
```bash
python --version  # Should show 3.13+
```

## Installation

### Phase I (Current)

No installation required - standard library only!

```bash
# Clone the repository
git clone https://github.com/GrowWidTalha/SDDRI-Hackathon-2-Todo-app.git
cd SDDRI-Hackathon-2-Todo-app

# Checkout the feature branch
git checkout 001-todo-cli

# Run the application (after implementation)
python src/main.py
```

## Quick Start

### Starting the Application

```bash
$ python src/main.py

═══════════════════════════════════
  Phase I Todo List - CLI
═══════════════════════════════════

No tasks available. Use 'add' command to create your first task.

> _
```

### Basic Workflow (5 Minutes)

**1. Add Your First Task**
```
> add "Write project documentation"
✓ Task created: [1] Write project documentation
```

**2. Add More Tasks**
```
> add "Review pull requests"
✓ Task created: [2] Review pull requests

> add "Update unit tests"
✓ Task created: [3] Update unit tests
```

**3. View All Tasks**
```
> list
Todo List (3 tasks):

Incomplete Tasks:
[ ] 1. Write project documentation
[ ] 2. Review pull requests
[ ] 3. Update unit tests
```

**4. Mark a Task Complete**
```
> complete 1
✓ Task #1 marked as complete: [✓] Write project documentation

> list
Todo List (3 tasks):

Incomplete Tasks:
[ ] 2. Review pull requests
[ ] 3. Update unit tests

Complete Tasks:
[✓] 1. Write project documentation
```

**5. Try Interactive Mode**
```
> interactive

┌─────────────────────────────────────────────┐
│ Todo List (Interactive Mode)               │
│                                             │
│   [✓] 1. Write project documentation       │
│ ▶ [ ] 2. Review pull requests              │  ← Use ↑/↓ arrows
│   [ ] 3. Update unit tests                 │
│                                             │
│ Arrow Keys: Navigate | Space: Toggle | ESC: Exit │
└─────────────────────────────────────────────┘

# Press SPACE to toggle task #2 complete
# Press ESC to return to command mode
```

**6. Edit a Task**
```
> edit 2 "Review pull requests - urgent"
✓ Task #2 updated: Review pull requests - urgent
```

**7. Delete a Task**
```
> delete 3
✓ Task #3 deleted: Update unit tests
```

**8. Exit Application**
```
> exit
Goodbye! All tasks will be lost (in-memory storage only).
```

## Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `add <description>` | Create new task | `add "Review code"` |
| `list` | View all tasks | `list` |
| `complete <id>` | Mark task complete | `complete 3` |
| `uncomplete <id>` | Mark task incomplete | `uncomplete 3` |
| `edit <id> <description>` | Update task | `edit 1 "New description"` |
| `delete <id>` | Delete task | `delete 5` |
| `interactive` | Enter interactive mode | `interactive` |
| `help` | Show command help | `help` |
| `exit` or `quit` | Exit application | `exit` |

**Pro Tip**: Type `help` anytime to see the full command list!

## Interactive Mode Guide

### Entering Interactive Mode

```
> interactive
```

### Controls

| Key | Action |
|-----|--------|
| `↑` (UP) | Move selection up |
| `↓` (DOWN) | Move selection down |
| `SPACE` | Toggle task completion |
| `ESC` | Exit to command mode |

### Interactive Mode Features

- **Circular Navigation**: Pressing DOWN at the bottom wraps to the top
- **Immediate Feedback**: Task status updates instantly on SPACE press
- **Visual Highlight**: Selected task clearly indicated with `▶` marker
- **No Typing Required**: Navigate and toggle without typing task IDs

### Exiting Interactive Mode

Press `ESC` to return to command prompt.

## Common Tasks

### Managing Your Daily Tasks

**Morning Routine - Plan Your Day**:
```
> add "Review emails"
> add "Standup meeting at 10am"
> add "Work on feature X"
> add "Lunch break"
> add "Code review session"
> list
```

**Throughout the Day - Track Progress**:
```
# Mark tasks complete as you finish them
> complete 1
> complete 2

# Check what's remaining
> list
```

**End of Day - Review**:
```
> list  # See what you accomplished (complete) vs. what remains
```

### Handling Changes

**Task Became More Urgent**:
```
> edit 3 "Work on feature X - URGENT - due today"
```

**Task No Longer Relevant**:
```
> delete 4
```

**Made a Mistake? Undo Completion**:
```
> uncomplete 2  # Marks task as incomplete again
```

## Tips and Best Practices

### Writing Good Task Descriptions

**✅ Good Examples**:
```
> add "Review PR #42 - authentication changes"
> add "Write unit tests for UserService"
> add "Update README with installation instructions"
```

**❌ Avoid**:
```
> add "stuff"           # Too vague
> add "work"            # Not specific
> add ""                # Empty (will error)
```

### Using Interactive Mode Efficiently

1. **Quick Status Updates**: Use interactive mode to rapidly toggle multiple tasks
2. **Review Sessions**: Enter interactive mode to scan through your task list
3. **Planning Mode**: Use command mode (`add`) to quickly capture tasks
4. **Execution Mode**: Use interactive mode (`SPACE` to toggle) to mark progress

### Managing Many Tasks

**For 20+ tasks**:
- Consider grouping related tasks with prefixes:
  ```
  > add "[Project X] Design database schema"
  > add "[Project X] Implement API endpoints"
  > add "[Meeting] Prepare slides"
  ```

**For 50+ tasks**:
- Use interactive mode for easier navigation (no need to remember IDs)
- Delete completed tasks periodically to keep list manageable

## Troubleshooting

### Common Issues

**Problem**: Interactive mode shows "curses library not supported"
```
Solution: Your terminal doesn't support curses (common on Windows).
Use command-based interface instead:
  > complete 3  # Instead of interactive toggle
```

**Problem**: Task description too long error
```
Error: Task description exceeds 500 characters.
Solution: Shorten your description to 500 characters or less.
```

**Problem**: "Task #X not found" error
```
Solution: Task was deleted or ID is wrong. Run 'list' to see current IDs.
```

**Problem**: All tasks lost after exiting
```
This is expected behavior in Phase I (in-memory only).
Data persistence comes in Phase II.
```

### Getting Help

**In-App Help**:
```
> help  # Shows all available commands
```

**Check Logs** (if implemented):
```bash
# Check application logs for errors
cat app.log  # If logging enabled
```

**Report Issues**:
- GitHub: https://github.com/GrowWidTalha/SDDRI-Hackathon-2-Todo-app/issues

## Limitations (Phase I)

### Known Constraints

⚠️ **No Persistence**: All data lost when application exits
- Workaround: Keep application running during work session
- Coming in Phase II: Database persistence

⚠️ **Single User**: No user accounts or multi-user support
- Coming in Phase II+: User authentication

⚠️ **No Search/Filter**: Must scan entire list
- Workaround: Use descriptive prefixes for grouping
- Coming in Future: Search and filtering features

⚠️ **No Due Dates**: Cannot set task deadlines
- Coming in Future: Task scheduling features

⚠️ **No Categories/Tags**: Cannot organize by category
- Coming in Future: Tagging system

### Performance Limits

- **Maximum Tasks**: ~1000 tasks (in-memory limit)
- **Response Time**: <1 second for commands, <2 seconds for large lists
- **Terminal Size**: Requires minimum 80x24 terminal for optimal display

## Next Steps

### After Quickstart

1. **Daily Usage**: Integrate into your workflow
2. **Explore Commands**: Try all commands to understand capabilities
3. **Provide Feedback**: Report bugs or suggest improvements
4. **Wait for Phase II**: Persistence and web interface coming soon!

### Advanced Usage (Future)

Phase II and beyond will add:
- ✨ Data persistence (database)
- ✨ Web interface
- ✨ Multi-user support
- ✨ Task prioritization
- ✨ Due dates and reminders
- ✨ Categories and tags

## Validation Checklist

Before reporting issues, verify:

- [ ] Python 3.13+ installed (`python --version`)
- [ ] Running from correct directory (repository root)
- [ ] Feature branch checked out (`git branch --show-current`)
- [ ] Terminal supports UTF-8 (for checkmark symbols)
- [ ] Followed command syntax from `help` output

## Support

**Documentation**:
- Full specification: `specs/001-todo-cli/spec.md`
- Implementation plan: `specs/001-todo-cli/plan.md`
- CLI commands reference: `specs/001-todo-cli/contracts/cli-commands.md`

**Community**:
- GitHub Issues: [Report bugs or request features](https://github.com/GrowWidTalha/SDDRI-Hackathon-2-Todo-app/issues)
- Pull Requests: Contributions welcome!

---

**Remember**: This is Phase I (in-memory only). All tasks are lost when you exit. Phase II will add persistence!
