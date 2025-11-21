inventaris = {}

while True:
    print("\n========= MENU INVENTARIS GUDANG =========")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Tambah Barang Baru")
    print("4. Perbarui Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":        
        if not inventaris:
            print("Tidak ada data barang di inventaris.")
        else:
            for ID, data in inventaris.items():
                nama, harga, stok = data
                print(f"ID: {ID} | Nama: {nama} | Harga: {harga} | Stok: {stok}")

    elif pilihan == "2":
        ID = input("Masukkan ID barang: ")
        if ID in inventaris:
            nama, harga, stok = inventaris[ID]
            print(f"Nama: {nama}, Harga: {harga}, Stok: {stok}")
        else:
            print("Barang dengan ID tersebut tidak ditemukan.")

    elif pilihan == "3":
        ID = input("ID Barang: ")
        if ID in inventaris:
            print("ID sudah digunakan! Gunakan ID lain.")
            continue

        nama = input("Nama Barang: ")

        while True:
            try:
                harga = int(input("Harga: "))
                if harga < 0:
                    print("Harga tidak boleh negatif! Coba lagi.")
                    continue
                break
            except ValueError:
                print("Harga harus berupa angka! Coba lagi.")

        while True:
            try:
                stok = int(input("Stok: "))
                if stok < 0:
                    print("Stok tidak boleh negatif! Coba lagi.")
                    continue
                break
            except ValueError:
                print("Stok harus berupa angka! Coba lagi.")

        inventaris[ID] = [nama, harga, stok]
        print("Barang berhasil ditambahkan!")

    elif pilihan == "4":
        ID = input("Masukkan ID barang: ")
        if ID in inventaris:
            while True:
                try:
                    perubahan = int(input("Jumlah perubahan stok (+/-): "))
                    if inventaris[ID][2] + perubahan < 0:
                        print("Error: Stok tidak boleh negatif! Ulangi input.")
                        continue
                    break
                except ValueError:
                    print("Input harus berupa angka! Coba lagi.")

            inventaris[ID][2] += perubahan
            print("Stok berhasil diperbarui!")
        else:
            print("Barang tidak ditemukan.")

    elif pilihan == "5":
        ID = input("Masukkan ID barang yang akan dihapus: ")
        if ID in inventaris:
            del inventaris[ID]
            print("Barang berhasil dihapus!")
        else:
            print("Barang tidak ditemukan.")

    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Menu tidak valid. Silakan pilih antara 1–6.")
