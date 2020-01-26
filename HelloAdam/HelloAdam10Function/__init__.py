#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== FUNCTION ======\n")
# Membuat fungsi sederhana


def suaraayam():
    print("kukuruyuuuk!!!")


def hargaayam():
    suaraayam()


def hargatotalayam(kg):
    suaraayam()
    harga = 10000
    hargatotal = kg * harga
    print("Harga", kg, "kg ayam adalah :", hargatotal)


suaraayam()
hargatotalayam(2)
hargatotalayam(0.5)
hargatotalayam(1)
hargatotalayam(9)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
