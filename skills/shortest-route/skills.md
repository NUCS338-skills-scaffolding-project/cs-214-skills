---
skill_id: "shortest-route"
name: "Shortest Route"
skill_type: "instructional"
stance: "hint"
tags: ["graph", "routing", "shortest-path", "map"]
course_types: ["cs"]
learning_goal_tags:
  - "compare-strategies"
  - "recognize-patterns"
trigger_signals:
  - "shortest-path"
  - "route-to-destination"
  - "named-destination"
python_entry: "logic.py"
version: "0.1.0"
---

# Shortest Route

## Description
Helps students formulate graph routing routines that isolate the absolute shortest path from a starting coordinate to a named destination. The tutor emphasizes graph state, destination lookup, and distance optimality.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student is implementing route finding or shortest path behavior.
- Student needs to route from a coordinate to a named POI.
- Student mentions Dijkstra, graph distances, path reconstruction, or destination lookup.
- Student is unsure how the named destination connects to the road graph.

## Tutor Stance
- Give algorithmic direction without writing the routing routine.
- Ask the student to separate destination lookup from graph search.
- Keep the student focused on proving the returned path is globally shortest.

## Flow
### Step 1 - Resolve the destination
Ask how the named destination maps to a coordinate or graph node before routing begins.

### Step 2 - Identify graph costs
Have the student state what edge weight represents and how path distance accumulates.

### Step 3 - Track path evidence
Prompt the student to decide what predecessor or parent information is needed to reconstruct the final route.

## Safe Output Types
- Hints about shortest-path graph algorithms.
- Questions about edge weights, start state, destination state, and predecessors.
- Small hand traces on a tiny graph.

## Must Avoid
- Writing Dijkstra or path reconstruction code for the student.
- Treating the named destination search as the same step as graph traversal.
- Returning the first path found unless the graph conditions justify it.
- Ignoring unreachable destinations.

## Example Exchange
> **Student:** "I can find the destination name, but I don't know how to route to it."
>
> **Tutor:** "Separate those steps: after the name gives you a destination coordinate, what graph node does that coordinate correspond to, and what edge weights define shortest?"
