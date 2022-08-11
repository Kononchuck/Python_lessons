import random

import pytest
from Lesson_9 import Durak

class testDurak:
    def setup(self):
        pass

    def teardown(self):
        pass

def test_N_2():
    assert Durak(2).num_players == 2
#
# def test_N_4():
#     assert Durak(4).num_players == 2




"""1. Написать не менее 3-х тестов к собственному классу из вебинара 9 с помощью

библиотеки pytest;"""




"""2. Написать не менее 3-х тестов к собственному классу из вебинара 9 с помощью

библиотеки unittest."""