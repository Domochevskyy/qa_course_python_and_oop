from typing import NamedTuple, Any

from src import Circle


class CircleCase(NamedTuple):
    radius: Any
    expected: int | float | None | Circle


circle_creating_cases = (CircleCase([], None),
                         CircleCase(-2, None),
                         CircleCase(2, Circle(2)),
                         CircleCase('2', None),
                         CircleCase(2.0, Circle(2.0)),
                         )
circle_perimeter_cases = (CircleCase(2, 12.566),
                          CircleCase(2.0, 12.566),
                          CircleCase(100, 628.318),
                          CircleCase(57, 358.141),
                          )
circle_area_cases = (CircleCase(2, 12.566),
                     CircleCase(2.0, 12.566),
                     CircleCase(100, 31415.926),
                     CircleCase(57, 10207.034),
                     )
