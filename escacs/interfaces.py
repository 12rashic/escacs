from zope.interface import Interface


class IPiece(Interface):
    def all_moves(pos):
        ...

    def legal_moves(pos):
        ...

    def is_safe():  # type: ignore
        ...


class IBoard(Interface):
    def clear():  # type: ignore
        ...

    def get_piece(self, pos):
        ...

    def place_piece(self, pos, piece):
        ...

    def move_piece(self, src_pos, dst_pos):
        ...

    def path(src_pos, dst_pos):
        ...


class IGame(Interface):
    def turn():  # type: ignore
        ...

    def player_move(src_pos, dst_pos):
        ...
