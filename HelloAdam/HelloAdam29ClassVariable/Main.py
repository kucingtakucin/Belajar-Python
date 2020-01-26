#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class Mahasiswa:
    jumlah = 0

    def __init__(self, input_nama, input_nim, input_jurusan):
        print("--- Data Mahasiswa ---")
        self.nama = input_nama
        print("Nama     :", self.nama)
        self.nim = input_nim
        print("NIM      :", self.nim)
        self.jurusan = input_jurusan
        print("Jurusan  :", self.jurusan)
        print('\n')

        Mahasiswa.jumlah += 1
        pass
    pass


def jumlah_mahasiswa():
    print("Jumlah mahasiswa :", Mahasiswa.jumlah)
    pass


MbahPutih = Mahasiswa("Mbah Putih Mulyosugito", "M3119000", "Teknik Informatika")
Adam = Mahasiswa("Adam Arthur Faizal", "M3119001", "Teknik Informatika")
Arthur = Mahasiswa("Arthur Pendragon", "M311900-1", "Teknik Informatika")
jumlah_mahasiswa()

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
