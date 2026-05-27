# logic.py - Identify Outputs skill

OUTPUT_SIGNALS = (
    ("return", ("return", "returns", "returned value")),
    ("print", ("print", "prints", "display", "console", "stdout")),
    ("file", ("write to a file", "save to a file", "output file", "csv", "txt file")),
    ("store", ("store", "update", "mutate", "modify in place")),
)

FORMAT_SIGNALS = (
    ("list or sequence", ("list", "array", "sequence", "values in order")),
    ("dictionary or mapping", ("dictionary", "dict", "map", "key-value")),
    ("string or formatted text", ("string", "str", "text", "line", "comma-separated")),
    ("number", ("integer", "int", "float", "number", "count", "sum", "average")),
    ("boolean", ("boolean", "bool", "true", "false")),
)


def _first_matching_label(text, signals, default):
    for label, phrases in signals:
        if any(phrase in text for phrase in phrases):
            return label
    return default


def run(input):
    """
    Identify the expected output mechanism and format from assignment context.

    input keys:
        - question/message: student's question about outputs
        - assignment/assignment_text: assignment prompt or requirements

    return: dict with output_type, output_format, and guidance
    """
    question = input.get("question") or input.get("message") or ""
    assignment = input.get("assignment") or input.get("assignment_text") or ""
    text = f"{assignment}\n{question}".lower()

    output_type = _first_matching_label(text, OUTPUT_SIGNALS, "unclear")
    output_format = _first_matching_label(text, FORMAT_SIGNALS, "not specified")

    if output_type == "unclear":
        guidance = (
            "I do not see a clear output mechanism in the wording yet. Look for a "
            "verb like return, print, display, write, store, or update. If none is "
            "present, that is an ambiguity to clarify before coding."
        )
    else:
        guidance = (
            f"The assignment wording most strongly points to `{output_type}` as the "
            f"output mechanism. The expected format looks like `{output_format}`. "
            "Use that as your target unless an example or instructor note says otherwise."
        )

    return {
        "output_type": output_type,
        "output_format": output_format,
        "guidance": guidance,
    }
