#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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
