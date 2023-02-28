
#!/usr/bin/python3

import os
import pyaes

file_name = "test.txt.ransomware"
file = open(file_name, "rb")
encrypted_data = file.read()
file.close()

key = b'0123456789ABCDEF'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(encrypted_data)

os.remove(file_name)

new_file = file_name[:-11]
file = open(new_file, "wb")
file.write(decrypt_data)
file.close()
