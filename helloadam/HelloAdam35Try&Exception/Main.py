#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
from sys import copyright

print("====== TRY & EXCEPTION ======\n")

while True:
    try:
        pembilang = int(input("Masukkan angka pembilang : "))
        penyebut = int(input("Masukkan angka penyebut : "))
        hasil = pembilang / penyebut
        break
        pass
    except ValueError:
        print("Yang kamu masukkan bukan angka!")
        pass
    except ZeroDivisionError:
        print("Penyebut tidak boleh nol!")
        pass
    except ImportError:
        print("Modul yang kamu cari engga ada!")
        pass
    except Exception as err:
        print(err)
        pass

    """
    Type of exception errors :
    1. IOError
    2. ImportError
    3. ValueError
    4. ZeroDivisionerror
    5. KeyboardInterupted
    6. EOError
    """

print("Hore berhasil, hasil pembagian adalah", hasil)

print('\n')
print(copyright)
# by Mbah Putih Mulyosugito
