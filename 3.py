import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_joke(n, double=False):
    """""
    Функция подбора шуток
    :параметр n: количество шуток
    :параметр :double дублирующиеся или нет

    """
    first = nouns.copy()
    second = adverbs.copy()
    third = adjectives.copy()
    jokes = []
    len_min = min(first, second, third)

    while n and len(len_min):
        num = random.randrange(len(len_min))
        if double:
            jokes.append(f'{first.pop(num)} {second.pop(num)} {third.pop(num)}')
        else:
            jokes.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
        n -= 1
    return jokes


print(get_joke(7, False))
