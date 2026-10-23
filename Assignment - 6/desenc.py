# DES ENCRYPTION

#Initial permutation
IP = [
58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7
]

#Final permutation
FP = [
40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25
]

# CORRECT 48-bit expansion table
E = [
32,1,2,3,4,5,
4,5,6,7,8,9,
8,9,10,11,12,13,
12,13,14,15,16,17,
16,17,18,19,20,21,
20,21,22,23,24,25,
24,25,26,27,28,29,
28,29,30,31,32,1
]

P = [
16,7,20,21,29,12,28,17,
1,15,23,26,5,18,31,10,
2,8,24,14,32,27,3,9,
19,13,30,6,22,11,4,25
]

PC1 = [
57,49,41,33,25,17,9,1,58,50,42,34,26,18,
10,2,59,51,43,35,27,19,11,3,60,52,44,36,
63,55,47,39,31,23,15,7,62,54,46,38,30,22,
14,6,61,53,45,37,29,21,13,5,28,20,12,4
]

PC2 = [
14,17,11,24,1,5,3,28,
15,6,21,10,23,19,12,4,
26,8,16,7,27,20,13,2,
41,52,31,37,47,55,30,40,
51,45,33,48,44,49,39,56,
34,53,46,42,50,36,29,32
]

SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)


def xor(a, b):
    result = ""

    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"

    return result


def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)


def left_shift(bits, n):
    return bits[n:] + bits[:n]


def generate_keys(key):

    key = text_to_bits(key)

    key = permute(key, PC1)

    C = key[:28]
    D = key[28:]

    keys = []

    for shift in SHIFTS:

        C = left_shift(C, shift)
        D = left_shift(D, shift)

        keys.append(permute(C + D, PC2))

    return keys


def f_function(R, key):

    # 32 bits -> 48 bits
    expanded = permute(R, E)

    # XOR
    x = xor(expanded, key)

    # Simple substitution
    result = ""

    for i in range(0, 48, 6):

        block = x[i:i + 6]

        value = int(block, 2)

        result += format(value % 16, '04b')

    # 32 bits
    return permute(result, P)


def encrypt_block(block, keys):

    block = permute(block, IP)

    L = block[:32]
    R = block[32:]

    for i in range(16):

        new_L = R
        new_R = xor(L, f_function(R, keys[i]))

        L = new_L
        R = new_R

    # Swap
    return permute(R + L, FP)


def pad(text):

    n = 8 - (len(text) % 8)

    return text + chr(n) * n


# -------- MAIN --------

plaintext = input("Enter plaintext: ")
key = input("Enter 8 character key: ")

if len(key) != 8:

    print("Key must contain exactly 8 characters.")

else:

    plaintext = pad(plaintext)

    keys = generate_keys(key)

    ciphertext = ""

    for i in range(0, len(plaintext), 8):

        block = plaintext[i:i + 8]

        bits = text_to_bits(block)

        encrypted = encrypt_block(bits, keys)

        # Binary -> Hexadecimal
        ciphertext += format(int(encrypted, 2), '016X')

    print("\nEncrypted text:")
    print(ciphertext)