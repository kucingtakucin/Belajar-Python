#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== PROGRAM TEKA-TEKI ======\n")
# Program teka-teki


def tekateki():
    print("--- Teka-teki")
    input("Tekan enter untuk memulai petunjuk\n")
    step_1()
    input("Tekan enter untuk petunjuk selanjutnya\n")
    step_2()
    input("Tekan enter untuk petunjuk selanjutnya\n")
    step_3()
    print('\n')
    jawaban()
    pass


def step_1():
    print("1. Aku adalah benda mati, yang sangat populer saat ini\n")
    pass


def step_2():
    print("2. Aku bisa digunakan untuk menjelajah melalui terowongan kabel kecil\n")
    pass


def step_3():
    print("3. Aku bisa mempercepat pekerjaan manusia,...\n")
    pass


def jawaban():
    jawab = input("Siapakah aku? ")
    if jawab is "komputer" or jawab is "Komputer" or jawab is "KOMPUTER":
        print("Selamat...jawaban kamu benar!!!")
        pass
    else:
        print("Maaf, tebakan kamu kurang tepat!")
        pass


tekateki()
print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
