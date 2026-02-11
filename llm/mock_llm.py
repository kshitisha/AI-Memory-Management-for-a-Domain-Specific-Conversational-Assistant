def generate_response(user_input, session_memory, long_term_memory):
    goal = long_term_memory.get("learning_goal", None)
    difficulty = session_memory.get("difficulty", None)

    response = ""

    if goal:
        response += f"Since you're preparing for {goal}, "

    if difficulty:
        response += f"I'll explain this more carefully. "

    response += f"Here is an explanation for: {user_input}"

    return response
