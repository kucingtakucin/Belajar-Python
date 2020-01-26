#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== FOR ELSE, RANGE & BREAK ======\n")
angka = 7
for i in range(0, 10, 1):
    print(i)
    if i is angka:
        print("Angka ditemukan", i)
        break
else:
    print("Angka tidak ditemukan")

print("Daerah di luar for loop")
print("Akhir dari program")

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
