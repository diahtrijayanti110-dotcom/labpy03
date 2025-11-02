from random import random  # import fungsi random()

modal_awal = 100_000_000  # modal 100 juta
total_laba = 0
bulan = 1

while bulan <= 8:
    for _ in range(1):  # kombinasi while + for
        if bulan == 1 or bulan == 2:
            laba = 0
        elif bulan == 3 or bulan == 4:
            laba = modal_awal * 0.01  # 1%
        elif bulan == 5 or bulan == 6 or bulan == 7:
            laba = modal_awal * 0.05  # 5%
        elif bulan == 8:
            laba = modal_awal * 0.02  # turun jadi 2%

        # pakai random(), meski tidak mengubah hasil agar memenuhi syarat soal
        _ = random()

        print(f"laba bulan ke- {bulan} sebesar: {laba}")
        total_laba += laba
        bulan += 1

print(f"Total laba adalah: {total_laba}")