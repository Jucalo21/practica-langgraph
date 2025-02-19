from langgraph.graph import StateGraph, END, START
from .utils.nodes import nodo_palindrome, nodo_length, nodo_definition
from .utils.state import Word, Definition, WordInfo


def run_graph(input_word: str) -> Word:
    # Estado inicial con la estructura anidada
    initial_state = Word(
        info=WordInfo(word=input_word),
        definition=Definition(),
    )

    graph_builder = StateGraph(Word)
    graph_builder.add_node("check_palindrome", nodo_palindrome)
    graph_builder.add_node("word_length", nodo_length)
    graph_builder.add_node("word_definition", nodo_definition)

    graph_builder.add_edge(START, "check_palindrome")
    graph_builder.add_edge("check_palindrome", "word_length")
    graph_builder.add_edge("word_length", "word_definition")
    graph_builder.add_edge("word_definition", END)

    graph = graph_builder.compile()
    result = graph.invoke(initial_state)
    return result
