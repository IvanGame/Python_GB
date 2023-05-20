# Проверка на счастье

ticket = input("Введите номер билетя для проверки: ")

first_half = int(ticket[:3])
second_half = int(ticket[3:])
first_sum = 0
second_sum = 0

while first_half != 0:
    first_sum += first_half % 10
    first_half //= 10

while second_half != 0:
    second_sum += second_half % 10
    second_half //= 10

if first_sum == second_sum:
    print("БИЛЕТ СЧАСТЛИВЫЙ, ВЫ - ВЕЗУНЧИК!")
else:
    print("Увы, вам не повезло :(")