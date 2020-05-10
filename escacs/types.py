from enum import Enum
from escacs.interfaces import ISquare
from typing import Union


class Color(str, Enum):
    white = "white"
    black = "black"


Coordinate = Union[str, ISquare]
