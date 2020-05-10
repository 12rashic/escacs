from escacs.interfaces import ISquare
from escacs.square import Square
from escacs.types import Coordinate


def get_square(pos: Coordinate) -> ISquare:
    if isinstance(pos, str):
        return Square(pos)  # type: ignore
    return pos
