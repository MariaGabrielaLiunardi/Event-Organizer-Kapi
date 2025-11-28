import pyodbc
import traceback

# Fungsi untuk koneksi ke database
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=Tubes;'
        'Trusted_Connection=yes'
    )