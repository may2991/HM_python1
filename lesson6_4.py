# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = None

    def go(self):
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name} stop')

    def turn(self, direction):
        print(f'{self.name} turn {direction}')

    def show_speed(self):
        print(f"{self.name}'s speed: {self.speed} km/h")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        if self.speed < 60:
            print(f"{self.name}'s speed: {self.speed} km/h")
        else:
            print(f"OVER SPEED!!! {self.name}'s speed: {self.speed} km/h")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        if self.speed < 40:
            print(f"{self.name}'s speed: {self.speed} km/h")
        else:
            print(f"OVER SPEED!!! {self.name}'s speed: {self.speed} km/h")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


a = TownCar(50, "red", "Volvo")
b = SportCar(50, "blue", "VW")
c = WorkCar(30, "pink", "BMW")
d = PoliceCar(100, "brown", "SAAB")
e = WorkCar(80, "green", "Fiat")
f = TownCar(70, "red", "Mersedes")
print(a.speed)
print(b.color)
print(c.name)
print(d.is_police)
print(e.is_police)
a.go()
b.stop()
c.turn('left')
f.turn('right')
a.show_speed()
e.show_speed()
d.show_speed()
f.show_speed()

