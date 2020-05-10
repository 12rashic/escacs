from escacs import pieces
from escacs.board import Board
from escacs.exceptions import InvalidMove
from escacs.exceptions import PieceNotFound
from escacs.interfaces import IBoard
from escacs.interfaces import IGame
from escacs.interfaces import IPiece
from escacs.square import Square
from escacs.types import Color
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from zope.interface import implementer


@implementer(IGame)
class Game:
    def __init__(self):
        self.start()

    def start(self):
        self._turn: Color = "white"
        self.moves: List[Tuple[Square, Square]] = []
        self.initialize_board()

    def initialize_board(self):
        self.board: IBoard = Board()
        for col in range(8):
            self.board[Square(col=col, row=1)] = pieces.Pawn("white")
            self.board[Square(col=col, row=6)] = pieces.Pawn("black")
        self.board["a1"] = pieces.Rook("white")
        self.board["h1"] = pieces.Rook("white")
        self.board["a8"] = pieces.Rook("black")
        self.board["h8"] = pieces.Rook("black")
        self.board["b1"] = pieces.Knight("white")
        self.board["g1"] = pieces.Knight("white")
        self.board["b8"] = pieces.Knight("black")
        self.board["g8"] = pieces.Knight("black")
        self.board["c1"] = pieces.Bishop("white")
        self.board["f1"] = pieces.Bishop("white")
        self.board["c8"] = pieces.Bishop("black")
        self.board["f8"] = pieces.Bishop("black")
        self.board["d1"] = pieces.Queen("white")
        self.board["d8"] = pieces.Queen("black")
        self.board["e1"] = pieces.King("white")
        self.board["e8"] = pieces.King("black")

    @property
    def turn(self) -> Color:
        return self._turn

    def pass_turn(self):
        if self._turn == "white":
            self._turn = "black"
        else:
            self._turn = "white"

    def player_move(self, _from: Square, _to: Square) -> Optional[IPiece]:
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
        self.pass_turn()


def legal_moves(_from: Square, board: Board) -> Set[Square]:
    """Returns all legal moves of the piece in a given piece in the board

    """
    piece: Optional[IPiece] = board[_from]
    if not piece:
        raise PieceNotFound(_from)

    legal_moves = set()
    for _to in piece.all_moves(_from):
        if not safe_king(board, _from, _to):
            print(f"King is not safe with {_from} -> {_to}")
            continue

        if not clear_path(board, _from, _to) and not isinstance(piece, pieces.Knight):
            print(f"Path not clear with {_from} -> {_to}")
            continue

        legal_moves.update({_to})

    return legal_moves


def clear_path(board: Board, _from: Square, _to: Square) -> bool:
    return True


def eating_move(board, _from: Square, _to: Square) -> bool:
    return False


def safe_king(*args, **kwargs) -> bool:
    return True
