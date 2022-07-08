from math import sqrt

'''Необходимо реализовать модуль divisor_master. Все функции модуля принимают на
вход натуральные числа от 1 до 1000. Модуль содержит функции:
1. проверка числа на простоту (простые числа - это те числа у которых делители
единица и они сами);
2. выводит список всех делителей числа;
3. выводит самый большой простой делитель числа.
'''

n = int(input('Введите число: '))
def natural_numbers():
    if n > 0 and n < 1001:
        print('Число в диапазоне от 1 до 1000')
        if n < 2:
            print('Число не простое!')
        for i in range(2, int(n ** 0.5 + 1)):
            if n % i == 0:
                print('Число не простое!')
        else:
            print('Число простое!')

    else:
        print('Число меньше 1 или больше 1000.')

print(natural_numbers())




#правильно
def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True
print(is_prime(int(input())))