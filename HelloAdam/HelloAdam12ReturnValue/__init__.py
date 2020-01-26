#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== RETURN VALUE ======\n")


# Fungsi dengan return value
def kuadrat(angka):
    total = angka ** 2
    return total


def kali(angka1, angka2):
    total = angka1 * angka2
    return total


def tambah(angka1, angka2):
    total = angka1 + angka2
    return total


a = 5
b = 6
print("Nilai", a, "kuadrat adalah ", kuadrat(angka=a))
print("Hasil dari", a, "*", b, "=", kali(a, b))
print("Hasil dari", a, "+", b, "=", tambah(a, b))

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
