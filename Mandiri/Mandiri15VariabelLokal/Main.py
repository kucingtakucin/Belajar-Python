#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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
