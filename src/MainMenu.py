from Database import get_connection, fetch_one
from Pemilik import tampilkan_menu_pemilik
from Asisten import tampilkan_menu_asisten  # Asumsikan kamu punya fungsi ini

def login(username, password):
    cnxn = get_connection()
    cursor = cnxn.cursor()
    query = '''
        SELECT id_User, username, password, role
        FROM [User]
        WHERE username = ? AND password = ?
    '''
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    cnxn.close()

    if user:
        _, _, _, role = user
        return True, role
    else:
        print("\nUsername atau password salah.")

        print("1. Coba login ulang")
        print("2. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            return True, "retry"
        elif pilihan == '2':
            return True, "exit"
        else:
            return True, "\nPilihan tidak valid."


def get_idUser(username):
    query = '''
            SELECT id_User
            FROM
                [User]
            WHERE
                username = ?
            '''
    hasil = fetch_one(query, (username,))

    # Fix: Extract the actual integer value from the result
    if hasil:
        # If fetch_one returns a tuple like (123,), extract the first element
        if isinstance(hasil, tuple):
            return hasil[0]
        # If fetch_one returns a Row object, access by index or column name
        elif hasattr(hasil, 'id_User'):
            return hasil.id_User
        elif hasattr(hasil, '__getitem__'):
            return hasil[0]
        else:
            return hasil
    return None

def main():
    print("\n=== Selamat datang di Aplikasi Manajemen Event ===")
    username = input("Username: ")
    password = input("Password: ")

    sukses, hasil = login(username, password)
    if sukses:
        if hasil == 'owner':
            tampilkan_menu_pemilik()
        elif hasil == 'asisten':
            id_User = get_idUser(username)
            tampilkan_menu_asisten(id_User)
        elif hasil == 'retry':
            return True
        elif hasil == 'exit':
            return
        else:
            print(f"\nRole tidak dikenali: {hasil}\n")
    else:
        print(hasil)

if __name__ == "__main__":
    while True:
        if not main():
            break
