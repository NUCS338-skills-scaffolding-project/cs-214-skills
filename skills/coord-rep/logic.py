def run(input):
    """
    Guide a student through representing raw coordinates without changing
    their meaning or precision.
    """
    message = (input.get("message") or input.get("question") or "").lower()

    if any(term in message for term in ["round", "truncate", "precision", "decimal"]):
        prompt = (
            "Before changing any numeric value, check the assignment's comparison rules. "
            "What type or representation lets you preserve the original coordinate values "
            "until the moment you need to compare or display them?"
        )
    elif any(term in message for term in ["latitude", "longitude", "lat", "lon", "lng"]):
        prompt = (
            "Write down the raw coordinate order first. Which field is latitude and which "
            "is longitude, and how will your object make that mapping impossible to confuse?"
        )
    else:
        prompt = (
            "Treat object construction as a lossless translation. What raw fields come in, "
            "what internal fields store them, and how could you verify that the same values "
            "come back out?"
        )

    return {"prompt": prompt}
