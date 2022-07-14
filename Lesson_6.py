"""1. Выберете дз, к функциям которого будете писать тесты;"""

# домашние задания 4 и 5

"""2. Создайте дополнительную ветку в репозитории GitHub с тестами;"""

# https://github.com/Kononchuck/Python_lessons/branches

"""3. Напишите не менее 5-ти тестов к функциям выбранного урока;"""

n = 777
del_list_all = []
del_list_simple = []

fib_num = lambda n: fib_num(n-1) + fib_num(n-2) if n > 2 else 1

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


def divisor(n):
    list = []
    for i in del_list_simple:
        while i <= n:
            if n % i ==0:
                list.append(i)
                n //= i
            else:
                i += 1
        return list


# def test_1_divisor_master():
#     assert divisor_master(777)

def test_2_fib_num():
    assert fib_num(6)==8




"""4. В качестве ответа на дз пришлите ссылку на ветку с тестами или ссылку на

PullRequest ветки с тестами с веткой master.
"""
#https://github.com/Kononchuck/Python_lessons/branches


