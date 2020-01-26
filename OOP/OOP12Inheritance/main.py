#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        pass
    pass


class HeroIntelligent(Hero):
    pass


class HeroStrength(Hero):
    pass


adam = Hero('Adam', 100)
arthur = HeroIntelligent('Arthur', 100)
mbahputih = HeroIntelligent('Mbah Putih', 100)

print('\n')
print(copyright)
