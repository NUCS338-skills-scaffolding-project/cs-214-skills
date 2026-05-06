def run(input):
    """
    Guides students toward a complete unit test strategy using
    behavior categories and representative cases without writing
    the full test suite.
    """
    message = " ".join([
        input.get("message", ""),
        input.get("assignment", ""),
        input.get("student_code", "")
    ]).lower()

    how_to_test_phrases = [
        "how do i test", "how should i test", "what tests",
        "test plan", "testing strategy", "unit test plan",
        "where do i start testing"
    ]

    requirements_phrases = [
        "requirements", "assignment", "spec", "prompt",
        "expected behavior", "deliverables"
    ]

    coverage_phrases = [
        "enough tests", "missing tests", "cover everything",
        "coverage", "all cases", "what else"
    ]

    edge_case_phrases = [
        "edge case", "boundary", "empty", "invalid",
        "error case", "corner case", "special case"
    ]

    code_ready_phrases = [
        "my code", "pseudocode", "function", "method",
        "implemented", "wrote"
    ]

    if any(p in message for p in how_to_test_phrases):
        return {
            "prompt": (
                "Build a small matrix before writing test code: typical case, boundary case, "
                "edge or error case, and one case tied to a specific requirement. For each row, "
                "write the input scenario and expected behavior in words."
            )
        }

    if any(p in message for p in requirements_phrases):
        return {
            "prompt": (
                "Turn each requirement into at least one test idea. Which requirement checks "
                "normal behavior, which checks a boundary, and which checks what should happen "
                "when input is invalid or unusual?"
            )
        }

    if any(p in message for p in coverage_phrases):
        return {
            "prompt": (
                "Check your plan against categories: normal, boundary, edge, error, and regression "
                "cases for bugs you've already seen. Which category has no representative case yet?"
            )
        }

    if any(p in message for p in edge_case_phrases):
        return {
            "prompt": (
                "For each edge case, write three things: the requirement it relates to, the input "
                "scenario, and the expected behavior. If you cannot state the expected behavior, "
                "the spec may need clarification before that test is useful."
            )
        }

    if any(p in message for p in code_ready_phrases):
        return {
            "prompt": (
                "Look at each branch or major behavior in your code and map it to a test case. "
                "Do you have a test that reaches each meaningful path, including the path most "
                "likely to fail?"
            )
        }

    return {
        "prompt": (
            "A solid unit test plan starts with behaviors, not code. List the required behaviors, "
            "then choose representative normal, boundary, and error cases for each important one."
        )
    }
