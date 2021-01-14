# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    weight_ed = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def rashet(self):
        print(f"масса асфальта, необходимого для покрытия всего дорожного полотна"
              f" {self._length * self._width * self.weight_ed * self.thickness / 1000} т")


def correct_input():
    """функция проверяет корректность введеных данных"""
    try:
        a, b = input("введите длину и ширину дороги в метрах через пробел").split()
    except ValueError:
        print("некорректный ввод")
        a, b = correct_input()
    except TypeError:
        print("некорректный ввод")
        a, b = correct_input()

    try:
        float(a)
        float(b)
    except ValueError:
        print("некорректный ввод")
        a, b = correct_input()

    if (float(a) <= 0) or (float(b) <= 0):
        print("некорректный ввод")
        a, b = correct_input()
    return float(a), float(b)

l, w = correct_input()
a = Road(l, w)
a.rashet()
