def update_session_memory(session_memory: dict, user_input: str) -> dict:
    if "confused" in user_input.lower():
        session_memory["difficulty"] = True
    return session_memory
