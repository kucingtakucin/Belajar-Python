#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== MENGHITUNG JUMLAH BILANGAN GANJIL & GENAP ======\n")
# Menghitung jumlah bilangan ganjil dan genap pada list
Daftar = [5, 7, 9, 0, 1, 6, 7, 3, 8, 0, 5, 2, 0, 4, 2, 1, 6, 8, 0, 9, 5, 7, 1]
Genap = []
Ganjil = []
jumlah_genap = 0
jumlah_ganjil = 0

for elemen in Daftar:
    if elemen % 2 is 0:
        Genap.append(elemen)
        jumlah_genap += 1
        pass
    else:
        Ganjil.append(elemen)
        jumlah_ganjil += 1
        pass
    pass

print("--- GANJIL ---")
for i in Ganjil:
    print(i)
    pass
print("Jumlah elemen ganjil adalah", jumlah_ganjil)
print("--- GENAP ---")
for j in Genap:
    print(j)
    pass
print("Jumlah elemen genap adalah", jumlah_genap)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
