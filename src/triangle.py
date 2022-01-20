from . import Figure


class Triangle(Figure):
    __slots__ = ('a', 'b', 'c')

    def __new__(cls, *args, **kwargs):
        if not args or not cls.__is_triangle_exist(*args):
            return None
        return super().__new__(cls)

    def __init__(self,
                 a: float | int = None,
                 b: float | int = None,
                 c: float | int = None,
                 ):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()

    def __repr__(self):
        return f'Triangle{self.a, self.b, self.c}'

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def _calculate_perimeter(self) -> float | int:
        return self.a + self.b + self.c

    def _calculate_area(self) -> int | float:
        half_perimeter = self._calculate_perimeter() / 2
        area = (half_perimeter *
                (half_perimeter - self.a) *
                (half_perimeter - self.b) *
                (half_perimeter - self.c)
                ) ** 0.5
        return round(area, 3)

    @classmethod
    def __is_triangle_exist(cls, *args):
        for i in args:
            if not isinstance(i, (int, float)) or i < 0:
                return False
        a, b, c = args
        if a + b > c and a + c > b and b + c > a:
            return True
        return False
