import os
import pyaes

files = [f for f in os.listdir('.') if os.path.isfile(f)]  

decrypted_files = []

for file_name in files:
    if file_name.endswith('.ransomwaretroll'):
        with open(file_name, "rb") as file:
            file_data = file.read()

        os.remove(file_name)

        key = b"ReisRansomwaresLongerKey12345"  

        aes = pyaes.AESModeOfOperationCTR(key)

        decrypted_data = aes.decrypt(file_data)

        new_file = file_name.replace(".ransomwaretroll", "")

        with open(new_file, "wb") as new_file_handle:
            new_file_handle.write(decrypted_data)

        decrypted_files.append(new_file)

print("Todos os arquivos foram Descriptografados com Sucesso!")

for decrypted_file in decrypted_files:
    print(decrypted_file)

print(f"Total de arquivos descriptografados: {len(decrypted_files)}")
