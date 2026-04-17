def fibonacci(n):
    a, b = 0, 1
    hasil = []
    for i in range(n):
        hasil.append(b)
        a, b = b, a + b
    return hasil

while True:
    print("\nMenu Pilihan")
    print("1. Barisan Fibonacci")
    print("2. M x N")
    print("0. Keluar")

    pilih = int(input("Pilih Menu: "))

    if pilih == 1:
        n = int(input("Masukkan jumlah suku: "))
        hasil = fibonacci(n)
        print("Barisan Fibonacci sebanyak", n, "suku:", hasil)

    elif pilih == 2:
        m = int(input("Masukkan bilangan: "))
        n = int(input("Masukkan pengali: "))
        print(m, "x", n, "=", m*n)

    elif pilih == 0:
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
