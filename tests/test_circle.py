import pytest

from src import Circle
from tests import (circle_creating_cases,
                   circle_perimeter_cases,
                   circle_area_cases,
                   )


@pytest.mark.parametrize(argnames=('radius', 'expected'),
                         argvalues=circle_creating_cases,
                         )
def test_circle_create(radius, expected):
    """Проверка создания объекта окружности"""

    assert Circle(radius) == expected


def test_circle_name():
    """Проверка атрибута у валидного объекта окружности"""

    assert Circle(2).name == 'Circle'


def test_circle_name_error():
    """Проверка атрибута у невалидного объекта окружности"""

    assert not hasattr(Circle(-3), 'name')


@pytest.mark.parametrize(argnames=('radius', 'expected'),
                         argvalues=circle_perimeter_cases,
                         )
def test_circle_perimeter(radius, expected):
    """Проверка вычисления периметра окружности"""

    assert abs(Circle(radius).perimeter - expected) <= 0.001


@pytest.mark.parametrize(argnames=('radius', 'expected'),
                         argvalues=circle_area_cases,
                         )
def test_circle_area(radius, expected):
    """Проверка вычисления площади треугольника"""

    assert round(abs(Circle(radius).area - expected), 3) <= 0.001
