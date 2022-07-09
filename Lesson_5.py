from math import sqrt

'''Необходимо реализовать модуль divisor_master. Все функции модуля принимают на
вход натуральные числа от 1 до 1000. Модуль содержит функции:
1. проверка числа на простоту (простые числа - это те числа у которых делители
единица и они сами);
2. выводит список всех делителей числа;
3. выводит самый большой простой делитель числа.
'''


def divisor_master():
    n = int(input('Введите число: '))
    del_list = []
    del_list_2 = []
    if n > 0 and n < 1001:
        print('Число лежит в диапазоне от 1 до 1000')
        for i in range(1, 1001):
            if n % i == 0:
                del_list.append(i)
            else:
                pass
        print('Список всех делителей: ', del_list)
        for i in del_list:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                del_list_2.append(i)
        print('Наибольший простой делитель числа: ', sorted(del_list_2, reverse=True)[0])
    else:
        print('Число меньше 1 или больше 1000.')

divisor_master()

