def run(input):
    """
    Guide POI record design by separating name, category, and location roles.
    """
    message = (input.get("message") or input.get("question") or "").lower()

    if "unique" in message or "name" in message:
        prompt = (
            "Ask what the assignment guarantees is unique. Is the POI name the lookup "
            "key, while category can repeat across many records?"
        )
    elif "category" in message:
        prompt = (
            "A category is usually for grouping, not identifying one place. What query "
            "will use the category, and what field will still identify each matching POI?"
        )
    else:
        prompt = (
            "For one POI input row, label the location, category, and name. Which later "
            "query depends on each field being stored separately?"
        )

    return {"prompt": prompt}
