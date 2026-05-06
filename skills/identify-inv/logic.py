def run(input):
    """
    Helps students identify candidate invariants for their current
    design and check whether those invariants are initialized and preserved.
    """
    message = " ".join([
        input.get("message", ""),
        input.get("current_design", ""),
        input.get("topic_area", "")
    ]).lower()

    counter_phrases = [
        "counter", "count", "running total", "sum", "accumulator",
        "max", "min", "average"
    ]

    index_phrases = [
        "index", "pointer", "two pointer", "left", "right",
        "i and j", "scan", "position"
    ]

    sorted_phrases = [
        "sorted", "ordered", "binary search", "partition",
        "smaller than", "larger than"
    ]

    structure_phrases = [
        "tree", "graph", "stack", "queue", "heap", "set",
        "dictionary", "map", "linked list"
    ]

    recursion_phrases = [
        "recursive", "recursion", "base case", "recursive call",
        "smaller problem"
    ]

    if any(p in message for p in counter_phrases):
        return {
            "prompt": (
                "For a counter or accumulator, ask what it summarizes so far. "
                "After processing the first k items, what exactly should the "
                "counter or running value represent?"
            )
        }

    if any(p in message for p in index_phrases):
        return {
            "prompt": (
                "For indexes or pointers, ask what each region means. "
                "What is known about the elements before the index, after the index, "
                "or between the pointers after each iteration?"
            )
        }

    if any(p in message for p in sorted_phrases):
        return {
            "prompt": (
                "When order matters, your invariant often describes which part of the "
                "input is already known, ruled out, or correctly placed. What ordered "
                "property should remain true after each step?"
            )
        }

    if any(p in message for p in structure_phrases):
        return {
            "prompt": (
                "For a data structure, identify the rule that must survive every update. "
                "Should membership, ordering, parent-child links, size, or reachability "
                "stay consistent after each operation?"
            )
        }

    if any(p in message for p in recursion_phrases):
        return {
            "prompt": (
                "For recursion, phrase the invariant as a promise about each call. "
                "What does a call guarantee for its subproblem, and how does the caller "
                "use that guarantee?"
            )
        }

    return {
        "prompt": (
            "List the pieces of state that change, then choose one relationship among "
            "them that should stay true. Is it true before the process starts, and does "
            "one normal step preserve it?"
        )
    }
