#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("===== FUNCTION & ARGUMENTS ======\n")


# Function dengan menggunakan argumen sederhana
def siswa(nama):
    print("Siswa ini bernama :", nama)


# Function dengan menggunakan keywords argumen
def guru(nama, pelajaran):
    print("Guru ini bernama :", nama)
    print("Mata pelajaran :", pelajaran)


siswa("Adam Arthur Faizal")
guru(nama="Mbah Putih", pelajaran="Informatika")
guru(pelajaran="Ilmu Komputer", nama="Mulyosugito")
guru("Olahraga", " Otong Surotong")


# Function dengan menggunakan default argumen
def penjagasekolah(nama, shift="Siang", galak="Iya"):
    print("Penjaga sekolah ini bernama :", nama)
    print("Shift :", shift)
    print("Dia galak engga?", galak)


penjagasekolah("Jamal")
penjagasekolah("Topik", shift="Malam")
penjagasekolah("Dobleh", galak="Iya")
# penjagasekolah(shift="Malam", galak="Iya")   # Akan menghasilkan error

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
