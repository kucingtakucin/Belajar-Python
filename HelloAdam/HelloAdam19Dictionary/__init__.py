#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== DICTIONARY ======\n")

print("--- Data Member 1 ---")
member1 = {"NIM": "M3119000", "Nama": "Adam Arthur Faizal", "Jurusan": "Teknik Informatika"}
print(member1["NIM"], member1["Nama"])
print(member1.keys())
print(member1.values())
print(member1.items())
print(member1.get("Jurusan"))
print("Bagian yang akan dihapus :", member1.popitem())
print(member1)
# print(member1.copy())
# member1.pop("Nama")


print("--- Data Member 2 ---")
member2 = {"NIM": "M3119001", "Nama": "Mbah Putih Mulyosugito", "Jurusan": "Teknik Informatika"}
print(member2["NIM"], member2["Nama"])
print(member2.keys())
print(member2.values())
print(member2.items())
print(member2.get("Jurusan"))
print("Bagian yang akan dihapus :", member2.popitem())
print(member2)
# print(member1.copy())

print("--- List Member ---")
member_list = {1: member1, 2: member2}

print(member_list[1])
print(member_list[2])

print("\n")
print(copyright)
# by Mbah Putih Mulyosugito
