"""1. Выберете дз, к функциям которого будете писать тесты;"""

# домашние задания 4 и 5

"""2. Создайте дополнительную ветку в репозитории GitHub с тестами;"""

# https://github.com/Kononchuck/Python_lessons/branches

"""3. Напишите не менее 5-ти тестов к функциям выбранного урока;"""


fib_num = lambda n: fib_num(n-1) + fib_num(n-2) if n > 2 else 1

def divisor_all(n):
    del_list_all = []
    for i in range(1, 1001):
        if n % i == 0:
            del_list_all.append(i)
        else:
            pass
    return del_list_all


def between (n):
    if n > 0 and n < 1001:
        return True

def simple_list(n):
    del_list_simple = []
    del_list_all = [1, 3, 7, 21, 37, 111, 259, 777]
    for i in del_list_all:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            del_list_simple.append(i)
    return del_list_simple


def divisor(n):
    del_list_simple = [3, 7, 37]
    list = []
    for i in del_list_simple:
        while i <= n:
            if n % i == 0:
                list.append(i)
                n //= i
            else:
                i += 1
        return list



def test_1_fib_num():
    assert fib_num(6) == 8

def test_2_between():
    assert between(777) == True

def test_3_divisor():
    assert divisor_all(777) == [1, 3, 7, 21, 37, 111, 259, 777]

def test_4_simple_list():
    assert simple_list(777) == [1, 3, 7, 37]

def test_5_divisor():
    assert divisor(777) == [3, 7, 37]



"""4. В качестве ответа на дз пришлите ссылку на ветку с тестами или ссылку на

PullRequest ветки с тестами с веткой master.
"""
#https://github.com/Kononchuck/Python_lessons/branches


