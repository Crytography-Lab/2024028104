def phi(n):
    result = n
    p=2
    while p*p<=n:
        if n%p==0:
            while n%p==0:
                n = n//p
            result = result - result//p
        p = p+1
    if n>1:
        result = result - result//n
    return int(result)

n = int(input("Enter your number"))
print("Phi of n is ",phi(n))

