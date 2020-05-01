from enum import Enum

from pydantic import BaseModel


class Position(BaseModel):
    row: int
    column: int


class Color(str, Enum):
    white = "white"
    black = "black"
