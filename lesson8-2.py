# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyExceptions(Exception):

    def __init__(self, err):
        self.err = err
        if err == 2:
            print("НЕКОРРЕКТНЫЙ ВВОД! деление на ноль недопустимо")
        elif err == 1:
            print("НЕКОРРЕКТНЫЙ ВВОД! введите делимое и делитель через пробел")


def validation_date():
    user_str = input("введи делимое и делитель через пробел")
    user_list = user_str.split()
    try:
        if len(user_list) != 2:
            raise MyExceptions(1)
        elif int(user_list[1]) == 0:
            raise MyExceptions(2)
        float(user_list[0]), float(user_list[1])
    except ValueError:
        print("НЕКОРРЕКТНЫЙ ВВОД! делимое и делитель должны быть числами")
        validation_date()
    except MyExceptions:
        validation_date()
    return float(user_list[0]), float(user_list[1])


a, b = validation_date()
print(f'частное: {a / b}')
