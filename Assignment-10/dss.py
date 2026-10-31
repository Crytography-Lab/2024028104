import hashlib
import secrets

def generate_keys():
    p = 23
    q = 11
    g = 4

    x = secrets.randbelow(q - 1) + 1
    y = pow(g, x, p)

    return (p, q, g, y), x

def sign(message, private_key, params):
    p, q, g, y = params
    x = private_key

    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q

    while True:
        k = secrets.randbelow(q - 1) + 1
        r = pow(g, k, p) % q

        if r == 0:
            continue

        s = (pow(k, -1, q) * (h + x * r)) % q

        if s != 0:
            return r, s

def verify(message, signature, public_key):
    p, q, g, y = public_key
    r, s = signature

    if not (0 < r < q and 0 < s < q):
        return False

    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q
    w = pow(s, -1, q)
    u1 = (h * w) % q
    u2 = (r * w) % q

    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

    return v == r

public_key, private_key = generate_keys()

message = input("Enter message: ")

signature = sign(message, private_key, public_key)
print("Signature:", signature)

print("Signature valid:", verify(message, signature, public_key))