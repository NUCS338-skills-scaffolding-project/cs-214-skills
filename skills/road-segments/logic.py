def run(input):
    """
    Guide road-segment parsing by focusing on endpoints, graph nodes, and edges.
    """
    message = (input.get("message") or input.get("question") or "").lower()

    if any(term in message for term in ["adjacent", "neighbors", "connected"]):
        prompt = (
            "Adjacency comes from shared endpoints. For one road segment, which endpoint "
            "should gain which neighbor, and does the assignment say that connection goes "
            "both directions?"
        )
    elif any(term in message for term in ["duplicate", "same coordinate", "dedup"]):
        prompt = (
            "Before adding a new node, ask whether that coordinate already exists in the "
            "map. What equality rule will let repeated endpoints refer to the same node?"
        )
    else:
        prompt = (
            "Trace one raw segment by hand. What are its start and end coordinates, what "
            "node records should exist after parsing it, and what edge or neighbor link "
            "should be added?"
        )

    return {"prompt": prompt}
