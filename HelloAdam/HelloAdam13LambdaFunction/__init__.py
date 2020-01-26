#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== LAMBDA FUNCTION ======\n")
a = 4
b = 5

# Membuat anonymous function dengan lambda
kali = lambda x, y: x * y
hasil = kali(a, b)
print("Hasil perkalian", a, "*", b, "=", hasil)

tambah = lambda x, y: x + y
hasil2 = tambah(a, b)
print("Hasil penjumlahan", a, "+", b, "=", hasil2)

print("\n")
print(copyright)
# by Mbah Putih Mulyosugito
