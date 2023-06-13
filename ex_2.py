def find_max_berries(berries):
    n = len(berries)
    max_berries = 0

    for i in range(n):
        # Вычисление суммы ягод на текущем кусте и его соседних кустах
        current_berries = berries[i] + \
            berries[(i + 1) % n] + berries[(i - 1) % n]
        max_berries = max(max_berries, current_berries)

    return max_berries


# Получение ввода от пользователя
n = int(input("Введите количество кустов на грядке: "))

berries = []
for i in range(n):
    berry_count = int(input(
        "Введите количество ягод на кусте {}: ".format(i + 1)))
    berries.append(berry_count)

# Вызов функции для решения задачи
result = find_max_berries(berries)

# Вывод результата
print("Максимальное количество ягод, которое может собрать собирающий модуль:", result)
