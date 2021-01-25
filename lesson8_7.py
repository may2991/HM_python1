# Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return f'({self.i}+{self.j}j)'

    def __add__(self, other):
        return Complex(self.i + other.i, self.j + other.j)

    def __mul__(self, other):
        return Complex(self.i * other.i - self.j * other.j, self.i * other.j + self.j * other.i)

a = Complex(1, 2)
b = Complex(3, 4)
c = 1+2j
d = 3+4j
print(a+b)
print(c+d)
print(a*b)
print(c*d)