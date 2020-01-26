#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Hero:

    def __init__(self, nama, nim, angkatan, nilai, health):
        self.__nama = nama
        self.__nim = nim
        self.__angkatan = angkatan
        self.__nilai = nilai
        self.__health = health
        pass

    # getter
    def getnilai(self):
        return self.__nilai
        pass

    def getnama(self):
        return self.__nama
        pass

    def gethealth(self):
        return self.__health

    # setter
    def diserang(self, serang):
        self.__health -= serang
        pass

    def sembuhkan(self, nilaibaru):
        self.__health = nilaibaru
        pass


adam = Hero('Adam Arthur Faizal', 'M3119001', 2019, 100, 100)
print(adam.getnama())
print(adam.getnilai())
adam.diserang(10)
print(adam.gethealth())
adam.sembuhkan(100)
print(adam.gethealth())

print('\n')
print(copyright)
