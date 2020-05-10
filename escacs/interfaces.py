from zope.iterface import Interface


class IPiece(Interface):
    def all_moves(pos):
        ...

    def legal_moves(pos):
        ...

    def is_safe():
        ...


class IBoard(Interface):
    def clear():
        ...

    def get_piece(pos):
        ...

    def place_piece(pos, piece):
        ...

    def move_piece(src_pos, dst_pos):
        ...

    def path(src_pos, dst_pos):
        ...


class IGame(Interface):
    def turn():
        ...

    def player_move(src_pos, dst_pos):
        ...
