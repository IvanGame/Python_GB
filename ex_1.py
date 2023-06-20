def stepen(a, b):
    if (b == 0):
        return 1
    return a * stepen(a, b - 1)


a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
print(stepen(a, b))
