---
trigger: always_on
glob: "**/*.{tsx,jsx,vue,svelte,html}"
description: "Frontend Project Structure Standards: Enforces Feature-First architecture, vertical slicing, and shared component patterns."
---

# Frontend Project Structure Standards

- **Role**: Frontend Architect
- **Purpose**: Define standards for organizing frontend project directories using modular, feature-based patterns.
- **Activates When**: Creating or reorganizing frontend project structures.

**Trigger**: always_on — Apply during the setup and evolution of frontend project structures.

## 1. Standards

### Principles

- **[REQ-FE_STR-01] Vertical Slicing**
  - Project directories MUST be organized by business features rather than technical layers.
- **[REQ-FE_STR-02] Strong Encapsulation**
  - Features MUST communicate through explicit public APIs (index.ts) to prevent deep coupling.
- **[REQ-FE_STR-03] Atomic Shared UI**
  - Generic UI primitives MUST be stored in a centralized, domain-agnostic `ui` directory.

### Project Hierarchy

| Directory | Purpose | Visibility |
| --- | --- | --- |
| `src/features/` | Modular business logic | Private/Internal |
| `src/components/ui/` | Generic UI atoms | Global |
| `src/hooks/` | Cross-feature hooks | Global |
| `src/utils/` | Pure logic helpers | Global |

### Must

- **[REQ-FE_STR-04] Public Exports**
  - Every feature directory MUST have an `index.ts` file that explicitly exports its public interfaces.
- **[REQ-FE_STR-05] Colocation**
  - Assets, styles, and tests specific to a feature MUST be colocated within that feature's directory.
- **[REQ-FE_STR-06] Layered DTOs**
  - Shared data transfer objects MUST reside in a `src/types` or `src/models` directory if shared across features.

### Must Not

- **[BAN-FE_STR-01] Deep Cross-Feature Imports**
  - Features MUST NOT import directly from the internal subdirectories of other features.
- **[BAN-FE_STR-02] Domain-Specific Logic in UI**
  - The `src/components/ui` directory MUST NOT contain any business-specific or domain-specific logic.

### Failure Handling

- **Stop Condition**: Stop reorganization if circular dependencies between features are identified.

## 2. Procedures

- **[PROC-FE_STR-01] Feature Creation**
  - IF creating a new feature THEN MUST initialize it with `components/`, `hooks/`, `api/`, and `index.ts`.
- **[PROC-FE_STR-02] Shared Extraction**
  - IF a component is used by 3+ features THEN MUST move it to `src/components/ui` or `src/components/shared`.

## 3. Examples

### Vertical Slice (Good)

```text
src/features/auth/
  ├── components/ (LoginForm.tsx)
  ├── hooks/      (useAuth.ts)
  ├── api/        (signIn.ts)
  └── index.ts    (Exports LoginForm, useAuth)
```

## 4. Validation Criteria

- **[VAL-FE_STR-01] Boundary Verification**
  - [ ] No imports cross the public API boundaries of features.
- **[VAL-FE_STR-02] UI Purity**
  - [ ] All components in `src/components/ui` are agnostic to business data.
- **[VAL-FE_STR-03] Asset Colocation**
  - [ ] Images and styles used exclusively by one feature reside in that feature's directory.
