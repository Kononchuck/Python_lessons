import names
import time

#1. Написать свой генератор последовательностей, свой тернарный оператор
# def gen_names (a):
#     list_gen = []
#     while a > 0:
#         list_gen.append(names.get_first_name())
#         a -= 1
#     return list_gen
#
# list_names = gen_names(200)
# #print(list_names)

N = 100
gen_simple = [i**2 for i in range (N+2)]
print(gen_simple)

L = 36
check_num = ['Есть число!' for i in gen_simple if i == L]
print(check_num)


#2. Написать свой декоратор


def simple_func():
    print('Hi')

def check_time():
    start_time = time.process_time()#начинаем замерять время на выполнение задач
    simple_func()
    check_num
    stop_time = time.process_time() - start_time#подсчитываем время на выполнение задач
    return stop_time


print(check_time())
