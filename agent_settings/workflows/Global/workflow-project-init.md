---
description: Initialize workspace rules and structural pillars from an implementation plan
---

1. Identify the active implementation plan (e.g., `specs/auth/plan.md`).
2. Verify that the plan contains a "Technical Context" section.
// turbo
3. Run the workspace setup script with the plan path.

   ```bash
   ./scripts/setup-workspace.sh <plan-path>
   ```

4. Verify that the relevant rule files have been copied to `.agent/rules/`.
5. Execute any project scaffolding commands identified in the setup output (e.g., `npm install`).
6. Confirm 100% adherence to the project's [Onboarding Guide](file:///d:/hy-home.SourceCode/Init-Project-Template/docs/onboarding.md).
