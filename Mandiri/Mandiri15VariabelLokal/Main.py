#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== VISIBILITAS VARIABEL LOKAL ======\n")


def burung():
    terbang = 1000
    print("Burung bisa terbang sejauh", terbang, "km tiap harinya")
    pass


def angsa():
    terbang = 3
    print("Angsa bisa terbang sejauh", terbang, "km tiap harinya")
    pass


def ayam():
    terbang = 0.5
    print("Ayam bisa terbang sejauh",terbang, "km tiap harinya")
    pass


burung()
angsa()
ayam()
print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
