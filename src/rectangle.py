from src import Figure


class Rectangle(Figure):
    __slots__ = ('a', 'b')

    def __init__(self, a: int | float = None, b: int | float = None):
        self.a = a
        self.b = b
        super().__init__()

    def __repr__(self):
        return f'Rectangle{self.a, self.b}'

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def _calculate_perimeter(self):
        return (self.a + self.b) * 2

    def _calculate_area(self):
        return self.a * self.b
