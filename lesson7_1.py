# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

from random import randint


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        buf_matrix = ""
        for str1 in self.matrix:
            buf_string = ""
            for el in str1:
                buf_string += str(el) + "\t"
            buf_matrix += buf_string + "\n" + "\n"
        return buf_matrix

    def __add__(self, other):
        buf_matrix = []
        for i in range(len(other.matrix)):
            buf_string = []
            for j in range(len(other.matrix[0])):
                buf_string.append(self.matrix[i][j] + other.matrix[i][j])
            buf_matrix.append(buf_string)
        return Matrix(buf_matrix)


def create_matrix(m, n):
    """функция формирует матрицу как список списков"""
    a = list()
    for i in range(m):
        a.append([randint(-10, 10) for el in range(n)])
    return a


def correct_input():
    """функция проверяет корректность введеных данных"""
    try:
        a, b = input("введите количество строк и количество столбцов матрицы через пробел").split()
    except ValueError:
        print("некорректный ввод")
        a, b = correct_input()
    except TypeError:
        print("некорректный ввод")
        a, b = correct_input()
    try:
        int(a)
        int(b)
    except ValueError:
        print("некорректный ввод")
        a, b = correct_input()

    if (int(a) <= 0) or (int(b) <= 0):
        print("некорректный ввод")
        a, b = correct_input()
    return int(a), int(b)


m, n = correct_input()
a = Matrix(create_matrix(m, n))
b = Matrix(create_matrix(m, n))
c = a + b
print(f'A \n{a}')
print(f'B \n{b}')
print(f'C \n{c}')
