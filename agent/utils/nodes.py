from .state import WordInfo, Definition, Word
from agent.utils.llamado_llm import definir_llm
import json


def nodo_palindrome(state: Word) -> Word:
    word = state["info"]["word"]
    inverted = "".join(reversed(word))

    # Actualizamos el estado (TypedDict)
    state["info"]["inverted_word"] = inverted
    state["info"]["is_palindrome"] = word.lower() == inverted.lower()

    return state


def nodo_length(state: Word) -> Word:
    state["info"]["length"] = len(state["info"]["word"])
    return state


def nodo_definition(state: Word) -> Word:
    client = definir_llm()

    prompt = f"Dale una sola definicion a la palabra {state["info"]["word"]}, y que la definicion sea en idioma español"
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": Definition,
        },
    )

    parsed = json.loads(response.text)

    state["definition"]["definition"] = parsed.get("definition", "")
    return parsed
