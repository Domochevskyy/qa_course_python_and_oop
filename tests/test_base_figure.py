import pytest

from src import Figure
from tests import cases_for_add_area, cases_for_add_area_error


def test_create_base_figure_object():
    """Проверка на то, запрет создания базового класса"""

    with pytest.raises(TypeError) as error:
        figure = Figure()
    assert error.type == TypeError, 'Выбросилось исключение не TypeError'


@pytest.mark.parametrize(argnames=('object_to_add', 'added_object', 'expected'),
                         argvalues=cases_for_add_area,
                         )
def test_add_area(object_to_add, added_object, expected):
    """Проверка метода .add_area()"""

    assert round(abs(object_to_add.add_area(added_object) - expected), 3) <= 0.001


@pytest.mark.parametrize(argnames=('object_to_add', 'added_object'),
                         argvalues=cases_for_add_area_error,
                         )
def test_add_area_error(object_to_add, added_object):
    """Проверка метода .add_area() на выбрасывание исключения"""

    with pytest.raises(ValueError) as error:
        object_to_add.add_area(added_object)
    assert error.type == ValueError
