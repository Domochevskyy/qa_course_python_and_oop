from typing import NamedTuple, Any

from src import Figure, Circle, Square, Rectangle, Triangle


class BaseCase(NamedTuple):
    object_to_add: Figure
    added_object: Any
    expected: int | float


cases_for_add_area = (BaseCase(Circle(1), Circle(1), 6.283),
                      BaseCase(Circle(1), Square(1), 4.141),
                      BaseCase(Circle(1), Rectangle(2, 2), 7.141),
                      BaseCase(Circle(1), Triangle(3, 4, 5), 9.141),
                      BaseCase(Square(1), Square(1), 2),
                      BaseCase(Square(1), Circle(1), 4.141),
                      BaseCase(Square(1), Rectangle(2, 2), 5),
                      BaseCase(Square(1), Triangle(3, 4, 5), 7),
                      BaseCase(Rectangle(2, 2), Rectangle(2, 2), 8),
                      BaseCase(Rectangle(2, 2), Circle(1), 7.141),
                      BaseCase(Rectangle(2, 2), Square(1), 5),
                      BaseCase(Rectangle(2, 2), Triangle(3, 4, 5), 10),
                      BaseCase(Triangle(3, 4, 5), Triangle(3, 4, 5), 12),
                      BaseCase(Triangle(3, 4, 5), Circle(1), 9.141),
                      BaseCase(Triangle(3, 4, 5), Square(1), 7),
                      BaseCase(Triangle(3, 4, 5), Rectangle(2, 2), 10),
                      )


class BaseCaseError(NamedTuple):
    object_to_add: Figure
    added_object: Any


cases_for_add_area_error = (BaseCaseError(Circle(1), None),
                            BaseCaseError(Square(1), None),
                            BaseCaseError(Rectangle(1, 1), None),
                            BaseCaseError(Triangle(1, 1, 1), None),
                            )
