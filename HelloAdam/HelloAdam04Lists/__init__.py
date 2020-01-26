#  Copyright (c) 2020. Adam Arthur Faizal
from sys import copyright

print("====== LIST =====\n")    # Semacam array di Python

Data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
LoopingList = []
for i in range(0, 10):
    LoopingList.append(i)
    pass

print("Data =", Data)
print("Looping List =", LoopingList)

print('\n--- Mengakses list ---')
# Mengakses list
Subdata1 = Data[2]
print("Nilai pada indeks ke 2 adalah", Subdata1)
Subdata2 = Data[-2]
print("Nilai pada indeks ke -2 adalah", Subdata2)

print('\n--- Memotong list ---')
# Memotong list
Subdata3 = Data[0:5]
print("Nilai pada indeks 0 s.d 5 adalah", Subdata3)
Subdata4 = Data[:5]
print("Nilai pada awal indeks s.d indeks ke 5 adalah", Subdata4)
Subdata5 = Data[5:]
print("Nilai pada indeks ke 5 s.d akhir indeks adalah", Subdata5)
Subdata6 = Data[5:10]
print("Nilai pada indeks ke 5 s.d 10 adalah", Subdata6)
Subdata7 = Data[len(Data) - 3:]
print("Nilai pada 3 indeks terakhir adalah", Subdata7)

Data2 = [100, 200, 300, 400, 500, 600]
print("\nData2 =", Data2)

print('\n--- Menambah list ---')
# Menambah list
Data3 = Data + Data2
print("Gabungan antara Data1 dengan Data2 adalah", Data3)
Data3 = [11, 22, 33, 44, 55]
Data3.extend(Data2)
print("Gabungan antara Data1 dengan Data2 menggunakan extend adalah", Data3)

Data2[:0] = '0'
print("Indeks pertama disisipkan nilai menjadi", Data2)
Data2[len(Data2):] = '1'
print("Indeks terakhir disisipkan nilai menjadi", Data2)

print('\n--- Mengubah nilai dari suatu indeks --- ')
# Mengubah konten / nilai dari suatu indeks dari list
Data2[1] = 250
print("Hasil Data2 yang dimodifikasi adalah", Data2)

print('\n--- Menghapus nilai dari suaru indeks ---')
Data2[0:1] = []
print("List setelah menghapus indeks pertama dan indeks kedua ", Data2)

print('\n--- Mengopy list ke variabel baru ---')
# Mengcopy list ke variabel baru
a = Data2[:]
print("Nilai a adalah", a)

print('\n--- Mengubah nilai dari suatu indeks dengan metode slicing ---')
# Mengubah konten list dengan menggunakan metode slicing
Data2[2:3] = [350, 450]
print("Hasil modifikasi pada Data2 indeks 2 s.d 3 adalah", Data2)

print('\n--- List multidimensi ---')
# List multidimensi (List dalam list)
x = [Data, Data2]
print("Data1 dan Data2 dalam list multidimensi adalah", x)

print('\n--- Mengakses list multidimensi ---')
# Mengakses list multidimensi
y1 = x[0][4]
print("Nilai pada baris ke-1 & kolom ke-5 dalam list multidimensi adalah", y1)
y2 = x[1][4]
print("Nilai pada baris ke-2 & kolom ke-5 dalam list multidimensi adalah", y2)

print('\n--- Method untuk list ---')
# Method untuk list
Data2.append(700)
print("Menambah satu member pada Data2 :", Data2)
Data2.insert(9, 650)
print("Menambah member pada indeks ke 10 :", Data2)

print('\n--- Function untuk list ---')
# Function yang bisa kita gunakan kepada list
panjangList = len(Data2)
print("Panjang list Data2 adalah", panjangList)
blablabla = callable(Data2)
print(blablabla)


print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
