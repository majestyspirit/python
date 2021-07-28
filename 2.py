my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

a = id(my_list)

for i in my_list:
    if i.replace('+', '').isdigit():
        if len(i) == 1:
            print(f'"{i:>02}"', end=' ')
        elif i[0] != '+':
            print(f'"{i}"', end=' ')
        elif i[0] == '+':
            print(f'"+{int(i):>02}"', end=' ')
    elif i != my_list[-1]:
        print(i, end=' ')
    else:
        print(i)

b = id(my_list)

print('решено in_place') if a == b else print('решено не верно')
