#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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
