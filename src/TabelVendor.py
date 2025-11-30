from Database import execute_query

def createJenisVendor():
    query = '''
    CREATE TABLE JenisVendor (
        id_JenisVendor INT IDENTITY(1,1) PRIMARY KEY, 
        jenis_vendor VARCHAR(50) NOT NULL
    )
    '''
    return "JenisVendor berhasil dibuat." if execute_query(query) else "JenisVendor gagal dibuat."

def createVendor():
    query = '''
    CREATE TABLE Vendor (
        id_Vendor INT IDENTITY(1,1) PRIMARY KEY, 
        nama VARCHAR(60) NOT NULL, 
        nama_pemilik VARCHAR(60) NOT NULL, 
        alamat VARCHAR(100) NOT NULL, 
        no_telepon VARCHAR(13) NOT NULL, 
        email VARCHAR(320) NOT NULL, 
        harga_min MONEY NOT NULL,
        harga_max MONEY NOT NULL, 
        id_JenisVendor INT NOT NULL,
        isActive BIT NOT NULL DEFAULT 1,
        FOREIGN KEY (id_JenisVendor) REFERENCES JenisVendor(id_JenisVendor)
    )
    '''
    return "Vendor berhasil dibuat." if execute_query(query) else "Vendor gagal dibuat."
