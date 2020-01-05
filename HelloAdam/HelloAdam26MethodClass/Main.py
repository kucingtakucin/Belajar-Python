#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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
