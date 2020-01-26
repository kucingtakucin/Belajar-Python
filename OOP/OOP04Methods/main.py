#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Hero:
    # Class variable
    jumlahHero = 0

    def __init__(self, nama, health, power, armor):
        self.nama = nama
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlahHero += 1
        pass

    # void function/method tanpa return, tanpa argumen
    def siapa(self):
        print('Namaku adalah', self.nama)
        pass

    def health_up(self, up):
        self.health += up
        pass

    def get_health(self):
        return self.health


hero1 = Hero('Mbah Putih', 200, 50, 100)
print(hero1.__dict__)
hero1.siapa()
hero1.health_up(100)
print(hero1.__dict__)
hero2 = Hero('Mulyosugito', 400, 100, 50)
hero2.siapa()
hero2.health_up(100)
print(hero2.__dict__)

print('\n')
print(copyright)
