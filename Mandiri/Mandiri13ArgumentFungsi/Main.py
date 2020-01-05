#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== FUNGSI DENGAN ARGUMENT ======\n")
print("--- List & tuple sebagai argument")
# List dan tuple sebagai argument


def tampil_tuple(data_tuple):
    for i in range(len(data_tuple)):
        print("%d. %s" % (i + 1, data_tuple[i]))
        pass
    pass


def tampil_list(data_list):
    for i in range(len(data_list)):
        print("%d. %s" % (i + 1, data_list[i]))
        pass
    pass


def utama():
    datalist = ["Teknik Informatika", "Teknik Elektro", "Teknik Industri", "Teknik Sipil", "Teknik Lingkungan"]
    datatuple = ("Fisika", "Kimia", "Biologi", "Matematika")
    print("Daftar prodi di Fakultas Teknik :")
    tampil_list(datalist)
    print("Daftar prodi di Fakultas MIPA :")
    tampil_tuple(datatuple)
    pass


utama()
print("\n--- Argument posisional")
# Argument posisional


def tampil(data):
    print("Hallooo...", data)
    pass


def tampil2(data_a, data_b):
    print("Hallooo...nama kami adalah %s dan %s" % (data_a, data_b))
    pass


tampil("Mbah Putih")
tampil2("Adam", "Arthur")
print("\n--- Argument default")
# Argument default


def tampil_string(kata, n=3):
    for i in range(n):
        print(kata[i])
        pass
    pass


def utama():
    kata = input("Masukkan kata : ")
    n = int(input("Jumlah karakter yang ingin ditampilkan : "))
    print("Menampilkan karakter berdasarkan jumlah yang diinginkan user : ")
    tampil_string(kata, n)
    print("\nMenampilkan karakter berdasarkan argument default : ")
    tampil_string(kata)
    pass


utama()
print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
