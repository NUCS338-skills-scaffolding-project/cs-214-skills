---
skill_id: "return-behavior"
name: "Decide Return Behavior"
skill_type: "instructional"
stance: "hint"
tags: ["functions", "return-values", "side-effects", "interfaces"]
course_types: ["cs"]
learning_goal_tags:
  - "specify-io"
  - "evaluate-modularity"
  - "extract-requirements"
trigger_signals:
  - "print-vs-return"
  - "side-effect-confusion"
  - "function-contract"
python_entry: "logic.py"
version: "0.1.0"
---

# Decide Return Behavior

## Description
Helps students choose between returning a value and producing side effects such as
printing or mutating data. The tutor grounds the choice in the assignment wording
and the student's current design without writing a prohibited final function contract.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student mixes printing and returning in the same function
- Student asks whether a function should print, return, or modify something
- Assignment wording is unclear about function output
- Student's tests fail because the function prints instead of returning
- Student is designing helper functions and unsure what each should produce

## Tutor Stance
The tutor helps the student reason from the assignment and from how the function will
be used. It explains consequences of each choice, but it does not hand over the exact
final contract when the assignment requires the student to decide it.

## Flow

### Step 1 — Read the assignment wording
Ask the student to find verbs like "return," "print," "display," "modify," or "update."

### Step 2 — Identify the caller
Ask who needs the result: a human reading the screen, another function, a test, or a
mutated object.

### Step 3 — Compare consequences
Explain that returned values can be reused and tested, while printing is mainly for
human-visible output and mutation changes existing state.

### Step 4 — Check consistency
Ask whether the function currently does more than one output behavior and whether
that matches the assignment.

### Step 5 — State a draft behavior
Have the student write a one-sentence draft of the function's behavior, labeled as
their own interpretation if the prompt is ambiguous.

## Safe Output Types
- Tradeoff explanations
- Examples of consequences
- Prompts about assignment wording and caller expectations
- Questions that separate return values from side effects

## Must Avoid
- Writing the correct final function contract if prohibited
- Replacing the student's design with a finished interface
- Treating ambiguous wording as settled
- Writing complete solution code
- Encouraging unnecessary printing inside reusable helper functions

---

## Inputs
The `run` function in `logic.py` expects a dictionary with the following keys:

| Key | Type | Description |
|-----|------|-------------|
| `message` | `str` | The student's question about returning, printing, or side effects |
| `assignment` | `str` | Optional assignment wording |
| `current_design` | `str` | Optional summary of the student's current function design |

## Outputs
Returns a dictionary with:

| Key | Type | Description |
|-----|------|-------------|
| `prompt` | `str` | A tutor-style prompt or tradeoff explanation about function behavior |

## Usage
```python
from logic import run

result = run({
    "message": "My function prints the answer but the test says it got None."
})
print(result)
```

## Example Exchange
> **Student:** "Should my helper print the result or return it?"
>
> **Tutor:** "Ask who needs that result next. If another part of your program or a unit test needs to use the value, returning keeps it available. If the assignment only asks to display something to the user, printing may be appropriate at the outer layer."

## Notes
- Pair this skill with Detect Ambiguity when the assignment does not clearly say what behavior is expected.
- Pair this skill with Identify Outputs when the student needs to name the expected result precisely.
