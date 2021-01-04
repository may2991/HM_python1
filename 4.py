# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("for_4_old.txt", "r") as f_old, open("for_4_new.txt", "w") as f_new:
    content = f_old.readlines()
    for str in content:
        list_buf = str.split()
        if list_buf[2] == '1':
            list_buf[0] = "Один"
        elif list_buf[2] == '2':
            list_buf[0] = "Два"
        elif list_buf[2] == '3':
            list_buf[0] = "Три"
        elif list_buf[2] == '4':
            list_buf[0] = "Четыре"
        f_new.writelines(list_buf)
        f_new.writelines("\n")
        print(list_buf)

