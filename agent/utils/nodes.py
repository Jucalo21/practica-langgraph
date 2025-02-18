from .state import Word


def nodo_1(state: Word):
    word = state["word"]
    inverted = "".join(reversed(word))

    # Actualizamos el estado (TypedDict)
    state["inverted_word"] = inverted
    state["is_palindrome"] = word == inverted

    return state
