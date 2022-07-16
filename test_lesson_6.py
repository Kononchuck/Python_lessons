#new file for pullrequest

import random

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


"""Придумайте 2 теста к грязной функции. Примером грязной функции является функция F из дз 4;"""


list_names = ['Jeffery', 'June', 'Christopher', 'Bryan', 'Robert', 'Harold', 'Doreen', 'John', 'Eric', 'Elmer', 'Brooke', 'Ann', 'Althea', 'George', 'Donna', 'Carlton', 'Michelle', 'Hazel', 'Jerry', 'Laura', 'Edward', 'Jeffrey', 'Roy', 'Mark', 'Harold', 'Richard', 'Tony', 'John', 'Robert', 'Ethel', 'Linda', 'John', 'Dorothy', 'Robert', 'Alfred', 'Jamie', 'Tiffany', 'Shawn', 'Danielle', 'Willie', 'Blanca', 'Anthony', 'William', 'William', 'Viola', 'Harold', 'Judy', 'Eric', 'Don', 'Ronald', 'Daniel', 'Cynthia', 'Jena', 'Betty', 'Kelley', 'Jamie', 'Richard', 'Jennifer', 'Rolando', 'Edna', 'Zoraida', 'Billy', 'Rachel', 'Sean', 'Mark', 'Lydia', 'Melba', 'Angela', 'Clarence', 'Margaret', 'Sally', 'William', 'Dale', 'Anthony', 'Ciara', 'Shirley', 'Travis', 'Lee', 'Joseph', 'Vickie', 'Edwin', 'Richard', 'Toni', 'Hilda', 'Roy', 'James', 'Manuel', 'Richard', 'Cecelia', 'Michael', 'Peggy', 'Sean', 'Edward', 'Walter', 'Anthony', 'Stanford', 'Dustin', 'Joseph', 'Gregory', 'Donald', 'Peter', 'Ernest', 'Jennifer', 'Mary', 'Joshua', 'Joshua', 'Frank', 'Casey', 'David', 'Wendy', 'Charity', 'Sharon', 'Harry', 'Karmen', 'Gary', 'Tracey', 'Larissa', 'Julie', 'Gary', 'Ray', 'Eric', 'Linda', 'Willie', 'Amy', 'Philip', 'Wilfred', 'Teresa', 'Gerard', 'Annie', 'Diana', 'William', 'Monique', 'Anna', 'John', 'Dawn', 'Howard', 'Steven', 'David', 'Justin', 'Christopher', 'Christine', 'Theresa', 'Dovie', 'Patricia', 'Gary', 'Randy', 'Sherry', 'Thelma', 'Alfred', 'Richard', 'Michelle', 'Olga', 'Sheron', 'James', 'Alvin', 'Nora', 'Kenneth', 'Richard', 'Frank', 'Carmen', 'Quinton', 'Kimberly', 'Ann', 'Douglas', 'Matt', 'William', 'Matthew', 'John', 'Lula', 'Humberto', 'Dale', 'James', 'Lyndon', 'Joe', 'Diana', 'Whitney', 'Robert', 'Lindsay', 'Garry', 'Rodney', 'Juan', 'Thomas', 'Jeanine', 'Clara', 'Miranda', 'Stephen', 'Tracy', 'Kathryn', 'Anthony', 'Basil', 'Carol', 'Robert', 'Debra', 'Kenneth', 'Benjamin', 'Kimberly', 'Robert', 'Bud', 'Sook', 'George']

def mixed (a, b):
    list_gen = []
    while b > 0:
        list_gen.append(random.choice(a))
        b -= 1
    return list_gen

def sorted_counts_names(a):
    counts = dict()
    for i in a:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return (sorted(counts.items(), reverse = True, key = lambda x: x[1])[0:1])[0][0]




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

def test_6_mixed():
    assert len(mixed(list_names, 20)) <=20

def test_7_sorted_counts_names():
    assert sorted_counts_names(list_names) == 'Robert'



"""4. В качестве ответа на дз пришлите ссылку на ветку с тестами или ссылку на

PullRequest ветки с тестами с веткой master.
"""
#https://github.com/Kononchuck/Python_lessons/branches


