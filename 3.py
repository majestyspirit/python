tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Mary', 'Nick', 'Jack'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9Д'
]

while len(tutors) > len(klasses):
    klasses.append('None')
    continue


def children(n):
    return ((tutors[i], klasses[i]) if len(tutors) >= n else exit(print('нету столько детей')) for i in range(0, n))


num = children(int(input('введите кол-во детей: ')))

print(type(num))

for a in num:
    print(a)
