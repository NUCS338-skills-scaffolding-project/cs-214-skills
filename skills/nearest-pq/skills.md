---
skill_id: "nearest-pq"
name: "Nearest Neighbor Priority Queue"
skill_type: "instructional"
stance: "hint"
tags: ["priority-queue", "nearest-neighbor", "distance", "ranking"]
course_types: ["cs"]
learning_goal_tags:
  - "choose-data-structures"
  - "compare-strategies"
trigger_signals:
  - "nearest-neighbor"
  - "priority-queue"
  - "spatial-distance-ranking"
python_entry: "logic.py"
version: "0.1.0"
---

# Nearest Neighbor Priority Queue

## Description
Helps students integrate a priority queue to track and sort spatial distances for nearest-neighbor calculations. The tutor focuses on what the queue prioritizes and when candidates are inserted or removed.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student is implementing closest-location or nearest-neighbor behavior.
- Student mentions a priority queue, heap, or sorted distances.
- Student is ranking candidate POIs or coordinates by spatial distance.
- Student is unsure what data belongs in each queue entry.

## Tutor Stance
- Provide implementation direction at the algorithm-design level only.
- Ask the student to define the priority value before choosing queue contents.
- Keep distance calculation separate from queue ordering.

## Flow
### Step 1 - Define the priority
Ask what numeric distance determines which candidate should come out first.

### Step 2 - Decide the queue entry shape
Have the student identify what must be stored with each distance so the result can be returned.

### Step 3 - Handle ties and stopping
Prompt the student to consider equal distances, requested result counts, and when the search is complete.

## Safe Output Types
- Questions about priority values and queue entries.
- Hints about heap behavior and distance sorting.
- Edge-case prompts for ties and empty candidate sets.

## Must Avoid
- Writing heap or priority queue code for the student.
- Recomputing distance in a way that changes ordering unpredictably.
- Sorting by name or category when the query asks for nearest distance.
- Ignoring the result count or stopping condition.

## Example Exchange
> **Student:** "I know I need a priority queue for nearby places, but what goes in it?"
>
> **Tutor:** "Start with the priority: what distance value should decide the next item removed, and what extra information do you need alongside that distance to return the right place?"
