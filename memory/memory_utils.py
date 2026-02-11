def summarize_session_memory(session_memory: dict) -> dict:
    summary = {}

    if session_memory.get("difficulty"):
        summary["difficulty"] = "User struggled previously"

    return summary
