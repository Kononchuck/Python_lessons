"""Реализовать собственный класс с использованием магических методов (не менее
10-ти). Можно использовать собственный класс из вебинара 10.
"""


class Man:
    def __init__(self, name, surname, age, weight, height, country):
        self.name = str(name)
        self.surname = str(surname)
        self.age = int(age)
        self.weight = int(weight)
        self.height = int(height)
        self.country = country
        self.__all = name, surname, age, weight, height, country

    # method 1
    def __repr__(self):
        return f"{self.__class__}: {self.name, self.surname, self.age, self.weight, self.height, self.country, self.__all}"

    # method 2
    def __str__(self):
        return f"{self.name, self.surname, self.age, self.weight, self.height, self.country, self.__all}"

    # method 3
    def __len__(self):
        return len(self.__all)

    # method 4
    def __abs__(self):
        return f"Body mass index: {(self.weight/((self.height/100)**2))}"

    # method 5
    def __del__(self):
        print('Delete: ' + str(self))

    # method 6
    def __add__(self, other):
        return Man(self.name, self.surname, self.age, self.weight, self.height, self.country
                   + other)

    # method 7
    # def __int__(self):

    # method 8
    # def __copy__(self):

    # method 9
    # def __delete__(self, instance):

    # method 10
    # def __instancecheck__(self, instance):



man_1 = Man('Den', 'Popov', 35, 97, 190, 'Russia')
man_2 = Man('Nikolay', 'Ivanov', 25, 87, 179, 'Russia')


print(len(man_1))
print(man_1)
print(abs(man_1))
print(man_1+' forever')

