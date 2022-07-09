'''
Необходимо реализовать модуль divisor_master. Все функции модуля принимают на
вход натуральные числа от 1 до 1000. Модуль содержит функции:
1. проверка числа на простоту (простые числа - это те числа у которых делители
единица и они сами);
2. выводит список всех делителей числа;
3. выводит самый большой простой делитель числа.
'''


n = int(input('Введите число: '))
del_list_all = []
del_list_simple = []


def divisor_master():
    if n > 0 and n < 1001:
        print('Число лежит в диапазоне от 1 до 1000')
        for i in range(1, 1001):
            if n % i == 0:
                del_list_all.append(i)
            else:
                pass
        print('Список всех делителей: ', del_list_all)
        for i in del_list_all:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                del_list_simple.append(i)
        print('Наибольший простой делитель числа: ', sorted(del_list_simple, reverse=True)[0])
        del_list_simple.remove(1)
    else:
        print('Число меньше 1 или больше 1000.')

divisor_master()



'''функция выводит каноническое разложение числа на простые множители'''

def diveser(n):
    list = []
    for i in del_list_simple:
        while i <= n:
            if n % i ==0:
                list.append(i)
                n //= i
            else:
                i += 1
        return list

print('Каноническое разложение числа на простые множители: ', diveser(n))



'''функция выводит самый большой делитель (не обязательно простой) числа.'''

print('Самый большой делитель (не обязательно простой) числа: ', sorted(del_list_all, reverse=True)[0])

