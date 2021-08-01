from random import randint
numbers_list = [randint(1, 100) for i in range(1, 100)]
print(f'src = {numbers_list}')
print(f'result = {[numbers_list[i] for i in range(1, len(numbers_list)) if numbers_list[i] > numbers_list[i - 1]]}')

