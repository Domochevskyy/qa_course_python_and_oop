from typing import NamedTuple, Any

from src import Triangle


class TriangleCase(NamedTuple):
    parameters: Any
    expected: int | float | None | Triangle


triangle_creating_cases = (TriangleCase([], None),
                           TriangleCase([0, 0, 0], None),
                           TriangleCase([None], None),
                           TriangleCase([-3, 4, 5], None),
                           TriangleCase([3, -4, 5], None),
                           TriangleCase([3, 4, -5], None),
                           TriangleCase([0, 0, 0], None),
                           TriangleCase(['3', '4', '5'], None),
                           TriangleCase(['3', 4, 5], None),
                           TriangleCase([3, '4', 5], None),
                           TriangleCase([3, 4, '5'], None),
                           TriangleCase([3, 4, 8], None),
                           TriangleCase([8, 4, 3], None),
                           TriangleCase([3, 8, 4], None),
                           TriangleCase([3, 4, 5], Triangle(3, 4, 5)),
                           TriangleCase([3.0, 4.0, 5.0],
                                        Triangle(3.0, 4.0, 5.0)),
                           )

triangle_perimeter_calculation_cases = (TriangleCase([3, 4, 5], 12),
                                        TriangleCase([3.0, 4.0, 5.0], 12.0),
                                        TriangleCase([1, 1, 1], 3),
                                        TriangleCase([2, 3, 2], 7),
                                        TriangleCase([14, 17, 15], 46),
                                        )

triangle_area_calculation_cases = (TriangleCase([3, 4, 5], 6),
                                   TriangleCase([3.0, 4.0, 5.0], 6),
                                   TriangleCase([1, 1, 1], 0.433),
                                   TriangleCase([2, 3, 2], 1.984),
                                   TriangleCase([14, 17, 15], 99.679),
                                   )
