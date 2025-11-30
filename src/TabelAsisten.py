from Database import execute_query

def createUser():
    query = '''
    CREATE TABLE [User] (
        id_User INT IDENTITY(1,1) PRIMARY KEY, 
        username VARCHAR(50) NOT NULL UNIQUE, 
        password VARCHAR(20) NOT NULL, 
        nama VARCHAR(60) NOT NULL, 
        alamat VARCHAR(100) NOT NULL, 
        no_telepon VARCHAR(13) NOT NULL, 
        email VARCHAR(320) NOT NULL, 
        role VARCHAR(7) NOT NULL,
        isActive BIT NOT NULL DEFAULT 1
    )
    '''
    return "User berhasil dibuat." if execute_query(query) else "User gagal dibuat."