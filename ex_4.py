# Разлом шоколадки

n = int(input("Введите ширину плитки шоколада: "))
m = int(input("Введите высоту плитки шоколада: "))
x = int(input("Введите колличтсво долек, которые желаете отломить: "))

if x < n * m and ((x % n == 0) or (x % m == 0)):
    print("Такое возможно")
else:
    print("Такое невозвожно")
