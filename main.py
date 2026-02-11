from graph.conversation_graph import build_graph
from memory.long_term import load_long_term_memory, save_long_term_memory


def run_demo():
    graph = build_graph()

   
    state = {
    "session_memory": {},
    "long_term_memory": load_long_term_memory(),
    "response": ""
}
   
    print("\n=== TURN 1 ===")
    state["user_input"] = "I want to prepare for my biology exam"
    state = graph.invoke(state)
    save_long_term_memory(state["long_term_memory"])

    print("Assistant:", state["response"])

    
    print("\n=== TURN 2 ===")
    state["user_input"] = "Can you explain photosynthesis?"
    state = graph.invoke(state)
    save_long_term_memory(state["long_term_memory"])

    print("Assistant:", state["response"])
    


if __name__ == "__main__":
    run_demo()
