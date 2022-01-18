from src import Rectangle


class Square(Rectangle):
    __slots__ = 'side'

    def __init__(self, side: int | float = None):
        self.side = side
        super().__init__(self.side, self.side)

    def __repr__(self):
        return f'Square({self.side})'
