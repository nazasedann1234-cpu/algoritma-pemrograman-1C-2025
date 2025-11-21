kupon = {
    "DISC10": 10,
    "HEMAT20": 20,
    "PROMO5": 5
}

while True:
    print("\n=== SISTEM KUPON ===")
    print("1. Tampilkan Semua Kupon")
    print("2. Proses Transaksi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("Kupon tersedia:")
        for kode, diskon in kupon.items():
            print(f"{kode}: {diskon}%")

    elif pilihan == "2":
        while True:
            try:
                total = float(input("Total belanja: "))
                if total < 0:
                    print("total tidak boleh negatif")
                    continue
                break
            except ValueError:
                print("input tidak valid. masukkan angka!")
        
        kode = input("Masukkan kode kupon: ")
        
        if kode in kupon:
            diskon = kupon[kode]
            potongan = total * (diskon / 100)
            total_bayar = total - potongan

            print(f"Diskon {diskon}% digunakan!")
            print(f"Total bayar: {total_bayar:.0f}")

            del kupon[kode]  
        else:
            print("Kode kupon tidak valid atau sudah dipakai.")

    elif pilihan == "3":
        break

    else:
        print("Menu tidak valid.")