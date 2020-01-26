#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== NILAI BALIK FUNGSI ======\n")
# Nilai balik fungsi


def perkalian(a, b):
    hasil = a * b
    return hasil
    pass


def teknik():
    a = ('Informatika', 'Elektro', 'Mesin', "Industri", 'Sipil')
    return a
    pass


def mipa():
    b = ['Fisika', 'Kimia', 'Biologi', 'Matematika']
    return b
    pass


x = int(input("Masukkan nilai x : "))
y = int(input("Masukkan nilai y : "))
kali = perkalian(x, y)
print("%d * %d = %d" % (x, y, kali))

print("\nMacam-macam prodi di Fakultas Teknik : ", teknik())
print("Macam-macam prodi di Fakultas MIPA : ", mipa())

print('\n')
print(copyright)
# Mbah Putih Mulyosugito
