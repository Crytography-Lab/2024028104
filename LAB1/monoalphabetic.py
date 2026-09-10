alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = input("Enter the text: ").upper()
key = input("Enter 26-letter key: ").upper()

# Encryption
encrypted = ""

for ch in text:
    if ch in alphabet:
        encrypted += key[alphabet.index(ch)]
    else:
        encrypted += ch

print("encrypted text:", encrypted)

# Decryption
decrypted = ""

for ch in encrypted:
    if ch in key:
        decrypted += alphabet[key.index(ch)]
    else:
        decrypted += ch

print("Decrypted text:", decrypted)

