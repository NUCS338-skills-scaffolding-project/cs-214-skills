def run(input):
    """
    Flags common sources of ambiguity in assignment wording and
    prompts the student to ask a precise clarification question.
    """
    message = " ".join([
        input.get("message", ""),
        input.get("assignment_text", "")
    ]).lower()

    vague_behavior_phrases = [
        "handle", "reasonably", "appropriately", "as needed",
        "properly", "robust", "clean", "good", "valid"
    ]

    output_phrases = [
        "return", "print", "output", "display", "show",
        "write", "format", "exactly"
    ]

    invalid_input_phrases = [
        "invalid", "bad input", "error", "exception", "none",
        "null", "empty", "missing", "malformed"
    ]

    performance_phrases = [
        "efficient", "fast", "optimized", "large input",
        "scalable", "performance"
    ]

    unclear_scope_phrases = [
        "etc", "and so on", "any", "all", "support",
        "multiple", "various", "similar"
    ]

    if any(p in message for p in invalid_input_phrases):
        return {
            "prompt": (
                "The prompt mentions an unusual or invalid case, but does it specify "
                "the required behavior? If not, ask: should this case return a value, "
                "raise an error, print a message, or be considered outside the valid input range?"
            )
        }

    if any(p in message for p in output_phrases):
        return {
            "prompt": (
                "Separate what the assignment explicitly says from what you're inferring. "
                "Does it require a returned value, printed text, or a specific output format? "
                "If that is unclear, quote the wording and ask for the expected interface."
            )
        }

    if any(p in message for p in performance_phrases):
        return {
            "prompt": (
                "Words like 'efficient' can be ambiguous unless the assignment gives a bound "
                "or input size. Ask what complexity target or performance expectation your "
                "solution should meet."
            )
        }

    if any(p in message for p in vague_behavior_phrases):
        return {
            "prompt": (
                "That wording sounds underspecified. What exact behavior would count as "
                "'proper' or 'reasonable' here? Try listing two possible interpretations, "
                "then turn the difference into a clarification question."
            )
        }

    if any(p in message for p in unclear_scope_phrases):
        return {
            "prompt": (
                "Scope words can hide ambiguity. What cases are definitely included, "
                "and what cases are only implied? A useful instructor question is: "
                "'Which specific cases are we expected to support?'"
            )
        }

    return {
        "prompt": (
            "Find the exact sentence that feels unclear. What does it explicitly require, "
            "and what are you assuming? Turn the assumption into a question before building "
            "it into your design."
        )
    }
