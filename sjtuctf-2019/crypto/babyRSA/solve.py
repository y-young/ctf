from math import isqrt
from Crypto.Util.number import *

f = open('enc')
lines = f.readlines()
n = int(lines[0])
c = int(lines[1])
product = int(str(n)[:255] + str(n)[1024-257:]) # a*b
square_sum = (n - 10**512 * product - product) // 10**256
sum = isqrt(square_sum + 2 * product)

delta = sum * sum - 4 * product
delta_root = isqrt(delta)
a = (sum + delta_root) // 2
b = (sum - delta_root) // 2

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

p = (10 ** 256) * a + b
q = (10 ** 256) * b + a
e = 65537
phi = (p - 1) * (q - 1)
d = modinv(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m))
