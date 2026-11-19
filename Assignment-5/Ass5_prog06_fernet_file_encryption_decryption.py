# Write a Python program to encrypt the contents of a text file using Fernet and save the key and the encrypted file
# separately. Write another program to decrypt the file. Show that decryption fails with a wrong key.

"""
pip install cryptography twisted
"""

# encrypt_file.py
from cryptography.fernet import Fernet

filename = input("Enter text file name: ")

# Generate a key and save it separately
key = Fernet.generate_key()
with open("secret.key", "wb") as f:
    f.write(key)

# Read, encrypt and save the encrypted file
with open(filename, "rb") as f:
    data = f.read()

encrypted = Fernet(key).encrypt(data)

with open(filename + ".enc", "wb") as f:
    f.write(encrypted)

print("Encrypted file:", filename + ".enc")
print("Key saved in : secret.key")

# ----------------------------------------------------------------------------
# decrypt_file.py

from cryptography.fernet import Fernet, InvalidToken

enc_file = input("Enter encrypted file name: ")
key_file = input("Enter key file name: ")

with open(key_file, "rb") as f:
    key = f.read()
with open(enc_file, "rb") as f:
    encrypted = f.read()

try:
    decrypted = Fernet(key).decrypt(encrypted)
    print("Decryption successful. Contents:")
    print(decrypted.decode())
except InvalidToken:
    print("Decryption FAILED: wrong key or file was changed")

# ----------------------------------------------------------------------------------

# wrong_key.py

from cryptography.fernet import Fernet

with open("wrong.key", "wb") as f:
    f.write(Fernet.generate_key())
print("wrong.key created")


"""
Run this program using following steps:
Create test.txt with some text.
Run encrypt_file.py and enter test.txt.
Run decrypt_file.py with test.txt.enc and secret.key. It shows the text.
Run make_wrong_key.py, then run decrypt_file.py with test.txt.enc and wrong.key. It prints “Decryption FAILED”.
"""
