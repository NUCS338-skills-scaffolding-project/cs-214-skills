def run(input):
    """
    Guide external workspace linking by checking artifact, root, and exact path.
    """
    message = (input.get("message") or input.get("question") or "").lower()

    if any(term in message for term in ["not found", "no such file", "cannot find"]):
        prompt = (
            "Treat this as a path evidence problem. What exact path did the build try, "
            "and where does the compiled artifact actually exist relative to the "
            "workspace root?"
        )
    elif any(term in message for term in ["link", "compiled", "object", "library"]):
        prompt = (
            "Separate the artifact from the source. Which compiled file is required, "
            "and what exact workspace-relative path does the assignment expect?"
        )
    else:
        prompt = (
            "Before editing the link line, identify three things: the workspace root, "
            "the artifact's actual location, and the exact path syntax the build system reads."
        )

    return {"prompt": prompt}
