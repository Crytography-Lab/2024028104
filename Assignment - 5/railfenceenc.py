text = input("Enter text: ").upper()
rails = int(input("Enter number of rails: "))

fence = [""] * rails
row = 0
direction = 1

for ch in text:
    fence[row] += ch

    if row == 0:
        direction = 1
    elif row == rails - 1:
        direction = -1

    row += direction

encrypted = ""

for r in fence:
    encrypted += r

print("Encrypted text:", encrypted)