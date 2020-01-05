#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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
