# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def find_lesson (str_lesson):
    '''функция ищет в списке количество пар и суммирует их общеее количество'''
    num_lesson = 0
    list_1_lesson = str_lesson.split()
    for  el in list_1_lesson:
        if el.find("(лаб)") > -1:
            num_lesson += int(el[0:el.find("(лаб)")])
        if el.find("(л)") > -1:
            num_lesson += int(el[0:el.find("(л)")])
        if el.find("(пр)") > -1:
            num_lesson += int(el[0:el.find("(пр)")])
    return num_lesson


my_dict ={}
with open("for_6.txt", "r") as f_1:
        content = f_1.readlines()
        for str in content:
            buf_list = str.split(":")
            my_dict.update({buf_list[0]: find_lesson(buf_list[1])})
print(my_dict)