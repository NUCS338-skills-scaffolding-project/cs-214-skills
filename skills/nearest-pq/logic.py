def run(input):
    """
    Guide nearest-neighbor work by clarifying priority queue entries.
    """
    message = (input.get("message") or input.get("question") or "").lower()

    if any(term in message for term in ["tie", "same distance", "equal"]):
        prompt = (
            "If two candidates have the same distance, what does the assignment say "
            "should happen? If it does not say, how will you make your tie behavior "
            "consistent and easy to explain?"
        )
    elif any(term in message for term in ["heap", "priority queue", "pq"]):
        prompt = (
            "Each queue entry needs a priority and enough payload to return the result. "
            "What distance value is the priority, and what coordinate or POI data must "
            "travel with it?"
        )
    else:
        prompt = (
            "For nearest-neighbor logic, list the candidates first. For each candidate, "
            "what distance from the starting coordinate would determine its queue order?"
        )

    return {"prompt": prompt}
