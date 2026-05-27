#!/usr/bin/env python3
"""
Terminal loop: you type student input; the skill's run() output is printed.

Usage (from repo root):
  python chat_with_skill.py
  python chat_with_skill.py --skill error-messages

Skills using a single text field must be listed in INPUT_KEY_BY_SKILL.
identify-outputs needs question + assignment + code; use skills/example-skill/app.py for that.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SKILLS_DIR = REPO_ROOT / "skills"

# skill folder name -> the key run() reads from the input dict
INPUT_KEY_BY_SKILL = {
    "data-rep-choice": "message",
    "trace-state": "message",
    "edge-case-tests": "message",
    "error-messages": "error_text",
}


def load_run(skill_slug: str):
    folder = SKILLS_DIR / skill_slug
    logic_path = folder / "logic.py"
    if not logic_path.is_file():
        sys.exit(f"No logic.py at {logic_path}")

    spec = importlib.util.spec_from_file_location(
        f"skill_{skill_slug.replace('-', '_')}", logic_path
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    run = getattr(mod, "run", None)
    if not callable(run):
        sys.exit(f"{logic_path} has no callable run()")
    return run


def main() -> None:
    parser = argparse.ArgumentParser(
        description="REPL: send lines to a skill's run() and print the result."
    )
    parser.add_argument(
        "--skill",
        default="data-rep-choice",
        help="Folder name under skills/ (default: data-rep-choice)",
    )
    args = parser.parse_args()

    key = INPUT_KEY_BY_SKILL.get(args.skill)
    if key is None:
        sys.exit(
            f"Skill {args.skill!r} is not configured here. "
            f"Options: {sorted(INPUT_KEY_BY_SKILL)}. "
            f"Add an entry to INPUT_KEY_BY_SKILL or use the Streamlit demo for richer inputs."
        )

    run = load_run(args.skill)
    print(f"Skill: {args.skill}  (run input key: {key!r})")
    print("Enter text, then Enter. Empty line to exit.\n")

    while True:
        try:
            line = input("You: ").strip()
        except EOFError:
            print()
            break
        if not line:
            break
        result = run({key: line})
        print("Result:")
        if isinstance(result, dict):
            for k, v in result.items():
                print(f"  {k}: {v}")
        else:
            print(f"  {result!r}")
        print()


if __name__ == "__main__":
    main()
