import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

n = p * q
phi = (p - 1) * (q - 1)

e = int(input("Enter public exponent (e): "))

while gcd(e, phi) != 1:
    print("e must be coprime with phi.")
    e = int(input("Enter another value for e: "))

d = mod_inverse(e, phi)

print("\nPublic Key: ({}, {})".format(e, n))
print("Private Key: ({}, {})".format(d, n))

msg = int(input("\nEnter message (integer less than {}): ".format(n)))

cipher = pow(msg, e, n)
print("Encrypted Message:", cipher)

plain = pow(cipher, d, n)
print("Decrypted Message:", plain)