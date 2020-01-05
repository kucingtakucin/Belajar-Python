#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== PROGRAM TEBAK ANGKA ======\n")
angka = 100

tebak = int(input("Masukkan tebakan kamu : "))
while tebak is not angka:
    if tebak > 100 and tebak <= 125:
        print("Waduh hampir mendekati, coba lagi!")
        tebak = int(input("Masukkan tebakan kamu : "))
        pass
    elif tebak > 125:
        print("Angka terlalu besar!")
        tebak = int(input("Masukkan tebakan kamu : "))
        pass
    elif tebak >= 90 and tebak < 100:
        print("Wah hampir mendekati, coba lagi!")
        tebak = int(input("Masukkan tebakan kamu : "))
        pass
    elif tebak < 90:
        print("Angka terlalu kecil!")
        tebak = int(input("Masukkan tebakan kamu : "))
        pass
    pass
print("SELAMAT TEBAKAN KAMU BENAR!")

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
