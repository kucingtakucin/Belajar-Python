#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright


class OjekKonvensional:

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah
        pass

    def cek_id(self):
        print("--- Data Pengendara ---")
        print("Nama      :", self.nama)
        print("Transmisi :", self.transmisi)
        print("Daerah    :", self.daerah)
        print('\n')
        pass

    pass


class Gojek(OjekKonvensional):
    def cek_id(self):
        print("Cek di Aplikasi gojek")
        pass
    pass


Otong = OjekKonvensional("Otong Surotong", "Matic", "Surakarta")
Otong.cek_id()
Ucup = OjekKonvensional("Ucup Surucup", "Manual", "Klaten")
Ucup.cek_id()
MbahPutih = Gojek("Mbah Putih Mulyosugito", "Matic", "Karanganyar")
MbahPutih.cek_id()

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
