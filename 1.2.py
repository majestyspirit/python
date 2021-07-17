print('Модуль перевода секунд')

duration = int(input('Введите количество секунд (0 - 31556926): '))

s = duration % 60
m = (duration % 3600) // 60
h = (duration % 86400) // 3600
d = (duration % 604800) // 86400
week = (duration % 2629743) // 604800
mon = (duration % 31556926) // 2629743

if duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    print(m, 'min', s, 'sec')
elif 3600 <= duration < 86400:
    print(h, 'hours', m, 'min', s, 'sec')
elif 86400 <= duration < 604800:
    print(d, 'day', h, 'hours', m, 'min', s, 'sec')
elif 604800 <= duration < 2629743:
    print(week, 'week', d, 'day', h, 'hours', m, 'min', s, 'sec')
elif 2629743 <= duration < 31556926:
    print(mon, 'month', week, 'week', d, 'day', h, 'hours', m, 'min', s, 'sec')
else:
    print('Good bye')
