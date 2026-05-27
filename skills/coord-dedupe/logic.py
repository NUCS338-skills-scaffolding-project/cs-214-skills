def run(input):
    """
    Guide category locate-all queries toward distinct coordinate results.
    """
    message = (input.get("message") or input.get("question") or "").lower()

    if any(term in message for term in ["duplicate", "dedup", "unique", "same"]):
        prompt = (
            "Define duplicate at the coordinate level. If two POIs share the same "
            "position, should the query return that position once or once per POI?"
        )
    elif "category" in message:
        prompt = (
            "First filter by category, then think about the result shape. After you find "
            "matching POIs, what exactly should be collected from each one?"
        )
    else:
        prompt = (
            "For a locate-all query, separate the two tasks: finding records with the "
            "requested category and ensuring the returned coordinates are distinct. "
            "Which equality rule handles the second task?"
        )

    return {"prompt": prompt}
