#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Mahasiswa:

    def __init__(self, nama, nim, kelas, angkatan):
        self.nama = nama
        self.NIM = nim
        self.kelas = kelas
        self.angkatan = angkatan
        pass


mahasiswa1 = Mahasiswa('Adam Arthur Faizal', 'M3119001', 'Ti A', 2019)
print(mahasiswa1)
print(mahasiswa1.__dict__)
print('\n')
print(copyright)


