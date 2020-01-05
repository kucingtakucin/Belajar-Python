#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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
