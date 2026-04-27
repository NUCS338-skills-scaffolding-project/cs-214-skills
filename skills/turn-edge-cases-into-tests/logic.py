def run(input):
    """
    Detects when a student needs help identifying edge cases and
    guides them toward converting tricky scenarios into concrete
    test cases without writing full test suites for them.
    """
    message = input.get("message", "").lower()

    need_test_ideas_phrases = [
        "what should i test", "what tests do i need",
        "how do i test this", "need test ideas",
        "don't know what to test", "not sure what to test",
        "what cases should i check", "what scenarios"
    ]

    boundary_phrases = [
        "boundary", "edge case", "edge cases", "corner case",
        "off by one", "off-by-one", "minimum value", "maximum value",
        "what about zero", "what about negative", "what about empty",
        "largest input", "smallest input"
    ]

    empty_input_phrases = [
        "empty list", "empty string", "empty input", "no input",
        "none", "null", "what if nothing", "what if there's nothing",
        "zero length", "no elements"
    ]

    duplicate_special_phrases = [
        "duplicates", "repeated", "same value", "all the same",
        "special characters", "weird input", "unusual input",
        "negative numbers", "mixed types"
    ]

    coverage_phrases = [
        "enough tests", "am i missing", "did i cover everything",
        "test coverage", "how many tests", "missing any cases",
        "is this enough", "what else could go wrong"
    ]

    failure_phrases = [
        "my test fails", "test doesn't pass", "expected vs actual",
        "wrong output in test", "test is broken", "assertion error",
        "assert fails", "test output wrong"
    ]

    if any(p in message for p in need_test_ideas_phrases):
        return {
            "prompt": (
                "Start by thinking about the categories of input your code could receive. "
                "What's a 'normal' input? What's the smallest possible input? "
                "The largest? Can you think of an input that might trip up your logic? "
                "List one example for each category."
            )
        }

    if any(p in message for p in boundary_phrases):
        return {
            "prompt": (
                "Good instinct — boundaries are where bugs love to hide. "
                "What are the minimum and maximum valid values for your inputs? "
                "Write down the exact boundary values and ask yourself: "
                "does my code handle the value right at the edge?"
            )
        }

    if any(p in message for p in empty_input_phrases):
        return {
            "prompt": (
                "Empty or missing input is a classic edge case. "
                "What should your code do when it receives nothing? "
                "Does the spec say it should return a default, raise an error, "
                "or is that case not supposed to happen? Name the expected behavior first."
            )
        }

    if any(p in message for p in duplicate_special_phrases):
        return {
            "prompt": (
                "Think about inputs that break your assumptions. "
                "What if every element is the same? What if the input contains "
                "unexpected types or characters? For each unusual scenario, "
                "describe what you expect your code to do — that becomes your test."
            )
        }

    if any(p in message for p in coverage_phrases):
        return {
            "prompt": (
                "Try organizing your tests into categories: "
                "typical cases, boundary cases, error cases, and special cases. "
                "Do you have at least one test in each category? "
                "Which category feels the thinnest?"
            )
        }

    if any(p in message for p in failure_phrases):
        return {
            "prompt": (
                "When a test fails, compare the expected output you wrote "
                "to what your code actually produces. Is the test wrong, "
                "or is the code wrong? Trace through the failing input by hand "
                "to figure out which side has the bug."
            )
        }

    return {
        "prompt": (
            "Before writing tests, think about the trickiest input "
            "your code might encounter. What assumptions does your logic make? "
            "Try to come up with one scenario that violates each assumption — "
            "those are your edge cases, and each one becomes a test."
        )
    }
