#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== METHOD PADA CLASS ======\n")


class Mahasiswa:
    nama = 'nama'
    NIM = 'NIM'
    jurusan = 'jurusan'

    def belajar(self, kondisi):
        print(self.nama, "sedang belajar", kondisi)

    def tidur(self, kondisi):
        print(self.nama, "tidur di kelas", kondisi)


Adam = Mahasiswa()
Arthur = Mahasiswa()

Adam.nama = "Adam Arthur Faizal"
Adam.NIM = "M3119000"
Adam.jurusan = "Teknik Informatika"
print(Adam.nama, "-", Adam.NIM, "-", Adam.jurusan)

Arthur.nama = "Mbah Putih Mulyosugito"
Arthur.NIM = "M3119001"
Arthur.jurusan = "Teknik Informatika"
print(Arthur.nama, "-", Arthur.NIM, "-", Adam.jurusan)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
