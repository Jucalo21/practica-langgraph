from langgraph.graph import StateGraph, END, START
from .utils.nodes import (
    node_translation,
    node_antonyms,
    node_palindrome,
    node_length,
    node_definition,
    node_synonyms,
    condition_length,
)
from .utils.state import Word, Definition, WordInfo, TranslationWord, SynAntState


def run_graph(input_word: str) -> Word:
    # Estado inicial con la estructura anidada
    initial_state = Word(
        info=WordInfo(
            word=input_word,
        ),
        definition=Definition(
            definition="",
        ),
        syn_ant=SynAntState(
            words=[],
            is_synonym=False,
        ),
        translate_word=TranslationWord(
            translation_word="",
            language="",
        ),
    )

    graph_builder = StateGraph(Word)
    graph_builder.add_node("check_palindrome", node_palindrome)
    graph_builder.add_node("word_length", node_length)
    graph_builder.add_node("word_definition", node_definition)
    graph_builder.add_node("word_antonyms", node_antonyms)
    graph_builder.add_node("word_synonyms", node_synonyms)
    graph_builder.add_node("translation_word", node_translation)

    graph_builder.add_edge(START, "check_palindrome")
    graph_builder.add_edge("check_palindrome", "word_length")
    graph_builder.add_conditional_edges(
        "word_length",
        condition_length,
        {
            "par": "word_synonyms",
            "impar": "word_antonyms",
        },
    )
    graph_builder.add_edge("word_antonyms", "word_definition")
    graph_builder.add_edge("word_synonyms", "word_definition")
    graph_builder.add_edge("word_definition", "translation_word")
    graph_builder.add_edge("translation_word", END)

    graph = graph_builder.compile()
    result = graph.invoke(initial_state)
    return result
