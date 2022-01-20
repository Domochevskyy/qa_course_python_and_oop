import pytest

from src import Rectangle
from tests import (rectangle_creating_cases,
                   rectangle_perimeter_cases,
                   rectangle_area_cases,
                   )


@pytest.mark.parametrize(argnames=('parameters', 'expected'),
                         argvalues=rectangle_creating_cases,
                         )
def test_rectangle_create(parameters, expected):
    """Проверка создания объекта прямоугольника"""

    assert Rectangle(*parameters) == expected


def test_rectangle_name():
    """Проверка атрибута у валидного объекта прямоугольника"""

    assert Rectangle(1, 2).name == 'Rectangle'


def test_rectangle_name_error():
    """Проверка атрибута у невалидного объекта прямоугольника"""

    assert not hasattr(Rectangle(-1, 2), 'name')


@pytest.mark.parametrize(argnames=('parameters', 'expected'),
                         argvalues=rectangle_perimeter_cases,
                         )
def test_rectangle_perimeter(parameters, expected):
    """Проверка вычисления периметра прямоугольника"""

    assert Rectangle(*parameters).perimeter == expected


@pytest.mark.parametrize(argnames=('parameters', 'expected'),
                         argvalues=rectangle_area_cases,
                         )
def test_rectangle_area(parameters, expected):
    """Проверка вычисления площади прямоугольника"""

    assert Rectangle(*parameters).area == expected
