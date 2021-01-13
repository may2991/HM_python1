# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


dict_replace = dict(One='Один', Two='Два', Three="Три", Four ='Четыре')
with open("for_4_old.txt", "r") as f_old, open("for_4_new.txt", "w") as f_new:
    content = f_old.readlines()
    print(content)
    for str in content:
        list_buf = str.split()
        list_buf[0] = dict_replace.get(list_buf[0])
        str_buf = " ".join(list_buf)
        f_new.writelines(str_buf + "\n")
        print(list_buf)
        
