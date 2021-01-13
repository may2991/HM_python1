# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("for_2.txt", "r") as f_1:
    content = f_1.readlines()
    num_of_str = len(content)
    print(f"количество строк: {num_of_str}")
    for index, str in enumerate(content):
        print(f"слов в {index+1}-й строке: {len(str.split())}")
