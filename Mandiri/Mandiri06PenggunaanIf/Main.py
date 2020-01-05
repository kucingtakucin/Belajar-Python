#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== PENGGUNAAN STATEMENT IF ======\n")
Angka = [0, 1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
print("--- Menghitung jumlah elemen tertentu di dalam list")
for indeks1, elemen1 in enumerate(Angka):
    hitung = 0
    # print("Perulangan ke", indeks)
    if elemen1 is Angka[len(Angka) - 1]:
        break
        pass
    if elemen1 is Angka[indeks1 + 1]:
        if elemen1 is Angka[len(Angka) - 2]:
            pass
        continue
        pass
    pass
    for indeks2, elemen2 in enumerate(Angka):
        if elemen1 is 0 and Angka[indeks2] is not Angka[indeks2 + 1]:
            hitung = 1
            break
            pass
        if elemen2 is Angka[len(Angka) - 1]:
            break
            pass
        elif elemen1 is Angka[indeks2 + 1]:
            hitung += 1
            pass
        pass
    pass
    print("Angka %d ada %d" % (elemen1, hitung))

print("\n--- ACCESS TO NIGHT CLUB PARTY")
umur = int(input("Masukkan umur kamu : "))
if umur >= 18 and umur <= 35:
    print("Anda boleh masuk")
    pass
else:
    print("Anda tidak boleh masuk")

print("\n--- HAK UNTUK MENGENDARAI MOBIL FERRARI")
print("Untuk mengendarai mobil ferrari kamu harus menjawab pertanyaan berikut : ")
SIM = input("Apakah kamu sudah memiliki SIM ? (Y/N) ")
bisa = input("Apakah kamu benar-benar bisa mengendarai mobil ? (Y/N) ")

if SIM is "Y" or bisa is 'y':
    print("Silahkan mengendarai mobil ini, semoga perjalanan anda menyenangkan!")
    pass

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
