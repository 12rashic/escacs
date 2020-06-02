from escacs.board import Board
from escacs.exceptions import InvalidMove
from escacs.pieces import Bishop
from escacs.pieces import King
from escacs.pieces import Knight
from escacs.pieces import Pawn
from escacs.pieces import Piece
from escacs.pieces import Queen
from escacs.pieces import Rook
from escacs.square import Square
from escacs.types import Color
from escacs.types import Coordinate
from typing import List
from typing import Optional
from typing import Tuple


class Game:
    """
    Represents the chess game.

    Attributes
    ----------
    _turn: Color
        states which player is next in the current moment.
    moves: list
        history of moves already realized in the game.
    board: Board
        object of the class Board.

    """

    def __init__(self):
        self.start()

    def start(self):
        self._turn: Color = "white"
        self.moves: List[Tuple[Square, Square]] = []
        self.initialize_board()

    def place_piece(self, piece_klas, color: Color, pos: Coordinate):
        piece = piece_klas(color, board=self.board, pos=pos)
        self.board.place_piece(pos, piece)

    def advantage(self, color: Color) -> int:
        points = self.get_points(color)
        opponent = "white" if color == "black" else "black"
        opponent_points = self.get_points(opponent)  # type: ignore
        return points - opponent_points

    def get_points(self, color: Color) -> int:
        points = 0
        for _, piece in self.board._board.items():
            if piece and piece.color == color:
                points += piece.points
        return points

    def initialize_board(self):
        self.board: Board = Board()
        for col in "abcdefgh":
            self.place_piece(Pawn, "white", f"{col}2")
            self.place_piece(Pawn, "black", f"{col}7")
        self.place_piece(Rook, "white", "a1")
        self.place_piece(Rook, "white", "h1")
        self.place_piece(Rook, "black", "a8")
        self.place_piece(Rook, "black", "h8")
        self.place_piece(Knight, "white", "b1")
        self.place_piece(Knight, "white", "g1")
        self.place_piece(Knight, "black", "b8")
        self.place_piece(Knight, "black", "g8")
        self.place_piece(Bishop, "white", "c1")
        self.place_piece(Bishop, "white", "f1")
        self.place_piece(Bishop, "black", "c8")
        self.place_piece(Bishop, "black", "f8")
        self.place_piece(Queen, "white", "d1")
        self.place_piece(Queen, "black", "d8")
        self.place_piece(King, "white", "e1")
        self.place_piece(King, "black", "e8")

    @property
    def turn(self) -> Color:
        return self._turn

    def pass_turn(self) -> None:
        if self._turn == "white":
            self._turn = "black"  # type: ignore
        else:
            self._turn = "white"  # type: ignore

    def player_move(self, _from: Square, _to: Square) -> Optional[Piece]:
        """Move a piece from a square to another one. Checks agains valid
        moves. Returns the eaten piece, if any.

        """
        # Check that there is a piece in source square
        piece = self.board.get_piece(_from)
        if not piece:
            # No piece found
            raise InvalidMove(_from, _to)

        # Check that the piece is from the same color as the player
        if piece.color != self.turn:
            raise InvalidMove(_from, _to)

        # Check that it's a valid piece move
        if _to not in piece.all_moves():
            raise InvalidMove(_from, _to)

        if not piece.is_legal_move(_to):
            raise InvalidMove(_from, _to)

        # TODO: Take into account moves where can take!
        # TODO: check that the move doesn't crash against any other
        # piece.
        # TODO: prevent moves that leave the king on check.
        # TODO: check for stalemate.
        taken: Optional[Piece] = self.board.move_piece(_from, _to)
        self.moves.append((_from, _to))
        self.pass_turn()
        return taken
