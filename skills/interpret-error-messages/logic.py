# logic.py — Interpret Error Messages skill
# Classifies errors common in data structures and algorithms coursework

def classify_error(error_text):
    """
    Look at the error text and return a type label.
    Returns one of: syntax, runtime, logic, unknown
    """
    if "SyntaxError" in error_text or "IndentationError" in error_text:
        return "syntax"
    
    runtime_errors = [
        "IndexError",
        "KeyError",
        "TypeError",
        "AttributeError",
        "RecursionError",
        "NameError",
        "ValueError",
        "NoneType"
    ]
    for error in runtime_errors:
        if error in error_text:
            return "runtime"
    
    return "unknown"


def get_likely_cause(error_type, error_text):
    """
    Return a plain-English explanation based on the error type and text.
    """
    if "IndexError" in error_text:
        return (
            "You tried to access a position in a list or array that doesn't exist. "
            "This is common in DS/A when your loop index goes one step too far, "
            "or when you access size instead of size-1."
        )
    if "KeyError" in error_text:
        return (
            "You tried to access a key in a dictionary that isn't there. "
            "This often happens in graph problems when a node hasn't been added yet."
        )
    if "RecursionError" in error_text:
        return (
            "Your recursive function never hit its base case and kept calling itself. "
            "Check that your base case is reachable and that each call makes the problem smaller."
        )
    if "NoneType" in error_text:
        return (
            "You're calling a method or accessing an attribute on something that is None. "
            "This is common in linked list problems when you traverse past the last node."
        )
    if "TypeError" in error_text:
        return (
            "You passed the wrong type into a function or operation. "
            "Check what your function expects vs what you're actually passing in."
        )
    if error_type == "syntax":
        return (
            "Python couldn't read your code at all. "
            "Look for a missing colon, mismatched parentheses, or bad indentation."
        )
    return "An error occurred. Check the line number in the traceback and inspect that area."


def get_guiding_question(error_text):
    """
    Return a guiding question to help the student find the fix themselves.
    """
    if "IndexError" in error_text:
        return "What is the valid range of indices for your list? What value does your index have at the moment of the crash?"
    if "KeyError" in error_text:
        return "Before you access that key, are you sure it has been added to the dictionary?"
    if "RecursionError" in error_text:
        return "What is your base case? Trace through one example by hand — does it ever reach the base case?"
    if "NoneType" in error_text:
        return "What value does that variable hold right before the crash? Could it be None?"
    if "TypeError" in error_text:
        return "What type does your function expect? What type are you actually passing in?"
    return "What line does the traceback point to? What are the values of your variables at that line?"


def run(input):
    """
    Main entry point for this skill.

    input: dict with keys:
        - error_text (str): the error message the student pasted
        - code_context (str, optional): the student's code near the crash

    return: dict with error_type, likely_cause, guiding_question
    """
    error_text = input.get("error_text", "")

    error_type = classify_error(error_text)
    likely_cause = get_likely_cause(error_type, error_text)
    guiding_question = get_guiding_question(error_text)

    return {
        "error_type": error_type,
        "likely_cause": likely_cause,
        "guiding_question": guiding_question
    }


# quick test — run this file directly to check it works
if __name__ == "__main__":
    test_cases = [
        {"error_text": "IndexError: list index out of range"},
        {"error_text": "RecursionError: maximum recursion depth exceeded"},
        {"error_text": "KeyError: 'A'"},
        {"error_text": "NoneType object has no attribute 'next'"},
    ]

    for i, test in enumerate(test_cases):
        print(f"--- Test {i + 1} ---")
        result = run(test)
        for key, value in result.items():
            print(f"{key}: {value}")
        print()