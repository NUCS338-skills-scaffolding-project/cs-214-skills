def run(input):
    """
    Detects when a student is unsure what their code should output
    and guides them toward clarifying the expected result and format.
    """
    message = input.get("message", "").lower()

    return_vs_print_phrases = [
        "should i print or return", "print or return",
        "do i return it", "do i print it",
        "return or print", "should i use print"
    ]

    format_confusion_phrases = [
        "what format", "what type should i return",
        "string or list", "list or string",
        "how should i format", "what should the output look like",
        "what does the output look like"
    ]

    unknown_output_phrases = [
        "what am i supposed to output", "what do i return",
        "what should i return", "what should i print",
        "don't know what to output", "not sure what to return",
        "what's the expected output", "what is the expected output"
    ]

    wrong_type_phrases = [
        "wrong type", "type error", "expected list got string",
        "returns the wrong thing", "output is wrong",
        "getting the wrong result", "my output doesn't match"
    ]

    if any(p in message for p in return_vs_print_phrases):
        return {
            "prompt": (
                "Good question — check the assignment wording. "
                "Does it say 'write a function that returns' or 'print the result'? "
                "Those require different approaches."
            )
        }

    if any(p in message for p in format_confusion_phrases):
        return {
            "prompt": (
                "Look at the example outputs in the assignment. "
                "What data type are they — a list, a string, a number? "
                "Do you notice any pattern in how they're structured?"
            )
        }

    if any(p in message for p in unknown_output_phrases):
        return {
            "prompt": (
                "Let's start from the assignment description. "
                "Can you find the sentence that describes what your code should produce? "
                "Try restating it in your own words."
            )
        }

    if any(p in message for p in wrong_type_phrases):
        return {
            "prompt": (
                "It sounds like your code produces a result, but not in the right form. "
                "Compare your output to the expected examples — "
                "is it the same type and structure, or does something need to change?"
            )
        }

    return {
        "prompt": (
            "Before writing your output logic, can you describe exactly "
            "what your code should produce and in what format? "
            "Check the assignment for example outputs to confirm."
        )
    }
