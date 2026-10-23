a = int(input("Enter a: "))
p = int(input("Enter a prime number p: "))

if a % p == 0:
    print("a is divisible by p, so the theorem does not apply.")
else:
    result = pow(a, p - 1, p)
    print("Result:", result)

    if result == 1:
        print("Fermat's Little Theorem is verified.")
    else:
        print("The theorem is not satisfied (check if p is prime).")