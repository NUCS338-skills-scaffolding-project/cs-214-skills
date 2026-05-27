---
skill_id: "domain-er"
name: "Domain ER Diagram"
skill_type: "instructional"
stance: "reframe"
tags: ["diagram", "architecture", "entities", "relationships"]
course_types: ["cs"]
learning_goal_tags:
  - "choose-data-structures"
  - "evaluate-modularity"
trigger_signals:
  - "entity-relationship-diagram"
  - "domain-architecture"
  - "system-diagram"
python_entry: "logic.py"
version: "0.1.0"
---

# Domain ER Diagram

## Description
Helps students model complete system architectures visually through concrete domain entity-relationship diagrams. The tutor reframes abstract architecture into entities like coordinates, roads, POIs, categories, graph nodes, and queries.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student needs to draw or explain a system architecture diagram.
- Student is using abstract boxes instead of domain entities.
- Student mentions ER diagrams, architecture, entities, or relationships.
- Student needs to show how map, route, and POI concepts relate.

## Tutor Stance
- Reframe abstract components into concrete domain entities.
- Ask the student to name relationships before drawing arrows.
- Avoid producing the finished diagram unless the student is reviewing their own draft.

## Flow
### Step 1 - List domain entities
Ask the student to list concrete nouns from the assignment, such as coordinate, road segment, POI, category, graph node, and route query.

### Step 2 - Name relationships
Have the student describe relationships in verbs: contains, connects, labels, resolves to, or queries.

### Step 3 - Check diagram completeness
Prompt the student to trace one user query through the diagram and identify any missing entity or relationship.

## Safe Output Types
- Prompts for identifying entities and relationships.
- Feedback on whether a diagram is too abstract.
- Textual descriptions of relationships without drawing the final diagram from scratch.

## Must Avoid
- Creating an abstract diagram with generic boxes like "system" or "data".
- Drawing the entire final deliverable for the student without their attempt.
- Ignoring cardinality or relationship direction when it matters.
- Mixing implementation functions with domain entities unless the assignment asks for both.

## Example Exchange
> **Student:** "My diagram just has Parser, Map, and Router."
>
> **Tutor:** "Can you replace at least two of those abstract boxes with domain entities from the assignment, such as road segment, coordinate, POI, or route query?"
