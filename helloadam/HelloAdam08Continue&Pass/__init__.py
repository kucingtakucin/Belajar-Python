#  Copyright (c) 2019. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== CONTINUE & PASS ======\n")
for i in range(0, 11):
    if i is 7:
        print("Nilai i adalah", i)
        # break = fungsinya untuk mengakhiri for (terminasi)
        # continue = fungsinya untuk melanjutkan ke perulangan berikutnya dan tidak mengeksekusi statement dibawahnya
        pass    # pass tidak melakukan apa-apa
        print("Cek teman-teman wkwk")

    print("Nilai saat ini adalah", i)
else:
    print("Akhir dari looping")

print("Akhir dari program")

print(copyright)
# by Mbah Putih Mulyosugito
