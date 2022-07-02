import random
from functools import reduce
import names
import re

'''Напишите функцию (F): на вход список имен и целое число N; 
на выходе список длины N случайных имен из первого списка 
(могут повторяться, можно взять значения: количество имен 20,
 N = 100, рекомендуется использовать функцию random);
'''

def gen_names (a):
    list_gen = []
    while a > 0:
        list_gen.append(names.get_first_name())
        a -= 1
    return list_gen

list_names = gen_names(200)
#print(list_names)


def mixed (a, b):
    list_gen = []
    while b > 0:
        list_gen.append(random.choice(a))
        b -= 1
    return list_gen

print(mixed(list_names, 20))


'''Напишите функцию вывода самого частого имени из списка на выходе функции F;'''

def sorted_counts_names(a):
    counts = dict()
    for i in a:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return (sorted(counts.items(), reverse = True, key = lambda x: x[1])[0:1])[0]

print(sorted_counts_names(list_names))



'''Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.'''


def find_rare_upper_case(a):
    counts = dict()
    for i in a:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return (((sorted(counts.items(), reverse = False, key = lambda x: x[1])[0:1][0])[0])[0])

print(find_rare_upper_case(list_names))


'''В файле с логами  найти дату самого позднего лога (по метке времени) '''