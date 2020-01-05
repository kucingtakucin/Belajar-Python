#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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
