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
    def all_moves(self) -> Set[Square]:
        if self.color == "white":
            if self.pos.row == 8:
                return set({})
            return {Square(col=self.pos.col, row=self.pos.row + 1)}
