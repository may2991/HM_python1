# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().



def int_func(word_user):
    return chr(ord(word_user[0]) - 32) + word_user[1:]


def check_word (word_user):
    """Функция проверки введенных данных"""
    for el in word_user:
        if 96 < ord(el) < 123:
            return False
        else:
            return True

flag = True
user_list = input("Введи строку из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем "
                  "регистре.").split()
for index, el in enumerate(user_list):
    if check_word(el):
        print("Некорректные данные")
        flag = False
        break
    user_list[index] = int_func(el)
if flag:
    print(" ".join(user_list))
