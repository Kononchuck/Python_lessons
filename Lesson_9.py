import random

class Durak:
    def __init__(self, N):
        self.random = random.Random()
        self.num_players = int(N)

    def cards(self):
        nominal = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        mast = ['ЧЕРВИ', 'БУБИ', 'КРЕСТИ', 'ПИКИ']
        coloda = [(x, y) for x in nominal for y in mast]
        cards_list = []
        global kozyr
        while self.num_players > 0:
            mix = random.sample(coloda, 6)
            cards_list.append(mix)
            self.num_players-=1
            coloda = [x for x in coloda if x not in mix]
            kozyr = random.sample(coloda, 1)
        return cards_list

    def players(self):
        num = int()
        for i in self.cards():
            num+=1
            print('Раздача карт игроку', num, ':', i)
        print('Козырная карта:', kozyr)


if __name__ == '__main__':
    print(Durak(2).players())