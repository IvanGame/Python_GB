def fill_arithmetic_progression():
    a1 = int(
        input("Введите первый элемент прогрессии: "))
    d = int(input("Введите разность прогрессии: "))
    n = int(input("Введите количество элементов: "))

    progression = []

    for i in range(n):
        element = a1 + i * d
        progression.append(element)

    return progression


result = fill_arithmetic_progression()
print("Арифметическая прогрессия:", result)
