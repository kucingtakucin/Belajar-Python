#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Mahasiswa:

    def __init__(self, nama, nim, angkatan, health, nilai):
        self.nama = nama
        self.__nim = nim
        self.__angkatan = angkatan
        self.__health = health
        self.__nilai = nilai
        pass
    pass

    @property
    def info(self):
        return 'Nama : {} \nNIM : {}'.format(self.nama, self.__nim)

    @property
    def nilai(self):
        pass

    @nilai.getter
    def nilai(self):
        return self.__nilai
        pass

    @nilai.setter
    def nilai(self, inputnilai):
        self.__nilai = inputnilai
        pass

    @nilai.deleter
    def nilai(self):
        print('Nilai dihapus!')
        self.__nilai = None
        pass


adam = Mahasiswa('Adam Arthur Faizal', 'M3119001', 2019, 100, 100)

print('Merubah info')
print(adam.info)
adam.name = 'Mbah Putih'
print(adam.info)

print('Getter dan setter')
print(adam.nilai)
adam.nilai = 90
print(adam.nilai)

print('Deleter')
del adam.nilai
print(adam.__dict__)

print('\n')
print(copyright)
