from typing import NamedTuple, Any

from src import Rectangle


class RectangleCase(NamedTuple):
    parameters: Any
    expected: int | float | None | Rectangle


rectangle_creating_cases = (RectangleCase([None], None),
                            RectangleCase([1, 2],
                                          Rectangle(1, 2)),
                            RectangleCase([1.0, 2.0],
                                          Rectangle(1.0, 2.0)),
                            RectangleCase([-1, 2], None),
                            RectangleCase([1, -2], None),
                            RectangleCase([-1, -2], None),
                            RectangleCase(['1', 2], None),
                            RectangleCase([1, '2'], None),
                            RectangleCase(['1', '2'], None),
                            )
rectangle_perimeter_cases = (RectangleCase([1, 2], 6),
                             RectangleCase([1, 1], 4),
                             RectangleCase([1.0, 1.0], 4.0),
                             RectangleCase([13, 17], 60),
                             RectangleCase([100, 100], 400),
                             )
rectangle_area_cases = (RectangleCase([1, 2], 2),
                        RectangleCase([1, 1], 1),
                        RectangleCase([1.0, 1.0], 1.0),
                        RectangleCase([1.0, 1.0], 1.0),
                        RectangleCase([13, 17], 221),
                        RectangleCase([100, 100], 10000),
                        )
