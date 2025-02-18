from langgraph.graph import StateGraph, END, START
from .utils.nodes import nodo_llm
from .utils.state import WordState


def run_graph(input_word: str):
    initial_state = WordState(word=input_word)

    graph_builder = StateGraph(WordState)
    graph_builder.add_node("check_palindrome", nodo_llm)

    graph_builder.add_edge(START, "check_palindrome")
    graph_builder.add_edge("check_palindrome", END)

    graph = graph_builder.compile()

    result = graph.invoke(initial_state)
    return result
