---
trigger: model_decision
glob: ["**/*"]
description: "Web Performance Standards: Enforces Core Web Vitals, optimal resource loading, and rendering efficiency."
---

# Web Performance Standards

- **Role**: Performance Engineer
- **Purpose**: Define standards for ensuring high-speed, responsive, and efficient user experiences across all web surfaces.
- **Activates When**: Developing UI components, configuring build pipelines, or optimizing asset delivery strategies.

**Trigger**: model_decision — Apply during the development and optimization of web assets.

## 1. Standards

### Principles

- **[REQ-PERF-01] Core Web Vital Centricity**
  - Applications MUST prioritize metrics that impact user perception: Largest Contentful Paint (LCP), First Input Delay (FID), and Cumulative Layout Shift (CLS).
- **[REQ-PERF-02] Progressive Enhancement**
  - Core functionality MUST be delivered using minimal payloads, with non-essential enhancements loaded asynchronously.
- **[REQ-PERF-03] Budget-Driven Development**
  - All new features MUST adhere to a "Performance Budget" (e.g., maximum JS bundle size, maximum total page weight).

### Performance Metrics Baseline

| Metric | Requirement ID | Target Threshold |
| --- | --- | --- |
| LCP | [REQ-PERF-04] | < 2.5 seconds |
| FID | [REQ-PERF-05] | < 100 milliseconds |
| CLS | [REQ-PERF-06] | < 0.1 |
| Bundle Size | [REQ-PERF-07] | < 200KB (Critical JS) |

### Must

- **[REQ-PERF-08] Mandatory Image Optimization**
  - All images MUST be appropriately sized, compressed, and served in modern formats (WebP/AVIF) with `loading="lazy"` where applicable.
- **[REQ-PERF-09] Explicit Height/Width on Assets**
  - To prevent CLS, all media elements (images, videos, ads) MUST have explicit `height` and `width` attributes or aspect-ratio CSS.
- **[REQ-PERF-10] Critical CSS Inlining**
  - Critical path CSS SHOULD be inlined in the `<head>` to ensure the first fold renders without waiting for external stylesheets.

### Must Not

- **[BAN-PERF-01] Synchronous Blocking Scripts**
  - Third-party scripts MUST NOT be loaded synchronously in the `<head>`; use `async` or `defer` attributes.
- **[BAN-PERF-02] Layout Trashing**
  - Avoid repeated read/write cycles of DOM properties (e.g., `offsetTop`) inside loops that cause browser reflow storms.

### Failure Handling

- **Stop Condition**: Stop feature deployment if a Lighthouse audit identifies an LCP score lower than "Good" (> 2.5s) on primary landing pages.

## 2. Procedures

- **[PROC-PERF-01] Bundle Audit**
  - IF a PR increases the compiled JS bundle by > 5% THEN MUST conduct a formal review of new dependencies.
- **[PROC-PERF-02] Real-User Monitoring (RUM)**
  - Regularly analyze RUM data to identify performance regressions across varied device types and network conditions.

## 3. Examples

### Efficient Resource Loading (Good)

```html
<link rel="preload" href="critical.js" as="script">
<img src="hero.webp" width="800" height="600" alt="Hero">
```

## 4. Validation Criteria

- **[VAL-PERF-01] Lighthouse Score**
  - [ ] 100% of production routes achieve a Lighthouse Performance score of > 90.
- **[VAL-PERF-02] CLS Verification**
  - [ ] Visual regression tests confirm that 0.0 layout shift occurs during resource loading.
- **[VAL-PERF-03] Bundle Analysis Pass**
  - [ ] Webpack/Vite bundle analyzer confirms that zero unused massive libraries are included in the initial chunk.
