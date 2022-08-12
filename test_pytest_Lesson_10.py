import random
import unittest
import pytest
from Lesson_9 import Durak
from collections.abc import Iterable


"""1. Написать не менее 5 тестов к собственному классу из вебинара 9 с помощью

библиотеки pytest;"""


def test_pytest_1():
    assert Durak(2).num_players == 2

def test_pytest_2():
    assert Durak(1).coloda() == [('6', 'ЧЕРВИ'), ('6', 'БУБИ'), ('6', 'КРЕСТИ'), ('6', 'ПИКИ'), ('7', 'ЧЕРВИ'), ('7', 'БУБИ'), ('7', 'КРЕСТИ'), ('7', 'ПИКИ'), ('8', 'ЧЕРВИ'), ('8', 'БУБИ'), ('8', 'КРЕСТИ'), ('8', 'ПИКИ'), ('9', 'ЧЕРВИ'), ('9', 'БУБИ'), ('9', 'КРЕСТИ'), ('9', 'ПИКИ'), ('10', 'ЧЕРВИ'), ('10', 'БУБИ'), ('10', 'КРЕСТИ'), ('10', 'ПИКИ'), ('J', 'ЧЕРВИ'), ('J', 'БУБИ'), ('J', 'КРЕСТИ'), ('J', 'ПИКИ'), ('Q', 'ЧЕРВИ'), ('Q', 'БУБИ'), ('Q', 'КРЕСТИ'), ('Q', 'ПИКИ'), ('K', 'ЧЕРВИ'), ('K', 'БУБИ'), ('K', 'КРЕСТИ'), ('K', 'ПИКИ'), ('A', 'ЧЕРВИ'), ('A', 'БУБИ'), ('A', 'КРЕСТИ'), ('A', 'ПИКИ')]

def test_pytest_3():
    assert len(Durak(1).coloda()) == 36

def test_pytest_4():
    assert type (Durak(1).coloda()) is not int

def test_pytest_5():
    assert ('6', 'КРЕСТИ') in Durak(1).coloda()

def test_pytest_6():
    assert isinstance(Durak(1).coloda(), Iterable)


"""2. Написать не менее 5 тестов к собственному классу из вебинара 9 с помощью

библиотеки unittest."""


class DurakUnitTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Durak(2).num_players, 2)

    def test_2(self):
        self.assertEqual(Durak(1).coloda(), [('6', 'ЧЕРВИ'), ('6', 'БУБИ'), ('6', 'КРЕСТИ'), ('6', 'ПИКИ'), ('7', 'ЧЕРВИ'), ('7', 'БУБИ'),
                                             ('7', 'КРЕСТИ'), ('7', 'ПИКИ'), ('8', 'ЧЕРВИ'), ('8', 'БУБИ'), ('8', 'КРЕСТИ'), ('8', 'ПИКИ'),
                                             ('9', 'ЧЕРВИ'), ('9', 'БУБИ'), ('9', 'КРЕСТИ'), ('9', 'ПИКИ'), ('10', 'ЧЕРВИ'), ('10', 'БУБИ'),
                                             ('10', 'КРЕСТИ'), ('10', 'ПИКИ'), ('J', 'ЧЕРВИ'), ('J', 'БУБИ'), ('J', 'КРЕСТИ'), ('J', 'ПИКИ'),
                                             ('Q', 'ЧЕРВИ'), ('Q', 'БУБИ'), ('Q', 'КРЕСТИ'), ('Q', 'ПИКИ'), ('K', 'ЧЕРВИ'), ('K', 'БУБИ'),
                                             ('K', 'КРЕСТИ'), ('K', 'ПИКИ'), ('A', 'ЧЕРВИ'), ('A', 'БУБИ'), ('A', 'КРЕСТИ'), ('A', 'ПИКИ')])

    def test_3(self):
        self.assertEqual(len(Durak(1).coloda()), 36)

    def test_4(self):
        firstValue = Durak(2).num_players
        message = "Test value is none."
        self.assertIsNotNone(firstValue, message)
    def test_5(self):
        key = ('6', 'КРЕСТИ')
        container = Durak(1).coloda()
        message = "all ok!"
        self.assertIn(key, container, message)



if __name__ == '__main__':
    unittest.main()
