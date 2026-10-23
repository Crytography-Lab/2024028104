import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = input("Enter key (16, 24, or 32 characters): ").encode()
text = input("Enter text: ")

if len(key) not in (16, 24, 32):
    print("Key must be 16, 24, or 32 bytes.")
else:
    nonce = os.urandom(12)

    # Encrypt
    encrypted = AESGCM(key).encrypt(nonce, text.encode(), None)
    encrypted = (nonce + encrypted).hex()

    print("Encrypted:", encrypted)

    # Decrypt
    data = bytes.fromhex(encrypted)
    nonce = data[:12]
    encrypted = data[12:]

    decrypted = AESGCM(key).decrypt(nonce, encrypted, None).decode()

    print("Decrypted:", decrypted)