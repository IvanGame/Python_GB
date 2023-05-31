# Петя и Катя

sum = int(input("Введите сумму чисел"))
mult = int(input("Введите произведение чисел"))

for i in range(sum):
    for j in range(mult):
        if i + j == sum and i * j == mult:
            num_1 = i
            num_2 = j
print(f"Первое число - {num_1}, второе число - {num_2}")
