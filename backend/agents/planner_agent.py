def plan_action(user_input: str) -> str:
    """
    Decides what action the agent should take.
    Returns: 'explain', 'solve', or 'question'
    """

    text = user_input.lower()

    if "explain" in text or "what is" in text:
        return "explain"

    if "solve" in text or "calculate" in text:
        return "solve"

    return "question"
