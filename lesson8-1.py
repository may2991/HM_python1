# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию (проверку на корректность) числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

from random import randint


class Date:
    def __init__(self, date):
        self.day, self.month, self.year = Date.extract_date(date)

    @classmethod
    def extract_date(cls, date):
        return date.split("-")

    @staticmethod
    def validation_date(date):
        try:
            day, month, year = date.split("-")
        except ValueError:
            print(f"дата {date} - некорректный ввод, дата должна быть формата dd-mm-yyyy")
            return False
        except TypeError:
            print(f"дата {date} - некорректный ввод, дата должна быть формата dd-mm-yyyy")
            return False
        try:
            int(day), int(month), int(year)
        except ValueError:
            print(f"дата {date} - некорректный ввод, дата должна состоять из 3х чисел")
            return False
        if int(year) < 0 or int(year) > 2078:
            print(f"введенный год - {year} - некорректен, введите год в диапазоне 0 ... 2077")
            return False
        elif int(month) <= 0 or int(month) > 12:
            print(f"введенный месяц - {month} - некорректен, введите месяц в диапазоне 1 ... 12")
            return False
        elif int(day) <= 0 or int(day) > 31:
            print(f"введенный день - {day} - некорректен, введите день в диапазоне 1 ... 31")
            return False
        elif int(day) > 30 and [2, 4, 6, 9, 11].count(int(month)):
            print(f"введенный день - {day} - некорректен, в {month} месяце меньше дней")
            return False
        elif int(month) == 2 and int(day) > 29:
            print(f"введенный день - {day} - некорректен, в {month} месяце меньше дней")
            return False
        elif int(month) == 2 and int(day) > 28 and int(year) % 4 != 0:
            print(f"введенный день - {day} - некорректен, в {month} месяце {year} года меньше дней")
            return False
        else:
            print(f"дата: {date} Ввод корретен")
            return True


list_of_incorrect_date = ["gf-22-3333", "22-3333", "11-22-3333", "11-22-2076", "29-02-1993"]
for el in list_of_incorrect_date:
    Date.validation_date(el)
list_of_objDate = list()
for i in range(20):
    date = str(randint(0, 60)) + "-" + str(randint(0, 20)) + "-" + str(randint(0, 3000))
    if Date.validation_date(date):
        list_of_objDate.append(Date(date))
print("Список корректных дат:")
for el in list_of_objDate:
    print(f"{el.day} {el.month} {el.year}")
