#  Copyright (c) 2019. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== MORE LIST ======\n")  # Beberapa method yang bisa digunakan untuk memanipulasi List
Barang = ["Meja", "Kursi", "Lemari", "Kulkas", "Tas"]
print(Barang)

# Method untuk menambah data kedalam list
Barang.append("Mobil")  # Menambah member list di indeks terakhir, tapi hanya terbatas pada satu member saja
print(Barang)
Barang.extend("Motor")  # Menambah member list yang di pisah per huruf
print(Barang)
Barang.insert(3, "Mobil")  # Menambah/menyisipkan member list di indeks tertentu
print(Barang)

# Method untuk menghitung anggota list
hitung = Barang.count("Mobil")  # Menghitung berapa jumlah mobil di dalam list
print("Jumlah mobil adalah", hitung)
panjanglist = len(Barang)   # Menghitung panjang list
print("Jumlah barang adalah", panjanglist)

# Method untuk menghapus data didalam list
Barang.pop(1)   # Menghapus data berdasarkan indeks list
print(Barang)
Barang.remove("Lemari")     # Menghapus data berdasarkan nama member list
print(Barang)
# Barang.clear()     # Menghapus keseluruhan anggota
# print(Barang)

# Method lainnya
Daftar = [2, 1, 3, 5, 4]
print(Daftar)
Daftar.sort()   # Mengurutkan list
print(Daftar)
Daftar.reverse()    # Reverse list
print(Daftar)
daftarbaru = Daftar.copy()  # Mengcopy list kedalam suatu variabel
daftarbaru2 = Daftar[:]     # Mengcopy list kedalam suatu variabel
daftarbaru.append(0)
daftarbaru2.append(-1)
print(daftarbaru)
print(daftarbaru2)
print(Daftar)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
