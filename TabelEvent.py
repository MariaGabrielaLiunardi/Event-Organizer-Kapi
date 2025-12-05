def createEvent():
    query = '''
    CREATE TABLE Event (
        id_Event INT IDENTITY(1,1) PRIMARY KEY, 
        nama VARCHAR(60) NOT NULL,
        tanggal_event DATE NOT NULL, 
        jumlah_undangan INT NOT NULL, 
        lokasi VARCHAR(100) NOT NULL, 
        status_event VARCHAR(50) NOT NULL, 
        total_budget MONEY NOT NULL, 
        id_Klien INT NOT NULL,
        id_JenisEvent INT NOT NULL,
        isActive BIT NOT NULL DEFAULT 1,
        FOREIGN KEY (id_Klien) REFERENCES Klien(id_Klien), 
        FOREIGN KEY (id_JenisEvent) REFERENCES JenisEvent(id_JenisEvent)
    )
    '''
    return "Event berhasil dibuat." if execute_query(query) else "Event gagal dibuat."

    def createJenisEvent():
    query = '''
    CREATE TABLE JenisEvent (
        id_JenisEvent INT IDENTITY(1,1) PRIMARY KEY,  
        jenis_event VARCHAR(50) NOT NULL
    )
    '''
    return "JenisEvent berhasil dibuat." if execute_query(query) else "JenisEvent gagal dibuat."

    def createEventVendor():
    query = '''
    CREATE TABLE EventVendor (
        id_Event INT NOT NULL, 
        id_Vendor INT NOT NULL, 
        harga_dealing MONEY NOT NULL,
        PRIMARY KEY (id_Event, id_Vendor), 
        FOREIGN KEY (id_Event) REFERENCES Event(id_Event), 
        FOREIGN KEY (id_Vendor) REFERENCES Vendor(id_Vendor)
    )
    '''
    return "EventVendor berhasil dibuat." if execute_query(query) else "EventVendor gagal dibuat."

    def createUserEvent():
    query = '''
    CREATE TABLE UserEvent (
        id_User INT NOT NULL, 
        id_Event INT NOT NULL, 
        PRIMARY KEY (id_User, id_Event), 
        FOREIGN KEY (id_User) REFERENCES [User](id_User), 
        FOREIGN KEY (id_Event) REFERENCES Event(id_Event)
    )
    '''
    return "UserEvent berhasil dibuat." if execute_query(query) else "UserEvent gagal dibuat."

    
