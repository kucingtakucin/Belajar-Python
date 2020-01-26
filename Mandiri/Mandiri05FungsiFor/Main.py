#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== FUNGSI YANG BERKAITAN DENGAN FOR ======\n")
print("--- Menampilkan list yang sudah terurut ---")
Data = [2, 1, 3, 5, 4, 8, 6, 7, 0, 9]
print("Isi list sebelum diurutkan :")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for i in Data:
    print(i)
    pass

print("Isi list setelah diurutkan : ")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for i in sorted(Data):
    print(i)
    pass

print("--- Membalik isi tuple ---")
Bahasa = ("Java", "C", "C++", "C#", "Pascal", "Python", "PHP", "Javascript")
print("Urutan tuple sebelum dibalik :")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for i in Bahasa:
    print(i)
    pass

print("Urutan tuple setelah dibalik :")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for i in reversed(Bahasa):
    print(i)
    pass

print("--- Fungsi zip dalam statement for ---")
X = ("Adam", "Arthur", "Faizal")
Y = (2002, 2003, 2004)
for i, j in zip(X, Y):
    print("%s lahir pada tahun %d" % (i, j))
    pass

print("--- Nested For ----")
Daftar = ((1, 2, 3), ("Adam", "Arthur", "Faizal"), ("Java", "C++", "Python"))
for i in range(len(Daftar)):
    print("--------", "<--- Baris", i + 1)
    pass
    for j in range(len(Daftar[i])):
        print(Daftar[i][j])
        pass

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
