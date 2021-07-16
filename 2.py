numbers = []                                        # создать пустой список

for number in range(1, 1000, 2):
    numbers.append(number ** 3)                     # определить числа в список
print('Список кубов нечетных чисел 1-1000:')
print(numbers)

numbers_sum = []
all_sum = 0
all_17 = 0                                          # будущие переменные

for element in numbers:
    summa = 0
    while element > 0:
        num = element % 10                          # 1) откидываем последнюю цифру
        summa += num                                # 2) прибавляем её
        element = element // 10                     # 3) уменьшаем порядок
    else:
        numbers_sum.append(summa)

for i in numbers_sum:
    if i % 7 == 0:
        all_sum += i
    elif (i + 17) % 7 == 0:
        all_17 += i

print('Сумма чисел кратных 7ми:')
print(all_sum)

print('Сумма чисел +17 к каждому кратных 7ми:')
print(all_17)
