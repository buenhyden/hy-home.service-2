# Collaboration & Team Governance

This guide defines how the team interacts, communicates, and makes decisions to
maintain high velocity and alignment.

## 0. Development Process / Collaboration Checklist

Complete this checklist during project kickoff and update it when team agreements
change.

| Item | Check Question | Required | Alignment Notes (Agreement) | Source of Truth |
| --- | --- | --- | --- | --- |
| Development Process | Have we agreed on Scrum, Kanban, or hybrid? | Must |  | Section 2 |
| Sprint Operation | Have sprint length and ceremonies (planning/daily/review/retro) been agreed? | Optional |  | Section 2 |
| Issue Management | Have we defined the issue tracker and required fields (labels/status/AC)? | Must |  | Section 5 |
| Branch Strategy | Have we agreed on a branching model (GitHub Flow/Trunk-based/GitFlow)? | Must |  | Section 6 |
| Merge Policy | Have we agreed on branch protection (no direct push to main, required checks, etc.)? | Must |  | Section 6 |
| Code Review Rules | Have we defined min reviewers and required checks (tests/security/perf)? | Must |  | Section 4 + [`0012-code-review-standard.md`][code-review] |
| PR Size Rule | Do we have PR size guidance (LOC / scope)? | Optional |  | Section 4 + [`0200-workflow-standard.md`][workflow] |
| Definition of Done | Do we have a checklist for “Done” (tests/docs/review)? | Must |  | Section 4 + [Development Guide][dev-guide] |
| Definition of Ready | Do we have a checklist for “Ready” before development starts? | Optional |  | Section 4 |
| Communication Channel | Are official channels and response SLA defined? | Must |  | Section 1 |
| Decision Making | Is decision ownership defined (PO, Tech Lead, etc.)? | Must |  | Section 3 |

## 1. Communication Channels

| Channel | Purpose | Expected Response (SLA) |
| :--- | :--- | :--- |
| **Slack / Teams** | Real-time sync, quick questions, alerts. | 4 business hours |
| **GitHub Issues** | Domain/Feature specific discussions. | 24 business hours |
| **GitHub PRs** | Code review and technical feedback. | 24 business hours |
| **Email** | Formal external communication, legal. | 48 business hours |

## 2. Delivery Process (Scrum / Kanban / Hybrid)

The project defaults to **Scrum** with a **2-week sprint**, but teams may adopt
**Kanban** or a **hybrid** model.

### Default Scrum Cadence (2-week)

- **Sprint Planning**: Every other Monday. Define Goal and Backlog.
- **Daily Sync**: 15 min daily. Blockers and progress check.
- **Sprint Review**: Last Friday of the sprint. Showcase deliverables to stakeholders.
- **Retrospective**: After Review. Discuss process improvements.

## 3. Decision-Making Structure

To ensure clear ownership and avoid gridlock:

- **Product Owner (PO)**: Final decision on **Scope**, **Priority**, and
  **Business Requirements**.
- **Tech Lead / Architect**: Final decision on **Technology Stack**,
  **System Design**, and **Security**.
- **The Team**: Decides on **Implementation details** and **Code structure**
  through Peer Review.

## 4. Work Discipline

### PR Size & Quality

- **Max PR Size**: Avoid PRs > 500 lines of code (excluding tests/data).
- **Review Requirement**: Minimum 1 peer approval required for all `main` branch
  merges.
- **Draft PRs**: Use for early feedback; non-eligible for merge.
- **Optional Local Check**: `pre-commit run check-pr-size --hook-stage manual`

### Code Review Rules (Required Checks)

- **Tests**: New/changed logic must be covered and pass in CI.
- **Security**: High-risk changes require a security pass (see `docs/manuals/09-security-qa.md`).
- **Performance**: Consider performance impact for hot paths; add benchmarks
  when needed.
- **Traceability**: PR should link PRD/Spec and requirement IDs when applicable.

### Definition of Ready (DoR)

A task is "Ready" when it has:

- Clear User Story and Context.
- Measurable Acceptance Criteria (Given-When-Then).
- Linked Technical Specification (for complex changes).

### Definition of Done (DoD)

A task is "Done" when:

- Code follows [0100] Standards.
- Tests have 100% coverage for new logic.
- Documentation (README/docs) is updated.
- Peer Review is completed and approved.

## 5. Issue Management (GitHub Issues Default)

The default tracker is **GitHub Issues** (but Jira/Linear/etc. are also acceptable
if agreed).

### Required Fields (Definition of Ready gate)

- **Problem statement** (what/why)
- **Acceptance Criteria** in **Given/When/Then**
- **Priority** (Critical/High/Medium/Low)
- **Labels** (at minimum: `bug`/`enhancement` and one priority label if your team
  uses them)
- **Status** (tracked in GitHub Projects or via labels)

Use the repository issue templates:

- Feature: `.github/ISSUE_TEMPLATE/feature_request.md`
- Bug: `.github/ISSUE_TEMPLATE/bug_report.md`

## 6. Branch Strategy & Merge Policy

### Branch Strategy

Default is a simplified GitFlow-style naming:

- `main`: production-ready
- `feature/<description>`
- `fix/<issue>`
- `hotfix/<issue>` (optional)

### Merge Policy (Recommended GitHub Settings)

These settings are enforced in GitHub repository configuration (not in-code),
but should be agreed at kickoff:

- Protect `main` (no direct pushes).
- Require PRs for all changes to `main`.
- Require at least **1 approval** before merge (more for high-risk areas).
- Require status checks (CI) to pass before merge.
- Require linear history (optional) and disallow force-push (recommended).
- Use CODEOWNERS for sensitive areas: `.github/CODEOWNERS`

[code-review]: ../../.agent/rules/0000-Agents/0012-code-review-standard.md
[workflow]: ../../.agent/rules/0200-Workflows/0200-workflow-standard.md
[dev-guide]: ./06-development-guide.md
