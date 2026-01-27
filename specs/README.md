# Specifications (Spec-Driven Development)

This directory is the **starting point** for all new features in the hy-home.service-2 workflow.

## The Flow

1. **Create a Plan**: Create a subfolder for your feature (e.g., `specs/auth-system/`).
2. **Draft the Plan**: Create a `plan.md` file describing your requirements.
3. **Bootstrap**: Run the setup script to generate a workspace tailored to that plan.

```bash
# Example
./scripts/setup-workspace.ps1 specs/auth-system/plan.md
```

## Structure

- **`plan.md`**: The high-level implementation plan (Goals, user stories).
- **`[feature].spec.md`**: Technical specifications (Schema, APIs).
- **`[feature].prd.md`**: Product Requirements (Metrics, Personas).

Use `templates/spec-template.md` and `templates/prd-template.md` as your baselines.

