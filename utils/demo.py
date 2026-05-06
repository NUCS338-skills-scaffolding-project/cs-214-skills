# demo.py — CLI demo for the multi-skill CS 214 tutor
from tutor_engine import run


ASSIGNMENT_WORD_THRESHOLD = 45


WELCOME = """
============================================================
       CS 214 — Multi-Skill Tutor Demo
============================================================

No default assignment is loaded. Paste your assignment first,
then ask about outputs, return behavior, data representation,
tests, edge cases, ambiguity, debugging, errors, or invariants.

Type 'quit' to exit.
"""


def main():
    print(WELCOME)
    assignment = ""
    state = {}
    history = []

    while True:
        message = input("\nStudent: ").strip()
        if message.lower() in {"quit", "exit"}:
            print("Tutor: Good luck with the assignment.")
            break

        history.append({"role": "user", "content": message})

        if len(message.split()) > ASSIGNMENT_WORD_THRESHOLD:
            assignment = message

        if not assignment:
            response = (
                "Please paste the assignment prompt first. I need that context before "
                "choosing a skill, otherwise I might route your question based on the wrong assumptions."
            )
            history.append({"role": "assistant", "content": response})
            print(f"Tutor: {response}")
            continue

        result = run({
            "message": message,
            "assignment": assignment,
            "history": history,
            "state": state,
        })
        state = result["state"]
        response = result["response"]
        history.append({"role": "assistant", "content": response})

        if result.get("skill_name") and result["skill_name"] != "Assignment Loaded":
            label = result["skill_name"]
            if result.get("stance"):
                label += f" | {result['stance']}"
            print(f"\n[{label}]")
        print(f"Tutor: {response}")


if __name__ == "__main__":
    main()
