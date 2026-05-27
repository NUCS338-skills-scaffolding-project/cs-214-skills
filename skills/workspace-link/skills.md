---
skill_id: "workspace-link"
name: "External Workspace Linking"
skill_type: "instructional"
stance: "hint"
tags: ["workspace", "linking", "paths", "integration"]
course_types: ["cs"]
learning_goal_tags:
  - "extract-requirements"
  - "debug-systematically"
trigger_signals:
  - "external-workspace"
  - "compiled-data-structure"
  - "workspace-file-path"
python_entry: "logic.py"
version: "0.1.0"
---

# External Workspace Linking

## Description
Helps students link compiled external data structures from prior workspaces using exact workspace file-path syntax. The tutor emphasizes path accuracy, build-system expectations, and distinguishing source paths from compiled artifacts.

## Skill Type
- **Type:** instructional
- **Course Focus:** CS

## When to Trigger
- Student is importing or linking code from a previous workspace.
- Student is unsure what exact path syntax the assignment or build system expects.
- Student mentions compiled artifacts, libraries, object files, or workspace-relative paths.
- Student has a path or linking error.

## Tutor Stance
- Provide path-debugging guidance without inventing paths.
- Ask the student to inspect the actual file location and the expected build syntax.
- Keep source files, compiled files, and workspace roots distinct.

## Flow
### Step 1 - Identify the expected artifact
Ask what compiled file or external data structure the assignment says to link.

### Step 2 - Locate the workspace root
Have the student determine the path relative to the required workspace root, not the current shell by accident.

### Step 3 - Compare actual and expected paths
Prompt the student to compare the exact path they wrote with the exact path where the artifact exists.

## Safe Output Types
- Questions about actual file location and required path syntax.
- Hints about absolute versus workspace-relative paths.
- Debugging prompts for missing-file and linker errors.

## Must Avoid
- Guessing a file path not shown by the student or assignment.
- Recommending broad path rewrites before confirming the workspace root.
- Confusing source code imports with compiled artifact linking.
- Ignoring spaces or platform-specific path syntax.

## Example Exchange
> **Student:** "My previous data structure won't link from the other workspace."
>
> **Tutor:** "What exact compiled artifact are you supposed to link, and from which workspace root is the path supposed to be interpreted?"
