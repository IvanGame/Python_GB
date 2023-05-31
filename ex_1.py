# Монетки

n = int(input('Введите колличетсво монет'))

orel = 0
reshka = 0

for i in range(n):
    x = int(input())
    if x == 1:
        orel += 1
    else:
        reshka += 1
if orel >= reshka:
    print(f"Нужно перевернуть {reshka} монет")
else:
    print(f"Нужно перевернуть {orel} монет")
