def run(input):
    """
    Guide shortest-route design through destination resolution and graph search.
    """
    message = (input.get("message") or input.get("question") or "").lower()

    if any(term in message for term in ["dijkstra", "priority", "shortest"]):
        prompt = (
            "For shortest path, identify the distance invariant: when is a node's best "
            "known distance final, and what information do you store to rebuild the path?"
        )
    elif any(term in message for term in ["name", "destination", "poi"]):
        prompt = (
            "Resolve the named destination before routing. What coordinate or graph node "
            "does the name point to, and how will the graph search know it has reached it?"
        )
    else:
        prompt = (
            "Break routing into three questions: what is the start node, what is the "
            "destination node, and what edge weight makes one route shorter than another?"
        )

    return {"prompt": prompt}
