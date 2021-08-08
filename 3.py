from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        assembled = zip_longest((''.join(i.split(',')) for i in users), hobby, fillvalue=None)
        my_dict = {str(n[0]).strip(): (str(n[1]).strip()) if n[0] else exit(1) for n in assembled}

        with open('assembled_list.json', 'w', encoding='utf-8') as file:
            dump(my_dict, file, ensure_ascii=False, indent=4)
            print(my_dict)
