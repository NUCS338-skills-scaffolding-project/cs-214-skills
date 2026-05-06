---
skill_id: "identify-outputs"
name: "Identify Outputs"
skill_type: "code"
tags: ["output", "result", "format"]
course_types: ["cs"]
learning_goal_tags:
  - "specify-io"
  - "extract-requirements"
trigger_signals:
  - "output-confusion"
  - "return-vs-print"
  - "wrong-output-format"
python_entry: "logic.py"
version: "0.1.0"
---

# Identify Outputs

## Description
Helps students clarify the required result and output format for a programming assignment.
This code skill can directly identify what the code should return, print, store,
or write when the assignment and examples make that clear.

## Skill Type
- **Type:** code
- **Course Focus:** CS

## When to Trigger
- Student is unsure what their function should return
- Student confuses printing output with returning a value
- Student asks "what am I supposed to output?" or "what format should the result be in?"
- Student's code produces a result but in the wrong type or structure
- Student does not distinguish between intermediate values and final output

## Code Behavior
The skill extracts output requirements from the assignment description and examples.
It can state the expected mechanism, type, and format directly, while avoiding a
complete implementation of the output logic.

## Flow

### Step 1 — Surface the assignment requirements
Ask the student to identify what the assignment or prompt specifies about expected output
(return type, print format, data structure, file output, etc.).

### Step 2 — Compare with examples
If example inputs/outputs are provided, ask the student what patterns they notice
in the expected results (e.g., data type, structure, separators, ordering).

### Step 3 — Distinguish output mechanisms
Ask whether the task requires `return`, `print`, writing to a file, or storing in a
data structure. Clarify the difference if the student conflates them.

### Step 4 — Confirm the output plan
Have the student state, in their own words, exactly what their code should produce
and in what format before they begin implementing.

## Safe Output Types
- Direct identification of expected output mechanism, type, and format
- Clarifications on return vs. print vs. store
- References to example output patterns
- Prompts asking the student to confirm ambiguous output behavior

## Must Avoid
- Writing a complete solution implementation
- Inventing output requirements when the assignment is ambiguous
- Converting the student's data structures for them when that is the core task

---

## Inputs
The `run` function in `logic.py` expects a dictionary with the following keys:

| Key | Type | Description |
|-----|------|-------------|
| `assignment` | `str` | The text of the assignment prompt or problem statement |
| `examples` | `list[dict]` | A list of example input/output pairs, each with `"input"` and `"expected_output"` keys |

## Outputs
Returns a dictionary with:

| Key | Type | Description |
|-----|------|-------------|
| `output_type` | `str` | The identified output mechanism (`"return"`, `"print"`, `"file"`, `"store"`) |
| `output_format` | `str` | A description of the expected format (e.g., `"list of integers"`, `"comma-separated string"`) |
| `guidance` | `str` | A tutor-style prompt to help the student confirm their understanding |

## Usage
```python
from logic import run

result = run({
    "assignment": "Write a function that takes a list of numbers and returns the even ones.",
    "examples": [
        {"input": [1, 2, 3, 4, 5], "expected_output": [2, 4]},
        {"input": [10, 15, 20], "expected_output": [10, 20]}
    ]
})
print(result)
```

## Example Exchange
> **Student:** "I filtered the even numbers but I don't know if I should print them or return them."
>
> **Tutor:** "Look at the assignment — does it say 'write a function that returns' or 'print the result'? What do the example outputs look like: are they shown as function return values or printed lines?"

## Notes
- Pair this skill with assignment-parsing utilities that can extract example I/O blocks automatically.
- Works best when the student already has a partial solution but is stuck on the final output step.
- For assignments with multiple output formats (e.g., both console and file), guide the student through each one separately.
