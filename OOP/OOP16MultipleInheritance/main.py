#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Team:
    def set_team(self, team):
        self.team = team
        pass

    def show_team(self):
        print(self.team)
        pass
    pass


class TipeHero:
    def set_tipe(self, tipe):
        self.tipe = tipe
        pass

    def show_tipe(self):
        print(self.tipe)
        pass
    pass

class Hero(Team, TipeHero):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        pass


adam = Hero('Adam Arthur Faizal', 100)
adam.set_team('Biru')
adam.set_tipe('Forward')

adam.show_team()
adam.show_tipe()

print('\n')
print(copyright)
