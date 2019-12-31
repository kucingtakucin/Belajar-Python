#  Copyright (c) 2019. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== IF ELIF ELSE ======\n")
nilai = 90

if nilai == 100:
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

print(copyright)
# by Mbah Putih Mulyosugito
