#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== FOR LOOP ======\n")   # Semacam for each
Data = ["Adam", "Arthur", "Faizal", "Mbah", "Putih", "Mulyosugito"]
for nama in Data:
    print(nama)

kata = "informatika"
for huruf in kata:
    print(huruf)

Buah = ["Apel", "Jeruk", "Semangka", "Mangga", "Anggur"]
Sayur = ["Bayam", "Kangkung", "Kol", "Pare", "Wortel"]

Gabungan = [Data, Buah, Sayur]
for i in Gabungan:
    print(i)
    for j in i:
        print(j)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
