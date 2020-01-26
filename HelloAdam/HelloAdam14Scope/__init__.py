#  Copyright (c) 2020. Adam Arthur Faizal
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
