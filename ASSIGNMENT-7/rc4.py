def rc4(text, key):
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    result = []

    for ch in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        k = S[(S[i] + S[j]) % 256]
        result.append(ch ^ k)

    return result


text = input("Enter text: ")
key = input("Enter key: ")

key_bytes = [ord(ch) for ch in key]
text_bytes = [ord(ch) for ch in text]

encrypted = rc4(text_bytes, key_bytes)
print("Encrypted text:", bytes(encrypted).hex())

decrypted = rc4(encrypted, key_bytes)
print("Decrypted text:", "".join(chr(ch) for ch in decrypted))