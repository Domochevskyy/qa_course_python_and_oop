import pytest

from src import Square
from tests import (square_creating_cases,
                   square_perimeter_cases,
                   square_area_cases,
                   )


@pytest.mark.parametrize(argnames=('side', 'expected'),
                         argvalues=square_creating_cases,
                         )
def test_square_create(side, expected):
    """Проверка создания объекта квадрата"""

    assert Square(side) == expected


def test_square_name():
    """Проверка атрибута у валидного объекта квадрата"""

    assert Square(1).name == 'Square'


def test_square_name_error():
    """Проверка атрибута у невалидного объекта квадрата"""

    assert not hasattr(Square(-1), 'name')


@pytest.mark.parametrize(argnames=('side', 'expected'),
                         argvalues=square_perimeter_cases,
                         )
def test_square_perimeter(side, expected):
    """Проверка вычисления периметра квадрата"""

    assert Square(side).perimeter == expected


@pytest.mark.parametrize(argnames=('side', 'expected'),
                         argvalues=square_area_cases,
                         )
def test_square_area(side, expected):
    """Проверка вычисления площади прямоугольника"""

    assert Square(side).area == expected
