#  Copyright (c) 2019. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
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

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
