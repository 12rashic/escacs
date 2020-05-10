from escacs.interfaces import ISquare
from escacs.square import Square
from escacs.types import Coordinate
from typing import cast


def get_square(pos: Coordinate) -> ISquare:
    if isinstance(pos, str):
        sq: ISquare = cast(ISquare, Square(pos))
    else:
        sq = pos
    return sq
