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
                    elif pilihan == '1':
                        print("\n--- Rincian Budgeting ---")
                        result = lihat_rincian_budgeting(id_Event)

                        if result != 'Tidak ada rincian budgeting ditemukan untuk klien ini.':
                            print("1. Lihat total harga dealing")
                            print("2. Tambah harga dealing")
                            print("3. Edit harga dealing")
                            print("0. Kembali")

                            pilihan = input("Pilih menu: ")

                            if pilihan == '0':
                                break
                            elif pilihan == '1':
                                print("\n--- Total Harga Dealing ---")
                                total_budget_event(id_Event)
                            elif pilihan == '2':
                                print("\n--- Tambah Harga Dealing ---")
                                try:
                                    print("Daftar vendor yang tersedia: \n")
                                    lihat_semua_data_vendor()

                                    id_Vendor = int(input("ID vendor: "))
                                    harga_dealing = int(input("Harga dealing: "))
                                    tambah_harga_dealing(id_Event, id_Vendor, harga_dealing)
                                except ValueError:
                                    print("\nInput tidak valid, harus berupa angka.\n")

                            elif pilihan == '3':
                                print("\n--- Edit Harga Dealing ---")
                                try:
                                    id_Vendor = int(input("ID vendor: "))
                                    harga_dealing = int(input("Harga dealing yang baru: "))
                                except ValueError:
                                    print("\nInput tidak valid, harus berupa angka.\n")
                                    continue
                                update_harga_dealing(id_Event, id_Vendor, harga_dealing)
                            else:
                                print("Pilihan tidak valid.")

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
