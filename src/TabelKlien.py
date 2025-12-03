from Database import execute_query

def createKlien():
    query = '''
    CREATE TABLE Klien (
        id_Klien INT IDENTITY(1,1) PRIMARY KEY, 
        nama VARCHAR(60) NOT NULL, 
        alamat VARCHAR(100) NOT NULL, 
        no_telepon VARCHAR(13) NOT NULL, 
        email VARCHAR(320) NOT NULL, 
        tanggal_registrasi DATE NOT NULL,
        isActive BIT NOT NULL DEFAULT 1
    )
    '''
    return "Klien berhasil dibuat." if execute_query(query) else "Klien gagal dibuat."