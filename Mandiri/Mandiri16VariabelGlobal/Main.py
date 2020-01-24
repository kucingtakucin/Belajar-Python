#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== VARIABLE GLOBAL ======\n")
data = 100


def teknik():
    print("Fakultas Teknik mengakses data global :", data)
    pass


def hukum():
    print("Fakultas Hukum mengakses data global :", data)
    pass


def ekonomi():
    print("Fakultas Ekonomi mengakses data global :", data)
    pass


teknik()
hukum()
ekonomi()
print("Arthur mengakses data global :", data)

krisis = 0.5
print('\n')


def var_global():
    print("Krisis global :", krisis)
    pass


def var_lokal():
    krisis = 10
    print("Krisis lokal :", krisis)
    pass


var_global()
var_lokal()

print("\n--- Pembaruan nilai variable global")
krisis2 = 0.5


def var_global2():
    print("Krisis global :", krisis2)
    pass


def var_lokal2():
    krisis2 = 10
    print("Krisis lokal :", krisis2)
    pass


def pembaruan(n):
    global krisis2
    krisis2 += n
    print("Pembaruan krisis global :", krisis2)
    pass


def utama():
    var_global2()
    var_lokal2()
    pembaruan(5)
    var_global2()
    var_lokal2()
    pass


utama()
print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
