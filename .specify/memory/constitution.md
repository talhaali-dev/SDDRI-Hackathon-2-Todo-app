<!--
Sync Impact Report:
Version: 1.0.0 → 1.1.0 (MINOR: Added Git Workflow section)
Modified Principles: None
Added Sections:
  - Git Workflow (under Governance) - Branch strategy, commit conventions, PR requirements
Removed Sections: None
Templates Status:
  - ✅ .specify/templates/plan-template.md (Constitution Check section compatible)
  - ✅ .specify/templates/spec-template.md (Requirements alignment compatible)
  - ✅ .specify/templates/tasks-template.md (Task categorization compatible)
Follow-up TODOs: None
Repository: https://github.com/GrowWidTalha/SDDRI-Hackathon-2-Todo-app.git
-->

# Multi-Phase Hackathon Todo App Constitution

## Core Principles

### I. Phase-Scoped Development

This project follows a strict five-phase incremental development model. Each phase builds on
the previous one and introduces new technologies and capabilities. All development work MUST
respect current phase boundaries.

**Phases**:
- **Phase I**: In-Memory Python Console App (Python, Claude Code, Spec-Kit Plus)
- **Phase II**: Full-Stack Web Application (Next.js, FastAPI, SQLModel, Neon DB)
- **Phase III**: AI-Powered Todo Chatbot (OpenAI ChatKit, Agents SDK, Official MCP SDK)
- **Phase IV**: Local Kubernetes Deployment (Docker, Minikube, Helm, kubectl-ai, kagent)
- **Phase V**: Advanced Cloud Deployment (Kafka, Dapr, DigitalOcean DOKS)

**Non-negotiable rules**:
- Features MUST only use technologies allowed in the current phase
- No forward-phase dependencies (e.g., no database in Phase I)
- No backward-incompatible changes that break previous phases
- Each phase MUST be fully functional before progressing to the next

**Rationale**: Incremental complexity ensures each phase delivers working software and
validates learning objectives before adding new technologies.

### II. Deterministic Behavior

All features MUST exhibit deterministic, predictable behavior. Commands and operations MUST
produce consistent outputs given the same inputs.

**Non-negotiable rules**:
- Commands MUST be explicit and predictable
- No hidden state or implicit behavior
- No random or non-deterministic operations without explicit user control
- State transitions MUST be traceable and reversible where applicable

**Rationale**: Deterministic behavior is essential for testing, debugging, and user trust.
Users must understand what each command does before executing it.

### III. Fail-Safe Error Handling

The application MUST handle errors gracefully with clear, actionable messages. Failures MUST
NOT corrupt state or leave the system in an undefined condition.

**Non-negotiable rules**:
- All errors MUST produce clear, human-readable messages
- Invalid inputs MUST be rejected with explanation before state changes
- Partial failures MUST NOT leave inconsistent state
- Error messages MUST suggest corrective action where possible

**Rationale**: Safe failure modes protect user data and provide better developer experience
during incremental development across phases.

### IV. Test-Driven Development (NON-NEGOTIABLE)

All features MUST follow strict TDD workflow: tests written → user approved → tests fail →
then implement. Red-Green-Refactor cycle is mandatory.

**Non-negotiable rules**:
- Tests written FIRST, before any implementation
- Tests MUST fail initially (red phase verified)
- Implementation proceeds only after test approval
- Refactoring only after tests pass (green phase)
- No implementation without corresponding test coverage

**Rationale**: TDD ensures specification compliance, prevents regression, and provides
living documentation across all five development phases.

### V. Simplicity Over Extensibility

Design decisions MUST favor simplicity and directness over future-proofing or speculative
features. Only implement what is explicitly required for the current phase.

**Non-negotiable rules**:
- No speculative abstractions or frameworks
- No features beyond current phase requirements
- Code MUST map directly to task definitions
- Prefer three lines of explicit code over premature abstraction
- YAGNI (You Aren't Gonna Need It) principle strictly enforced

**Rationale**: Each phase introduces sufficient complexity through new technologies.
Over-engineering wastes time and violates phase boundaries.

### VI. Code Quality Standards

Code MUST be readable, maintainable, and purposeful. Every file and function MUST serve a
defined task from the specification.

**Non-negotiable rules**:
- Clear, descriptive function and variable names
- Single Responsibility Principle (one function, one purpose)
- No dead code or commented-out code
- No duplicate logic without explicit justification
- Code MUST directly trace to a task in tasks.md
- Every file exists to serve a defined task

**Rationale**: High code quality reduces debugging time and eases the transition between
phases as complexity increases.

## Phase I: In-Memory Python Console App (CURRENT PHASE)

### Technology Constraints

**Language**: Python 3.13+
**Runtime**: Local execution only
**Dependencies**: Standard library only (no external packages)
**Packaging**: Simple Python project structure (no build tools)

**Non-negotiable Phase I rules**:
- NO persistence (no files, databases, or external storage)
- NO external services or network calls
- NO UI beyond terminal output (stdin/stdout only)
- NO third-party libraries or frameworks
- Data stored in memory only (Python data structures)

**Rationale**: Phase I establishes core todo logic without infrastructure complexity.
Later phases will add persistence, web interfaces, and cloud services incrementally.

### Scope Boundaries

**In Scope**:
- Command-line interface for todo operations
- In-memory task storage
- Basic CRUD operations (Create, Read, Update, Delete)
- Task state transitions
- Input validation and error handling

**Out of Scope**:
- Any form of persistence
- Web or GUI interfaces
- Authentication or multi-user support
- External integrations
- Advanced features from future phases

**Rationale**: Strict scope enforcement ensures Phase I remains focused on core logic
and prevents premature implementation of future phase features.

### Functional Principles

**Commands MUST be explicit**: All operations require explicit user commands. No automatic
or background operations.

**Predictable state changes**: Every command that modifies state MUST show before/after
confirmation or produce observable output.

**Validation before mutation**: All inputs MUST be validated before any state changes occur.
Invalid operations reject early with clear messages.

**No magic behavior**: No implicit defaults, auto-corrections, or hidden transformations.
What the user commands is exactly what executes.

## Completion Definition

Phase I is considered complete ONLY when ALL of the following criteria are met:

- [ ] All basic todo operations are implemented (add, list, update, delete, mark complete)
- [ ] Behavior matches the specification exactly (spec.md compliance)
- [ ] All tests pass (TDD green phase achieved)
- [ ] CLI runs without errors on Python 3.13+
- [ ] All code quality standards above are followed
- [ ] No violations of Phase I technology constraints
- [ ] All tasks in tasks.md are completed and verified
- [ ] Documentation accurately reflects implemented behavior

**Critical**: Working code without spec compliance is considered INCOMPLETE. Adherence to
specification is non-negotiable for phase completion.

## Governance

### Amendment Procedure

1. Proposed changes MUST be documented with rationale
2. Changes affecting multiple phases require impact analysis
3. Constitution amendments require version bump (see Versioning Policy)
4. All dependent templates and documentation MUST be updated synchronously

### Versioning Policy

Constitution follows semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Backward incompatible governance/principle removals or redefinitions
- **MINOR**: New principle/section added or materially expanded guidance
- **PATCH**: Clarifications, wording, typo fixes, non-semantic refinements

### Compliance Review

- All specifications (spec.md) MUST verify compliance with current phase constraints
- All implementation plans (plan.md) MUST include Constitution Check gate
- All task lists (tasks.md) MUST reference applicable principles
- Code reviews MUST verify adherence to Code Quality Standards
- Pull requests advancing to new phase MUST verify previous phase completion criteria

### Git Workflow

**Repository**: https://github.com/GrowWidTalha/SDDRI-Hackathon-2-Todo-app.git

**Branch Strategy**:
- `master` (or `main`): Production-ready code, always deployable
- `phase-N-dev` (e.g., `phase-1-dev`, `phase-2-dev`): Development branch for each phase
- `NNN-feature-name`: Feature branches for individual features/tasks

**Non-negotiable rules**:
- All work MUST be done in feature branches created from current phase development branch
- Feature branch naming: `NNN-feature-name` where NNN is the feature/issue number
- Commits MUST follow conventional commit format: `type(scope): description`
  - Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`
  - Example: `feat(cli): add task creation command`
- Commits MUST reference task IDs when implementing tasks (e.g., `feat(cli): add list command [T005]`)
- Pull requests MUST target the current phase development branch (not master directly)
- PRs MUST include:
  - Description of changes
  - Reference to specification/tasks
  - Test results (all tests passing)
  - Constitution compliance verification
- Master branch updates ONLY occur when phase is complete and all completion criteria met

**Phase Transition Strategy**:
1. Complete all Phase N tasks on `phase-N-dev` branch
2. Verify all Phase N completion criteria (see Completion Definition)
3. Create PR: `phase-N-dev` → `master` with full phase completion checklist
4. After merge, tag release: `vN.0.0` (e.g., `v1.0.0` for Phase I completion)
5. Create `phase-N+1-dev` branch from updated `master` for next phase

**Commit Message Format**:
```
<type>(<scope>): <subject>

[optional body]

[optional footer with task references]
```

**Examples**:
```
feat(todo): add create task operation [T012]
test(todo): add unit tests for task creation [T010]
docs(spec): update Phase I completion criteria
fix(cli): handle empty task list display [T015]
```

**Rationale**: Structured git workflow ensures traceability between code changes and
specifications, enables clean phase transitions, and maintains a clear project history
across all five development phases.

### Development Guidance

Runtime development guidance is maintained in `CLAUDE.md` for agent-specific workflows
(PHR creation, ADR suggestions, execution contracts). The constitution defines WHAT
principles govern the project; `CLAUDE.md` defines HOW agents execute against those
principles.

**Version**: 1.1.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
