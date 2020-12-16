vir = float(input("введи выручку"))
izd = float(input("введи издержки"))
if vir < izd:
    print("УБЫТОК!")
else:
    print("рентабельность:", ((vir - izd) / vir) * 100, "%")
    sotr = int(input("введи количество сотрдуников"))
    print("прибыль на сотрудника:", (vir - izd) / sotr)