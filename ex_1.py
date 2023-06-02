# Сколько раз встерчается число
import random

n = int(input('Введите размер массива'))
m = int(input('Введите число для обозначения максимально возможного значения элемента массива'))
x = int(input('Введите число для поиска'))
count = 0
s = []

for i in range(n):
    s.append(random.randint(1, m))
print(s)

for i in s:
    if i == x:
        count += 1
print(
    f'число {x} встречается в массиве {count} раз')
