from abc import ABC, abstractmethod


class Figure(ABC):
    __slots__ = ('_name', '_area', '_perimeter')

    def __new__(cls, *args, **kwargs):
        for i in args:
            if not isinstance(i, (int, float)) or i < 0:
                return None
        return super().__new__(cls)

    def __init__(self):
        self._name = self.__get_class_name()
        self._area = self._calculate_area()
        self._perimeter = self._calculate_perimeter()

    def __get_class_name(self):
        # Какой-то супер костыль,
        # хорошего решения определить для объекта его _name
        # я не нашел.
        return str(self.__class__).split('.')[-1].split('\'')[0]

    def add_area(self, figure):
        if not isinstance(figure, Figure) or not hasattr(figure, '_area'):
            raise ValueError('Передан не экземпляр подкласса класса фигуры.')
        return self._area + figure._area

    @abstractmethod
    def _calculate_area(self):
        ...

    @abstractmethod
    def _calculate_perimeter(self):
        ...

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    @property
    def name(self):
        return self._name
