from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

# Membuat key dari password
def get_key(password):
    return hashlib.sha256(password.encode()).digest()

# Enkripsi file
def encrypt_file(input_file, output_file, password):
    key = get_key(password)

    with open(input_file, 'rb') as f:
        data = f.read()

    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    encrypted_data = cipher.encrypt(
        pad(data, AES.block_size)
    )

    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_data)

    print("File berhasil dienkripsi!")

# Dekripsi file
def decrypt_file(input_file, output_file, password):
    key = get_key(password)

    with open(input_file, 'rb') as f:
        file_data = f.read()

    iv = file_data[:16]
    encrypted_data = file_data[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)

    decrypted_data = unpad(
        cipher.decrypt(encrypted_data),
        AES.block_size
    )

    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

    print("File berhasil didekripsi!")

# Menu Program
while True:
    print("\n===== AES FILE ENCRYPTION =====")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Pilih menu: ")

    if choice == "1":
        infile = input("Nama file TXT: ")
        outfile = input("Nama file hasil enkripsi: ")
        password = input("Password: ")

        encrypt_file(infile, outfile, password)

    elif choice == "2":
        infile = input("File terenkripsi: ")
        outfile = input("Nama file hasil dekripsi: ")
        password = input("Password: ")

        decrypt_file(infile, outfile, password)

    elif choice == "3":
        break

    else:
        print("Pilihan tidak valid!")