#  Copyright (c) 2020. Adam Arthur Faizal
import sys
import timeit
from sys import copyright

print("====== TUPLES ======")

# List
ganjil = [1, 3, 5, 7, 9]
print("Tipe class :", type(ganjil))
print("Data ganjil =", ganjil)

# Tuple
genap = (0, 2, 4, 6, 8)
print("Tipe class :", type(genap))
print("Data genap =", genap)

data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, "Adam", "Arthur", "Faizal", True, False, 3.14]
besar_datalist = sys.getsizeof(data_list)
data_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, "Adam", "Arthur", "Faizal", True, False, 3.14)
besar_datatuple = sys.getsizeof(data_tuple)

waktu_list = timeit.timeit(stmt="[1, 2, 3, 4, 5, 6, 7, 8, 9, \"Adam\", \"Arthur\", \"Faizal\", True, False, 3.14]", number=1000000)
print("Waktu untuk memproses list :", waktu_list)
waktu_tuple = timeit.timeit(stmt="(1, 2, 3, 4, 5, 6, 7, 8, 9, \"Adam\", \"Arthur\", \"Faizal\", True, False, 3.14)", number=1000000)
print("Waktu untuk memproses tuple :", waktu_tuple)

# Tuple data tunggal
A = ("a",)  # Harus diakhiri dengan koma
print(A, "Tipe class :", type(A))
B = (8,)
print(B, "Tipe class :", type(B))

# Mengkonversi tuple menjadi list
C = list(A)
print(C, "Tipe class :", type(C))

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
