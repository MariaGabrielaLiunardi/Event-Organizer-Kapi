from Database import fetch_one, fetch_all, execute_query
from tabulate import tabulate
import textwrap

# Menu utama untuk pemilik
def tampilkan_menu_pemilik():
    MENU_OPTIONS = {
        '2': menu_kelola_vendor,
        '3': menu_kelola_jenis_vendor
    }

    while True:
        print("\n=== Menu Pemilik ===")
        print("2. Kelola data vendor")
        print("3. Kelola data jenis vendor")
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



# Menu untuk kelola vendor
def menu_kelola_vendor():
    while True:
        print("--- Data Vendor ---")
        print("1. Lihat data vendor")
        print("2. Tambah vendor")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            break

        elif pilihan == '1':
            while True:
                print("--- Semua Data Vendor ---")
                lihat_semua_data_vendor()

                print("1. Lihat vendor spesifik")
                print("0. Kembali")

                pilihan = input("Pilih menu: ")
                print()

                if pilihan == '0':
                    break

                elif pilihan == '1':
                    print("--- Lihat Vendor Spesifik ---")
                    try:
                        id_Vendor = int(input("ID vendor: "))
                    except ValueError:
                        print("\nInput tidak valid. ID harus berupa angka.\n")
                        continue
                    hasil = lihat_data_vendor(id_Vendor)

                    if hasil != 'Vendor tidak ditemukan.':
                        print("1. Edit data vendor")
                        print("2. Hapus data vendor")
                        print("0. Kembali")

                        pilihan = input("Pilih menu: ")

                        if pilihan == '0':
                            break
                        elif pilihan == '1':
                            print("\n--- Daftar jenis vendor yang tersedia ---")
                            lihat_data_jenis_vendor()

                            print("\n---- Edit Data Vendor ---")
                            nama_baru = input("Nama vendor baru: ")
                            pemilik_baru = input("Pemilik baru: ")
                            alamat_baru = input("Alamat baru: ")
                            telepon_baru = input("Telepon baru: ")
                            email_baru = input("Email baru: ")

                            try:
                                harga_min_baru = int(input("Harga min baru: "))
                                harga_max_baru = int(input("Harga max baru: "))
                                id_JenisVendor = int(input("ID jenis vendor: "))
                            except ValueError:
                                print("\nInput tidak valid, harus berupa angka.\n")
                                continue
                            edit_data_vendor(nama_baru, pemilik_baru, alamat_baru, telepon_baru, email_baru, harga_min_baru, harga_max_baru, id_JenisVendor, id_Vendor)

                        elif pilihan == '2':
                            print("\nHapus Vendor?")
                            print("1. Ya")
                            print("2. Tidak")
                            pilihan = input("Pilih menu: ")

                            if pilihan == '1':
                                hapus_vendor(id_Vendor)
                            elif pilihan == '2':
                                break
                            else:
                                print("Pilihan tidak valid.")

                        else:
                            print("Pilihan tidak valid.")

                else:
                    print("Pilihan tidak valid.")

        elif pilihan == '2':
            print("--- Daftar jenis vendor yang tersedia ---")
            lihat_data_jenis_vendor()

            print("--- Tambah Vendor ---")
            nama = input("Nama: ")
            nama_pemilik = input("Nama Pemilik: ")
            alamat = input("Alamat: ")
            no_telepon = input("No Telepon: ")
            email = input("Email: ")

            try:
                harga_min = int(input("Harga Min: "))
                harga_max = int(input("Harga Max: "))
                id_JenisVendor = int(input("ID Jenis Vendor: "))
                tambah_vendor(nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, id_JenisVendor)
            except ValueError:
                print("\nInput tidak valid, harus berupa angka.\n")

        else:
            print("Pilihan tidak valid.")

        pass

# Menu untuk kelola jenis vendor
def menu_kelola_jenis_vendor():
    while True:
        print("--- Data Jenis Vendor ---")
        print("1. Lihat jenis vendor")
        print("2. Tambah jenis vendor")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            break
        elif pilihan == '1':
            print("--- Semua Jenis Vendor ---")
            lihat_data_jenis_vendor()
            print()

            print("1. Edit jenis vendor")
            print("0. Kembali")

            pilihan = input("Pilih menu: ")

            if pilihan == '0':
                break
            elif pilihan == '1':
                print("\n--- Edit Jenis Vendor ---")
                try:
                    id_JenisVendor = int(input("ID Jenis Vendor: "))
                except ValueError:
                    print("\nInput tidak valid, ID harus berupa angka.\n")
                    continue

                jenis_baru = input("Jenis baru: ")
                result = cek_jenis_vendor(jenis_baru)

                if result != 'Gagal, jenis vendor sudah ada.':
                    edit_jenis_vendor(id_JenisVendor, jenis_baru)
            else:
                print("Pilihan tidak valid.")

        elif pilihan == '2':
            print("--- Tambah Jenis Vendor ---")
            jenis_vendor = input("Jenis vendor: ")

            result = cek_jenis_vendor(jenis_vendor)
            if result != 'Gagal, jenis vendor sudah ada.':
                tambah_jenis_vendor(jenis_vendor)
        else:
            print("Pilihan tidak valid.")
        pass

# Fungsi untuk menu vendor
def tambah_vendor(nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, id_JenisVendor):
    if len(nama) > 60:
        print("\n input data vendor: nama terlalu panjang, max 60 karakter.\n")
        return
    elif len(nama_pemilik) > 60:
        print("\nGagal input data vendor: nama pemilik terlalu panjang, max 60 karakter.\n")
        return
    elif len(alamat) > 100:
        print("\nGagal input data vendor: alamat terlalu panjang, max 100 karakter.\n")
        return
    elif len(no_telepon) > 13:
        print("\nGagal input data vendor: no telepon terlalu panjang, max 14 karakter.\n")
        return
    elif len(email) > 320:
        print("\nGagal input data vendor: email terlalu panjang, max 320 karakter.\n")
        return

    query = '''INSERT INTO 
                    Vendor (nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, id_JenisVendor)
               VALUES 
                    (?, ?, ?, ?, ?, ?, ?, ?)'''
    print()
    print("Input data vendor berhasil.") if execute_query(query, (nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, id_JenisVendor)) else print("Input data vendor gagal.")

def tambah_jenis_vendor(jenis_vendor):
    query = '''INSERT INTO 
                    JenisVendor 
               VALUES 
                    (?)
            '''
    print()
    print("Input jenis vendor berhasil.") if execute_query(query, (jenis_vendor,)) else print("Input jenis vendor gagal.")

def lihat_semua_data_vendor():
    hasil = fetch_all('''SELECT 
                             id_Vendor, nama, alamat, harga_min, harga_max, jenis_vendor 
                         FROM 
                             Vendor 
                             JOIN JenisVendor ON Vendor.id_JenisVendor = JenisVendor.id_JenisVendor 
                         WHERE 
                             isActive = 1''')
    print()

    if hasil:
        hasil_format = [(id_Vendor, nama_vendor, alamat, format_rupiah(harga_min), format_rupiah(harga_max), jenis_vendor)
                        for id_Vendor, nama_vendor, alamat, harga_min, harga_max, jenis_vendor in hasil]
        kolom = ['ID', 'Nama Vendor', 'Alamat', 'Harga Min', 'Harga Max', 'Jenis Vendor']
        print(tabulate(hasil_format, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada data vendor ditemukan.")
    print()

def lihat_data_vendor(id_Vendor):
    hasil = fetch_one('''SELECT 
                                    nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, jenis_vendor 
                                FROM 
                                    Vendor 
                                    JOIN JenisVendor ON Vendor.id_JenisVendor = JenisVendor.id_JenisVendor 
                                WHERE isActive = 1 AND Vendor.id_Vendor = ?''', (id_Vendor,))
    print()

    if hasil:
        # Unpack tuple-nya
        nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, jenis_vendor = hasil

        alamat = textwrap.fill(alamat, width=25)
        email = textwrap.fill(email, width=20)

        # Format harga ke dalam format rupiah
        data_format = [nama, nama_pemilik, alamat, no_telepon, email, format_rupiah(harga_min), format_rupiah(harga_max), jenis_vendor]
        kolom = ['Nama Vendor', 'Pemilik', 'Alamat', 'No Telepon', 'Email', 'Harga Min', 'Harga Max', 'Jenis Vendor']
        print(tabulate([data_format], headers=kolom, tablefmt='grid'))
    else:
        print("Vendor tidak ditemukan.")
        return "Vendor tidak ditemukan."
    print()

def edit_data_vendor(nama_baru, pemilik_baru, alamat_baru, telepon_baru, email_baru, harga_min_baru, harga_max_baru, id_JenisVendor, id_Vendor):
    if len(nama_baru) > 60:
        print("\nGagal mengubah data vendor: nama terlalu panjang, max 60 karakter.\n")
        return
    elif len(pemilik_baru) > 60:
        print("\nGagal mengubah data vendor: nama pemilik terlalu panjang, max 60 karakter.\n")
        return
    elif len(alamat_baru) > 100:
        print("\nGagal mengubah data vendor: alamat terlalu panjang, max 100 karakter.\n")
        return
    elif len(telepon_baru) > 13:
        print("\nGagal mengubah data vendor: no telepon terlalu panjang, max 14 karakter.\n")
        return
    elif len(email_baru) > 320:
        print("\nGagal mengubah data vendor: email terlalu panjang, max 320 karakter.\n")
        return

    query = '''UPDATE 
                    Vendor 
               SET 
                    nama = ?, nama_pemilik = ?, alamat = ?, no_telepon = ?, email = ?, harga_min = ?, harga_max = ?, id_JenisVendor = ? 
                WHERE 
                    id_Vendor = ?'''
    print("Data vendor berhasil diubah.") if execute_query(query, (nama_baru, pemilik_baru, alamat_baru, telepon_baru, email_baru, harga_min_baru, harga_max_baru, id_JenisVendor, id_Vendor)) else print("Gagal mengubah data vendor.")

def hapus_vendor(id_Vendor):
    query = '''UPDATE 
                   Vendor 
               SET 
                   isActive = 0 
               WHERE 
                   id_Vendor = ?'''
    print()
    print("Data vendor berhasil dihapus.\n") if execute_query(query, (id_Vendor,)) else print("Gagal menghapus vendor.\n")

# Fungsi untuk Jenis Vendor
def lihat_data_jenis_vendor():
    hasil = fetch_all('''SELECT 
                             * 
                         FROM 
                             JenisVendor''')

    if hasil:
        kolom = ['ID', 'Jenis Vendor']
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
    else:
        print("Tidak ada data jenis vendor ditemukan.\n")

def edit_jenis_vendor(id_JenisVendor, jenis_baru):
    if len(jenis_baru) > 50:
        print("Gagal mengubah data jenis vendor: jenis vendor terlalu panjang, max 50 karakter.\n")
        return

    query = '''UPDATE 
                   JenisVendor 
               SET 
                   jenis_vendor = ? 
               WHERE 
                   id_JenisVendor = ?'''
    print("Jenis vendor berhasil diperbarui.\n") if execute_query(query, (jenis_baru, id_JenisVendor)) else print("Gagal memperbarui jenis vendor.\n")

def cek_jenis_vendor(jenis_vendor):
    hasil = fetch_one('''SELECT 
                             id_JenisVendor
                         FROM
                             JenisVendor
                         WHERE
                             jenis_vendor = ?''', (jenis_vendor))
    print()
    if hasil:
        print("Gagal, jenis vendor sudah ada.\n")
        return "Gagal, jenis vendor sudah ada."
    else:
        return

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

# Menu untuk kelola vendor
def menu_kelola_vendor():
    while True:
        print("--- Data Vendor ---")
        print("1. Lihat data vendor")
        print("2. Tambah vendor")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            break

        elif pilihan == '1':
            while True:
                print("--- Semua Data Vendor ---")
                lihat_semua_data_vendor()

                print("1. Lihat vendor spesifik")
                print("0. Kembali")

                pilihan = input("Pilih menu: ")
                print()

                if pilihan == '0':
                    break

                elif pilihan == '1':
                    print("--- Lihat Vendor Spesifik ---")
                    try:
                        id_Vendor = int(input("ID vendor: "))
                    except ValueError:
                        print("\nInput tidak valid. ID harus berupa angka.\n")
                        continue
                    hasil = lihat_data_vendor(id_Vendor)

                    if hasil != 'Vendor tidak ditemukan.':
                        print("1. Edit data vendor")
                        print("2. Hapus data vendor")
                        print("0. Kembali")

                        pilihan = input("Pilih menu: ")

                        if pilihan == '0':
                            break
                        elif pilihan == '1':
                            print("\n--- Daftar jenis vendor yang tersedia ---")
                            lihat_data_jenis_vendor()

                            print("\n---- Edit Data Vendor ---")
                            nama_baru = input("Nama vendor baru: ")
                            pemilik_baru = input("Pemilik baru: ")
                            alamat_baru = input("Alamat baru: ")
                            telepon_baru = input("Telepon baru: ")
                            email_baru = input("Email baru: ")

                            try:
                                harga_min_baru = int(input("Harga min baru: "))
                                harga_max_baru = int(input("Harga max baru: "))
                                id_JenisVendor = int(input("ID jenis vendor: "))
                            except ValueError:
                                print("\nInput tidak valid, harus berupa angka.\n")
                                continue
                            edit_data_vendor(nama_baru, pemilik_baru, alamat_baru, telepon_baru, email_baru, harga_min_baru, harga_max_baru, id_JenisVendor, id_Vendor)

                        elif pilihan == '2':
                            print("\nHapus Vendor?")
                            print("1. Ya")
                            print("2. Tidak")
                            pilihan = input("Pilih menu: ")

                            if pilihan == '1':
                                hapus_vendor(id_Vendor)
                            elif pilihan == '2':
                                break
                            else:
                                print("Pilihan tidak valid.")

                        else:
                            print("Pilihan tidak valid.")

                else:
                    print("Pilihan tidak valid.")

        elif pilihan == '2':
            print("--- Daftar jenis vendor yang tersedia ---")
            lihat_data_jenis_vendor()

            print("--- Tambah Vendor ---")
            nama = input("Nama: ")
            nama_pemilik = input("Nama Pemilik: ")
            alamat = input("Alamat: ")
            no_telepon = input("No Telepon: ")
            email = input("Email: ")

            try:
                harga_min = int(input("Harga Min: "))
                harga_max = int(input("Harga Max: "))
                id_JenisVendor = int(input("ID Jenis Vendor: "))
                tambah_vendor(nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, id_JenisVendor)
            except ValueError:
                print("\nInput tidak valid, harus berupa angka.\n")

        else:
            print("Pilihan tidak valid.")

        pass