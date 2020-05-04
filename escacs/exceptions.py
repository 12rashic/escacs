class InvalidSquare(Exception):
    def __init__(self, pos):
        self.pos = pos


class InvalidMove(Exception):
    def __init__(self, _from, _to):
        self._from = _from
        self._to = _to
