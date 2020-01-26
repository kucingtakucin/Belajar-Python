#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== ARGUMENT BERDASARKAN PANJANG VARIABEL ======\n")
print("--- Non-keyword argument (tuple)")
# Non-keyword argument (tuple)


def tampil_data(a, b, *c):
    print("Formal argument A :", a)
    print("Formal argument B :", b)
    for elemen in c:
        print("Non-keyword argument C :", elemen)
    pass


def utama():
    a = input("Masukkan a : ")
    b = input("Masukkan b : ")
    data = []
    while True:
        data.append(input("Masukkan c : "))
        c = data
        konfirmasi = int(input("Ingin masukkan c lagi? (1/0) "))
        if konfirmasi == 1:
            continue
        elif konfirmasi == 0:
            break
            pass
        while konfirmasi is not 1 and konfirmasi is not 0:
            print("Salah input! coba lagi!")
            konfirmasi = int(input("Ingin masukkan c lagi? (1/0) "))

    tampil_data(a, b, c)
    pass


utama()
print("\n--- Keyword argument")
# Keyword argument (dictionaries)


def argdict(a, b, **c):
    print("Formal argument a :", a)
    print("Formal argument b :", b)
    for elemen in c.keys():
        print("Keyword argument", elemen, "adalah", c[elemen])
        pass
    pass


def utama():
    argdict(a="abc", b=123, X=100, Y=200, Z=300)
    pass


utama()
print("\n--- Implementasi non-keyword dan keyword argument")


def ntb(a, b, *c, **d):
    print("Argument formal a :", a)
    print("Argument formal b :", b)
    for elemen in c:
        print("Non-keyword argumen :", elemen)
        pass
    for elemen2 in d.keys():
        print("Keyword argumen :", elemen2)
        pass
    pass


def utama2():
    ntb(1, 2, 10, 20, 30, x="Adam", y="Arthur", z="Faizal")
    pass


utama2()
print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
