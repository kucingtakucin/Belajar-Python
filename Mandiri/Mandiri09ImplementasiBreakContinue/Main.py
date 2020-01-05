#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== IMPLEMENTASI BREAK & CONTINUE ======\n")
print("--- Implementasi statemen break pada for")
# Implementasi statemen break
Daftar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nMencari elemen tertentu pada list : ")
nomer = int(input("Masukkan angka : "))
for i in range(len(Daftar)):
    if nomer is Daftar[i]:
        print("%d terdapat pada indeks %d" % (nomer, i))
        break
        pass
    pass

print("--- Implementasi statemen break pada while")
# Implementasi statemen break pada while
hitung = 3
pswd = "admin"
while hitung > 0:
    password = input("Masukkan password : ")
    if password is pswd:
        print("Login sukses!")
        break
        pass
    else:
        print("Password salah, ulangi!")
        hitung -= 1
        pass
    pass

print("--- Implementasi statemen continue")
# Implementasi statemen break pada while
spasi = 0
print("Menghitung jumlah spasi pada kalimat : ")
str = input("Masukkan kalimat : ")
print("Kalimat yang kamu masukkan adalah %s" % (str))
for i in range(len(str)):
    if str[i] is '.':
        break
        pass
    elif str[i] is not ' ':
        continue
        pass
    spasi += 1
    pass
print("Jumlah spasi nya adalah sebanyak %s spasi" % (spasi))

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
