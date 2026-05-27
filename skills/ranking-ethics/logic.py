def run(input):
    """
    Guide spatial recommendation ethics by surfacing stakeholders and trade-offs.
    """
    message = (input.get("message") or input.get("question") or "").lower()

    if any(term in message for term in ["paid", "sponsored", "commercial"]):
        prompt = (
            "Start with incentives. What does the platform gain from paid placement, "
            "and what might users lose if ranking no longer reflects distance, quality, "
            "or relevance?"
        )
    elif any(term in message for term in ["fair", "bias", "trust"]):
        prompt = (
            "Name the stakeholder affected by the fairness issue. Is the concern about "
            "user trust, business visibility, geographic access, or unequal competition?"
        )
    else:
        prompt = (
            "Build a balanced claim: what is one possible benefit of commercialized "
            "spatial rankings, and what is one concrete societal or economic risk?"
        )

    return {"prompt": prompt}
