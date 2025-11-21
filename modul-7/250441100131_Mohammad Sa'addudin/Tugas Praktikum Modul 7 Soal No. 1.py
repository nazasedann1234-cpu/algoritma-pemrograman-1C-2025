kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("tidak ada kontak yang tersimpan.")
    else:
        print("daftar kontak: ")
        for nama, details in kontak.items():
            print(f"nama: {nama}, telepon: {details[0]}, email: {details[1]}")

def cari_kontak():
    nama = input("masukkan nama kontak yang ingin dicari: ").strip()
    if nama in kontak:
        details = kontak[nama]
        print(f"nama: {nama}, telepon: {details[0]}, email: {details[1]}")
    else:
        print("kontak tidak ditemukan")

def valid_telepon(no):
    no = no.strip()  
    if not no.isdigit(): 
        return False
    if not (10 <= len(no) <= 13):
        return False
    return True

def tambah_kontak():
    nama = input("masukkan nama kontak: ").strip()
    if not nama:
        print("nama tidak boleh kosong")
        return
    while True:
        telepon = input("masukkan nomor telepon: ").strip()
        if valid_telepon(telepon):
            break
        else:
            print("nomor telepon tidak valid. harus angka dan terdiri dari 10-12 digit.")
    while True:            
        email = input("masukkan email: ").strip()
        if email.endswith("@gmail.com"):
            break
        else:
            print("format email tidak valid")

    if nama in kontak:
        print("kontak dengan nama tersebut sudah ada")
    else:
        kontak[nama] = [telepon, email]
        print("kontak berhasil ditambahkan")
    
def update_email():
    nama = input("masukkan nama kontak yang ingin diupdate emailnya: ").strip()
    if nama in kontak:
        while True:
            new_email = input("masukkan email baru: ").strip()
            if new_email.endswith("@gmail.com"):
                break
            else:
                print("format email tidak valid. email harus berakhiran @gmail.com")       
        
        kontak[nama][1] = new_email
        print("email berhasil diupdate")
    else:
        print("kontak tidak ditemukan")

def hapus_kontak():
    nama = input("masukkan nama yang ingin dihapus: ").strip()
    if nama in kontak:
        del kontak[nama]
        print("kontak berhasil dihapus")
    else:
        print("kontak tidak ditemukan")

def main():
    while True:
        print("\nMenu Contact Book:")
        print("1. Tampilkan semua kontak")
        print("2. Cari kontak berdasarkan nama")
        print("3. Tambah kontak baru")
        print("4. Update email kontak")
        print("5. Hapus kontak")
        print("6. Keluar")
        
        try:
            menu = int(input("Pilih opsi (1-6): "))
            if menu == 1:
                tampilkan_kontak()
            elif menu == 2:
                cari_kontak()
            elif menu == 3:
                tambah_kontak()
            elif menu == 4:
                update_email()
            elif menu == 5:
                hapus_kontak()
            elif menu == 6:
                print("Terima kasih telah menggunakan Contact Book.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1-6.")
        except ValueError:
            print("Input tidak valid. Masukkan angka antara 1-6.")

main()
    


