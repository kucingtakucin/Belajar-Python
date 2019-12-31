#  Copyright (c) 2019. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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
