def num_translate(n):
    num_e_r = {'zero': 'ноль',
               'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'
               }
    print(num_e_r.get(n))


num_translate(n=input('напишите число на английском: '))
