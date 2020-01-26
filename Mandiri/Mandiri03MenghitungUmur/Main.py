#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== PROGRAM MENGHITUNG UMUR ======\n")

while True:
    nama = input("Masukkan nama : ")
    tahunlahir = int(input("Tahun Lahir : "))
    tahunsekarang = int(input("Tahun Sekarang : "))

    umur = tahunsekarang - tahunlahir
    print("%s umur kamu adalah %d tahun" % (nama, umur))

    pilih = input("Ingin menghitung umur lagi? (Y/N) ")
    while (pilih is not "Y" and pilih is not 'y') and (pilih is not "N" and pilih is not "n"):
        print("Salah input!")
        pilih = input("Ingin menghitung umur lagi? (Y/N) ")
    if pilih is "N" or pilih is "n":
        break
    pass

print("Program selesai\n")
print(copyright)
# by Mbah Putih Mulyosugito
