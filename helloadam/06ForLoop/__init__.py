#  Copyright (c) 2019. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== FOR LOOP ======\n")   # Semacam for each
Nama = ["Adam", "Arthur", "Faizal", "Mbah", "Putih", "Mulyosugito"]
for nama in Nama:
    print(nama)

kata = "informatika"
for huruf in kata:
    print(huruf)

Buah = ["Apel", "Jeruk", "Semangka", "Mangga", "Anggur"]
Sayur = ["Bayam", "Kangkung", "Kol", "Pare", "Wortel"]

Gabungan = [Nama, Buah, Sayur]
for i in Gabungan:
    print(i)
    for j in i:
        print(j)

print(copyright)
# by Mbah Putih Mulyosugito
