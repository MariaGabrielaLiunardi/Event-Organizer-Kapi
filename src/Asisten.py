from Database import fetch_one, fetch_all, execute_query
from tabulate import tabulate
from Pemilik import lihat_data_jenis_vendor
import textwrap

# Menu utama untuk asisten
def tampilkan_menu_asisten(id_User):
    while True:
        print("\n=== Menu Asisten ===")
        print("1. Kelola data klien")
        print("2. Kelola data event")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            print("Keluar dari menu asisten.")
            break
       
        elif pilihan == '2':
            menu_event(id_User)
        else:
            print("Pilihan tidak valid.")

# Menu untuk kelola event
def menu_event(id_User):
    while True:
        print("--- Kelola Data Event ---")
        print("1. Lihat semua event")
        print("2. Tambah event")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == '0':
            break
        elif pilihan == '1':
            print("\n--- Lihat Semua Event ---")
            lihat_data_event()

            print("1. Lihat event spesifik")
            print("0. Kembali")

            pilihan = input("Pilih menu: ")

            if pilihan == '0':
                break
            elif pilihan == '1':
                print("\n--- Lihat Event Spesifik ---")

                try:
                    id_Event = int(input("ID event: "))
                except ValueError:
                    print("\nInput tidak valid. ID harus berupa angka.\n")
                    continue

                result = lihat_event_spesifik(id_Event)
                if result != "Tidak ada event untuk klien ini.":
                    print("1. Lihat rincian budgeting")
                    print("2. Edit event")
                    print("3. Hapus event")
                    print("0. Kembali")

                    pilihan = input("Pilih menu: ")

                    if pilihan == '0':
                        break
                    
                    elif pilihan == '2':
                        nama = input("Nama event: ")
                        tanggal_event = input("Tanggal (YYYYMMDD): ")
                        try:
                            jumlah_undangan = int(input("Jumlah undangan: "))
                        except ValueError:
                            print("Input tidak valid, jumlah undangan harus berupa angka.")
                            continue
                        lokasi = input("Lokasi: ")
                        try:
                            total_budget = int(input("Total budget: "))
                        except ValueError:
                            print("Input tidak valid, total budget harus berupa angka.\n")
                            continue
                        edit_event(id_Event, nama, tanggal_event, jumlah_undangan, lokasi, total_budget)

                    elif pilihan == '3':
                        print("\nHapus Event?")
                        print("1. Ya")
                        print("2. Tidak")
                        pilihan = input("Pilih menu: ")

                        if pilihan == '1':
                            hapus_event(id_Event)
                        elif pilihan == '2':
                            break
                        else:
                            print("Pilihan tidak valid.")

                    else:
                        print("Pilihan tidak valid.")

            else:
                print("Pilihan tidak valid.")

        elif pilihan == '2':
            print("Daftar jenis event yang tersedia")
            lihat_data_jenis_event()

            print('--- Input Data Event ---')
            nama = input("Nama event: ")
            tanggal_event = input("Tanggal event (YYYYMMDD): ")

            try:
                jumlah_undangan = int(input("Jumlah undangan: "))
            except ValueError:
                print("\nInput tidak valid, jumlah undangan berupa angka.\n")
                continue

            lokasi = input("Lokasi: ")

            try:
                total_budget = int(input("Total budget: "))
                id_Klien = int(input("ID klien: "))
                id_JenisEvent = int(input("ID jenis event: "))
            except ValueError:
                print("\nInput tidak valid, harus berupa angka.\n")
                continue
            tambah_event(nama, tanggal_event, jumlah_undangan, lokasi, total_budget, id_Klien, id_JenisEvent)
            tambah_user_event(id_User)

        else:
            print("Pilihan tidak valid.")

# Menu untuk vendor
def menu_vendor():
    while True:
        print("--- Data Vendor ---")

        print("1. Lihat semua vendor")
        print("2. Lihat vendor berdasarkan jenisnya")
        print("0. Kembali")

        pilihan = input("Pilih menu: ")

        if pilihan == '0':
            break
        elif pilihan =='1':
            lihat_semua_data_vendor()
        elif pilihan == '2':
            print("Daftar jenis vendor yang tersedia")
            lihat_data_jenis_vendor()

            try:
                id_JenisVendor = int(input("ID Jenis Vendor: "))
                lihat_data_vendor(id_JenisVendor)
            except ValueError:
                print("\nInput tidak valid. ID jenis vendor harus berupa angka.")
                continue

        else:
            print("Pilihan tidak valid.")

# Fungsi kelola event
def tambah_event(nama, tanggal_event, jumlah_undangan, lokasi, total_budget, id_Klien, id_JenisEvent):
    query = '''INSERT INTO 
                   Event (nama, tanggal_event, jumlah_undangan, lokasi, total_budget, id_Klien, status_event, id_JenisEvent) 
               VALUES 
                   (?, ?, ?, ?, ?, ?, 'Upcoming', ?) '''
    print()
    print("Tambah event berhasil.") if execute_query(query, (nama, tanggal_event, jumlah_undangan, lokasi, total_budget, id_Klien, id_JenisEvent)) else print("Tambah event gagal.")

def get_id_event():
    query = '''
        SELECT 
            id_Event
        FROM 
            Event
        ORDER BY 
            id_Event DESC
    '''
    hasil = fetch_one(query)
    return hasil[0]

def tambah_user_event(id_User):
    id_Event = get_id_event();
    query = '''INSERT INTO 
                   UserEvent (id_Event, id_User) 
               VALUES 
                   (?, ?)'''
    print("Tambah user event berhasil.\n") if execute_query(query, (id_Event, id_User)) else print("Tambah User Event gagal.\n")

def lihat_data_event():
    query = '''
            SELECT 
                e.id_Event, e.nama, tanggal_event, lokasi, jenis_event, status_event
            FROM 
                Event e
                JOIN JenisEvent je ON je.id_JenisEvent = e.id_JenisEvent
            WHERE 
                status_event = 'Upcoming' OR status_event = 'Completed'
            GROUP BY 
                e.id_Event, e.nama, tanggal_event, lokasi, jenis_event, status_event
            '''
    hasil = fetch_all(query)

    if hasil:
        hasil_format = [(id_Event, nama_event, tanggal_event, lokasi, jenis_event, status_event)
            for id_Event, nama_event, tanggal_event, lokasi, jenis_event, status_event in hasil]
        kolom = [
            'ID Event', 'Nama Event', 'Tanggal Event', 'Lokai Event', 'Jenis Event', 'Status Event'
        ]
        print(tabulate(hasil_format, headers=kolom, tablefmt='grid'))
        print()
    else:
        print("Tidak ada data event ditemukan.")

def lihat_event_spesifik(id_Event):
    query = '''
            SELECT 
                e.id_Event, e.nama, k.nama, tanggal_event, jumlah_undangan, lokasi, total_budget, jenis_event
            FROM 
                Event e 
                JOIN Klien k ON e.id_Klien = k.id_Klien
                JOIN JenisEvent je ON je.id_JenisEvent = e.id_JenisEvent
            WHERE 
                e.id_Event = ?
            GROUP BY 
                e.id_Event, e.nama, k.nama, tanggal_event, jumlah_undangan, lokasi, total_budget, jenis_event
            '''
    hasil = fetch_all(query, (id_Event,))
    print()

    if hasil:
        hasil_format = [
            (id_Event, nama_event, nama_klien, tanggal_event, jumlah_undangan, lokasi, format_rupiah(total_budget), jenis_event)
            for id_Event, nama_event, nama_klien, tanggal_event, jumlah_undangan, lokasi, total_budget, jenis_event in hasil]
        kolom = [
            'ID Event', 'Nama Event', 'Nama Klien', 'Tanggal Event', 'Jumlah Undangan', 'Lokasi', 'Total Budget', 'Jenis Event'
        ]
        print(tabulate(hasil_format, headers=kolom, tablefmt='grid'))
        print()
    else:
        print("Tidak ada event dengan ID ini.")
        return "Tidak ada event dengan ID ini."

def edit_event(id_Event, nama, tanggal, jumlah_undangan, lokasi, total_budget):
    query = '''
        UPDATE 
            Event 
        SET     
            nama = ?, tanggal_event = ?, jumlah_undangan = ?, lokasi = ?, total_budget = ?
        WHERE
            id_Event = ? '''
    print("\nEdit event berhasil.") if execute_query(query, (nama, tanggal, jumlah_undangan, lokasi, total_budget, id_Event)) else print("\n Edit event gagal.")

def hapus_event(id_Event):
    query = '''
        UPDATE 
            Event 
        SET 
            status_event = 'Cancelled'
        WHERE 
            id_Event = ? 
    
    '''
    print("\nHapus event berhasil.\n") if execute_query(query, (id_Event,)) else print("\nHapus event gagal.\n")

def completed_event(id_User):
    query = '''
            SELECT 
                e.nama, k.nama, status_event 
            FROM 
                UserEvent ev 
                JOIN [User] u ON u.id_User = ev.id_User
                JOIN Event e ON e.id_Event = ev.id_Event
                JOIN Klien k ON e.id_Klien = k.id_Klien
            WHERE 
                status_event = 'Completed' AND u.id_User = ?
            '''
    hasil = fetch_all(query, (id_User,))
    print()

    if hasil:
        kolom = [
            'Nama Event', 'Nama Klien', 'Status Event'
        ]
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
        print()
    else:
        print("Event tidak ditemukan.")

def upcoming_event(id_User):
    query = '''
            SELECT 
                u.nama, k.nama, e.nama, tanggal_event, status_event 
            FROM 
                UserEvent ev
                JOIN [User] u ON u.id_User = ev.id_User
                JOIN Event e ON e.id_Event = ev.id_Event
                JOIN Klien k ON e.id_Klien = k.id_Klien
            WHERE 
                status_event = 'Upcoming' AND u.id_User = ?
            '''
    hasil = fetch_all(query, (id_User,))
    print()

    if hasil:
        kolom = [
            'Nama Asisten', 'Nama Klien', 'Nama Event', 'Tanggal Event', 'Status Event'
        ]
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
        print()
    else:
        print("Event tidak ditemukan.")

def lihat_data_jenis_event():
    query = ''' SELECT 
                    *
                FROM 
                    JenisEvent
            '''
    hasil = fetch_all(query)
    print()

    if hasil:
        kolom = ['ID Jenis Event', 'Jenis Event']
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
        print()
    else:
        print("Data jenis event tidak ditemukan.")

def lihat_event_berdasarkan_jenis(id_User, id_JenisEvent):
    query = '''
        SELECT 
            u.nama, k.nama, e.nama, tanggal_event, status_event 
        FROM
            UserEvent ev
            JOIN [User] u ON u.id_User = ev.id_User
            JOIN Event e ON e.id_Event = ev.id_Event
            JOIN Klien k ON e.id_Klien = k.id_Klien
        WHERE
            (status_event = 'Upcoming' OR status_event = 'Completed') AND u.id_User = ? AND id_JenisEvent = ?
    '''
    hasil = fetch_all(query, (id_User, id_JenisEvent))
    print()

    if hasil:
        kolom = [
            'Nama Asisten', 'Nama Klien', 'Nama Event', 'Tanggal Event', 'Status Event'
        ]
        print(tabulate(hasil, headers=kolom, tablefmt='grid'))
        print()
    else:
        print("Event tidak ditemukan.")

def lihat_semua_data_vendor():
    hasil = fetch_all('''SELECT 
                             id_Vendor, nama, alamat, harga_min, harga_max, jenis_vendor 
                         FROM 
                             Vendor 
                             JOIN JenisVendor ON Vendor.id_JenisVendor = JenisVendor.id_JenisVendor 
                         WHERE 
                             isActive = 1''')
    if hasil:
        hasil_format = [(id_Vendor, nama_vendor, alamat, format_rupiah(harga_min), format_rupiah(harga_max), jenis_vendor)
                        for id_Vendor, nama_vendor, alamat, harga_min, harga_max, jenis_vendor in hasil]
        kolom = ['ID', 'Nama Vendor', 'Alamat', 'Harga Min', 'Harga Max', 'Jenis Vendor']
        print(tabulate(hasil_format, headers=kolom, tablefmt='grid'))
        print()
    else:
        print("Tidak ada data vendor ditemukan.")

def lihat_data_vendor(id_JenisVendor):
    query = '''
            SELECT 
                nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max
            FROM 
                Vendor 
                JOIN JenisVendor ON Vendor.id_JenisVendor = JenisVendor.id_JenisVendor
            WHERE 
                JenisVendor.id_JenisVendor = ? AND Vendor.isActive = 1
            '''
    hasil = fetch_all(query, (id_JenisVendor,))
    print()

    if hasil:
        hasil_format = []
        for row in hasil:
            nama, pemilik, alamat, telepon, email, h_min, h_max = row
            hasil_format.append((
                nama,
                pemilik,
                textwrap.fill(alamat, width=30),
                telepon,
                textwrap.fill(email, width=30),
                format_rupiah(h_min),
                format_rupiah(h_max),
            ))
        kolom = ['Nama Vendor', 'Nama Pemilik', 'Alamat', 'Email', 'No Telepon', 'Harga Min', 'Harga Max']
        print(tabulate(hasil_format, headers=kolom, tablefmt='grid'))
        print()
    else:
        print("Vendor dengan jenis tersebut tidak ditemukan.")

