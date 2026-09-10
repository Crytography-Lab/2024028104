import numpy as np

text = input("Enter encrypted text: ").upper()

key_inverse = np.array([[15, 17],
                        [20, 9]])

numbers = [ord(ch) - 65 for ch in text]

decrypted = ""

for i in range(0, len(numbers), 2):
    block = np.array([[numbers[i]],
                      [numbers[i + 1]]])

    result = np.dot(key_inverse, block) % 26

    decrypted += chr(result[0][0] + 65)
    decrypted += chr(result[1][0] + 65)

print("Decrypted text:", decrypted)