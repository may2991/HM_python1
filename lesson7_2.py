# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
from random import randint


class Wear(ABC):
    total_consumption = 0

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Wear):

    def __init__(self, v):
        self.v = v
        Wear.total_consumption += self.tissue_consumption()

    def tissue_consumption(self):
        return self._v / 6.5 + 0.5

    @property
    def correct_height(self):
        return self._v

    @correct_height.setter
    def v(self, v):
        if v < 100 or v > 240:
            print(f'рост {v} - некорректен, в расчете не учитывается')
            self._v = -3.25
        else:
            print(f'пальто с ростом {v} -  в расчете учитывается')
            self._v = v


class Costume(Wear):

    def __init__(self, h):
        self.h = h
        Wear.total_consumption += self.tissue_consumption(self.h)

    def tissue_consumption(self, h):
        return 2 * h + 0.3

    @property
    def correct_size(self):
        return self._h

    @correct_size.setter
    def h(self, h):
        if h < 30 or h > 70:
            print(f'размер {h} - некорректен, в расчете не учитывается')
            self._h = -0.15
        else:
            print(f'костюм с размером {h} - в расчете учитывается')
            self._h = h


a = Coat(randint(50, 290))
b = Coat(randint(50, 290))
c = Coat(randint(50, 290))
d = Coat(randint(50, 290))
e = Coat(randint(50, 290))
f = Costume(randint(0, 100))
g = Costume(randint(0, 100))
n = Costume(randint(0, 100))
h = Costume(randint(0, 100))
j = Costume(randint(0, 100))
print(f' общий расход ткани: {Wear.total_consumption:.5}')
