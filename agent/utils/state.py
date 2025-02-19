from pydantic import BaseModel, Field
from typing import TypedDict


class WordInfo(TypedDict):
    word: str
    inverted_word: str
    is_palindrome: bool
    length: int


class Definition(TypedDict):
    definition: str


class Word(TypedDict):
    info: WordInfo
    definition: Definition
