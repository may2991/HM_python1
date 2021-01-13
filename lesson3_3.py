# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(var_1, var_2, var_3):
    if var_1 > var_2:
        if var_2 > var_3:
            summa = var_1 + var_2
        else:
            summa = var_1 + var_3
    elif var_1 > var_3:
        summa = var_1 + var_2
    else:
        summa = var_2 + var_3
    return summa


a, b, c = (input("введи 3 числа через пробел").split())
print("сумма двух наибольших аргументов", my_func(int(a), int(b), int(c)))
