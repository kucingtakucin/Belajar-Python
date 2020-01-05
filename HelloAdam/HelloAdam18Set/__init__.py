#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("===== SET ======")

# Set adalah semacam himpunan
superhero = set()
superhero.add("Captain America")        # self.add berfungsi untuk menambahkan elemen tunggal
superhero.add("Ironman")
superhero.add("Thor")
superhero.add("Hulk")
superhero.add("Black Panther")
print(superhero)

ganjil = {1, 3, 5, 7, 9}
genap = {0, 2, 4, 6, 8}
prima = {1, 2, 3, 5, 7}
print("Union :", ganjil.union(genap))       # Gabungan
print("Intersection :", ganjil.intersection(prima))     # Irisan

# Set mutable / bisa diubah ukurannya (Set dinamis)
X = set("Pemrograman Python")
print(X)
print("Tipe class :", type(X))
X.add("Ular")   # self.add berfungsi untuk menambahkan elemen tunggal
X.update("Ular")    # self.update berfungsi untuk menambahkan sekumpulan elemen
X.remove("U")   # self.remove berfungsi untuk menghapus suatu elemen pada set
# X.clear()       # self.clear berfungsi untuk menghapus semua elemen pada set
X.pop()         # self.pop berfungsi untuk menghapus elemen pertama pada set

# Set immutable / tidak bisa diubah ukurannya (Set statis)
Y = frozenset("Pemrograman Java")
print(Y)
print("Tipe class :", type(Y))

a = set(genap)
print("Bilangan genap :", a)
b = frozenset(ganjil)
print("Bilangan ganjil :", b)
c = set(prima)
print("Bilangan prima :", c)

gabungan = a | b
print("Gabungan =", gabungan)
irisan = a & c
print("Irisan1 =", irisan)
irisan2 = b & c
print("Irisan2 =", irisan2)
komplemen = a - b
komplemen2 = b.difference(c)
print("Komplemen =", komplemen)
print("Komplemen2 =", komplemen2)
bedasetangkup = a ^ b
bedasetangkup2 = a.symmetric_difference(c)
print("Beda setangkup =", bedasetangkup)
print("Beda setangkup2 =", bedasetangkup2)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
