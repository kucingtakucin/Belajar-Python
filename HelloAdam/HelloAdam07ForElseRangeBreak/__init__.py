#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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
