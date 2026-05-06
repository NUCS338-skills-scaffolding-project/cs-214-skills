def run(input):
    """
    Helps students reason about return values versus side effects
    by looking at assignment wording and how the function will be used.
    """
    message = " ".join([
        input.get("message", ""),
        input.get("assignment", ""),
        input.get("current_design", "")
    ]).lower()

    print_return_phrases = [
        "print or return", "return or print", "should i print",
        "should i return", "prints but", "return value", "returns none",
        "got none", "why none"
    ]

    test_phrases = [
        "test", "assert", "expected", "unit test",
        "autograder", "grader", "pytest"
    ]

    side_effect_phrases = [
        "modify", "mutate", "change the list", "update",
        "in place", "side effect", "global"
    ]

    assignment_wording_phrases = [
        "assignment says", "prompt says", "instructions say",
        "supposed to", "asks me to", "requires"
    ]

    helper_phrases = [
        "helper", "function", "method", "use later",
        "another function", "call it"
    ]

    if any(p in message for p in print_return_phrases):
        return {
            "prompt": (
                "Look for who needs the result. If another function or test needs to use it, "
                "returning keeps the value available. If the goal is only to show text to a "
                "person, printing may belong at the outer interaction point. Which situation "
                "does your assignment describe?"
            )
        }

    if any(p in message for p in test_phrases):
        return {
            "prompt": (
                "A test usually checks a returned value or a changed object, not text printed "
                "to the screen unless the assignment specifically says to print. What is your "
                "test expecting to observe?"
            )
        }

    if any(p in message for p in side_effect_phrases):
        return {
            "prompt": (
                "If a function mutates existing data, the result is visible through that changed "
                "object. If it returns a new value, callers can choose what to do with it. "
                "Which behavior is the assignment asking for, and which one would be easier to test?"
            )
        }

    if any(p in message for p in assignment_wording_phrases):
        return {
            "prompt": (
                "Quote the exact verb from the prompt: return, print, display, update, modify, "
                "or compute. That verb is the strongest clue. If the verb is missing or vague, "
                "treat it as an ambiguity to clarify."
            )
        }

    if any(p in message for p in helper_phrases):
        return {
            "prompt": (
                "For a helper function, ask what the caller needs back. A helper is often easier "
                "to reuse and test when it returns a value instead of printing, but the assignment "
                "wording should still guide the final choice."
            )
        }

    return {
        "prompt": (
            "Decide what should observe the result: the screen, the caller, or an object being "
            "changed. Then check whether the assignment wording supports printing, returning, "
            "or mutation."
        )
    }
