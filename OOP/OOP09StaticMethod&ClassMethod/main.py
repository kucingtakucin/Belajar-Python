#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Hero:
    # Private class variable
    __jumlah = 0

    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Hero.__jumlah += 1
        pass

    # Method ini hanya berlaku untuk objek
    def getjumlah0(self):
        return Hero.__jumlah

    # Method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getjumlah1():
        return Hero.__jumlah

    # Method static (decorator) menempel pada objek dan kelas
    @staticmethod
    def getjumlah2():
        return Hero.__jumlah
        pass

    @classmethod
    def getjumlah3(kelas):
        return kelas.__jumlah
    pass

adam = Hero('Adam', 'M3119001', 2019)
print(Hero.getjumlah2())
arthur = Hero('Arthur', 'M3119001', 2019)
print(adam.getjumlah2())
mbahputih = Hero('Mbah Putih', 'M3119000', 2019)
print(Hero.getjumlah3())

print('\n')
print(copyright)
