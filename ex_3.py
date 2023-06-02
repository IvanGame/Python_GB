# Scrabble

point_1 = 'АВЕИНОРСТAEIOULNSTR'
point_2 = 'ДКЛМПУDG'
point_3 = 'БГЁЬЯBCMP'
point_4 = 'ЙЫFHVWY'
point_5 = 'ЖЗХЦЧK'
point_8 = 'ШЭЮJX'
point_10 = 'ФЩЪQZ'

count = 0

word = input('Введите слово для подсчёта очков(на Английском или Русском)\n')
word = word.upper()

for i in word:
    if i in point_1:
        count += 1
    if i in point_2:
        count += 2
    if i in point_3:
        count += 3
    if i in point_4:
        count += 4
    if i in point_5:
        count += 5
    if i in point_8:
        count += 8
    if i in point_10:
        count += 10
print(count)