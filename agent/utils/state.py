from pydantic import BaseModel, Field
from typing import TypedDict


class WordState(BaseModel):
    word: str = Field(..., description="Una palabra elegida por el usuario")
    inverted_word: str = Field(
        "", description="La palabra elegida por el usuario invertida"
    )
    is_palindrome: bool = Field(
        False,
        description="True o False dependiendo de si es palindroma la palabra",
    )


class WordResponse(BaseModel):
    word: str = Field(..., description="Una palabra elegida por el usuario")
    inverted_word: str = Field(
        ..., description="La palabra elegida por el usuario invertida"
    )
    is_palindrome: bool = Field(
        ...,
        description="True o False dependiendo de si es palindroma la palabra",
    )
