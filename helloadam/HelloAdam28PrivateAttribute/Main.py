#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright


class Mahasiswa:
    __nilaiuts = 0
    __nilaiuas = 0

    def __init__(self, input_nama, input_nim, input_jurusan):
        print("--- Data Mahasiswa ---")
        self.__nama = input_nama
        print("Nama     :", self.__nama)
        self.__nim = input_nim
        print("NIM      :", self.__nim)
        self.__jurusan = input_jurusan
        print("Jurusan  :", self.__jurusan)
        pass

    def uts(self, input_nilai):
        self.__nilaiuts = input_nilai * 0.5
        pass

    def uas(self, input_nilai):
        self.__nilaiuas = input_nilai * 0.5
        pass

    def nilai_akhir(self):
        hasil = self.__nilaiuts + self.__nilaiuas
        if 85 < hasil <= 100:
            status = "A"
            print("Nilai    :", hasil)
            print("IP       :", status)
            pass
        elif 80 < hasil <= 85:
            status = "A-"
            print("Nilai    :", hasil)
            print("IP       :", status)
            pass
        elif 75 < hasil <= 80:
            status = "B+"
            print("Nilai    :", hasil)
            print("IP       :", status)
            pass
        elif 70 < hasil <= 75:
            status = "C"
            print("Nilai    :", hasil)
            print("IP       :", status)
            pass
        elif 65 < hasil <= 70:
            status = "D"
            print("Nilai    :", hasil)
            print("IP       :", status)
            pass
        elif 60 < hasil <= 65:
            status = "D"
            print("Nilai    :", hasil)
            print("IP       :", status)
            pass
        elif 0 <= hasil <= 60:
            status = "E"
            print("Nilai    :", hasil)
            print("IP       :", status)
            pass
        else:
            print("Kamu salah input nilai")
            pass
        print('\n')
        pass


MbahPutih = Mahasiswa("Mbah Putih Mulyosugito", "M3119000", "Teknik Informatika")
MbahPutih.uts(80)
MbahPutih.uas(85)
MbahPutih.nilai_akhir()

Adam = Mahasiswa("Adam Arthur Faizal", "M3119001", "Teknik Informatika")
Adam.uts(90)
Adam.uas(85)
Adam.nilai_akhir()

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
