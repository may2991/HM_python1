# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

def profit (list_of_firm):
    if int(list_of_firm[2]) - int(list_of_firm[3]) > 0:
        return int(list_of_firm[2]) - int(list_of_firm[3])


dict_profit_firm = {}

with open("for_7.txt", "r") as f_1, open("for_7.json", "w") as f_2:
    content = f_1.readlines()
    print(content)
    num_profit_firm = 0
    sum_profit_firm = 0
    for el in content:
        if profit(el.split()):
            dict_profit_firm.update({el.split()[0]: profit(el.split())})
            sum_profit_firm += profit(el.split())
            num_profit_firm += 1
    print(sum_profit_firm / num_profit_firm)
    print(dict_profit_firm)
    list_profit = [dict_profit_firm, {"average_profit": sum_profit_firm / num_profit_firm}]
    print(list_profit)
    json.dump(list_profit, f_2)