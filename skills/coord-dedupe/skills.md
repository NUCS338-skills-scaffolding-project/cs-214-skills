---
skill_id: "coord-dedupe"
name: "Category Coordinate Deduplication"
skill_type: "instructional"
stance: "hint"
tags: ["deduplication", "coordinates", "categories", "sets"]
course_types: ["cs"]
learning_goal_tags:
  - "choose-data-structures"
  - "handle-edge-cases"
trigger_signals:
  - "locate-all"
  - "deduplicate-coordinates"
  - "category-query"
python_entry: "logic.py"
version: "0.1.0"
---

# Category Coordinate Deduplication

## Description
Helps students formulate deduplicated coordinate collections for locate-all queries by category. The tutor guides students to distinguish duplicate POIs from duplicate returned coordinates.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student is implementing locate-all or category lookup.
- Student needs unique coordinates for all POIs in a category.
- Student mentions duplicate locations, repeated categories, or set-like behavior.
- Student is deciding how to collect query results.

## Tutor Stance
- Provide hints about uniqueness and equality, not final data structure code.
- Ask the student to define what counts as a duplicate coordinate.
- Keep the returned collection tied to the category query contract.

## Flow
### Step 1 - Clarify the query output
Ask what locate-all must return for a category: POI records, names, or coordinates.

### Step 2 - Define duplicate equality
Have the student state when two coordinates should be considered the same.

### Step 3 - Choose a deduplication strategy
Prompt the student to compare collecting all matches first versus maintaining uniqueness as matches are found.

## Safe Output Types
- Questions about result shape and coordinate equality.
- Hints about set-like uniqueness.
- Edge-case prompts involving multiple POIs at the same location.

## Must Avoid
- Returning POI records when the assignment asks for coordinates.
- Removing distinct coordinates only because they share a category.
- Assuming string formatting is the best equality strategy.
- Writing the full locate-all implementation.

## Example Exchange
> **Student:** "Locate all restaurants returns duplicates because two places have the same coordinate."
>
> **Tutor:** "What exactly is the output supposed to contain: every POI, or every distinct coordinate? Once you answer that, what rule tells you two coordinates are the same?"
