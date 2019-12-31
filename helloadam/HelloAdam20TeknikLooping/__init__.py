#  Copyright (c) 2019. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== TEKNIK LOOPING ======\n")
hewan = ["Kucing", "Kelinci", "Sapi", "Ular", "Burung"]
print("Daftar hewan :", hewan)
buah = ["Mangga", "Stroberi", "Pepaya", "Melon"]
print("Daftar buah :", buah)

# Enumerate
print("--- Enumerate ---")
for nomer, nama in enumerate(hewan):
    print(nomer, ":", nama)

# Zip
print("--- Zip ---")
for namahewan, namabuah in zip(hewan, buah):
    print(namahewan, ":", namabuah)

# Jika diterapkan pada set dan dictionary
# Set
barang = {"TV", "Lemari", "Meja", "Kursi", "Kipas Angin"}
print("Daftar barang :", barang)

for namabarang in sorted(barang):
    print(namabarang)

# Dictionary
playlist = {"Linkin Park": "In The End", "Avenged Sevenfold": "So Far Away", "Maroon 5": "Payphone", "Slipknot": "Snuff", "Asking Alexandria": "Moving On"}

for band, lagu in enumerate(playlist.items()):
    print(band, "-", lagu)

# Lain-lain
print("--- Lain-lain ---")
for i in reversed(range(1, 10, 1)):
    print(i)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
