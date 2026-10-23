text = input("Enter text: ").upper().replace(" ", "")
key = input("Enter key: ").upper()

def columnar(text, key):
    n = len(key)

    # Add X if needed
    while len(text) % n != 0:
        text += "X"

    result = ""

    # Read columns according to alphabetical order of key
    for i in sorted(range(n), key=lambda x: key[x]):
        result += text[i::n]

    return result

# First transposition
text = columnar(text, key)

# Second transposition
text = columnar(text, key)

print("Encrypted text:", text)