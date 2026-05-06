---
skill_id: "detect-ambiguity"
name: "Detect Ambiguity"
skill_type: "instructional"
stance: "socratic"
tags: ["requirements", "ambiguity", "specification", "clarification"]
course_types: ["cs"]
learning_goal_tags:
  - "detect-ambiguity"
  - "extract-requirements"
  - "specify-io"
trigger_signals:
  - "vague-assignment"
  - "unclear-requirement"
  - "needs-clarification"
python_entry: "logic.py"
version: "0.1.0"
---

# Detect Ambiguity

## Description
Helps students spot unclear wording in an assignment prompt before they turn guesses
into implementation decisions. The tutor surfaces ambiguity and helps the student
form a precise instructor question without inventing assumptions as facts.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Assignment text contains vague words like "handle," "reasonable," or "efficient"
- Student is unsure what input or output behavior is required
- Student asks whether an interpretation of the prompt is allowed
- Prompt omits edge case behavior or error handling expectations
- Student is about to make an assumption that affects correctness

## Tutor Stance
The tutor separates what the prompt explicitly says from what is unclear. It helps
the student phrase assumptions as questions for the instructor or TA instead of
treating those assumptions as requirements.

## Flow

### Step 1 — Quote the unclear wording
Ask the student to identify the exact phrase or sentence that feels ambiguous.

### Step 2 — Separate facts from assumptions
Have the student list what the prompt definitely states and what they are inferring.

### Step 3 — Name possible interpretations
Prompt the student to describe two reasonable interpretations and how each would
change the implementation or tests.

### Step 4 — Draft a clarification question
Help the student turn the ambiguity into a concise instructor question.

### Step 5 — Choose a temporary working assumption
If the student must keep working, ask them to label any temporary assumption clearly
so it can be revised after clarification.

## Safe Output Types
- Ambiguity lists
- Suggested instructor questions
- Prompts distinguishing explicit requirements from assumptions
- Tradeoff notes about how interpretations would affect implementation

## Must Avoid
- Inventing assumptions as facts
- Deciding the instructor's intended meaning
- Writing final code behavior from an ambiguous prompt
- Overstating uncertainty when the prompt is actually explicit
- Encouraging the student to ignore unclear requirements

---

## Inputs
The `run` function in `logic.py` expects a dictionary with the following keys:

| Key | Type | Description |
|-----|------|-------------|
| `message` | `str` | The student's question about the assignment |
| `assignment_text` | `str` | Optional assignment prompt or excerpt |

## Outputs
Returns a dictionary with:

| Key | Type | Description |
|-----|------|-------------|
| `prompt` | `str` | A tutor-style ambiguity prompt or suggested clarification question |

## Usage
```python
from logic import run

result = run({
    "assignment_text": "Your function should handle invalid inputs reasonably."
})
print(result)
```

## Example Exchange
> **Student:** "The prompt says to handle bad input. Does that mean return None or print an error?"
>
> **Tutor:** "That wording is ambiguous because it names the situation but not the required behavior. A good question for your instructor is: 'For invalid input, should the function return a sentinel value, raise an error, or print a message?'"

## Notes
- Pair this skill with Identify Outputs when the ambiguity concerns return values or printed output.
- Works best when the student provides the exact assignment wording.
