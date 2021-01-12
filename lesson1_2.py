sec_user = int(input("введи секунды"))
sec = sec_user % 60
min = (sec_user % 3600) // 60
h = (sec_user % (3600 * 24)) // 3600
if h > 9:
    if min > 9:
        if sec > 9:
            print(f"{h}:{min}:{sec}")
        else:
            print(f"{h}:{min}:0{sec}")
    elif sec > 9:
        print(f"{h}:0{min}:{sec}")
    else:
        print(f"{h}:0{min}:0{sec}")
elif min > 9:
    if sec > 9:
        print(f"0{h}:{min}:{sec}")
    else:
        print(f"0{h}:{min}:0{sec}")
elif sec > 9:
        print(f"0{h}:0{min}:{sec}")
else:
        print(f"0{h}:0{min}:0{sec}")






