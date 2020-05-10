from zope.interface import Attribute
from zope.interface import Interface


class IPiece(Interface):
    def all_moves(self, pos):
        ...

    def legal_moves(self):
        ...

    def move(self, pos):
        ...


class IBoard(Interface):
    def clear(self):
        ...

    def get_piece(self, pos):
        ...

    def place_piece(self, pos, piece):
        ...

    def move_piece(self, src_pos, dst_pos):
        ...

    def path(self, src_pos, dst_pos):
        ...


class ISquare(Interface):
    color = Attribute("color")


class IGame(Interface):
    turn = Attribute("turn")

    def player_move(src_pos, dst_pos):
        ...
