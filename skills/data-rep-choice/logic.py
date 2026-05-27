def run(input):
    """
    Detects when a student is unsure which data structure to use
    and guides them toward choosing an appropriate representation
    by reasoning about entities, relationships, and operations.
    """
    message = input.get("message", "").lower()

    array_vs_map_phrases = [
        "list or dictionary", "array or map", "array or hash",
        "dictionary or list", "should i use a dict", "should i use a list",
        "list or dict", "dict or list", "hashmap or array",
        "array or dictionary"
    ]

    set_confusion_phrases = [
        "should i use a set", "do i need a set", "set or list",
        "list or set", "remove duplicates", "unique values",
        "no duplicates", "avoid duplicates"
    ]

    nested_structure_phrases = [
        "list of lists", "nested dictionary", "dict of lists",
        "list of dicts", "nested structure", "2d array",
        "dictionary of dictionaries", "how do i nest",
        "multi-level", "hierarchical data"
    ]

    what_to_store_phrases = [
        "what should i store", "what do i keep track of",
        "what data do i need", "what variables do i need",
        "don't know what to store", "not sure what to track",
        "what information do i need", "what fields"
    ]

    relationship_phrases = [
        "how do i connect", "relate two things", "link between",
        "map one thing to another", "associate", "lookup",
        "key value", "pair things", "match items"
    ]

    operation_phrases = [
        "need fast lookup", "search quickly", "find by key",
        "sort the data", "order matters", "need to iterate",
        "count occurrences", "frequency", "access by index"
    ]

    if any(p in message for p in array_vs_map_phrases):
        return {
            "prompt": (
                "Think about how you'll access the data. "
                "Do you need to look things up by a specific key or label, "
                "or are you working with an ordered sequence of items? "
                "That distinction usually points you toward the right structure."
            )
        }

    if any(p in message for p in set_confusion_phrases):
        return {
            "prompt": (
                "Ask yourself: does your problem care about duplicates? "
                "And do you need to preserve the order items were added? "
                "Your answers to those two questions will help you decide."
            )
        }

    if any(p in message for p in nested_structure_phrases):
        return {
            "prompt": (
                "Before nesting structures, sketch out the entities involved. "
                "What is the 'outer' thing, and what belongs 'inside' each one? "
                "Try describing the relationship in a sentence like "
                "'each ___ has multiple ___'."
            )
        }

    if any(p in message for p in what_to_store_phrases):
        return {
            "prompt": (
                "Go back to the problem statement and list every noun — "
                "those are your candidate entities. "
                "Which of them change over time or need to be referenced later? "
                "Those are the things worth storing."
            )
        }

    if any(p in message for p in relationship_phrases):
        return {
            "prompt": (
                "It sounds like you have two concepts that need to be linked. "
                "Is this a one-to-one relationship, or can one item relate to many? "
                "Describing the cardinality will help you pick the right structure."
            )
        }

    if any(p in message for p in operation_phrases):
        return {
            "prompt": (
                "Think about the most frequent operation your code will perform. "
                "Will you mostly be searching, iterating in order, or counting? "
                "Different structures make different operations efficient — "
                "which operation matters most for your problem?"
            )
        }

    return {
        "prompt": (
            "Before choosing a data structure, try describing the problem's "
            "entities and how they relate to each other. "
            "What are you storing, and what will you need to do with it? "
            "Sketch that out and the right representation often becomes clear."
        )
    }
