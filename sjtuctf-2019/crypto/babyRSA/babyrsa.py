from flag import FLAG
from Crypto.Util.number import *
import gmpy2
import random

while True:
    p = int(gmpy2.next_prime(random.randint(10**0x1ff, 10**0x200-1)))
    q = int(str(p)[0x100:]+str(p)[:0x100])
    if gmpy2.is_prime(q):
        break
m = bytes_to_long(FLAG)
n = p*q
e = 65537
c = pow(m,e,n)
with open("enc","wb") as f:
    f.write(str(n))
    f.write("\n")
    f.write(str(c))