---
skill_id: "poi-records"
name: "POI Record Construction"
skill_type: "instructional"
stance: "hint"
tags: ["poi", "records", "locations", "categories"]
course_types: ["cs"]
learning_goal_tags:
  - "choose-data-structures"
  - "specify-io"
trigger_signals:
  - "point-of-interest"
  - "poi-record"
  - "structured-location-category-name"
python_entry: "logic.py"
version: "0.1.0"
---

# POI Record Construction

## Description
Helps students construct point-of-interest records with structured locations, semantic categories, and unique names. The tutor emphasizes clear fields and searchable records.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student is parsing or storing points of interest.
- Student needs to decide what fields a POI record contains.
- Student mentions location, category, and name data together.
- Student is unsure how POIs relate to map coordinates.

## Tutor Stance
- Give structural hints about record fields without implementing the record.
- Ask the student to connect each field to a later query.
- Keep unique names and categories conceptually separate.

## Flow
### Step 1 - Name the required fields
Ask the student to identify the location, category, and name in one POI input record.

### Step 2 - Connect fields to future queries
Have the student explain which queries use the name, which use the category, and which use the coordinate.

### Step 3 - Check record uniqueness
Prompt the student to decide what must be unique and what may repeat across multiple POIs.

## Safe Output Types
- Field-identification prompts.
- Conceptual record diagrams described in words.
- Questions about lookup by name, category filtering, and stored coordinates.

## Must Avoid
- Writing the POI class or struct.
- Treating category as a unique identifier.
- Treating display name and internal key as identical without assignment support.
- Losing the structured coordinate by storing only text.

## Example Exchange
> **Student:** "For POIs, should I just store strings?"
>
> **Tutor:** "Which later operation needs the coordinate, which one needs the category, and which one needs the unique name? That tells you which fields belong in each POI record."
