n = int(input("введите целое положительное число"))
m = n % 10
p = 0
while (n // (10 ** p)) > 9:
    p = p + 1
while n > 10:
    if n // (10 ** p) > m:
        m = n // (10 ** p)
    n = n % (10 ** p)
    p = p - 1
print(m)


