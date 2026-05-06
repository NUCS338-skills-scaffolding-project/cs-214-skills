---
skill_id: "ask-invariant"
name: "Ask for Invariant"
skill_type: "instructional"
stance: "socratic"
tags: ["correctness", "invariants", "reasoning", "loops"]
course_types: ["cs"]
learning_goal_tags:
  - "identify-invariants"
  - "evaluate-reasoning"
trigger_signals:
  - "loop-correctness"
  - "recursive-reasoning"
  - "data-structure-invariant"
python_entry: "logic.py"
version: "0.1.0"
---

# Ask for Invariant

## Description
Supports correctness reasoning by prompting students to name what should remain true
as a loop, recursive call, or data structure operation progresses. The tutor asks for
the student's own invariant instead of supplying a formal proof.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student is working with a loop and asks whether it is correct
- Student is reasoning about recursion or repeated state changes
- Student has a data structure operation that must preserve a property
- Student has an informal idea but has not stated what stays true
- Student asks why an algorithm works, not just how to code it

## Tutor Stance
The tutor does not write a formal proof or provide the invariant as the final answer.
It asks a focused question that helps the student articulate a candidate invariant
in their own words and connect it to their current idea.

## Flow

### Step 1 — Locate the repeated process
Ask the student where the repeated step happens: loop body, recursive call, or data
structure update.

### Step 2 — Ask what should stay true
Prompt the student to state one fact that should be true before and after each step.
Keep the language informal at first.

### Step 3 — Connect to progress
Ask how that fact helps the algorithm move toward the goal without losing correctness.

### Step 4 — Check preservation
Have the student test the candidate invariant against one iteration or operation.

### Step 5 — Refine wording
If the statement is too vague, ask the student to name the variables, range, or structure
property involved.

## Safe Output Types
- Invariant prompts
- Questions about what stays true before and after a step
- Informal correctness checks
- Requests for the student to refine a candidate invariant

## Must Avoid
- Formal proof dumps
- Supplying the complete invariant as the answer
- Writing the student's proof or correctness argument
- Fixing the implementation while bypassing the reasoning step
- Treating an unstated assumption as a proven property

---

## Inputs
The `run` function in `logic.py` expects a dictionary with the following keys:

| Key | Type | Description |
|-----|------|-------------|
| `message` | `str` | The student's question or idea about a loop, recursion, or data structure |
| `student_idea` | `str` | Optional short summary of the student's current idea |

## Outputs
Returns a dictionary with:

| Key | Type | Description |
|-----|------|-------------|
| `prompt` | `str` | A tutor-style invariant prompt |

## Usage
```python
from logic import run

result = run({
    "student_idea": "I keep a running count while scanning the list."
})
print(result)
```

## Example Exchange
> **Student:** "I think my loop works because it counts the matches as it goes."
>
> **Tutor:** "Before proving the whole loop, try naming one fact that should stay true after every iteration. After processing the first k items, what should your count represent?"

## Notes
- Pair this skill with Trace State Changes when the student needs to test their invariant on a small input.
- Works best once the student has a proposed loop, recursive structure, or update operation.
