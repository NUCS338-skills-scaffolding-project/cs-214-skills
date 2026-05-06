def run(input):
    """
    Guides students to articulate a candidate invariant for a loop,
    recursive process, or data structure update without supplying
    the full correctness proof.
    """
    message = " ".join([
        input.get("message", ""),
        input.get("student_idea", "")
    ]).lower()

    loop_phrases = [
        "loop", "while", "for loop", "iteration", "iterate",
        "each pass", "every time through", "off by one"
    ]

    recursion_phrases = [
        "recursion", "recursive", "base case", "recursive call",
        "call itself", "induction"
    ]

    structure_phrases = [
        "stack", "queue", "tree", "graph", "heap", "list",
        "dictionary", "map", "set", "data structure"
    ]

    correctness_phrases = [
        "prove", "correct", "why works", "why it works",
        "invariant", "stays true", "always true"
    ]

    if any(p in message for p in loop_phrases):
        return {
            "prompt": (
                "Focus on one loop iteration. After processing the first k items, "
                "what should be true about your variables? Try stating that in one "
                "sentence before thinking about the whole loop."
            )
        }

    if any(p in message for p in recursion_phrases):
        return {
            "prompt": (
                "For the recursive step, what fact are you assuming is already true "
                "for the smaller problem? How should the current call preserve or "
                "extend that fact?"
            )
        }

    if any(p in message for p in structure_phrases):
        return {
            "prompt": (
                "After each update to the structure, what property should still hold? "
                "Think about ordering, membership, size, or parent-child relationships, "
                "depending on the structure you're using."
            )
        }

    if any(p in message for p in correctness_phrases):
        return {
            "prompt": (
                "Before writing a proof, try naming the fact that never stops being true "
                "as the algorithm runs. What is true at the start, remains true after one "
                "step, and helps explain the final result?"
            )
        }

    return {
        "prompt": (
            "What is one fact your approach needs to keep true while it works? "
            "State it informally first, then check whether it is true before and "
            "after a single step of your process."
        )
    }
