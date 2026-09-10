text = input("Enter text: ").upper()
key = input("Enter key: ").upper()

encrypted = ""
j = 0

# Encryption
for ch in text:
    if ch.isalpha():
        value = (ord(ch) - ord('A') + ord(key[j])) - ord('A')
        value = value % 26
        encrypted += chr(value + ord('A'))
        j = (j + 1) % len(key)
    else:
        encrypted += ch

print("Encrypted text:", encrypted)

# Decryption
decrypted = ""
j = 0

for ch in encrypted:
    if ch.isalpha():
        value = (ord(ch) - ord('A') - (ord(key[j]) - ord('A')))
        value = value % 26
        decrypted += chr(value + ord('A'))
        j = (j + 1) % len(key)
    else:
        decrypted += ch

print("Decrypted text:", decrypted)