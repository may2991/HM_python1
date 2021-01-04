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

def find_lesson (list_1_lesson):
    '''функция ищет в списке количество пар и суммирует их общеее количество'''
    num_lesson = 0
    for  el in list_1_lesson:
        if el.find("(лаб)") > -1:
            num_lesson += int(el[0:el.find("(лаб)")])
        if el.find("(л)") > -1:
            num_lesson += int(el[0:el.find("(л)")])
        if el.find("(пр)") > -1:
            num_lesson += int(el[0:el.find("(пр)")])
    return num_lesson


def find_key (list_1_lesson):
    ''' функция ищет в списке название предметов, если название составное - склеивает название в одну строку'''
    key = ""
    for  index, el in enumerate(list_1_lesson):
        if el.find(":") > -1:
            if index == 0:
                key = el[0:el.find(":")]
            else:
                for part_of_lesson in range(index):
                    key = key + list_1_lesson[part_of_lesson] + " "
                key = key + el[0:el.find(":")]
    return key


my_dict ={}
with open("for_6.txt", "r") as f_1:
        content = f_1.readlines()
        for str in content:
            buf_list = str.split()
            my_dict.update({find_key(buf_list): find_lesson(buf_list)})
print(my_dict)