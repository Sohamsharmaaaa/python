# Write a Python program using the cryptography library (Fernet) to encrypt a message and then decrypt it.

from cryptography.fernet import Fernet

# Generate a secret key
key = Fernet.generate_key()
fernet = Fernet(key)

message = input("Enter a message: ")

# Encrypt (needs bytes)
encrypted = fernet.encrypt(message.encode())
print("Encrypted:", encrypted)

# Decrypt
decrypted = fernet.decrypt(encrypted).decode()
print("Decrypted:", decrypted)
