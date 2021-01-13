# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import cycle
from sys import argv


script, num = argv
'''num - количество слов фразы'''
с = 1
for el in cycle(["карл", "у", "клары", "украл", "кораллы", "а", "клара", "у", "карла", "украла", "клорнет"]):
    if с > int(num):
        break
    print(el)
    с += 1
