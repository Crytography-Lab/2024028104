def power(a, b, p):
    result = 1
    a = a % p

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % p

        a = (a * a) % p
        b = b // 2

    return result


a = int(input("Enter a: "))
p = int(input("Enter prime p: "))

if a % p == 0:
    print("Inverse does not exist.")
else:
    inverse = power(a, p - 2, p)
    print("Modular inverse of", a, "modulo", p, "is", inverse)