---
trigger: model_decision
glob: ["**/*.test.ts", "**/*.spec.py", "tests/**/*"]
description: "Testing Standards: TDD workflow, Coverage requirements, and Type definitions for QA."
---

# 0700-Testing-Standards

- **Role**: QA Engineer / Developer
- **Purpose**: Ensure code reliability through automated testing and quality gates.
- **Activates When**: Writing code, refactoring, or submitting a Pull Request.

## 1. Standards

### 1.1 Principles

- **[REQ-TST-GEN-01] Testing Pyramid**: Organization MUST prioritize Unit > Integration > E2E tests.
- **[REQ-TST-GEN-02] TDD**: Developers SHOULD write tests before implementation (Red-Green-Refactor).
- **[REQ-TST-GEN-03] Isolation**: Unit tests MUST mock external dependencies (DB, API).

### 1.2 Scope

- **In-Scope**: Unit, Integration, E2E, Performance Testing.
- **Out-of-Scope**: Manual QA scripts (managed in TestRail/Jira).

### 1.3 Must / Must Not

- **[REQ-TST-COV-01] Coverage**: Codebase MUST maintain >80% branch coverage.
- **[BAN-TST-DET-01] Flakiness**: Tests MUST NOT rely on external state or timing (sleeps).
- **[REQ-TST-NAM-01] Naming**: Test files MUST match `*.test.ts` or `test_*.py`.

## 2. Procedures

### 2.1 TDD Workflow

1. **Red**: Write a failing test for the requirement.
2. **Green**: Write the minimal code to pass the test.
3. **Refactor**: Optimize code while keeping tests passing.

### 2.2 Bug Fix Workflow

1. **Reproduce**: Write a test case that replicates the bug (Red).
2. **Fix**: Implement the fix (Green).
3. **Verify**: Ensure regression suite passes.

## 3. Examples

### 3.1 Unit Test (TypeScript/Jest)

```typescript
// math.test.ts
import { add } from './math';

describe('Math Lib', () => {
  it('should add two numbers', () => {
    expect(add(1, 2)).toBe(3);
  });
});
```

## 4. Validation Criteria

- [ ] **[VAL-TST-COV-01]** CI pipeline fails if coverage < 80%.
- [ ] **[VAL-TST-NAM-01]** Test files follow naming convention.
- [ ] **[VAL-TST-MOC-01]** Unit tests do not hit network/DB.

## 5. References

- Related: [0330-infrastructure-cicd.md](../0300-DevOps_and_Infrastructure/0330-infrastructure-cicd.md)


