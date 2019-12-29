#  Copyright (c) 2019. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== WHILE LOOP ======\n")
angka = 0
while angka < 10:
    print("Nilai angka adalah :", angka)
    angka += 1
print("Di luar while")

angka2 = 0
start = True
while start:
    print("Nilai angka2 adalah :", angka2)
    angka2 += 1
    if angka2 is 10:
        print("Oke udah sampe angka 10 nih")
        start = False

angka3 = 0
while angka3 < 10:
    print("Nilai angka adalah :", angka3)
    angka3 += 1
    if angka3 is 7:
        print("Checkpoint gais, ini nomer", angka3)
        # break
        continue
        # pass
else:
    print("Nilai angka di akhir while adalah :", angka3)

print("Akhir dari program")

print(copyright)
# by Mbah Putih Mulyosugito
