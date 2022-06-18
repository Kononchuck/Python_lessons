#Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

items = '0'
for i in range (5):
    print(i, items)

#Пользователь в цикле вводит 10 цифр.Найти количество введенных пользователем цифр 5.

zero = []
five = 0
while True:
    numbers_1 = int(input('Введите число: '))
    if len(zero) < 9:
        zero.append(numbers_1)
        if numbers_1 == 5:
            five += 1
    else:
        print('Вы ввели цифру 5: ', five, 'раз')
        break


#Найти сумму ряда чисел от 1 от 100. Полученный результат вывести на экран.

zero = 0
for i in range (1, 101):
    zero += i
print(zero)

#Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

one = 1
for i in range (1, 11):
    one *= i
print(one)

#Вывести цифры числа на каждой строчке.

numbers_2 = 23462437
for i in str (numbers_2):
    print(i)