from pydantic import BaseModel, Field
from typing import TypedDict


class Word(TypedDict):
    word: str
    inverted_word: str = ""
    is_palindrome: bool = False
