from Database import execute_query

# Insert Data Dummy ke Database
def insertUser():
    query = '''
    INSERT INTO 
        [User] (username, password, nama, alamat, no_telepon, email, role) 
    VALUES 
        ('kapi', 'owner123', 'Kapi Nugroho', 'Jl. Sudirman No. 123, Jakarta Pusat', '081234567890', 'kapi@eventorganizer.com', 'owner'),
        ('asisten01', 'asisten123', 'Siti Nurhaliza', 'Jl. Gatot Subroto No. 45, Jakarta Selatan', '081234567891', 'siti.nurhaliza@eventorganizer.com', 'asisten'),
        ('asisten02', 'asisten123', 'Budi Santoso', 'Jl. Thamrin No. 67, Jakarta Pusat', '081234567892', 'budi.santoso@eventorganizer.com', 'asisten'),
        ('asisten03', 'asisten123', 'Dewi Sartika', 'Jl. Kebon Jeruk No. 89, Jakarta Barat', '081234567893', 'dewi.sartika@eventorganizer.com', 'asisten'),
        ('asisten04', 'asisten123', 'Andi Wijaya', 'Jl. Cempaka Putih No. 12, Jakarta Pusat', '081234567894', 'andi.wijaya@eventorganizer.com', 'asisten'),
        ('asisten05', 'asisten123', 'Maya Indira', 'Jl. Kuningan No. 34, Jakarta Selatan', '081234567895', 'maya.indira@eventorganizer.com', 'asisten'),
        ('asisten06', 'asisten123', 'Reza Pratama', 'Jl. Menteng No. 56, Jakarta Pusat', '081234567896', 'reza.pratama@eventorganizer.com', 'asisten'),
        ('asisten07', 'asisten123', 'Linda Maharani', 'Jl. Kelapa Gading No. 78, Jakarta Utara', '081234567897', 'linda.maharani@eventorganizer.com', 'asisten'),
        ('asisten08', 'asisten123', 'Hendra Gunawan', 'Jl. Pondok Indah No. 90, Jakarta Selatan', '081234567898', 'hendra.gunawan@eventorganizer.com', 'asisten'),
        ('asisten09', 'asisten123', 'Ratna Sari', 'Jl. Senayan No. 11, Jakarta Pusat', '081234567899', 'ratna.sari@eventorganizer.com', 'asisten'),
        ('asisten10', 'asisten123', 'Doni Setiawan', 'Jl. Pancoran No. 22, Jakarta Selatan', '081234567800', 'doni.setiawan@eventorganizer.com', 'asisten'),
        ('asisten11', 'asisten123', 'Fitri Handayani', 'Jl. Tanah Abang No. 33, Jakarta Pusat', '081234567801', 'fitri.handayani@eventorganizer.com', 'asisten'),
        ('asisten12', 'asisten123', 'Bayu Aditya', 'Jl. Kemang No. 44, Jakarta Selatan', '081234567802', 'bayu.aditya@eventorganizer.com', 'asisten'),
        ('asisten13', 'asisten123', 'Novi Susanti', 'Jl. Pluit No. 55, Jakarta Utara', '081234567803', 'novi.susanti@eventorganizer.com', 'asisten'),
        ('asisten14', 'asisten123', 'Agus Setiawan', 'Jl. Meruya No. 66, Jakarta Barat', '081234567804', 'agus.setiawan@eventorganizer.com', 'asisten'),
        ('asisten15', 'asisten123', 'Diana Putri', 'Jl. Cibubur No. 77, Jakarta Timur', '081234567805', 'diana.putri@eventorganizer.com', 'asisten'),
        ('asisten16', 'asisten123', 'Fajar Ramadhan', 'Jl. Cipete No. 88, Jakarta Selatan', '081234567806', 'fajar.ramadhan@eventorganizer.com', 'asisten'),
        ('asisten17', 'asisten123', 'Indah Permata', 'Jl. Rawamangun No. 99, Jakarta Timur', '081234567807', 'indah.permata@eventorganizer.com', 'asisten'),
        ('asisten18', 'asisten123', 'Yoga Pratama', 'Jl. Bintaro No. 10, Jakarta Selatan', '081234567808', 'yoga.pratama@eventorganizer.com', 'asisten'),
        ('asisten19', 'asisten123', 'Lina Marlina', 'Jl. Sunter No. 21, Jakarta Utara', '081234567809', 'lina.marlina@eventorganizer.com', 'asisten'),
        ('asisten20', 'asisten123', 'Taufik Hidayat', 'Jl. Kalideres No. 32, Jakarta Barat', '081234567810', 'taufik.hidayat@eventorganizer.com', 'asisten'),
        ('asisten21', 'asisten123', 'Rina Andayani', 'Jl. Duren Sawit No. 43, Jakarta Timur', '081234567811', 'rina.andayani@eventorganizer.com', 'asisten'),
        ('asisten22', 'asisten123', 'Bambang Sudarsono', 'Jl. Pasar Minggu No. 54, Jakarta Selatan', '081234567812', 'bambang.sudarsono@eventorganizer.com', 'asisten'),
        ('asisten23', 'asisten123', 'Sari Dewi', 'Jl. Pademangan No. 65, Jakarta Utara', '081234567813', 'sari.dewi@eventorganizer.com', 'asisten'),
        ('asisten24', 'asisten123', 'Wahyu Saputra', 'Jl. Cengkareng No. 76, Jakarta Barat', '081234567814', 'wahyu.saputra@eventorganizer.com', 'asisten');
    '''
    return "User berhasil dimasukkan." if execute_query(query) else "User gagal dimasukkan."

def insertKlien():
    query = '''
    INSERT INTO 
        Klien (nama, alamat, no_telepon, email, tanggal_registrasi) 
    VALUES
        ('Budi Suharto', 'Jl. Merdeka No. 15, Jakarta', '081234567890', 'budi.suharto@gmail.com', '2024-01-15'),
        ('Ratna Dewi', 'Jl. Sudirman No. 25, Jakarta', '081234567891', 'ratna.dewi@gmail.com', '2024-01-20'),
        ('PT. Maju Bersama', 'Jl. HR Rasuna Said No. 100, Jakarta', '021-5551001', 'info@majubersama.com', '2024-02-01'),
        ('Andi Wijaya', 'Jl. Diponegoro No. 50, Bandung', '081234567892', 'andi.wijaya@gmail.com', '2024-02-10'),
        ('Sari Kusuma', 'Jl. Margonda Raya No. 30, Depok', '081234567893', 'sari.kusuma@gmail.com', '2024-02-15'),
        ('CV. Sukses Mandiri', 'Jl. Gatot Subroto No. 123, Jakarta', '021-5551002', 'contact@suksesmandiri.com', '2024-03-01'),
        ('Doni Pratama', 'Jl. Kemang No. 71, Jakarta', '081234567894', 'doni.pratama@gmail.com', '2024-03-05'),
        ('Maya Purnama', 'Jl. MH Thamrin No. 28, Jakarta', '081234567895', 'maya.purnama@gmail.com', '2024-03-15'),
        ('Hotel Grand Indonesia', 'Jl. MH Thamrin Kav 28-30, Jakarta', '021-5551008', 'events@grandindonesia.com', '2024-03-20'),
        ('Hendra Gunawan', 'Jl. Gaya Motor Raya No. 8, Jakarta', '081234567896', 'hendra.gunawan@gmail.com', '2024-04-01'),
        ('Linda Sari', 'Jl. Brawijaya No. 15, Jakarta', '081234567897', 'linda.sari@gmail.com', '2024-04-10'),
        ('Fajar Nugroho', 'Jl. Cipete Raya No. 25, Jakarta', '081234567898', 'fajar.nugroho@gmail.com', '2024-04-15'),
        ('Yayasan Pendidikan Nusantara', 'Jl. Semampir II No. 1, Kediri', '0354-5551012', 'admin@ypnusantara.org', '2024-05-01'),
        ('Kartika Dewi', 'Jl. Puri Indah No. 10, Jakarta', '081234567899', 'kartika.dewi@gmail.com', '2024-05-05'),
        ('Bambang Santoso', 'Jl. Budi Kemuliaan No. 6, Jakarta', '081234567900', 'bambang.santoso@gmail.com', '2024-05-10'),
        ('Rudi Hermawan', 'Jl. Cikini Raya No. 25, Jakarta', '081234567901', 'rudi.hermawan@gmail.com', '2024-05-15'),
        ('Novi Kartika', 'Jl. Kemang Selatan No. 30, Jakarta', '081234567902', 'novi.kartika@gmail.com', '2024-05-20'),
        ('PT. Pertamina', 'Jl. Medan Merdeka Timur No. 6, Jakarta', '021-5551015', 'events@pertamina.com', '2024-06-01'),
        ('Teguh Mustofa', 'Jl. Ganesha No. 10, Bandung', '081234567903', 'teguh.mustofa@gmail.com', '2024-06-05'),
        ('Indira Putri', 'Jl. Pondok Bambu No. 12, Jakarta', '081234567904', 'indira.putri@gmail.com', '2024-06-10');
    '''
    return "Klien berhasil dimasukkan." if execute_query(query) else "Klien gagal dimasukkan."

def insertEvent():
    query = '''
    INSERT INTO 
        Event (nama, tanggal_event, jumlah_undangan, lokasi, status_event, total_budget, id_Klien, id_JenisEvent) 
    VALUES
        ('Wedding Ceremony Suharto-Ratna', '2024-07-15', 300, 'Hotel Grand Indonesia Ballroom', 'Completed', 150000000.00, 11, 1),
        ('Annual Corporate Meeting 2024', '2024-08-20', 150, 'Plaza Indonesia Convention Hall', 'Completed', 75000000.00, 1, 3),
        ('Product Launch Smartphone X', '2024-09-10', 200, 'Ballroom Mewah Jakarta', 'Completed', 120000000.00, 10, 5),
        ('Graduation Ceremony UI 2024', '2024-10-05', 500, 'Balai Sidang UI Depok', 'Cancelled', 200000000.00, 5, 6),
        ('Birthday Party Ratna 50th', '2024-11-12', 100, 'Rumah Pribadi Cipete', 'Completed', 50000000.00, 12, 2),
        ('Corporate Training Workshop', '2024-12-03', 80, 'Hotel Mandarin Oriental', 'Upcoming', 60000000.00, 6, 10),
        ('Charity Gala Dinner', '2025-01-18', 250, 'JCC Jakarta', 'Upcoming', 180000000.00, 16, 15),
        ('Tech Conference 2025', '2025-02-22', 400, 'ICE BSD Tangerang', 'Upcoming', 300000000.00, 9, 4),
        ('Wedding Anniversary 25th', '2025-03-08', 150, 'The Ritz Carlton Jakarta', 'Upcoming', 100000000.00, 14, 7),
        ('Baby Shower Celebration', '2025-04-15', 50, 'Rumah Pribadi Kemang', 'Upcoming', 25000000.00, 17, 8),
        ('Engagement Party', '2025-05-10', 80, 'Sky Dining Jakarta', 'Cancelled', 40000000.00, 20, 9),
        ('Medical Seminar RSCM', '2025-06-20', 200, 'Auditorium RSCM Jakarta', 'Cancelled', 80000000.00, 7, 11),
        ('Art Exhibition Opening', '2025-07-05', 120, 'National Gallery Jakarta', 'Upcoming', 70000000.00, 18, 12),
        ('Music Concert Charity', '2025-08-14', 500, 'Istora Senayan Jakarta', 'Upcoming', 400000000.00, 16, 13),
        ('Cultural Festival', '2025-09-17', 1000, 'Monas Jakarta', 'Upcoming', 500000000.00, 3, 14),
        ('Business Networking Event', '2025-10-12', 100, 'Hotel Shangri-La Jakarta', 'Upcoming', 60000000.00, 1, 16),
        ('Team Building Activity', '2025-11-08', 60, 'Puncak Resort Bogor', 'Upcoming', 45000000.00, 10, 17),
        ('Awards Ceremony Banking', '2025-12-15', 300, 'Ballroom Hotel Mulia Jakarta', 'Upcoming', 250000000.00, 6, 18),
        ('Fashion Show Collection 2026', '2026-01-20', 200, 'Jakarta Fashion Week Venue', 'Upcoming', 200000000.00, 8, 19),
        ('School Anniversary SMK', '2026-02-25', 800, 'Gedung Sekolah SMK Negeri 1', 'Cancelled', 100000000.00, 15, 20);
    '''
    return "Event berhasil dimasukkan." if execute_query(query) else "Event gagal dimasukkan."

def insertVendor():
    query = '''
    INSERT INTO 
        Vendor (nama, nama_pemilik, alamat, no_telepon, email, harga_min, harga_max, id_JenisVendor)
    VALUES
        ('Catering Nusantara', 'Budi Cahyono', 'Jl. Kelapa Sawit No. 15, Jakarta', '021-7771001', 'info@cateringnusantara.com', 50000.00, 150000.00, 1),
        ('Photo Studio Cantik', 'Rina Susanti', 'Jl. Cikajang No. 20, Jakarta', '021-7771002', 'booking@photocantik.com', 2000000.00, 8000000.00, 2),
        ('Sound System Pro', 'Hendra Gunawan', 'Jl. Fatmawati No. 30, Jakarta', '021-7771003', 'rental@soundpro.com', 1500000.00, 5000000.00, 3),
        ('Dekorasi Indah', 'Maya Purnama', 'Jl. Panglima Polim No. 25, Jakarta', '021-7771004', 'order@dekorasiindah.com', 3000000.00, 15000000.00, 4),
        ('Ballroom Mewah', 'Agus Triyanto', 'Jl. Senopati No. 45, Jakarta', '021-7771005', 'booking@ballroommewah.com', 10000000.00, 50000000.00, 5),
        ('Wedding Organizer Elite', 'Sari Dewi', 'Jl. Kemang Raya No. 35, Jakarta', '021-7771006', 'info@wedelite.com', 15000000.00, 75000000.00, 6),
        ('Toko Bunga Segar', 'Lina Handayani', 'Jl. Blok M No. 18, Jakarta', '021-7771007', 'order@bungasegar.com', 500000.00, 5000000.00, 7),
        ('Transport VIP', 'Doni Setiawan', 'Jl. Warung Buncit No. 12, Jakarta', '021-7771008', 'booking@transportvip.com', 1000000.00, 8000000.00, 8),
        ('Security Professional', 'Bambang Santoso', 'Jl. Mampang Prapatan No. 22, Jakarta', '021-7771009', 'service@securitypro.com', 2000000.00, 10000000.00, 9),
        ('AV Solutions', 'Rudi Hermawan', 'Jl. Tebet Raya No. 40, Jakarta', '021-7771010', 'rental@avsolutions.com', 3000000.00, 12000000.00, 10),
        ('Lighting Spektakuler', 'Andi Prasetya', 'Jl. Kuningan Barat No. 28, Jakarta', '021-7771011', 'info@lightingspek.com', 2500000.00, 15000000.00, 11),
        ('MC Profesional', 'Ratna Wulandari', 'Jl. Menteng Dalam No. 16, Jakarta', '021-7771012', 'booking@mcpro.com', 1500000.00, 5000000.00, 12),
        ('Salon Kecantikan Prima', 'Dewi Anggraini', 'Jl. Cikini Raya No. 33, Jakarta', '021-7771013', 'appointment@salonprima.com', 1000000.00, 8000000.00, 13),
        ('Video Production House', 'Fajar Ramadhan', 'Jl. Kemayoran No. 19, Jakarta', '021-7771014', 'project@videoph.com', 5000000.00, 25000000.00, 14),
        ('Photo Booth Fun', 'Novi Kartika', 'Jl. Senen Raya No. 24, Jakarta', '021-7771015', 'rental@photoboothfun.com', 2000000.00, 8000000.00, 15),
        ('Live Music Band', 'Teguh Mustofa', 'Jl. Salemba No. 31, Jakarta', '021-7771016', 'booking@livemusicband.com', 3000000.00, 15000000.00, 16),
        ('DJ Party', 'Indira Safitri', 'Jl. Cempaka Putih No. 27, Jakarta', '021-7771017', 'booking@djparty.com', 2000000.00, 10000000.00, 17),
        ('Event Coordinator Pro', 'Kartika Sari', 'Jl. Johar Baru No. 21, Jakarta', '021-7771018', 'service@eventpro.com', 5000000.00, 30000000.00, 18),
        ('Tenda Pesta', 'Hasan Basri', 'Jl. Rawasari No. 17, Jakarta', '021-7771019', 'rental@tendapesta.com', 3000000.00, 20000000.00, 19),
        ('Furniture Rental', 'Yuni Pratiwi', 'Jl. Kramat No. 26, Jakarta', '021-7771020', 'rental@furniturerent.com', 2000000.00, 12000000.00, 20);
    '''
    return "Vendor berhasil dimasukkan." if execute_query(query) else "Vendor gagal dimasukkan."

def insertEventVendor():
    query = '''
    INSERT INTO 
        EventVendor 
    VALUES
        -- Event 1: Wedding Ceremony (Budget: 150M) - Vendor yang dibutuhkan: Catering, Photo, Decoration, Wedding Organizer, Florist
        (1, 1, 35000000.00), -- Catering Nusantara
        (1, 2, 6000000.00), -- Photo Studio Cantik
        (1, 4, 12000000.00), -- Dekorasi Indah
        (1, 6, 60000000.00), -- Wedding Organizer Elite
        (1, 7, 3000000.00), -- Toko Bunga Segar
        -- Event 2: Corporate Meeting (Budget: 75M) - Vendor: Catering, Sound, AV, MC
        (2, 1, 12000000.00), -- Catering Nusantara
        (2, 3, 4000000.00), -- Sound System Pro
        (2, 10, 8000000.00), -- AV Solutions
        (2, 12, 3000000.00), -- MC Profesional
        -- Event 3: Product Launch (Budget: 120M) - Vendor: Catering, Photo, Sound, Decoration, Lighting
        (3, 1, 20000000.00), -- Catering Nusantara
        (3, 2, 7000000.00), -- Photo Studio Cantik
        (3, 3, 4500000.00), -- Sound System Pro
        (3, 4, 15000000.00), -- Dekorasi Indah
        (3, 11, 12000000.00), -- Lighting Spektakuler
        -- Event 4: Graduation Ceremony (Budget: 200M) - Vendor: Catering, Photo, Sound, MC
        (4, 1, 45000000.00), -- Catering Nusantara
        (4, 2, 5000000.00), -- Photo Studio Cantik
        (4, 3, 5000000.00), -- Sound System Pro
        (4, 12, 4000000.00), -- MC Profesional
        -- Event 5: Birthday Party (Budget: 50M) - Vendor: Catering, Photo, Decoration
        (5, 1, 3500000.00), -- Catering Nusantara
        (5, 2, 3000000.00), -- Photo Studio Cantik
        (5, 4, 8000000.00), -- Dekorasi Indah
        -- Event 6: Workshop (Budget: 60M) - Vendor: Catering, AV
        (6, 1, 8500000.00), -- Catering Nusantara
        (6, 10, 6000000.00), -- AV Solutions
        -- Event 7: Charity Gala (Budget: 180M) - Vendor: Catering, Decoration, Lighting
        (7, 1, 22000000.00), -- Catering Nusantara
        (7, 4, 18000000.00), -- Dekorasi Indah
        (7, 11, 15000000.00), -- Lighting Spektakuler
        -- Event 8: Tech Conference (Budget: 300M) - Vendor: Sound, AV, MC
        (8, 3, 25000000.00), -- Sound System Pro
        (8, 10, 12000000.00), -- AV Solutions
        (8, 12, 5000000.00), -- MC Profesional
        -- Event 9: Anniversary (Budget: 100M) - Vendor: Catering, Wedding Organizer, Florist
        (9, 1, 9500000.00), -- Catering Nusantara
        (9, 6, 45000000.00), -- Wedding Organizer Elite
        (9, 7, 4000000.00), -- Toko Bunga Segar
        -- Event 10: Baby Shower (Budget: 25M) - Vendor: Catering, Decoration
        (10, 1, 6000000.00), -- Catering Nusantara
        (10, 4, 5000000.00), -- Dekorasi Indah
        -- Event 11: Engagement Party (Budget: 40M) - Vendor: Catering, Photo, Decoration
        (11, 1, 8000000.00), -- Catering Nusantara
        (11, 2, 4000000.00), -- Photo Studio Cantik
        (11, 4, 6000000.00), -- Dekorasi Indah
        -- Event 12: Medical Seminar (Budget: 80M) - Vendor: Catering, AV, MC
        (12, 1, 15000000.00), -- Catering Nusantara
        (12, 10, 10000000.00), -- AV Solutions
        (12, 12, 4000000.00), -- MC Profesional
        -- Event 13: Art Exhibition (Budget: 70M) - Vendor: Catering, Lighting, Security
        (13, 1, 12000000.00), -- Catering Nusantara
        (13, 11, 8000000.00), -- Lighting Spektakuler
        (13, 9, 5000000.00), -- Security Professional
        -- Event 14: Music Concert (Budget: 400M) - Vendor: Sound, Lighting, Security, Live Band
        (14, 3, 50000000.00), -- Sound System Pro
        (14, 11, 30000000.00), -- Lighting Spektakuler
        (14, 9, 15000000.00), -- Security Professional
        (14, 16, 80000000.00), -- Live Music Band
        -- Event 15: Cultural Festival (Budget: 500M) - Vendor: Catering, Sound, Security, Tent
        (15, 1, 100000000.00), -- Catering Nusantara
        (15, 3, 80000000.00), -- Sound System Pro
        (15, 9, 25000000.00), -- Security Professional
        (15, 19, 50000000.00), -- Tenda Pesta
        -- Event 16: Networking Event (Budget: 60M) - Vendor: Catering, AV
        (16, 1, 15000000.00), -- Catering Nusantara
        (16, 10, 8000000.00), -- AV Solutions
        -- Event 17: Team Building (Budget: 45M) - Vendor: Catering, Transport
        (17, 1, 12000000.00), -- Catering Nusantara
        (17, 8, 10000000.00), -- Transport VIP
        -- Event 18: Awards Ceremony (Budget: 250M) - Vendor: Catering, Photo, Sound, Decoration, Lighting
        (18, 1, 50000000.00), -- Catering Nusantara
        (18, 2, 15000000.00), -- Photo Studio Cantik
        (18, 3, 25000000.00), -- Sound System Pro
        (18, 4, 30000000.00), -- Dekorasi Indah
        (18, 11, 20000000.00), -- Lighting Spektakuler
        -- Event 19: Fashion Show (Budget: 200M) - Vendor: Sound, Lighting, Makeup, Photo
        (19, 3, 30000000.00), -- Sound System Pro
        (19, 11, 25000000.00), -- Lighting Spektakuler
        (19, 13, 15000000.00), -- Salon Kecantikan Prima
        (19, 2, 20000000.00), -- Photo Studio Cantik
        -- Event 20: School Anniversary (Budget: 100M) - Vendor: Catering, Sound, Photo
        (20, 1, 25000000.00), -- Catering Nusantara
        (20, 3, 15000000.00), -- Sound System Pro
        (20, 2, 8000000.00); -- Photo Studio Cantik

    '''
    return "EventVendor berhasil dimasukkan." if execute_query(query) else "EventVendor gagal dimasukkan."

