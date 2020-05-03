from abc import ABCMeta, abstractmethod
from typing import List, Optional, Set, Tuple

from .square import Square
from .types import Color


class Piece(metaclass=ABCMeta):
    """
    Meta-class that encapsulates all comon piece logic
    """

    # Used to compute all possible moves per piece
    _vectors: Optional[List[Tuple[int, int]]] = None

    def __init__(self, color: Color, pos: Square):
        self.color = color
        self.pos = pos
        self.init()

    def init(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.pos})"

    @abstractmethod
    def all_moves(self) -> Set[Square]:
        """Returns all possible squares of the piece given the current
        position (this includes ilegal moves too)

        """
        ...

    def _all_moves(self) -> Set[Square]:
        moves = set({})
        for vector in self._vectors or []:
            x, y = vector
            factor = 1
            while True:
                col = self.pos.col
                row = self.pos.row
                if x != 0:
                    col += x * factor
                if y != 0:
                    row += y * factor
                factor = factor + 1
                if not self._in_board(col, row):
                    break
                else:
                    moves.update({Square(col=col, row=row)})
        return moves

    def _in_board(self, col, row) -> bool:
        return col in range(8) and row in range(8)

    def move(self, pos: Square):
        self.pos = pos

    def raw(self):
        self.pos.raw

    def col(self):
        self.pos.col


class Pawn(Piece):
    def init(self):
        self.direction = 1 if self.color == "white" else -1
        self.start_row = 1 if self.color == "white" else 6

    def all_moves(self) -> Set[Square]:
        moves = set({})

        # On starting position, pawn can jump 2 squares
        if self.pos.row == self.start_row:
            col = self.pos.col
            row = self.pos.row + (self.direction * 2)
            moves.update({Square(col=col, row=row)})

        # Moving one square ahead + capturing moves
        for side in (-1, 0, 1):
            row = self.pos.row + self.direction
            col = self.pos.col + side
            if self._in_board(col, row):
                moves.update({Square(col=col, row=row)})

        return moves


class Knight(Piece):
    def all_moves(self) -> Set[Square]:
        moves = set({})
        for (x, y) in [
            [1, 2],
            [1, -2],
            [2, 1],
            [2, -1],
            [-1, 2],
            [-1, -2],
            [-2, 1],
            [-2, -1],
        ]:
            col = self.pos.col + x
            row = self.pos.row + y
            if not self._in_board(col, row):
                continue
            moves.update({Square(col=col, row=row)})
        return moves


class Bishop(Piece):
    _vectors = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def all_moves(self) -> Set[Square]:
        return self._all_moves()


class Rook(Piece):
    _vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def all_moves(self) -> Set[Square]:
        return self._all_moves()


class Queen(Piece):
    _vectors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def all_moves(self) -> Set[Square]:
        return self._all_moves()


class King(Piece):
    def all_moves(self) -> Set[Square]:
        moves = set({})
        for (x, y) in [
            [1, 0],
            [1, 1],
            [1, -1],
            [0, -1],
            [0, 1],
            [-1, 0],
            [-1, 1],
            [-1, -1],
        ]:
            col = self.pos.col + x
            row = self.pos.row + y
            if not self._in_board(col, row):
                continue
            moves.update({Square(col=col, row=row)})
        return moves
