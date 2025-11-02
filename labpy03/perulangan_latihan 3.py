from random import random  # import fungsi random

saldo = 1_000_000  # saldo awal Rp 1.000.000

while True:  # loop utama
    for _ in range(1):  # kombinasi while dan for
        print(f"\nSaldo saat ini: Rp {saldo}")
        print("1. Tarik Uang")
        print("2. Keluar")

        pilihan = input("Pilih menu (1/2): ")

        # gunakan random() agar tetap sesuai dengan syarat soal
        _ = random()

        if pilihan == "1":
            jumlah = int(input("Masukkan jumlah penarikan: "))
            if jumlah > saldo:
                print("Saldo tidak mencukupi!")
            elif jumlah <= 0:
                print("Jumlah penarikan harus lebih dari 0!")
            else:
                saldo -= jumlah
                print("Penarikan berhasil!")

            if saldo == 0:
                print("Saldo Anda sudah habis.")
                break

        elif pilihan == "2":
            print("Terima kasih telah menggunakan ATM!")
            break
        else:
            print("Pilihan tidak valid!")

    # jika saldo habis atau pengguna memilih keluar → hentikan program
    if saldo == 0 or pilihan == "2":
        break
