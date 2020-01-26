#  Copyright (c) 2020. Adam Arthur Faizal


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

