from enum import Enum
from escacs.square import Square
from typing import Union


class Color(str, Enum):
    white = "white"
    black = "black"


Coordinate = Union[str, Square]
