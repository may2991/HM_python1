# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, введя переключение цветов в отдельном потоке (С помощью класса Threads)
# и реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
# Подсказка: Подтверждения переключение можно показать вызовом print(self.color) через заданные промежутки времени для каждого цвета.

from time import monotonic
from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self, start):
        color = ["red", "yelow", "green"]
        color_of_trafficlight = cycle(color)
        while True:
            self.__color = next(color_of_trafficlight)
            print(self.__color, monotonic() - start)
            sleep(7)
            self.__color = next(color_of_trafficlight)
            print(self.__color, monotonic() - start)
            sleep(2)
            self.__color = next(color_of_trafficlight)
            print(self.__color, monotonic() - start)
            sleep(6)

a = TrafficLight()
a.running(monotonic())
