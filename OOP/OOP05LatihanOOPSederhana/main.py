#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Hero:
    pass

    def __init__(self, nama, health, attack, defence):
        self.nama = nama
        self.health = health
        self.attack = attack
        self.defence = defence
        pass

    def serang(self, lawan):
        print(self.nama, 'menyerang', lawan.nama)
        lawan.diserang(self, self.attack)
        pass

    def diserang(self, lawan, attackpower_lawan):
        print(self.nama, 'diserang', lawan.nama)
        attack_diterima = attackpower_lawan / self.defence
        print('Serangan terasa', attack_diterima)
        self.health -= attack_diterima
        print('darah', self.nama, 'tersisa', self.health)
        pass


mbahputih = Hero('Mbah Putih Mulyosugito', 100, 10, 5)
arthur = Hero('Adam Arthur Faizal', 100, 20, 10)

arthur.serang(mbahputih)

print('\n')
print(copyright)
