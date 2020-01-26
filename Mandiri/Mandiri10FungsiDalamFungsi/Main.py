#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== PEMANGGILAN FUNGSI DALAM FUNGSI ======\n")
# Pemanggilan fungsi didalam fungsi


def fungsi_1():
    print("Halooo...saya fungsi 1")
    pass


def fungsi_2():
    print("Halooo...saya fungsi 2, panggil fungsi 1 dulu yaa...")
    pass


def fungsi_utama():
    print("Panggil semua")
    fungsi_2()
    pass


fungsi_utama()
# Pemanggilan fungsi didalam fungsi


def cek_prima():
    prima = True
    cek = 2
    data = int(input("Masukkan angka : "))
    while cek < data:
        if data % cek is 0:
            prima = False
        cek += 1
        pass
    if prima is True and data > 1:
        print("%d adalah bilangan prima" % data)
        pass
    else:
        print("%d bukan bilangan prima" % data)
        pass
    pass


def utama():
    print("\nProgram utnuk mengecek bilangan prima : ")
    for i in range(3):
        cek_prima()
    pass


utama()
print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
