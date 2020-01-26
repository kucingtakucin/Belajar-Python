#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Hero:
    # Class variable
    jumlah = 0
    __privateJumlah = 7

    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan

        # Variable instance private
        self.__nilai = 100
        # Variable instance protected
        self._ipk = 4
        pass
    pass


adam = Hero('Adam', 'M3119001', 2019)
print(adam.__dict__)
print(Hero.__dict__)

print('\n')
print(copyright)
