#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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
