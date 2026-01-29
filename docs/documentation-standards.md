# Documentation Structure & Standards

This document defines how documentation is organized within the `docs/` folder and the standards for creating new documentation files.

## 📂 Folder Layout

```text
docs/
├── adr/                        # Architecture Decision Records
├── prd/                        # Product Requirement Documents
├── 01-project-overview.md      # Mission & Philosophy
├── 02-architecture.md          # System Design
├── ...                         # Numbered guides 03-10
├── onboarding.md               # Entry point for new developers
├── README.md                   # Documentation index (Root of /docs)
└── documentation-standards.md  # This file
```

---

## 🏷️ Naming Conventions

Files should follow a numbered system to ensure a logical reading order:

- **`01-project-overview.md`**: Mission, philosophy, and high-level goals.
- **`02-architecture.md`**: System design and boundaries.
- **`03-governance-standards.md`**: Rules and policies.
- ... and so on.

This structure allows new developers to read sequentially from 01 to 10 to gain a complete understanding of the system.

---

## 📝 Document Standards

Every documentation file MUST follow this basic template:

1. **H1 Title**: Clear and descriptive.
2. **Context**: 1-2 sentences explaining why this guide is needed.
3. **Prerequisites**: List any tools or access required.
4. **Steps**: Clear, numbered instructions with code blocks where applicable.
5. **Verification**: How to test if the setup/fix was successful.

### Code Block Policy

- Always specify the language for syntax highlighting.
- Use full paths or context (e.g., `// File: .env.example`) within code comments if the file is not obvious.

---

## 🤖 AI Alignment

Documentation is designed to be machine-parseable. Avoid flowery language and prioritize structural clarity, code snippets, and explicit step-by-step instructions. Reference specific Pillar rules (e.g., `[REQ-0130-01]`) where applicable to ensure alignment with project standards.
