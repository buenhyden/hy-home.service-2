# Specifications (Spec-Driven Development)

This directory is the **starting point** for all new features in the
Init-Project-Template workflow.

## The Flow

1. **Create a Plan**: Create a subfolder for your feature (e.g., `specs/auth-system/`).
2. **Draft the Plan**: Create a `plan.md` file describing your requirements.
3. **Bootstrap**: Run the setup script to generate a workspace tailored to that
   plan.

```bash
# Example
./scripts/setup-workspace.ps1 specs/auth-system/plan.md
```

## Structure

- **`plan.md`**: The high-level implementation plan (Goals, user stories).
- **`spec.md`**: Technical specification (Schema, APIs), must reference the PRD.
- **PRD (Product Requirements)**: Stored in `docs/prd/<feature>-prd.md` (Vision,
  Metrics, Personas, Use Cases).

Use `templates/spec-template.md` and `templates/prd-template.md` as your
baselines.

Specs should complete the architecture/stack checklist in
`templates/spec-template.md` Section 0 and link ADRs (`docs/adr/`) when a
decision is significant.

## Quick Start

- Windows: `./scripts/new-prd.ps1 -Feature "my-feature" -WithSpec`
- Unix: `WITH_SPEC=1 ./scripts/new-prd.sh "my-feature"`
