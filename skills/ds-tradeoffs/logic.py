def run(input):
    """
    Guide written data-structure comparisons toward explicit runtime trade-offs.
    """
    message = (input.get("message") or input.get("question") or "").lower()

    if any(term in message for term in ["big-o", "runtime", "complexity"]):
        prompt = (
            "Tie each Big-O claim to an operation. Which operation are you analyzing, "
            "and what is the time cost for each candidate data structure?"
        )
    elif any(term in message for term in ["report", "write", "paragraph"]):
        prompt = (
            "Before drafting the paragraph, make a comparison row for each structure: "
            "main operation, time cost, space cost, and one drawback. What are your rows?"
        )
    else:
        prompt = (
            "Pick two candidate structures and one important operation. How does each "
            "structure perform on that operation, and what trade-off would you mention "
            "in the report?"
        )

    return {"prompt": prompt}
