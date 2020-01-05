#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== INPUT OUTPUT FILE ======\n")

"""
w = write mode --> Mode untuk menulis dan menghapus data lama, jika file belum ada maka akan dibuatkan
r = read mode only --> Hanya mode baca saja
a = appending mode --> Menambahkan data di akhir baris
r+ = write and read mode --> Menulis sekaligus membaca
"""

# Membuat file text
myFile = open("data.txt", "w")
myFile.write("Adam Arthur Faizal\n")
myFile.write("Mbah Putih Mulyosugito\n")
myFile.write("Ini adalah baris ketiga\n")
myFile.write("Ini adalah baris keempat\n")
myFile.close()

# Membaca file text
myFile2 = open("data.txt", "r+")
# print(myFile2.readline())
print(myFile2.read())
myFile2.close()

# Appending mode
myFile3 = open("data.txt", "a")
myFile3.write("Ini adalah baris yang dibuat dengan mode Appending\n")
myFile3.close()

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito