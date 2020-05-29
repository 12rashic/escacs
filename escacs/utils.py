from escacs.square import Square
from escacs.types import Coordinate


def get_square(pos: Coordinate) -> Square:
    if isinstance(pos, str):
        return Square(pos)  # type: ignore
    return pos
