from typing import TypedDict, Dict, Any
from langgraph.graph import StateGraph, END
from llm.mock_llm import generate_response
from memory.memory_utils import summarize_session_memory


class ConversationState(TypedDict):
    user_input: str
    session_memory: Dict[str, Any]
    long_term_memory: Dict[str, Any]
    response: str
def memory_read_node(state: ConversationState) -> ConversationState:
    print("\n[Memory Read]")
    print("Session Memory:", state["session_memory"])
    print("Long-Term Memory:", state["long_term_memory"])

    return state
def response_generation_node(state: ConversationState) -> ConversationState:
    response = generate_response(
        state["user_input"],
        state["session_memory"],
        state["long_term_memory"]
    )

    state["response"] = response
    return state
def memory_update_node(state: ConversationState) -> ConversationState:
    user_input = state["user_input"].lower()

  
    if "prepare" in user_input and "exam" in user_input:
        state["long_term_memory"]["learning_goal"] = "biology exam"
    if "confused" in user_input or "don't understand" in user_input:
        state["session_memory"]["difficulty"] = True

    print("\n[Memory Update]")
    print("Updated Session Memory:", state["session_memory"])
    print("Updated Long-Term Memory:", state["long_term_memory"])
    if len(state["session_memory"]) > 1:
     state["session_memory"] = summarize_session_memory(state["session_memory"])
    return state

def build_graph():
    graph = StateGraph(ConversationState)

    graph.add_node("memory_read", memory_read_node)
    graph.add_node("generate_response", response_generation_node)
    graph.add_node("memory_update", memory_update_node)
    graph.set_entry_point("memory_read")
    graph.add_edge("memory_read", "generate_response")
    graph.add_edge("generate_response", "memory_update")
    graph.add_edge("memory_update", END)
    return graph.compile()

