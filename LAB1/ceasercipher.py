# # encryption
# tex = input("Enter your text: ")
# key = int(input("Enter your key value: "))
# # 97-122
# for i in tex:
#     ascval = ord(i)
#     pos = ascval - 97
#     pos = (pos+key) % 26
#     newasc = 97 + pos
#     print(chr(newasc),end="")


# decryption
tex = input("Enter your cipher text: ")
for j in range(1,27):
    print(f"Key {j} is",end=" ")
    for i in tex:
        ascval = ord(i)
        pos = ascval - 97
        pos = (pos - j)%26
        newasc = 97+pos
        print(chr(newasc),end="")
    print("\n")