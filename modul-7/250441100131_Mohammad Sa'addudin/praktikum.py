Kupon = {
    "DISC", 20,
    "PROMO", 10,
    "HEMAT", 5,
}

while True:
    print("===pilih 1-3 ===")
    print("1.tampilkan kupon")
    print("2.total belanja")
    print("3. selesai")

    nama = input("pilih menu 1-3")

    def tampilkan_kupon():
        nama = input("masukkan nama kupon")
        if nama in Kupon:
            print("kupon masih tersedia").strip()
        elif nama not in Kupon:
            print("Kupon tidak tersedia")
        else:
            print("inputan tidak valid")
    
    def total_belanja():
        nama = input("masukkan total belanja")

        if nama in belanja:

    
