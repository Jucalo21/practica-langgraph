from pydantic import BaseModel, Field
from typing import TypedDict


class WordInfo(TypedDict):
    word: str
    inverted_word: str
    is_palindrome: bool
    length: int


class Definition(TypedDict):
    definition: str


class TranslationWord(TypedDict):
    TranslationWord: str
    language: str


class SynAntState(TypedDict):
    words: list[str]
    is_synonym: bool


class Word(TypedDict):
    info: WordInfo
    translate_word: TranslationWord
    syn_ant: SynAntState
    definition: Definition
