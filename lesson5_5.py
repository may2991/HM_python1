# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint
rand_list = [randint(-1000, 1000) for el in range(randint(0, 100))]

with open("for_5.txt", "w") as f_1:
    for el in rand_list:
        f_1.write(str(el) + " ")

with open("for_5.txt", "r") as f_1:
    list_of_numb = f_1.readline().split()
    sum = 0
    for el in list_of_numb:
        sum += int(el)
    print(sum)
