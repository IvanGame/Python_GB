set1 = set()
set2 = set()

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

print("Введите элементы первого множества:")
for i in range(n):
    element = int(input())
    set1.add(element)

print("Введите элементы второго множества:")
for i in range(m):
    element = int(input())
    set2.add(element)

common = set1.intersection(set2)

print("Общие элементы, встречающиеся в обоих множествах (в порядке возрастания):")
for element in sorted(common):
    print(element)
