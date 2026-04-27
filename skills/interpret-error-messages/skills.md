---
skill_id: "interpret-error-messages"
name: "Interpret Error Messages"
skill_type: "code"
tags: ["debugging", "errors", "data-structures", "algorithms"]
python_entry: "logic.py"
---

# Interpret Error Messages

## Description
Classifies and explains compiler, runtime, and logic errors common in
data structures and algorithms coursework. Returns an error type label,
a plain-English explanation of likely causes, and a guiding question.

## Skill Type
- **Type:** code
- **Course Focus:** CS

## When to Trigger
- Student pastes an error message into the chat
- Student says they don't understand why their code crashed
- Student is stuck on a DS/A assignment involving lists, trees, graphs, or recursion

---

## Inputs
A dict with these keys:
- `error_text` (str): the full error message the student pasted
- `code_context` (str, optional): the student's code snippet near the crash

## Outputs
A dict with:
- `error_type` (str): one of `"syntax"`, `"runtime"`, `"unknown"`
- `likely_cause` (str): plain-English explanation of what probably went wrong
- `guiding_question` (str): a question to point the student toward the fix

## Usage
```python
from logic import run
result = run({
    "error_text": "IndexError: list index out of range",
    "code_context": "return self.array[self.size]"
})
print(result)
```

## Notes
This skill never returns corrected code. It only classifies the error
and guides the student to find the fix themselves. Safe to use on any DS/A assignment.