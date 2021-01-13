# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def not_int(var):
    """функция определяет целое ли число"""
    try:
        int(var)
        return False
    except ValueError:
        return True


def correct_input():
    """функция проверяет корректность введеных данных"""
    try:
        a, b = input("введите действительное положительное число x и целое отрицательное число y через пробел").split()
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

    if (float(a) <= 0) or (float(b) >= 0) or not_int(b):
        print("некорректный ввод")
        a, b = correct_input()
    return float(a), float(b)


my_func_1 = lambda a, b: a ** b


def my_func_2(a, b):
    stepen = 0
    rez = 1
    while stepen > b:
        rez /= a
        stepen -= 1
    return rez


x, y = correct_input()
print(f"Результат через оператор **: {my_func_1(x, y)}")
print(f"Результат через цикл: {my_func_2(x, y)}")
