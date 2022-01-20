from math import pi

from src import Figure


class Circle(Figure):
    __slots__ = 'radius'

    def __init__(self, radius: float | int = None):
        self.radius = radius
        super().__init__()

    def __repr__(self):
        return f'Circle({self.radius})'

    def __eq__(self, other):
        return abs(self.radius - other.radius) < 0.001

    def _calculate_perimeter(self):
        return round(2 * self.radius * pi, 3)

    def _calculate_area(self):
        return round(pi * (self.radius ** 2), 3)
