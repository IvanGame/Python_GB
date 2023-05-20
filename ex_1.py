# Найдите сумму цифр трехзначного числа

number = int(input("Введите трехзначное число: "))
first_number = number
sum = 0
while number != 0:
    sum += number % 10
    number //= 10
print(f"Сумма цифр числа {first_number}: {sum}")
