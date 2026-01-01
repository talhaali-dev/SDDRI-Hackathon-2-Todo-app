---
id: 0002
title: Add Git Workflow Guidelines
stage: constitution
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: system
command: /sp.constitution
labels: ["constitution", "amendment", "git-workflow", "governance", "version-control"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - N/A (constitution document)
---

## Prompt

Add proper git workflow guidelines in constitution git remote add origin https://github.com/GrowWidTalha/SDDRI-Hackathon-2-Todo-app.git

## Response snapshot

Amended constitution from v1.0.0 to v1.1.0 (MINOR version bump) to add comprehensive Git Workflow section under Governance.

**Git Workflow Section Added**:

**Repository**: https://github.com/GrowWidTalha/SDDRI-Hackathon-2-Todo-app.git

**Branch Strategy**:
- `master`: Production-ready code, always deployable
- `phase-N-dev`: Development branch for each phase (e.g., `phase-1-dev`, `phase-2-dev`)
- `NNN-feature-name`: Feature branches for individual features/tasks

**Non-negotiable Rules**:
- All work in feature branches from current phase development branch
- Feature branch naming: `NNN-feature-name` (NNN = feature/issue number)
- Conventional commits: `type(scope): description`
  - Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`
  - Must reference task IDs: `[T005]`
- PRs target phase development branch (not master)
- PRs must include: description, spec/task references, test results, compliance verification
- Master updates only when phase completion criteria fully met

**Phase Transition Strategy**:
1. Complete all Phase N tasks on `phase-N-dev`
2. Verify all completion criteria
3. PR: `phase-N-dev` → `master` with completion checklist
4. Tag release: `vN.0.0` after merge
5. Create `phase-N+1-dev` from updated master

**Commit Message Format**:
```
<type>(<scope>): <subject>

[optional body]

[optional footer with task references]
```

**Examples**:
- `feat(todo): add create task operation [T012]`
- `test(todo): add unit tests for task creation [T010]`
- `docs(spec): update Phase I completion criteria`
- `fix(cli): handle empty task list display [T015]`

Also configured git remote origin to repository URL.

## Outcome

- ✅ Impact: Constitution v1.1.0 - Added Git Workflow governance ensuring traceability between code changes and specifications across all 5 phases
- 🧪 Tests: N/A (governance document, no executable tests)
- 📁 Files: Updated .specify/memory/constitution.md (267 lines, +59 lines added)
- 🔁 Next prompts: Create `phase-1-dev` branch for Phase I development, /sp.specify <feature-name> to begin feature work with git workflow in place
- 🧠 Reflection: Git workflow amendment establishes critical version control discipline for multi-phase project. Branch strategy (phase-dev branches) enables parallel phase work while protecting master stability. Conventional commits with task references ensure full traceability from code to tasks to specifications.

## Evaluation notes (flywheel)

- Failure modes observed: None. Git remote successfully added, constitution updated with comprehensive workflow rules.
- Graders run and results (PASS/FAIL): PASS - Version correctly bumped (MINOR: 1.0.0 → 1.1.0), dates updated, no unresolved placeholders, workflow rules are declarative and testable
- Prompt variant (if applicable): N/A (constitution amendment)
- Next experiment (smallest change to try): Test workflow by creating first feature branch following new naming convention and commit format when implementing first Phase I feature
