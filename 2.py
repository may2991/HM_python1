# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def func_info(surname, name, year, city, email, tel):
    print(f"фамилия: {surname}; имя: {name}; год рождения: {year}; город: {city}; email: {email}; телефон: {tel}")


dict1 = dict(фамилия="5", имя="9", год_рождения=5, город=3, email=3, телефон=555)
for var in dict1:
    dict1.update({var: input(f"vvedi {var}")})
print(dict1)
func_info(year=dict1.get("год_рождения"), city=dict1.get("город"), name=dict1.get("имя"),
          surname=dict1.get("фамилия"), tel=dict1.get("телефон"), email=("email"))
