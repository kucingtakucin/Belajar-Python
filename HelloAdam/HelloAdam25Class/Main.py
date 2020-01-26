#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Mahasiswa:
    nama = ""
    NIM = ""
    jurusan = ""


Adam = Mahasiswa()
MbahPutih = Mahasiswa()
print("====== CLASS ======\n")
MbahPutih.nama = "Mbah Putih Mulyosugito"
MbahPutih.NIM = "M3119000"
MbahPutih.jurusan = "Teknik Informatika"
print(MbahPutih.nama, "-", MbahPutih.NIM, "-", MbahPutih.jurusan)

Adam.nama = "Adam Arthur Faizal"
Adam.NIM = "M3119001"
Adam.jurusan = "Teknik Informatika"
print(Adam.nama, "-", Adam.NIM, "-", Adam.jurusan)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
