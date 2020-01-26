#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== STRING ======\n")   # String di Python

# String dapat ditulis dengan tanda petik 1 maupun petik 2
print("Hello World")
text = 'hello dunia'
text2 = "halo dunia"
print(text, "&", text2)

# Untuk menulis string dalam beberapa kalimat bisa menggunakan 3 kali petik 2
print('\n')
text3 = """
Halo adam
Adam Arthur Faizal
"""
print(text3)

# Untuk mengatasi permasalahan tanda petik dalam string bisa menggunakan backslash
print('\n')
text4 = 'Mbah \'putih\' Mulyosugito'
text5 = "Mbah \"Putih\" Mulyosugito"
print(text4, "&", text5)

# Enter pada string
print('\n')
text6 = "Ini adalah enter \nIni adalah enter"
print(text6)
text7 = r"Ini bukan enter \nIni bukan enter"
print(text7)

# Macam - macam method pada string
print('\n')
text8 = "Ini adalah text terbaru"
print("self.upper :", text8.upper())    # Mengubah keseluruhan menjadi huruf besar
print("self.lower :", text8.lower())    # Mengubah keseluruhan menjadi huruf kecil
print("self.capitalize :", text8.capitalize())   # Mengubah huruf pertama menjadi huruf kapital
print("self.casefold :", text8.casefold())  # Mengubah semua huruf kapital menjadi huruf kecil
print("self.swapcase :", text8.swapcase())  # Membalik uppercase menjadi lowercase dan sebaliknya (Swapping)
print("self.title :", text8.title())    # Mengubah huruf pertama pada setiap kata dalam kalimat menjadi huruf kapital
print("self.join :", text8.join("AB"))  # Menambahkan setidaknya 2 huruf pada awal dan akhir kalimat
print("self.count :", text8.count("a", 0, len(text8)))  # Mencari berapa jumlah suatu huruf/kata dalam suatu string
print("self.center :", text8.center(35, "-"))   # Membuat string menjadi rata tengah/center
# print(text8.expandtabs(5))
print("self.find :", text8.find("adalah", 0, len(text8)))   # Mencari posisi indeks pada suatu kata/huruf
# print(text8.format_map(""))
print("self.ljust :", text8.ljust(32, "-"))     # Membuat string menjadi rata kiri
print("self.rjust :", text8.rjust(32, "-"))     # Membuat string menjadi rata kanan
print("self.replace :", text8.replace("Ini", "Itu"))  # Mengganti suatu huruf/kata dalam string
print("self.partition :", text8.partition("a"))     # Mengisolasi suatu huruf/kata
print("self.split :", text8.split())    # Memisahkan kata berdasarkan delimiter
print("self.splitlines :", text8.splitlines())
# print(text8.strip(""))
print("self.zfill :", text8.zfill(50))

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
