import pytest

from src import Triangle
from tests import (triangle_creating_cases,
                   triangle_area_calculation_cases,
                   triangle_perimeter_calculation_cases,
                   )


@pytest.mark.parametrize(argnames=('parameters', 'expected'),
                         argvalues=triangle_creating_cases,
                         )
def test_triangle_create(parameters, expected):
    """Проверка создания объекта треугольника"""

    assert Triangle(*parameters) == expected


def test_triangle_name():
    """Проверка атрибута у валидного объекта треугольника"""

    assert Triangle(3, 4, 5).name == 'Triangle'


def test_triangle_name_error():
    """Проверка атрибута у невалидного объекта треугольника"""

    assert not hasattr(Triangle(3, 4, 8), 'name')


@pytest.mark.parametrize(('parameters', 'expected'),
                         triangle_perimeter_calculation_cases,
                         )
def test_perimeter(parameters, expected):
    """Проверка вычисления периметра треугольника"""

    assert Triangle(*parameters).perimeter == expected


@pytest.mark.parametrize(('parameters', 'expected'),
                         triangle_area_calculation_cases,
                         )
def test_area(parameters, expected):
    """Проверка вычисления периметра треугольника"""

    assert Triangle(*parameters).area == expected
