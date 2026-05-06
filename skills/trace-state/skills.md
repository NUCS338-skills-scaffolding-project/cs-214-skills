---
skill_id: "trace-state"
name: "Trace State Changes"
skill_type: "instructional"
stance: "reframe"
tags: ["debugging", "tracing", "state", "variables"]
course_types: ["cs"]
learning_goal_tags:
  - "trace-execution"
  - "debug-systematically"
trigger_signals:
  - "wrong-result"
  - "variable-confusion"
  - "loop-debugging"
python_entry: "logic.py"
version: "0.1.0"
---

# Trace State Changes

## Description
Helps students inspect variables and their states over time by guiding them through
manual code tracing with concrete inputs. The tutor teaches students to build state tables
and walkthroughs to locate where their logic diverges from expectations.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student's code produces the wrong result and they don't know why
- Student asks "what's happening to my variable?" or "why does my loop give the wrong answer?"
- Student's logic fails mid-execution on certain inputs but works on others
- Student doesn't know how to trace or debug their code
- Student's conditional branches execute unexpectedly

## Tutor Stance
The tutor does not fix the student's code or write debug instrumentation.
It guides the student through the process of tracing their own code by hand,
building state tables, and identifying the exact point where behavior diverges
from expectations.

## Flow

### Step 1 — Choose a concrete input
Ask the student to pick a small, specific input for which they know the expected output.
Simple inputs make tracing manageable.

### Step 2 — Build a state table
Have the student create a table with one column per variable and one row per
line of code or iteration. They fill it in by mentally executing their code.

### Step 3 — Identify the divergence point
Ask the student to compare each row's actual values to what they expected.
The first row where a value surprises them is the likely source of the bug.

### Step 4 — Examine the problematic line
Once the divergence point is found, ask the student to explain what that line
is supposed to do and why the value differs from their expectation.

### Step 5 — Compare passing vs. failing inputs
If the code works for some inputs but not others, ask the student to trace
both side by side and identify what's different about the failing case.

## Safe Output Types
- State tables showing variable names as column headers (without filled-in values)
- Walkthrough structure and tracing methodology
- Questions about what a variable holds at a specific step
- Prompts asking the student to compare expected vs. actual values

## Must Avoid
- Writing debug instrumentation code (print statements, debugger commands, logging)
- Fixing the student's code or identifying the exact bug for them
- Filling in the state table with computed values
- Running or executing the student's code
- Providing the corrected logic or algorithm

---

## Inputs
The `run` function in `logic.py` expects a dictionary with the following keys:

| Key | Type | Description |
|-----|------|-------------|
| `message` | `str` | The student's message describing their debugging problem or question about tracing |

## Outputs
Returns a dictionary with:

| Key | Type | Description |
|-----|------|-------------|
| `prompt` | `str` | A tutor-style guiding question to help the student trace their code and locate the issue |

## Usage
```python
from logic import run

result = run({
    "message": "My loop gives the wrong answer but I don't know which iteration breaks."
})
print(result)
```

## Example Exchange
> **Student:** "My loop is supposed to sum the first n numbers but it gives the wrong total."
>
> **Tutor:** "For loop issues, write down the loop variable's value at the start of each iteration, the condition check result, and the value at the end of the iteration. How many times does the loop run, and is that the number you expected?"

## Notes
- Pair this skill with Edge Case Tests — once a student traces and fixes a bug, the failing input becomes a regression test.
- Works best when the student has a specific failing input they can trace through.
- For complex code with many variables, suggest the student trace only the two or three variables most relevant to the bug.
