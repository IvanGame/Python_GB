def find_indices_in_range(lst, minimum, maximum):
    indices = []

    for i, element in enumerate(lst):
        if minimum <= element <= maximum:
            indices.append(i)

    return indices

# Пример использования
my_list = [1, 5, 3, 8, 2, 7, 6, 4, 9]
min_value = 3
max_value = 7

result = find_indices_in_range(my_list, min_value, max_value)
print("Индексы элементов в заданном диапазоне:", result)
