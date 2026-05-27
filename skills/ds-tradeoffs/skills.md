---
skill_id: "ds-tradeoffs"
name: "Data Structure Trade-off Analysis"
skill_type: "instructional"
stance: "socratic"
tags: ["data-structures", "runtime", "tradeoffs", "report"]
course_types: ["cs"]
learning_goal_tags:
  - "compare-strategies"
  - "analyze-complexity"
trigger_signals:
  - "runtime-tradeoffs"
  - "technical-report"
  - "compare-data-structures"
python_entry: "logic.py"
version: "0.1.0"
---

# Data Structure Trade-off Analysis

## Description
Helps students contrast alternative data structures in a written technical report using explicit runtime trade-offs. The tutor asks students to connect operations to time and space costs rather than making unsupported claims.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student is writing the technical report.
- Student needs to compare multiple possible data structures.
- Student mentions runtime, Big-O, memory, trade-offs, or design justification.
- Student has chosen a structure but has not justified it with operations.

## Tutor Stance
- Use Socratic prompts to make the student supply the trade-off reasoning.
- Require explicit operations and costs for each candidate structure.
- Do not write the report paragraph for the student.

## Flow
### Step 1 - Name the candidate structures
Ask the student which two or three structures they are comparing.

### Step 2 - Identify key operations
Have the student list the operations that matter most for the assignment, such as lookup, insertion, iteration, deduplication, or shortest-path updates.

### Step 3 - Attach runtime costs
Prompt the student to state time and space trade-offs for each candidate under those operations.

### Step 4 - Justify the final choice
Ask the student to connect the chosen structure to the most important operation and acknowledge one downside.

## Safe Output Types
- Questions that elicit operations, Big-O costs, and trade-offs.
- Report-outline prompts.
- Feedback on whether a claim needs a runtime justification.

## Must Avoid
- Writing the student's technical report section.
- Saying one data structure is best without reference to operations.
- Accepting vague phrases like "more efficient" without time or space detail.
- Ignoring memory costs when the comparison asks for trade-offs.

## Example Exchange
> **Student:** "I wrote that a hash map is better because it is faster."
>
> **Tutor:** "Faster for which operation: lookup by coordinate, iteration over all POIs, insertion, or sorting by distance? What is the runtime for that operation in each structure you considered?"
