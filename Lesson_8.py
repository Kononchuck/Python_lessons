import os
import sys

import names
import time


import psutil

#1. Написать свой генератор последовательностей, свой тернарный оператор

N = 1000000
gen_simple = [i**2 for i in range (N+2)]
#print(gen_simple)

L = 36
check_num = ['Есть число!' for i in gen_simple if i == L]
#print(check_num)


# 2. Написать свой декоратор
# 2. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
# 3. 4. Сравнить объем оперативной памяти для функции создания генератора и
# функции создания списка с элементами: натуральные числа от 1 до 1000000.

def check_time(f):
    start_time = time.process_time()#начинаем замерять время на выполнение задач
    #print('Начало отсчета: ', start_time)
    f()
    stop_time = time.process_time()-start_time #подсчитываем время на выполнение задач
    #print('Затрачено времени на выполнение функции: ', time.process_time())
    #print('Времени занято процессом: ', stop_time)
    return stop_time

def check_memory(f):
    start_proc = psutil.Process(os.getpid())#начинаем замерять время на выполнение задач
    print('Использовано памяти до выполнения функции: ' + str(start_proc.memory_info().rss/1000000))
    f()
    stop_proc = psutil.Process(os.getpid()) #подсчитываем время на выполнение задач
    print('Использовано памяти после выполнения функции: ' + str(stop_proc.memory_info().rss/1000000))
    #print(sum_proc)
    #return sum_proc


@check_time
def simple_func_list():
    n = []
    for i in range(1000000):
        n.append(i)
    return n
print('Затрачено времени на выполнение функции: ', simple_func_list)


@check_memory
def simple_func_list():
    n = []
    for i in range(1000000):
        n.append(i)
    return n
print(simple_func_list)



gen_simple_one = [i for i in range (1000000)]
gen_simple_two = (i for i in range (1000000))

print('Memory: ', sys.getsizeof(gen_simple_one))
print('Memory: ', sys.getsizeof(gen_simple_two))

