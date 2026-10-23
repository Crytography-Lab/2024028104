text = input("Enter encrypted text: ").upper()
rails = int(input("Enter number of rails: "))

n = len(text)
pattern = list(range(rails)) + list(range(rails-2, 0, -1))

rows = [pattern[i % len(pattern)] for i in range(n)]

decrypted = ""
k = 0

for r in range(rails):
    for i in range(n):
        if rows[i] == r:
            rows[i] = text[k]
            k += 1

k = 0
for i in range(n):
    decrypted += rows[i]

print("Decrypted text:", decrypted)