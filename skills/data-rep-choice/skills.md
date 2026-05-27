---
skill_id: "data-rep-choice"
name: "Choose Data Representation"
skill_type: "instructional"
stance: "hint"
tags: ["data-structure", "representation", "modeling", "design"]
course_types: ["cs"]
learning_goal_tags:
  - "choose-data-structures"
  - "compare-strategies"
trigger_signals:
  - "data-structure-choice"
  - "representation-confusion"
  - "performance-tradeoff"
python_entry: "logic.py"
version: "0.1.0"
---

# Choose Data Representation

## Description
Helps students model entities and relationships by comparing the conceptual fit of
arrays, maps, sets, and other data structures. The tutor guides students to reason about
what they need to store and which operations matter most, without prescribing a specific implementation.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student is unsure which data structure to use for a problem
- Student asks "should I use a list or a dictionary?"
- Student doesn't know what information to store or track
- Student needs to relate two entities but isn't sure how to represent the link
- Student is choosing between flat and nested structures
- Student asks about performance trade-offs between structures

## Tutor Stance
The tutor does not name a specific data structure as the answer or build any part of the solution.
It helps the student reason about their problem's entities, relationships, and key operations
so the student can arrive at an informed choice independently.

## Flow

### Step 1 — Identify the entities
Ask the student to list the nouns or concepts in the problem. What are the distinct
things the program needs to represent or keep track of?

### Step 2 — Describe the relationships
Ask the student how the entities relate. Is it one-to-one, one-to-many, or many-to-many?
Does order matter? Are there duplicates?

### Step 3 — Identify the key operations
Ask what the code will do most often with the data — search, iterate, insert, count, or
look up by key. This narrows the set of suitable structures.

### Step 4 — Compare candidate structures
Without naming the "right" answer, prompt the student to evaluate two or three structures
against the relationships and operations they identified. Ask which one best fits.

### Step 5 — Confirm the choice
Have the student state which structure they will use and why, in their own words,
before they begin implementing.

## Safe Output Types
- Questions that help the student identify entities and relationships
- Prompts asking the student to consider access patterns and operations
- General descriptions of how categories of structures differ (ordered vs. unordered, keyed vs. indexed)
- Requests for the student to justify their choice

## Must Avoid
- Naming the exact data structure the student should use
- Providing implementation details beyond high-level conceptual categories
- Building any part of the solution around the chosen structure
- Writing code that initializes or populates a data structure
- Making the decision for the student

---

## Inputs
The `run` function in `logic.py` expects a dictionary with the following keys:

| Key | Type | Description |
|-----|------|-------------|
| `message` | `str` | The student's message or question about data structure choice |

## Outputs
Returns a dictionary with:

| Key | Type | Description |
|-----|------|-------------|
| `prompt` | `str` | A tutor-style guiding question to help the student reason about their choice |

## Usage
```python
from logic import run

result = run({
    "message": "Should I use a list or a dictionary for storing student grades?"
})
print(result)
```

## Example Exchange
> **Student:** "I need to store student names and their grades but I don't know if I should use a list or a dictionary."
>
> **Tutor:** "Think about how you'll access the data. Do you need to look things up by a specific key or label, or are you working with an ordered sequence of items? That distinction usually points you toward the right structure."

## Notes
- Pair this skill with Identify Outputs to first clarify what the program should produce, then choose how to represent it internally.
- Works best when the student has already read the problem but hasn't started coding yet.
- For problems involving multiple related entities, guide the student through each entity's representation separately before combining them.
