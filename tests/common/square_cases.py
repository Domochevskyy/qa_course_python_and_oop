from typing import NamedTuple, Any

from src import Square


class SquareCase(NamedTuple):
    side: Any
    expected: int | float | None | Square


square_creating_cases = (SquareCase(1, Square(1)),
                         SquareCase(1.0, Square(1.0)),
                         SquareCase(-1, None),
                         SquareCase('1', None),
                         SquareCase([], None),
                         )
square_perimeter_cases = (SquareCase(1, 4),
                          SquareCase(1.0, 4.0),
                          SquareCase(100, 400))
square_area_cases = (SquareCase(1, 1),
                     SquareCase(1.0, 1.0),
                     SquareCase(100, 10000),
                     )
