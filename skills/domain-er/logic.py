def run(input):
    """
    Guide architecture diagrams toward concrete domain ER modeling.
    """
    message = (input.get("message") or input.get("question") or "").lower()

    if any(term in message for term in ["abstract", "system", "component"]):
        prompt = (
            "Try replacing abstract boxes with domain nouns. Which boxes could become "
            "coordinate, road segment, POI, category, graph node, or route query?"
        )
    elif any(term in message for term in ["arrow", "relationship", "connect"]):
        prompt = (
            "Before drawing an arrow, write the relationship as a verb phrase. Does one "
            "entity contain, connect to, label, resolve to, or query another entity?"
        )
    else:
        prompt = (
            "Start your ER diagram with concrete nouns from the assignment. What are the "
            "main domain entities, and what is one relationship between two of them?"
        )

    return {"prompt": prompt}
