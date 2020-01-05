#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== SCOPE ======\n")
namakucing = "Adam"
makanankucing = "Whiskas"


def ubahnamakucing(namabaru):
    global namakucing
    namakucing = namabaru
    return namakucing


def kasihmakankucing(makananbaru, namabaru):
    global makanankucing, namakucing
    namakucing = namabaru
    makanankucing = makananbaru
    return namabaru, makananbaru


print("Aku ubah nama kucing yang semula bernama", namakucing, "menjadi", ubahnamakucing("Arthur"))
print("List nama kucingku dan makanannya adalah", kasihmakankucing(namabaru="Mba hPutih", makananbaru="Universal"))

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
