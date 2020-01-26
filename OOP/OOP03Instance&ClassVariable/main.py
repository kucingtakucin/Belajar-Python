#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Mahasiswa:
    jumlahMahasiswa = 0

    def __init__(self, nama, nim, kelas, angkatan):
        self.Nama = nama
        self.NIM = nim
        self.Kelas = kelas
        self.angkatan = angkatan
        Mahasiswa.jumlahMahasiswa += 1
        pass


mahasiswa1 = Mahasiswa('Adam Arthur Faizal', 'M3119001', 'TiA', 2019)
print(mahasiswa1.__dict__)
print('Jumlah mahasiswa saat ini adalah', Mahasiswa.jumlahMahasiswa)

print('\n')
print(copyright)
