"""Реализовать собственный класс с использованием магических методов (не менее
10-ти). Можно использовать собственный класс из вебинара 10.
"""


class Man:

    min_age = 16
    max_age = 65
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
        return f"Индекс массы тела: {(self.weight/((self.height/100)**2))}"

    # method 5
    def __del__(self):
        print('Delete: ' + str(self))

    # method 6
    def __add__(self, other):
        return Man(self.name, self.surname, self.age, self.weight, self.height, self.country
                   + other)

    # method 7
    def __getitem__(self, index):
        return f"Вы выбрали: {self.__all[index]}"

    # method 8
    def __eq__(self, obj):
        if isinstance(obj, Man):
            if self.age == obj.age:
                return f"Возраст эквивалентен"
            else:
                return f"Возраст не эквивалентен"

    # method 9
    def __gt__(self, obj):
        if isinstance(obj, Man):
            if self.weight > obj.weight:
                return f"Вес больше сравниваемого"
            else:
                return f"Вес меньше сравниваемого"

    # method 10
    def __ne__(self, obj):
        if isinstance(obj, Man):
            if self.height != obj.height:
                return f"Рост эквивалентен"
            else:
                return f"Рост не эквивалентен"

    @classmethod
    def validator(cls, age):
        return cls.min_age < age < cls.max_age

    @staticmethod
    def check_bmi(weight, height):
        return f"Проверка ИМТ: {weight/((height/100)**2)}"



man_1 = Man('Den', 'Popov', 25, 97, 190, 'Russia')
man_2 = Man('Nikolay', 'Ivanov', 25, 87, 179, 'Russia')


print(len(man_1))
print(man_1)
print(abs(man_1))
print(man_1+' forever')
print(Man.validator(30))
print(Man.check_bmi(97, 190))
print(man_1[1])
print(man_1==man_2)
print(man_1>man_2)
print(man_1!=man_2)