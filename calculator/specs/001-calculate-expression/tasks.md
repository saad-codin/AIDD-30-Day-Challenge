# Tasks: Calculate Expression

**Input**: Design documents from `specs/001-calculate-expression/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Create project directories: `src/calculator`, `tests`
- [X] T002 [P] Create `src/calculator/__init__.py`
- [X] T003 [P] Create `src/calculator/main.py`
- [X] T004 [P] Create `tests/test_calculator.py`

---

## Phase 2: User Story 1 - Basic Arithmetic Calculation (Priority: P1) 🎯 MVP

**Goal**: Implement the core calculator logic to parse and evaluate basic arithmetic expressions.

**Independent Test**: The calculator can be run with a string expression and will return the correct numerical result or a descriptive error message.

### Tests for User Story 1

- [X] T005 [P] [US1] Add unit test for addition in `tests/test_calculator.py`
- [X] T006 [P] [US1] Add unit test for subtraction in `tests/test_calculator.py`
- [X] T007 [P] [US1] Add unit test for multiplication in `tests/test_calculator.py`
- [X] T008 [P] [US1] Add unit test for division in `tests/test_calculator.py`
- [X] T009 [P] [US1] Add unit test for division by zero in `tests/test_calculator.py`
- [X] T010 [P] [US1] Add unit test for invalid expressions in `tests/test_calculator.py`

### Implementation for User Story 1

- [X] T011 [US1] Implement expression validation in `src/calculator/main.py`
- [X] T012 [US1] Implement safe evaluation of the expression in `src/calculator/main.py` (depends on T011)
- [X] T013 [US1] Implement CLI argument parsing in `src/calculator/main.py`

---

## Dependencies & Execution Order

- **Phase 1** must be completed before **Phase 2**.
- Within **Phase 2**, tests (T005-T010) should be written first and are parallelizable.
- Implementation tasks (T011-T013) in **Phase 2** should be done after the tests.
