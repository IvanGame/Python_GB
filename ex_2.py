# Найти самый близкий элемент

import random

n = int(input('Введите размер массива\n'))
m = int(input('Введите число для обозначения максимально возможного значения элемента массива\n'))
x = int(input('Введите число для поиска ближайшего к нему\n'))
y = m
num = 0
pos = 0
s = []

for i in range(n):
    s.append(random.randint(1, m))
print(s)

for i in range(len(s) - 1):
    if abs(x - s[i]) < y:
        y = abs(x - s[i])
        num = s[i]
        pos = i
        print(num, pos)

print(
    f'Самое близкое число к числу {x} является {num} находится на {pos + 1} позиции в массиве')
