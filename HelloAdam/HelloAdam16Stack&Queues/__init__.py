#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from _collections import deque
from sys import copyright

print("====== STACK & QUEUES ======\n")

# Stack / Tumpukan
tumpukan = [0, 1, 2, 3, 4, 5, 6, 7]
print("Tumpukan sekarang :", tumpukan)

tumpukan.append(8)      # Menambahkan data tumpukan
print("Data masuk :", 8)
print("Tumpukan sekarang :", tumpukan)

out = tumpukan.pop()    # Mengurangi jumlah tumpukan
print("Data keluar :", out)
print("Tumpukan sekarang :", tumpukan)
out = tumpukan.pop()
print("Data keluar :", out)
print("Tumpukan sekarang :", tumpukan)

# Queues / Antrian
antrian = deque([0, 1, 2, 3, 4, 5, 6, 7])
print("Antrian sekarang :", antrian)

antrian.append(8)       # Menambahkan data antrian
print("Data masuk :", 8)
print("Antrian sekarang :", antrian)
antrian.append(9)
print("Data masuk :", 9)
print("Antrian sekarang :", antrian)

out = antrian.popleft()     # Mengurangi jumlah antrian
print("Data keluar :", out)
print("Antrian sekarang :", antrian)
out = antrian.popleft()
print("Data keluar :", out)
print("Data sekarang :", antrian)
out = antrian.popleft()
print("Data keluar :", out)
print("Data sekarang :", antrian)
antrian.append(10)
print("Data masuk :", 10)
print("Data sekarang :", antrian)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
