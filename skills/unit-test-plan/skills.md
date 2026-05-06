---
skill_id: "unit-test-plan"
name: "Build a Unit Test Plan"
skill_type: "instructional"
stance: "hint"
tags: ["testing", "unit-tests", "test-plan", "verification"]
course_types: ["cs"]
learning_goal_tags:
  - "design-test-plans"
  - "handle-edge-cases"
  - "specify-io"
trigger_signals:
  - "how-to-test"
  - "test-strategy"
  - "missing-test-plan"
python_entry: "logic.py"
version: "0.1.0"
---

# Build a Unit Test Plan

## Description
Creates a structured testing strategy by helping students identify behavior categories,
representative cases, and expected outcomes. The tutor can produce a test matrix or
case list, but it does not implement a full test suite for the student.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student asks how to test their function or program
- Student has code or pseudocode but no testing strategy
- Student only tests happy paths
- Student needs to turn assignment requirements into test cases
- Student asks whether their planned tests are enough

## Tutor Stance
The tutor helps the student organize tests by behavior and risk. It can suggest
representative case categories and ask for expected outcomes, but the student writes
the actual test code and assertions.

## Flow

### Step 1 — Extract behaviors
Ask the student to list the distinct behaviors the assignment requires.

### Step 2 — Define test categories
Organize cases into typical, boundary, edge, error, and interaction cases as relevant.

### Step 3 — Pick representative cases
For each category, ask the student to choose one concrete input or scenario and state
the expected behavior.

### Step 4 — Prioritize coverage
Ask which cases cover the most important requirements and which cases are most likely
to reveal bugs.

### Step 5 — Check traceability
Have the student connect each planned test back to one requirement or design assumption.

## Safe Output Types
- Test matrix
- Representative case list
- Prompts asking for expected outcomes
- Coverage and risk checklists

## Must Avoid
- Full test suite implementation
- Writing copyable test functions or assertions
- Supplying exact expected outputs when the assignment expects the student to derive them
- Fixing the student's implementation while planning tests
- Treating tests as complete without checking against requirements

---

## Inputs
The `run` function in `logic.py` expects a dictionary with the following keys:

| Key | Type | Description |
|-----|------|-------------|
| `message` | `str` | The student's question about testing |
| `assignment` | `str` | Optional assignment wording or requirements |
| `student_code` | `str` | Optional code or pseudocode summary |

## Outputs
Returns a dictionary with:

| Key | Type | Description |
|-----|------|-------------|
| `prompt` | `str` | A tutor-style prompt for building a unit test plan |

## Usage
```python
from logic import run

result = run({
    "message": "How should I test my function that parses a score string?"
})
print(result)
```

## Example Exchange
> **Student:** "How do I test my function?"
>
> **Tutor:** "Start with a test matrix: one normal valid input, one boundary input, one invalid input, and one case that checks a requirement people might forget. For each row, write the requirement it checks and the expected behavior before writing any test code."

## Notes
- Pair this skill with Edge Case Tests when the student needs deeper help finding boundary and special cases.
- Pair this skill with Detect Ambiguity if the assignment does not define expected behavior for a case.
