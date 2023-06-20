def check_rhythm(poem):
    lines = poem.split()

    # Получаем число слогов для первой фразы
    first_line_syllables = count_syllables(lines[0])

    # Проверяем число слогов для остальных фраз
    for line in lines[1:]:
        if count_syllables(line) != first_line_syllables:
            return "Пам парам"

    return "Парам пам-пам"


def count_syllables(line):
    words = line.split("-")
    syllables = 0

    for word in words:
        syllables += count_vowels(word)

    return syllables


def count_vowels(word):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0

    for char in word:
        if char in vowels:
            count += 1

    return count


# Ввод стихотворения Винни-Пуха
poem = input("Введите стихотворение: ")

result = check_rhythm(poem)
print(result)
