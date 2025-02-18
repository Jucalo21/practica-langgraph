from .state import WordResponse, WordState
from agent.utils.llamado_llm import definir_llm
import json


def nodo_1(state: WordResponse):
    word = state["word"]
    inverted = "".join(reversed(word))

    # Actualizamos el estado (TypedDict)
    state["inverted_word"] = inverted
    state["is_palindrome"] = word == inverted

    return state


def nodo_llm(state: WordState):
    client = definir_llm()

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Verifica si la palabra {state.word} es palindroma",
        config={
            "response_mime_type": "application/json",
            "response_schema": WordResponse,
        },
    )

    parsed_json = json.loads(response.text)
    parsed_response = WordResponse.model_validate(parsed_json)

    updated_state = WordState(
        word=state.word,
        inverted_word=parsed_response.inverted_word,
        is_palindrome=parsed_response.is_palindrome,
    )

    return updated_state
