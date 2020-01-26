#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== IMPLEMENTASI FUNGSI RANGE ======\n")
print("--- Bagian 1 --- (Menampilkan rentang nilai)")   # Menampilkan rentang nilai
awal = int(input("Masukkan nilai awal : "))
akhir = int(input("Masukkan nilai akhir : "))
pembaruan = int(input("Masukkan nilai pembaruan : "))
for i in range(awal, akhir, pembaruan):
    print(i)
    pass

print("\n--- Bagian 2 --- (Membangkitkan nilai dengan rentang tertentu)")     # Membangkitkan nilai dengan rentang tertentu
awal2 = int(input("Masukkan batas awal : "))
akhir2 = int(input("Masukkan batas akhir : "))
for i in range(awal2, akhir2):
    print(i)
    pass

print("\n--- Bagian 3 --- (Memasukkan elemen list)")     # Memasukkan elemen list
jumlah = int(input("Masukkan jumlah elemen list : "))
print("Silahkan masukkan elemen list")
Daftar = []
for i in range(jumlah):
    elemen = input("- ")
    Daftar.insert(i, elemen)
    pass

print("Isi dari list :", Daftar)
print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
