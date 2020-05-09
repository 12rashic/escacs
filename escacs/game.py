from typing import Optional

from .board import Board
from .exceptions import InvalidMove
from .pieces import *
from .square import Square
from .types import Color


class Game:
    def __init__(self):
        self._turn: Color = "white"
        self.moves: List[Tuple[Square, Square]] = []
        self.board = Board()

    @property
    def turn(self) -> Color:
        return self._turn

    def pass_turn(self):
        if self._turn == "white":
            self._turn = "black"
        else:
            self._turn = "white"

    def move(self, _from: Square, _to: Square) -> Optional[Piece]:
        """Move a piece from a square to another one. Checks agains valid
        moves. Returns the eaten piece, if any.

        """
        # Check that there is a piece in source square
        piece = self.board[_from]
        if not piece:
            # No piece found
            raise InvalidMove(_from, _to)

        # Check that the piece is from the same color as the player
        if piece.color != self.turn:
            raise InvalidMove(_from, _to)

        # Check that it's a valid piece move
        all_moves = piece.all_moves(_from)
        if _to not in all_moves:
            raise InvalidMove(_from, _to)

        # TODO: check that the move doesn't crash against any other
        # piece.
        # TODO: prevent moves that leave the king on check.
        # TODO: check for stale.
        self.board.move(_from, _to)
        self.moves.append((_from, _to))


def legal_moves(piece: Piece, board: Board) -> Set[Square]:
    """
    Returns all legal moves for a given piece in the board
    """
    current: Square = board.get_square(piece)
    legal_moves = set()
    for move in piece.all_moves(current):

        if not safe_king(board, piece, move):
            print("King is not safe with {current} -> {move}")
            continue

        if not clear_path(board, piece, move):
            print("Path not clear with {current} -> {move}")
            continue

        legal_moves.update({move})


def clear_path(*args, **kwargs) -> bool:
    pass


def safe_king(*args, **kwargs) -> bool:
    pass
