from .state import Definition, Word, TranslationWord, SynAntState
from agent.utils.llamado_llm import definir_llm
import json


def node_palindrome(state: Word) -> Word:
    word = state["info"]["word"]
    inverted = "".join(reversed(word))

    # Actualizamos el estado (TypedDict)
    state["info"]["inverted_word"] = inverted
    state["info"]["is_palindrome"] = word.lower() == inverted.lower()

    return state


def node_length(state: Word) -> Word:
    state["info"]["length"] = len(state["info"]["word"])
    return state


def node_definition(state: Word) -> Word:
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
    return state


def node_translation(state: Word) -> Word:
    client = definir_llm()
    prompt = ""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": Definition,
        },
    )

    parsed = json.loads(response.text)

    state["translate_word"]["TranslationWord"] = parsed.get("")
    return state


def node_synonyms(state: Word):
    client = definir_llm()
    prompt = f"""Dame 5 sinonimos de la siguiente palabra: {state['info']['word']} teniendo en cuenta la definicion {state['definition']["definition"]}.
    Si no es posible dar sinonimos, explica el por qué."""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": SynAntState,
        },
    )

    parsed = json.loads(response.text)
    state["syn_ant"]["is_synonym"] = True
    state["syn_ant"]["words"] = parsed.get("words", "")
    return state


def node_antonyms(state: Word):
    client = definir_llm()
    prompt = f"""Dame 5 antonimos de la siguiente palabra: {state['info']['word']} teniendo en cuenta la definicion 
    {state['definition']["definition"]}.
    Si no es posible dar sinonimos, explica el por qué."""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": SynAntState,
        },
    )

    parsed = json.loads(response.text)
    state["syn_ant"]["is_synonym"] = False
    state["syn_ant"]["words"] = parsed.get("words", "")
    return state


def condition_length(state: Word):
    if state["info"]["length"] % 2 == 0:
        return "par"
    else:
        return "impar"
