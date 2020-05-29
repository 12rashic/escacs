from copy import copy
from escacs.exceptions import PieceNotFound
from escacs.pieces import Piece
from escacs.square import Square
from escacs.types import Coordinate
from escacs.utils import get_square
from typing import Dict
from typing import List
from typing import Optional

_none = object()


class Board:
    """
    Stores the position of the pieces along the game.
    """

    def __init__(self):
        self.clear()

    def clear(self):
        self._board: Dict[Square, Optional[Piece]] = {
            Square(col=col, row=row): None for col in range(8) for row in range(8)
        }

    def __getitem__(self, pos: Coordinate) -> Optional[Piece]:
        return self._board[get_square(pos)]

    def __setitem__(self, pos: Coordinate, piece: Optional[Piece]) -> None:
        sq = get_square(pos)
        if piece:
            piece.board = self
            piece.move(sq)
        self._board[sq] = piece

    get_piece = __getitem__
    place_piece = __setitem__

    def path(self, _from: Coordinate, _to: Coordinate) -> List[Square]:
        """Returns the ordered list of squares that conform the shortest path
        between 2 board coordinates.
        """
        src: Square = get_square(_from)
        dst: Square = get_square(_to)
        path = []
        while src != dst:
            for attr in ("row", "col"):
                srcx = getattr(src, attr)
                dstx = getattr(dst, attr)
                if srcx == dstx:
                    continue
                if srcx > dstx:
                    setattr(src, attr, srcx - 1)
                else:
                    setattr(src, attr, srcx + 1)
            path.append(copy(src))
        return path

    def move_piece(self, _from: Coordinate, _to: Coordinate):
        """Moves whichever piece is found in _from to _to positions. If no
        piece found, nothing is done.

        It does not check against valid chess moves.

        """
        src: Square = get_square(_from)
        dst: Square = get_square(_to)
        piece: Optional[Piece] = self[src]
        if not piece:
            # No piece found
            return

        self[src] = None
        self[dst] = piece
        piece.move(dst)

    def get_square(self, piece: Piece) -> Square:
        for square, p in self._board.items():
            if not p:
                continue
            if p == piece:
                return square
        raise PieceNotFound(piece)
