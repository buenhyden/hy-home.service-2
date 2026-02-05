import contextlib
import importlib.util
import os
import sys
import unittest
from pathlib import Path


def _load_module(module_name: str, path: Path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Failed to load module spec: {module_name} from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


@contextlib.contextmanager
def _chdir(path: Path):
    old = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)


class ValidateDocsTests(unittest.TestCase):
    def setUp(self):
        repo_root = Path(__file__).resolve().parents[1]
        self._work_base_dir = repo_root / "tests" / ".tmp_validate_docs"
        self._work_base_dir.mkdir(parents=True, exist_ok=True)
        self.validate_prd = _load_module(
            "validate_prd",
            repo_root / "scripts" / "validate_prd.py",
        )
        self.validate_spec = _load_module(
            "validate_spec",
            repo_root / "scripts" / "validate_spec.py",
        )

    def _workdir(self, name: str) -> Path:
        root = self._work_base_dir / name
        root.mkdir(parents=True, exist_ok=True)
        return root

    def test_prd_non_strict_accepts_star_bullet_status(self):
        root = self._workdir("prd_non_strict")
        prd = root / "docs" / "prd" / "feature-prd.md"
        prd.parent.mkdir(parents=True, exist_ok=True)
        prd.write_text(
            "\n".join(
                [
                    "# Feature PRD",
                    "",
                    "* **Status**: Draft",
                    "",
                    "## 1. Vision & Problem Statement",
                    "x",
                    "## 2. Target Personas (Primary & Secondary)",
                    "x",
                    "## 3. Success Metrics (Quantitative)",
                    "x",
                    "## 4. Key Use Cases & Acceptance Criteria (GWT)",
                    "x",
                    "## 5. Scope & Functional Requirements",
                    "x",
                    "## 6. Out of Scope",
                    "x",
                    "## 7. Milestones & Roadmap",
                    "x",
                    "## 8. Risks, Security & Compliance",
                    "x",
                    "",
                ]
            ),
            encoding="utf-8",
        )

        errors = self.validate_prd.validate_prd(prd, strict=False)
        self.assertEqual(errors, [])

    def test_prd_strict_requires_approved_ids_and_three_stories(self):
        root = self._workdir("prd_strict")
        prd = root / "docs" / "prd" / "feature-prd.md"
        prd.parent.mkdir(parents=True, exist_ok=True)
        prd.write_text(
            "\n".join(
                [
                    "# Feature PRD",
                    "",
                    "- **Status**: Approved",
                    "",
                    "## 1. Vision & Problem Statement",
                    "Vision: done",
                    "Problem: done",
                    "## 2. Target Personas (Primary & Secondary)",
                    "Persona: done",
                    "## 3. Success Metrics (Quantitative)",
                    "- REQ-PRD-MET-01: latency p95 < 200ms",
                    "- REQ-PRD-MET-02: conversion > 5%",
                    "## 4. Key Use Cases & Acceptance Criteria (GWT)",
                    "- STORY-01: Given A When B Then C",
                    "- STORY-02: Given A When B Then C",
                    "- STORY-03: Given A When B Then C",
                    "## 5. Scope & Functional Requirements",
                    "- [REQ-PRD-FUN-01] Something",
                    "- [REQ-PRD-FUN-02] Something else",
                    "## 6. Out of Scope",
                    "- Not building X",
                    "## 7. Milestones & Roadmap",
                    "- MVP: 2026-01-01",
                    "## 8. Risks, Security & Compliance",
                    "- Risk: mitigated",
                    "",
                ]
            ),
            encoding="utf-8",
        )

        errors = self.validate_prd.validate_prd(prd, strict=True)
        self.assertEqual(errors, [])

    def test_spec_strict_requires_local_approved_prd(self):
        root = self._workdir("spec_strict")
        prd = root / "docs" / "prd" / "feature-prd.md"
        spec = root / "specs" / "feature" / "spec.md"
        prd.parent.mkdir(parents=True, exist_ok=True)
        spec.parent.mkdir(parents=True, exist_ok=True)

        prd.write_text(
            "\n".join(
                [
                    "# Feature PRD",
                    "",
                    "- **Status**: Approved",
                    "",
                    "## 1. Vision & Problem Statement",
                    "x",
                    "## 2. Target Personas (Primary & Secondary)",
                    "x",
                    "## 3. Success Metrics (Quantitative)",
                    "- REQ-PRD-MET-01: x",
                    "## 4. Key Use Cases & Acceptance Criteria (GWT)",
                    "- STORY-01: x",
                    "- STORY-02: x",
                    "- STORY-03: x",
                    "## 5. Scope & Functional Requirements",
                    "- [REQ-PRD-FUN-01] x",
                    "## 6. Out of Scope",
                    "x",
                    "## 7. Milestones & Roadmap",
                    "x",
                    "## 8. Risks, Security & Compliance",
                    "x",
                    "",
                ]
            ),
            encoding="utf-8",
        )

        spec.write_text(
            "\n".join(
                [
                    "# Feature Technical Specification",
                    "",
                    "- **Status**: Draft",
                    "- **PRD Reference**: docs/prd/feature-prd.md",
                    "- **Architecture Reference**: ARCHITECTURE.md",
                    "",
                    "## 0. Architecture / Tech Stack Checklist (Fill Before Implementation)",
                    "x",
                    "## 0. Quality / Testing / Security Checklist (Fill Before Implementation)",
                    "x",
                    "## 0. Operations / Deployment / Monitoring Checklist (Fill Before Implementation)",
                    "x",
                    "## 1. Technical Overview & Architecture Style",
                    "x",
                    "## 2. Coded Requirements (Traceability)",
                    "| ID | Requirement Description | Priority | Parent PRD REQ |",
                    "| --- | --- | --- | --- |",
                    "| **REQ-SPC-001** | Something | High | REQ-PRD-FUN-01 |",
                    "## 3. Data Modeling & Storage Strategy",
                    "x",
                    "## 4. Interface Definitions",
                    "x",
                    "## 5. Non-Functional Requirements (NFR)",
                    "x",
                    "## 6. Scalability & Infrastructure",
                    "x",
                    "## 7. Verification Plan",
                    "- VAL-SPC-001: Unit test",
                    "## 9. Operations & Observability",
                    "x",
                    "",
                ]
            ),
            encoding="utf-8",
        )

        with _chdir(root):
            errors = self.validate_spec.validate_spec(spec, strict=True)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
