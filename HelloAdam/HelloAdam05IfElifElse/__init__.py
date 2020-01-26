#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== IF ELIF ELSE ======\n")
nilai = int(input("Masukkan nilai : "))

if nilai is 100:
    print("Nilai kamu adalah", nilai)

if nilai is not 100:
    print("Nilai kamu bukan 100")

if nilai is nilai:
    print("Nilai kamu adalah", nilai)

if 85 <= nilai <= 100:
    print("IP kamu A")
elif 80 <= nilai < 85:
    print("IP kamu A-")
elif 75 <= nilai < 80:
    print("IP kamu B")
elif 70 <= nilai < 75:
    print("IP kamu B-")
elif 65 <= nilai < 70:
    print("IP kamu C")
elif 50 <= nilai < 65:
    print("IP kamu D")
elif 0 <= nilai < 50:
    print("IP kamu E")
else:
    print("Kamu salah input")

Data = ["Adam", "Arthur", "Faizal", "Mbah", "Putih", "Mulyosugito"]
nama = "Adam"

if nama in Data:
    print(nama, "kamu ada di", Data)

if not nama in Data:
    print(nama, "Kamu engga ada di", Data)

karakter = 'a'
if karakter in nama:
    print("Ada huruf", karakter, "di", "nama", nama)
else:
    print("Tidak ada huruf", karakter, "di", "nama", nama)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
