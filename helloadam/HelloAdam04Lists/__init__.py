#  Copyright (c) 2019. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== LIST =====\n")    # Semacam array di Python

Data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Data =", Data)
# Mengakses list
Subdata1 = Data[2]
print("Nilai pada indeks ke 2 adalah", Subdata1)
Subdata2 = Data[-2]
print("Nilai pada indeks ke -2 adalah", Subdata2)

# Memotong list
Subdata3 = Data[0:5]
print("Nilai pada indeks 0 s.d 5 adalah", Subdata3)
Subdata4 = Data[:5]
print("Nilai pada awal indeks s.d indeks ke 5 adalah", Subdata4)
Subdata5 = Data[5:]
print("Nilai pada indeks ke 5 s.d akhir indeks adalah", Subdata5)
Subdata6 = Data[5:10]
print("Nilai pada indeks ke 5 s.d 10 adalah", Subdata6)

Data2 = [100, 200, 300, 400, 500, 600]
print("\nData2 = ", Data2)
# Menambah list
Data3 = Data + Data2
print("Gabungan antara Data1 dengan Data2 adalah", Data3)

# Mengubah konten / nilai dari suatu indeks dari list
Data2[1] = 250
print("Hasil Data2 yang dimodifikasi adalah", Data2)

# Mengcopy list ke variabel baru
a = Data2[:]
print("Nilai a adalah", a)

# Mengubah konten list dengan menggunakan metode slicing
Data2[2:3] = [350, 450]
print("Hasil modifikasi pada Data2 indeks 2 s.d 3 adalah", Data2)

# List multidimensi (List dalam list)
x = [Data, Data2]
print("Data1 dan Data2 dalam list multidimensi adalah", x)

# Mengakses list multidimensi
y1 = x[0][4]
print("Nilai pada baris ke-1 & kolom ke-5 dalam list multidimensi adalah", y1)
y2 = x[1][4]
print("Nilai pada baris ke-2 & kolom ke-5 dalam list multidimensi adalah", y2)

# Method untuk list
Data2.append(700)
print("Menambah satu member pada Data2 :", Data2)

# Function yang bisa kita gunakan kepada list
panjangList = len(Data2)
print("Panjang list Data2 adalah", panjangList)

print(copyright)
# by Mbah Putih Mulyosugito
