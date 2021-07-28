my_list = ['-2', 'nothing', '1', 'else', '1.1', 'a', '+3', 'matters', '2.1']
num = []
alfa = []

for i in my_list:
    if i.replace('-', '').replace('.', '').replace('+', '').isdigit():
        num.append(i)
    elif i.isalpha():
        alfa.append(i)
print(' '.join(num))
print(' '.join(alfa))

###################################################################################################

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for double in my_list:
    i = list(double.split())
    print(f'Привет, {i[-1].title()}!')
