from Database import fetch_one, fetch_all, execute_query
from tabulate import tabulate
import textwrap

# Menu utama untuk pemilik
def tampilkan_menu_pemilik():
    MENU_OPTIONS = {
        '1': menu_kelola_asisten,
    }

    while True:
        print("\n=== Menu Pemilik ===")
        print("1. Kelola asisten")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            print("Keluar dari menu pemilik.")
            break
        elif pilihan in MENU_OPTIONS:
            MENU_OPTIONS[pilihan]()
        else:
            print("Pilihan tidak valid.\n")

# Menu untuk kelola asisten
def menu_kelola_asisten():
    while True:
        print("--- Data Asisten ---")

        print("1. Lihat data asisten")
        print("2. Tambah asisten")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            break

        elif pilihan =='1':
            print("--- Semua Data Asisten ---")
            lihat_semua_data_asisten()

            print("1. Lihat data asisten spesifik")
            print("0. Kembali")

            pilihan = input("Pilih menu: ")

            if pilihan == '0':
                break
            elif pilihan == '1':
                print("\n--- Data Asisten Spesifik ---")

                try:
                    id_User = int(input("ID asisten: "))
                    result = lihat_data_asisten(id_User)

                    if result != 'Asisten tidak ditemukan.':
                        print("1. Edit data asisten")
                        print("2. Hapus data asisten")
                        print("0. Kembali")

                        pilihan = input("Pilih menu: ")
                        print()

                        if pilihan == '0':
                            break
                        elif pilihan == '1':
                            print("--- Edit Data Asisten ---")
                            nama_baru = input("Nama Baru: ")
                            alamat_baru = input("Alamat Baru: ")
                            telepon_baru = input("Telepon Baru: ")
                            email_baru = input("Email Baru: ")

                            edit_data_asisten(id_User, nama_baru, alamat_baru, telepon_baru, email_baru)

                        elif pilihan == '2':
                            print("\nHapus Asisten?")
                            print("1. Ya")
                            print("2. Tidak")
                            pilihan = input("Pilih menu: ")

                            if pilihan == '1':
                                hapus_asisten(id_User)
                            elif pilihan == '2':
                                break
                            else:
                                print("Pilihan tidak valid.\n")

                        else:
                            print("Pilihan tidak valid.\n")

                except ValueError:
                    print("\nInput tidak valid. ID harus berupa angka.\n")

            else:
                print("Pilihan tidak valid.\n")

        elif pilihan == '2':
            print("--- Tambah Asisten ---")
            username = input("Username: ")
            password = input("Password: ")
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            no_telepon = input("No Telepon: ")
            email = input("Email: ")
            role = 'asisten'

            hasil = cek_username(username)
            if hasil != 'Gagal, username sudah ada.':
                tambah_asisten(username, password, nama, alamat, no_telepon, email, role)

        else:
            print("Pilihan tidak valid.")
        pass

# Fungsi untuk menu asisten
def tambah_asisten(username, password, nama, alamat, no_telepon, email, role):
    if len(username) > 50:
        print("\nGagal input data asisten: username terlalu panjang, max 50 karakter.\n")
        return
    elif len(password) > 50:
        print("\nGagal input data asisten: password terlalu panjang, max 20 karakter.\n")
        return
    elif len(nama) > 60:
        print("\nGagal input data asisten: nama terlalu panjang, max 60 karakter.\n")
        return
    elif len(alamat) > 100:
        print("\nGagal input data asisten: alamat terlalu panjang, max 100 karakter.\n")
        return
    elif len(no_telepon) > 13:
        print("\nGagal input data asisten: no telepon terlalu panjang, max 14 karakter.\n")
        return
    elif len(email) > 320:
        print("\nGagal input data asisten: email terlalu panjang, max 320 karakter.\n")
        return

    query = '''INSERT INTO 
                   [User] 
               VALUES 
                   (?, ?, ?, ?, ?, ?, ?)'''
    print("Input data asisten berhasil.") if execute_query(query, (username, password, nama, alamat, no_telepon, email, role)) else print("Input data asisten gagal.")

def cek_username(username):
    hasil = fetch_one('''SELECT
                    id_User
                FROM
                    [User]
                WHERE
                    username = ?''', (username))
    print()
    if hasil:
        print("Gagal, username sudah ada.\n")
        return "Gagal, username sudah ada."
    else:
        return

def lihat_semua_data_asisten():
    hasil = fetch_all('''SELECT 
                             id_User, nama, alamat, no_telepon, email 
                         FROM 
                             [User]
                         WHERE 
                             role = 'asisten' AND isActive = 1''')
    print()
    if hasil:
        kolom = ['ID', 'Nama', 'Alamat', 'No Telepon', 'Email']  # Sesuaikan dengan struktur tabelmu
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada data asisten ditemukan.")
    print()

def lihat_data_asisten(id_User):
    hasil = fetch_one('''SELECT 
                                    id_User, nama, alamat, no_telepon, email 
                                FROM 
                                    [User] 
                                WHERE 
                                    id_User = ? AND isActive = 1 AND role = 'asisten' ''', (id_User,))
    print()

    if hasil:
        kolom = ['ID', 'Nama', 'Alamat', 'Nomor Telepon', 'Email']
        print(tabulate([hasil], headers=kolom, tablefmt='grid'))
    else:
        print("Asisten tidak ditemukan.\n")
        return "Asisten tidak ditemukan."
    print()

def edit_data_asisten(id_User, nama_baru, alamat_baru, telepon_baru, email_baru):
    if len(nama_baru) > 60:
        print("\nGagal mengubah data asisten: nama terlalu panjang, max 60 karakter.\n")
        return
    elif len(alamat_baru) > 100:
        print("\nGagal mengubah data asisten: alamat terlalu panjang, max 100 karakter.\n")
        return
    elif len(telepon_baru) > 13:
        print("\nGagal mengubah data asisten: no telepon terlalu panjang, max 14 karakter.\n")
        return
    elif len(email_baru) > 320:
        print("\nGagal mengubah data asisten: email terlalu panjang, max 320 karakter.\n")
        return

    query = '''UPDATE 
                   [User] 
               SET 
                   nama = ?, alamat = ?, no_telepon = ?, email = ? 
               WHERE 
                   id_User = ?'''
    print()
    print("Data asisten berhasil diubah.") if execute_query(query, (nama_baru, alamat_baru, telepon_baru, email_baru, id_User)) else print("Gagal mengubah data asisten.")

def hapus_asisten(id_User):
    query = '''UPDATE 
                   [User] 
               SET 
                   isActive = 0 
               WHERE 
                   id_User = ?'''
    print()
    print("Data asisten berhasil dihapus.\n") if execute_query(query, (id_User,)) else print("Gagal menghapus data asisten.")