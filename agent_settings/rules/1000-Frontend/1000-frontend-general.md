---
trigger: model_decision
glob: ["**/*.tsx", "**/*.jsx", "**/*.html", "**/*.css"]
description: "Frontend General: Component structure, State management, and Performance."
---

# 1000-Frontend-General

- **Role**: Frontend Engineer
- **Purpose**: Ensure responsive, performant, and maintainable user interfaces.
- **Activates When**: Writing UI components or CSS.

## 1. Standards

### 1.1 Principles

- **[REQ-FE-GEN-01] Componentization**: UI MUST be built as reusable, atomic components.
- **[REQ-FE-GEN-02] Responsiveness**: UI MUST adapt to Mobile, Tablet, and Desktop.
- **[REQ-FE-GEN-03] State Management**: Local state preferred over Global state.
- **[REQ-FE-GEN-04] Semantic First**: Use semantic tags (`<header>`, `<main>`, `<form>`, `<button>`) to ensure accessibility and SEO.
- **[REQ-FE-GEN-05] Pure Props**: Data MUST flow down, and events MUST bubble up through explicit callbacks.

### 1.2 Scope

- **In-Scope**: React/Vue/Svelte components, CSS/Tailwind, Responsive Design, Semantic HTML.
- **Out-of-Scope**: API Logic (see 0910).

### 1.3 Must / Must Not

- **[REQ-FE-CMP-01] Atomic Design**: Components SHOULD follow Atomic Design (Atoms, Molecules, Organisms).
- **[BAN-FE-DOM-01] No Direct DOM**: MUST NOT manipulate DOM directly (use Refs).
- **[REQ-FE-IMG-01] Optimization**: Images MUST use `lazy` loading and `webp` format.

## 2. Procedures

### 2.1 Component Structure

1. **Imports**: External first, then Internal.
2. **Types**: Props interface definition.
3. **Logic**: Hooks/State.
4. **Render**: JSX/Template.

### 2.2 Performance Checklist

1. **Lighthouse**: Score > 90.
2. **Bundle Size**: Split chunks > 500KB.
3. **Memoization**: Use `useMemo` for expensive calculations.

## 3. Examples

### 3.1 Standard Component (React)

```tsx
import { useState } from 'react';
import { Button } from '@/components/ui';

interface Props {
  title: string;
}

export const Card = ({ title }: Props) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="p-4 border rounded">
      <h2 className="text-xl">{title}</h2>
      <Button onClick={() => setIsOpen(!isOpen)}>Toggle</Button>
    </div>
  );
};
```

## 4. Validation Criteria

- [ ] **[VAL-FE-RES-01]** UI works on mobile viewport.
- [ ] **[VAL-FE-LGT-01]** Lighthouse Performance score > 90.
- [ ] **[VAL-FE-CMP-01]** Components are typed.

## 5. References

- Related: [1010-frontend-accessibility.md](./1010-frontend-accessibility.md)
