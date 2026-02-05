---
trigger: model_decision
glob: ["**/*.tsx", "**/*.html"]
description: "Accessibility (a11y): WCAG 2.1 AA Compliance standards."
---

# 1010-Frontend-Accessibility

- **Role**: Frontend Engineer / Designer
- **Purpose**: Ensure applications are usable by everyone, regardless of disability.
- **Activates When**: Creating UI elements, forms, or navigation.

## 1. Standards

### 1.1 Principles

- **[REQ-ACC-GEN-01] WCAG Compliance**: MUST meet WCAG 2.1 Level AA.
- **[REQ-ACC-GEN-02] Keyboard Nav**: All interactive elements MUST be keyboard accessible.
- **[REQ-ACC-GEN-03] Semantic HTML**: Use `<button>`, `<nav>`, `<main>` over `<div>`.

### 1.2 Scope

- **In-Scope**: Semantic HTML, ARIA attributes, Color contrast, Focus management.
- **Out-of-Scope**: Design aesthetics (unless contrast related).

### 1.3 Must / Must Not

- **[REQ-ACC-IMG-01] Alt Text**: Images MUST have `alt` text (or null for decorative).
- **[REQ-ACC-FRM-01] Labels**: Form inputs MUST have associated labels.
- **[BAN-ACC-EVT-01] No Click on Div**: MUST NOT put `onClick` on non-interactive elements without role/tabindex.

## 2. Procedures

### 2.1 Testing Workflow

1. **Automated**: Run `axe-core` scan.
2. **Keyboard**: Tab through the entire page. Verify focus indicators.
3. **Screen Reader**: Test with VoiceOver/NVDA for complex widgets.

## 3. Examples

### 3.1 Accessible Form

```html
<!-- GOOD -->
<label htmlFor="email">Email Address</label>
<input id="email" type="email" aria-required="true" />

<!-- BAD -->
<div>Email</div>
<input type="text" />
```

## 4. Validation Criteria

- [ ] **[VAL-ACC-WCA-01]** Zero critical a11y violations in audit.
- [ ] **[VAL-ACC-KEY-01]** Focus ring is visible on all inputs/buttons.

## 5. References

- Reference: [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
