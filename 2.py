# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

string = input("Введи элементы списка через пробел")
test_list = string.split()
for index, var in enumerate(test_list):
    if index % 2:
        test_list[index],  test_list[index - 1] = test_list[index - 1],  test_list[index]
print(test_list)
