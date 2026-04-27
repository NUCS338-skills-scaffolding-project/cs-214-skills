def run(input):
    """
    Detects when a student's logic fails mid-execution and
    guides them toward tracing variable states step by step
    to locate where their code diverges from expectations.
    """
    message = input.get("message", "").lower()

    wrong_result_phrases = [
        "wrong answer", "wrong result", "wrong output",
        "not what i expected", "getting the wrong value",
        "my code gives the wrong", "incorrect output",
        "result is off", "answer is wrong"
    ]

    variable_tracking_phrases = [
        "what's the value of", "what is the value",
        "how does this variable change", "track the variable",
        "what happens to", "where does it change",
        "variable is wrong", "value doesn't update"
    ]

    loop_confusion_phrases = [
        "loop doesn't work", "loop gives wrong", "stuck in a loop",
        "infinite loop", "loop runs too many", "loop stops early",
        "off by one in loop", "loop index", "wrong iteration",
        "loop skips", "loop count"
    ]

    conditional_phrases = [
        "wrong branch", "if statement wrong", "condition is wrong",
        "goes into the wrong if", "skips my if", "else runs instead",
        "condition never true", "condition always true",
        "logic in my if"
    ]

    mid_execution_phrases = [
        "works for some inputs", "fails halfway", "breaks in the middle",
        "first part works", "stops working after", "fails on certain",
        "only works sometimes", "partially correct"
    ]

    trace_help_phrases = [
        "how do i trace", "walk through my code", "step through",
        "how do i debug", "trace table", "state table",
        "hand trace", "dry run", "trace by hand"
    ]

    if any(p in message for p in wrong_result_phrases):
        return {
            "prompt": (
                "Let's find where things go wrong. Pick a small input "
                "you know the expected answer for. Now, go through your code "
                "line by line and write down what each variable holds after "
                "each step. At which line does the actual value first differ "
                "from what you expected?"
            )
        }

    if any(p in message for p in variable_tracking_phrases):
        return {
            "prompt": (
                "Make a table with columns for each variable and a row for "
                "each step or line. Fill it in as you mentally execute your code. "
                "Where does a variable's value first surprise you? "
                "That's the line to examine closely."
            )
        }

    if any(p in message for p in loop_confusion_phrases):
        return {
            "prompt": (
                "For loop issues, write down the loop variable's value at the "
                "start of each iteration, the condition check result, and the "
                "value at the end of the iteration. How many times does the loop "
                "run, and is that the number you expected?"
            )
        }

    if any(p in message for p in conditional_phrases):
        return {
            "prompt": (
                "Evaluate your condition by hand with your specific input values. "
                "Write down each part of the condition and whether it's true or false. "
                "Does the overall result match the branch you expected to enter? "
                "If not, which part of the condition is evaluating differently than you thought?"
            )
        }

    if any(p in message for p in mid_execution_phrases):
        return {
            "prompt": (
                "If it works for some inputs but not others, compare a passing input "
                "to a failing one. Trace both side by side — at which step do they "
                "diverge? What's different about the failing input that causes "
                "your code to behave differently?"
            )
        }

    if any(p in message for p in trace_help_phrases):
        return {
            "prompt": (
                "Here's how to trace: create a table where each column is a variable "
                "and each row is a line of code. Start with your initial values and "
                "update the table as you step through each line. "
                "Which variable do you want to start tracking?"
            )
        }

    return {
        "prompt": (
            "When your code doesn't produce the right result, the best first step "
            "is to trace through it with a concrete input. Pick a simple example, "
            "write down what each variable should be at every step, "
            "then compare that to what your code actually does. "
            "Where do the two diverge?"
        )
    }
