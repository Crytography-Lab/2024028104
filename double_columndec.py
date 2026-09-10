text = input("Enter encrypted text: ").upper()
key = input("Enter key: ").upper()

def decrypt(text, key):
    n = len(key)
    rows = len(text) // n

    # Create empty table
    table = [[""] * n for _ in range(rows)]

    # Fill columns according to alphabetical order of key
    order = sorted(range(n), key=lambda x: key[x])

    k = 0
    for col in order:
        for row in range(rows):
            table[row][col] = text[k]
            k += 1

    # Read row by row
    result = ""
    for row in table:
        result += "".join(row)

    return result

# First decryption
text = decrypt(text, key)

# Second decryption
text = decrypt(text, key)

print("Decrypted text:", text)