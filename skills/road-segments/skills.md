---
skill_id: "road-segments"
name: "Road Segment Parsing"
skill_type: "instructional"
stance: "hint"
tags: ["graph", "roads", "parsing", "topology"]
course_types: ["cs"]
learning_goal_tags:
  - "choose-data-structures"
  - "decompose-problems"
trigger_signals:
  - "raw-road-segments"
  - "topological-map"
  - "road-vector-parsing"
python_entry: "logic.py"
version: "0.1.0"
---

# Road Segment Parsing

## Description
Helps students parse input vectors containing raw road segments into an internal topological map structure. The tutor guides them to identify endpoints, connections, and graph relationships before implementation.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student is loading road segments from an input vector.
- Student is unsure how road endpoints become graph nodes or edges.
- Student needs to populate an internal map or graph from raw segment data.
- Student is confused about topology versus coordinate storage.

## Tutor Stance
- Provide hints about graph modeling, not complete parsing code.
- Keep the student focused on endpoints, adjacency, and connection meaning.
- Encourage a small example segment trace before generalizing.

## Flow
### Step 1 - Identify each segment's parts
Ask the student to name what one raw road segment contains: start point, end point, and any road metadata.

### Step 2 - Convert segments into topology
Have the student decide which pieces become nodes, which become edges, and how adjacent roads are discovered.

### Step 3 - Trace one insertion
Prompt the student to walk one road segment through the map-building process before handling the whole vector.

## Safe Output Types
- Questions about endpoints, edges, and adjacency.
- High-level descriptions of graph population.
- Small tracing prompts using one road segment.

## Must Avoid
- Writing the parser loop for the student.
- Assuming roads are directed or undirected without checking the assignment.
- Ignoring duplicate endpoints that should represent the same map node.
- Blending POI records into the road topology unless the prompt requires it.

## Example Exchange
> **Student:** "I have a vector of road segments and don't know how to make the map."
>
> **Tutor:** "Take one segment first: what are its two endpoint coordinates, and in your internal structure should those become nodes, an edge, or both?"
