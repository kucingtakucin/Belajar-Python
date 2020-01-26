#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== MENGENAL __init__ ======\n")


class Mahasiswa:

    def __init__(self, input_nama, input_nim, input_jurusan):
        print("--- Data Mahasiswa ---")
        self.nama = input_nama
        print("Nama     :", self.nama)
        self.NIM = input_nim
        print("NIM      :", self.NIM)
        self.jurusan = input_jurusan
        print("Jurusan  :", self.jurusan)
        print('\n')

    def belajar(self, kondisi):
        print(self.nama, "sedang belajar", kondisi)

    def tidur(self, kondisi):
        print(self.nama, "sedang tidur", kondisi)


MbahPutih = Mahasiswa("Mbah Putih Mulyosugito", "M3119000", "Teknik Informatika")
Adam = Mahasiswa("Adam Arthur Faizal", "M3119001", "Teknik Informatika")

Adam.belajar("dengan giat")
Adam.tidur("dengan pulas")
MbahPutih.tidur("dengan santuy")
MbahPutih.belajar("dengan serius")

print('\n')
print(copyright)
# by Nbah Putih Mulyosugito
