import numpy as np

text = input("Enter plaintext: ").upper()

key = np.array([[3, 3],
                [2, 5]])

# Convert letters to numbers
numbers = [ord(ch) - 65 for ch in text]

# If length is odd, add X
if len(numbers) % 2 != 0:
    numbers.append(23)

encrypted = ""

for i in range(0, len(numbers), 2):
    block = np.array([[numbers[i]],
                      [numbers[i + 1]]])

    result = np.dot(key, block) % 26

    encrypted += chr(result[0][0] + 65)
    encrypted += chr(result[1][0] + 65)

print("Encrypted text:", encrypted)


