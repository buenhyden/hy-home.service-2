---
description: Initialize workspace rules and structural pillars from an implementation plan
---

1. Identify the active implementation plan (e.g., `specs/auth/plan.md`).
2. Confirm the feature PRD exists and is approved:
   - Expected path: `docs/prd/<feature>-prd.md`
   - If missing, scaffold one (and an optional spec):
     - Windows: `./scripts/new-prd.ps1 -Feature "<feature>" -WithSpec`
     - Unix: `WITH_SPEC=1 ./scripts/new-prd.sh "<feature>"`
3. Confirm the feature spec exists and references the PRD:
   - Expected path: `specs/<feature>/spec.md`
   - The spec MUST include a `PRD Reference` line and traceability IDs.
4. Complete QA prerequisites in the spec before coding:
   - Fill `templates/spec-template.md` Section 0: **Quality / Testing / Security Checklist (Fill Before Implementation)**
   - Fill `templates/spec-template.md` Section 7: **Verification Plan (Unit/Integration/E2E/Load + coverage targets)**
   - If E2E or Load testing is not applicable, write `N/A (reason: ...)` in the Verification Plan.
   - Gate: `./scripts/validate-docs.ps1 -Strict` (Windows) or `./scripts/validate-docs.sh --strict` (Unix)
5. If you make a significant architectural decision, create an ADR and link it from the spec:
   - Windows: `./scripts/new-adr.ps1 -Title "..." -Authors "..."`
   - Unix: `./scripts/new-adr.sh "..." "..."`
6. If you introduce or change a reusable implementation pattern, create/update an ARD and link it from the spec:
   - `docs/ard/*.md` (living reference, kept current with code)
7. Verify that the plan contains a "Technical Context" section.
8. Run the workspace setup script with the plan path.

   ```bash
   # Windows
   ./scripts/setup-workspace.ps1 specs/<feature>/plan.md

   # Unix
   ./scripts/setup-workspace.sh specs/<feature>/plan.md
   ```

9. Verify that the relevant rule files have been copied to `.agent/rules/`.
10. Execute any project scaffolding commands identified in the setup output (e.g., `npm install`).
11. Confirm 100% adherence to the project's [Onboarding Guide](../../../docs/guides/getting-started.md).
