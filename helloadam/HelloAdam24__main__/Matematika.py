#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.


def main():
    print("Ini adalah main")


def penjumlahan(a, b):
    print("--- Penjumlahan ---")
    hasil = a + b
    print(a, "+", b, "=", hasil)


def pengurangan(a, b):
    print("--- Pengurangan ---")
    hasil = a - b
    print(a, "-", b, "=", hasil)


def perkalian(a, b):
    print("--- Perkalian ---")
    hasil = a * b
    print(a, "*", b, "=", hasil)


def pembagian(a, b):
    print("--- Pembagian ---")
    hasil = a / b
    print(a, "/", b, "=", hasil)

if __name__ == "__main__":
    main()

