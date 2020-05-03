from abc import ABCMeta, abstractmethod
from typing import Set

from .square import Square
from .types import Color


class Piece(metaclass=ABCMeta):
    def __init__(self, color: Color, pos: Square):
        self.color = color
        self.pos = pos
        self.init()

    def init(self):
        pass

    @abstractmethod
    def all_moves(self) -> Set[Square]:
        """Returns all possible moves of the piece given the current square
        (this includes ilegal moves too)
        """
        ...

    def move(self, pos: Square):
        self.pos = pos


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
            if row in range(8) and col in range(8):
                moves.update({Square(col=col, row=row)})

        return moves
