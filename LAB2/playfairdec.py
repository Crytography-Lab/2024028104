key = input("Enter key: ").upper()
text = input("Enter encrypted text: ").upper()

key = key.replace("J", "I")

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
matrix = ""

for ch in key + alphabet:
    if ch not in matrix:
        matrix += ch

# Prepare text
text = text.replace("J", "I")
text = text.replace(" ", "")

decrypted = ""

for i in range(0, len(text), 2):
    a = text[i]
    b = text[i + 1]

    p1 = matrix.index(a)
    p2 = matrix.index(b)

    r1, c1 = p1 // 5, p1 % 5
    r2, c2 = p2 // 5, p2 % 5

    if r1 == r2:
        decrypted += matrix[r1 * 5 + (c1 - 1) % 5]
        decrypted += matrix[r2 * 5 + (c2 - 1) % 5]

    elif c1 == c2:
        decrypted += matrix[((r1 - 1) % 5) * 5 + c1]
        decrypted += matrix[((r2 - 1) % 5) * 5 + c2]

    else:
        decrypted += matrix[r1 * 5 + c2]
        decrypted += matrix[r2 * 5 + c1]

print("Decrypted text:", decrypted)
