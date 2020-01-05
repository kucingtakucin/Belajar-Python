#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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
