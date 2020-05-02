from typing import Optional, Tuple, Union

from .exceptions import InvalidSquare
from .types import Color


class Square:
    row: int
    col: int

    def __init__(
        self,
        pos: Optional[Union[str, Tuple[int, int]]] = None,
        col: Optional[int] = None,
        row: Optional[int] = None,
    ):
        if pos is not None:
            if isinstance(pos, str):
                col, row = _from_string(pos)
            else:
                col, row = pos
        else:
            col = col or 0
            row = row or 0

        if row not in range(8) or col not in range(8):
            raise InvalidSquare((row, col))
        self.row = row
        self.col = col

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self}")'

    def __eq__(self, other) -> bool:
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash(repr(self))

    @property
    def color(self) -> Color:
        if (self.row + self.col) % 2 == 0:
            return "black"
        return "white"

    def __str__(self) -> str:
        """
        Translates matrix position to chess coordinates
        Square(row=0, col=0) --> a1'
        """
        try:
            col = "abcdefgh"[self.col]
            row = range(1, 9)[self.row]
            return "".join([col, str(row)])
        except KeyError:
            raise InvalidSquare((self.col, self.row))


def _from_string(pos: str) -> Tuple[int, int]:
    """
    Translates chess coordinates to a matrix position
    'a1' --> Square(row=0, col=0)
    """
    if len(pos) != 2:
        raise InvalidSquare(pos)
    try:
        col = "abcdefgh".index(pos[0])
        row = range(1, 9).index(int(pos[1]))
        return col, row
    except ValueError:
        raise InvalidSquare(pos)
