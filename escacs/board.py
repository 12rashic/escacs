from copy import copy
from escacs.exceptions import PieceNotFound
from escacs.interfaces import IBoard
from escacs.interfaces import IPiece
from escacs.interfaces import ISquare
from escacs.square import Square
from escacs.types import Coordinate
from escacs.utils import get_square
from typing import Dict
from typing import List
from typing import Optional
from zope.interface import implementer

_none = object()


@implementer(IBoard)
class Board:
    """
    Stores the position of the pieces along the game.
    """

    def __init__(self):
        self.clear()

    def clear(self):
        self._board: Dict[ISquare, Optional[IPiece]] = {
            Square(col=col, row=row): None for col in range(8) for row in range(8)
        }

    def __getitem__(self, pos: Coordinate) -> Optional[IPiece]:
        pos: ISquare = get_square(pos)
        return self._board[pos]

    def __setitem__(self, pos: Coordinate, piece: Optional[IPiece]) -> None:
        pos: ISquare = get_square(pos)
        if piece:
            piece.board = self
            piece.move(pos)
        self._board[pos] = piece

    get_piece = __getitem__
    place_piece = __setitem__

    def path(self, _from: Coordinate, _to: Coordinate) -> List[Square]:
        """Returns the ordered list of squares that conform the shortest path
        between 2 board coordinates.
        """
        src: ISquare = get_square(_from)
        dst: ISquare = get_square(_to)
        path = []
        while src != dst:
            if src.row > dst.row:
                src.row += 1
            elif dst.row < src.row:
                src.row -= 1
            if dst.col > src.col:
                src.col += 1
            elif dst.col < src.col:
                src.col -= 1
            path.append(copy(src))
        return path

    def move_piece(self, _from: Coordinate, _to: Coordinate):
        """Moves whichever piece is found in _from to _to positions. If no
        piece found, nothing is done.

        It does not check against valid chess moves.

        """
        src: ISquare = get_square(_from)
        dst: ISquare = get_square(_to)
        piece: Optional[IPiece] = self[src]
        if not piece:
            # No piece found
            return

        self[src] = None
        self[dst] = piece
        piece.move(dst)

    def get_square(self, piece: IPiece) -> Square:
        for square, p in self._board.items():
            if not p:
                continue
            if p == piece:
                return square
        raise PieceNotFound(piece)
