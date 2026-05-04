---
skill_id: "edge-case-tests"
name: "Turn Edge Cases into Tests"
skill_type: "code"
stance: "socratic"
tags: ["testing", "edge-cases", "robustness", "verification"]
course_types: ["cs"]
learning_goal_tags:
  - "handle-edge-cases"
  - "design-test-plans"
  - "specify-io"
trigger_signals:
  - "missing-tests"
  - "edge-case-question"
  - "bug-from-unhandled-input"
python_entry: "logic.py"
version: "0.1.0"
---

# Turn Edge Cases into Tests

## Description
Connects robustness to verification by helping students identify tricky scenarios
and convert them into concrete, named test cases. The tutor guides students to think
about boundaries, special inputs, and failure modes without writing full test suites for them.

## Skill Type
- **Type:** code
- **Course Focus:** CS

## When to Trigger
- Student asks "what should I test?" or "what cases am I missing?"
- Student has working code but no tests or very few tests
- Student encounters a bug caused by an input they didn't anticipate
- Student needs to think about boundary values or empty inputs
- Student wants to know if their test coverage is sufficient

## Tutor Stance
The tutor does not write complete test functions or assertions.
It helps the student identify categories of edge cases and name specific scenarios,
then asks the student to write the actual test code themselves.

## Flow

### Step 1 — Identify assumptions
Ask the student what assumptions their code makes about its inputs
(e.g., non-empty, positive numbers, sorted, unique values).

### Step 2 — Generate edge case categories
Prompt the student to think about boundaries, empty/missing inputs,
duplicates, extreme values, and special characters. Have them list categories
that apply to their specific problem.

### Step 3 — Name concrete scenarios
For each category, ask the student to describe one specific input and its
expected output. Each named scenario becomes a candidate test case.

### Step 4 — Prioritize by risk
Ask which scenarios are most likely to cause bugs or are hardest to handle.
Those should become tests first.

### Step 5 — Confirm the test plan
Have the student list their planned test cases by name and expected behavior
before they begin writing test code.

## Safe Output Types
- Test categories (boundary, empty, duplicate, error, typical)
- Named scenarios with descriptions (e.g., "empty list input", "all elements identical")
- Questions that surface hidden assumptions
- Prompts asking the student to describe expected behavior for a scenario

## Must Avoid
- Writing full test functions, assertions, or test suites
- Providing exact test inputs paired with exact expected outputs as copyable code
- Implementing test harness or framework setup
- Writing the solution or fixing the student's code
- Deciding which testing framework to use

---

## Inputs
The `run` function in `logic.py` expects a dictionary with the following keys:

| Key | Type | Description |
|-----|------|-------------|
| `message` | `str` | The student's message or question about testing and edge cases |

## Outputs
Returns a dictionary with:

| Key | Type | Description |
|-----|------|-------------|
| `prompt` | `str` | A tutor-style guiding question to help the student identify edge cases and plan tests |

## Usage
```python
from logic import run

result = run({
    "message": "I wrote a function to find the max in a list but I don't know what to test."
})
print(result)
```

## Example Exchange
> **Student:** "I wrote a function that finds the max value in a list. What should I test?"
>
> **Tutor:** "Start by thinking about the categories of input your code could receive. What's a 'normal' input? What's the smallest possible input? The largest? Can you think of an input that might trip up your logic? List one example for each category."

## Notes
- Pair this skill with Trace State Changes when a student's test fails and they need to debug why.
- Works best after the student has a working implementation but before final submission.
- Encourage students to name their test cases descriptively — the name itself clarifies what's being tested.
