#  Copyright (c) 2020. Adam Arthur Faizal
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
