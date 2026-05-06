---
skill_id: "identify-inv"
name: "Identify Invariants"
skill_type: "instructional"
stance: "socratic"
tags: ["invariants", "loops", "data-structures", "correctness"]
course_types: ["cs"]
learning_goal_tags:
  - "identify-invariants"
  - "trace-execution"
  - "evaluate-reasoning"
trigger_signals:
  - "loop-invariant"
  - "structure-property"
  - "correctness-check"
python_entry: "logic.py"
version: "0.1.0"
---

# Identify Invariants

## Description
Helps students state what must remain true while they work with loops, recursion,
or mutable data structures. The tutor turns the student's current design into
invariant prompts and lightweight correctness checks without completing a formal proof.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student is designing or debugging a loop
- Student is maintaining a data structure across updates
- Student asks whether an algorithm is correct
- Student needs to reason about recursive progress
- Student has a topic area but has not identified the property that must be preserved

## Tutor Stance
The tutor helps the student discover candidate invariants by asking about state,
progress, and preservation. It may give categories of possible invariants, but it
does not complete a formal proof or certify the student's algorithm as correct.

## Flow

### Step 1 — Name the changing state
Ask which variables, indexes, counters, or structure fields change during the process.

### Step 2 — Name the stable property
Ask what relationship or property should stay true despite those changes.

### Step 3 — Tie the invariant to the goal
Prompt the student to explain how that stable property supports the final output.

### Step 4 — Check initialization
Ask whether the property is true before the first iteration, call, or update.

### Step 5 — Check preservation
Ask whether one normal step keeps the property true.

## Safe Output Types
- Invariant prompts
- Correctness checks for initialization and preservation
- Categories of invariant candidates
- Questions about variable relationships and data structure properties

## Must Avoid
- Formal proof completion if not requested
- Claiming an invariant is correct without checking it
- Rewriting the algorithm to make the invariant work
- Providing finished proof text the student can submit
- Ignoring the student's current design and replacing it with a new one

---

## Inputs
The `run` function in `logic.py` expects a dictionary with the following keys:

| Key | Type | Description |
|-----|------|-------------|
| `message` | `str` | The student's question about correctness, loops, or data structures |
| `current_design` | `str` | Optional description of the student's design |
| `topic_area` | `str` | Optional topic area such as loops, recursion, trees, or graphs |

## Outputs
Returns a dictionary with:

| Key | Type | Description |
|-----|------|-------------|
| `prompt` | `str` | A tutor-style prompt for identifying or checking an invariant |

## Usage
```python
from logic import run

result = run({
    "current_design": "Use two pointers that move inward while scanning a sorted list.",
    "topic_area": "loops"
})
print(result)
```

## Example Exchange
> **Student:** "I'm using two pointers, but I'm not sure how to argue the loop is right."
>
> **Tutor:** "Ask what the two pointers mean after each iteration. Which part of the input has already been ruled out, and what must still be true about the part between the pointers?"

## Notes
- Pair this skill with Ask for Invariant when the student needs a single focused prompt.
- Pair this skill with Trace State Changes when the student needs to test an invariant on concrete state.
