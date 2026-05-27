---
skill_id: "coord-rep"
name: "Coordinate Representation"
skill_type: "instructional"
stance: "hint"
tags: ["coordinates", "objects", "precision", "map"]
course_types: ["cs"]
learning_goal_tags:
  - "choose-data-structures"
  - "specify-io"
trigger_signals:
  - "raw-position-coordinates"
  - "coordinate-object-representation"
  - "geographic-precision"
python_entry: "logic.py"
version: "0.1.0"
---

# Coordinate Representation

## Description
Helps students map raw position coordinates to internal object-oriented representations without losing geographic precision. The tutor focuses attention on exact field meaning, ordering, and preserving numeric values.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student is converting latitude/longitude or coordinate pairs into objects.
- Student is unsure how to represent a position internally.
- Student mentions rounding, truncating, swapping, or normalizing coordinates.
- Student needs to preserve geographic precision across parsing and storage.

## Tutor Stance
- Give a directional hint about preserving the input contract, but do not write the class or constructor for the student.
- Keep the student focused on the exact meaning of each coordinate field.
- Ask the student to verify that object construction is a lossless transformation.

## Flow
### Step 1 - Identify the raw coordinate contract
Ask the student to name the coordinate fields in order and state what each value represents.

### Step 2 - Match fields to object state
Have the student map each raw field to one internal field without changing type, order, or precision.

### Step 3 - Check for loss
Prompt the student to describe how they would test that the object returns the same coordinate values that were parsed.

## Safe Output Types
- Conceptual hints about field mapping and precision.
- Questions about coordinate order, numeric type, and object invariants.
- Small checklists for verifying lossless conversion.

## Must Avoid
- Writing the student's coordinate class or constructor.
- Choosing exact field names unless the assignment already specifies them.
- Suggesting rounding or truncation unless explicitly required by the prompt.
- Treating latitude and longitude as interchangeable.

## Example Exchange
> **Student:** "I have raw coordinates and need to make location objects, but I am not sure what to store."
>
> **Tutor:** "Start with the input contract: which value is latitude, which value is longitude, and what numeric type preserves them exactly enough for the assignment's comparisons?"
