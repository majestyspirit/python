print('Привет!')

a = int(input('Введите число: '))

if a == 1 or a % 10 == 1 and 20 < a < 100:
    b = 'процент'
elif 1 < a < 5 or 21 < a < 25 or 31 < a < 35 or 41 < a < 45:
    b = 'процента'
else:
    b = 'процентов'

print(a, b)
