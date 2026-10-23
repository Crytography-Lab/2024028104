a1 = int(input("Enter value of a1 in x ≅ a1(mod n1)"))
n1 = int(input("Enter value of n1 in x ≅ a1(mod n1)"))
a2 = int(input("Enter value of a2 in x ≅ a2(mod n2)"))
n2 = int(input("Enter value of n2 in x ≅ a2(mod n2)"))
a3 = int(input("Enter value of a3 in x ≅ a3(mod n3)"))
n3 = int(input("Enter value of n3 in x ≅ a3(mod n3)"))

n = n1*n2*n3
N1 = n//n1
N2 = n//n2
N3 = n//n3

def inverse(a, p):
    for x in range(1, p):
        if (a * x) % p == 1:
            return x

M1 = inverse(int(N1), n1)
M2 = inverse(int(N2), n2)
M3 = inverse(int(N3), n3)

x = a1*N1*M1 + a2*N2*M2 + a3*N3*M3

print(x%n)