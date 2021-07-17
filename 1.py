print('Модуль перевода секунд')

duration = int(input('Введите количество секунд (0 - 603799): '))
if duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    s = duration % 60
    m = duration // 60
    print(m, 'min', s, 'sec')
elif 3600 <= duration < 86400:
    s = duration % 60
    m = (duration % 3600) // 60
    h = duration // 3600
    print(h, 'hours', m, 'min', s, 'sec')
elif 86400 <= duration < 604800:
    s = duration % 60
    m = (duration % 3600) // 60
    h = (duration % 86400) // 3600
    d = duration // 86400
    print(d, 'day', h, 'hours', m, 'min', s, 'sec')
else:
    print('Good bye')
