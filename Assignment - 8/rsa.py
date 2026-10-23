# p = int(input("Enter 1st prime no "))
# q = int(input("Enter 2nd prime no "))

# n = p*q
# e = int(input("Enter public key e "))

# mess = int(input("Enter message(number) "))

# cipher = pow(mess,e,n)
# print("Public key is", (e,n))
# print("Encrypted message is ",cipher)







#decryption
p = int(input("Enter first prime number: "))
q = int(input("Enter second prime number: "))

n = p * q
phi = (p - 1) * (q - 1)

d = int(input("Enter private key d: "))
cipher = int(input("Enter encrypted message: "))

message = pow(cipher, d, n)

print("Private key:", (d, n))
print("Decrypted message:", message)
