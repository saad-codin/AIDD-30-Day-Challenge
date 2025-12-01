<!--
---
sync_impact_report:
  version_change: "none -> v1.0.0"
  modified_principles:
    - "New Principle: Simplicity and Focus"
  added_sections: []
  removed_sections:
    - "Principle 2: [PRINCIPLE_2_NAME]"
    - "Principle 3: [PRINCIPLE_3_NAME]"
  template_updates:
    - path: ".specify/templates/plan-template.md"
      status: "pending"
    - path: ".specify/templates/spec-template.md"
      status: "pending"
    - path: ".specify/templates/tasks-template.md"
      status: "pending"
  todos: []
---
-->
# Constitution for Simple Calculator

> This document outlines the non-negotiable principles governing the Simple Calculator project. All specifications, plans, and code MUST adhere to these rules.

**Version**: `v1.0.0`
**Ratification Date**: `2025-12-02`
**Last Amended**: `2025-12-02`

---

## 1. Guiding Principles

### Principle 1: Simplicity and Focus

- **Description**: The project must focus exclusively on basic arithmetic operations (addition, subtraction, multiplication, division). No scientific, financial, or other complex functions will be included.
- **Rationale**: To maintain a lightweight, easy-to-use, and bug-free application. This aligns with the project's core identity as a 'simple calculator'.

---

## 2. Governance and Amendments

This constitution is a living document. Amendments can be proposed via a pull request and MUST be ratified by the project owner.

### Versioning

Changes to this constitution MUST follow semantic versioning:
- **MAJOR**: Backward-incompatible changes (e.g., removing a core principle).
- **MINOR**: Adding a new principle or significant new guidance.
- **PATCH**: Clarifications, typo fixes, or minor wording changes.

### Compliance

All project artifacts (specifications, plans, code) are subject to review for compliance with this constitution. Non-compliant work MUST be revised.