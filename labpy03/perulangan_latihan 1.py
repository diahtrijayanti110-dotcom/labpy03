from random import random

# Input nilai n saat runtime
n = int(input("Masukkan Nilai N: "))

count = 0  # penghitung bilangan yang sudah muncul

while count < n:
    for _ in range(1):  # menggunakan for di dalam while
        angka = random()
        if angka < 0.5:
            count += 1
            print(f"data ke: {count} => {angka}")
            if count == n:
                break

print("Selesai")
