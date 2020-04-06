import sys
sys.setrecursionlimit(1000000)
class LCGPrng():
    def __init__(self, seed, m, c, p):
        self.state = seed
        self.m = m
        self.c = c
        self.p = p

    def next(self):
        self.state = (self.state * self.m + self.c) % self.p
        return self.state

def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0
def egcd(a, b):
    print a,b
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(b, n):
    g, x, _ = egcd(b, n)
    print g, x
    #if g == 1:
    return x % n
    #else:
    #    raise Exception('No modular inverse')

def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return multiplier, increment

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)


p = int(raw_input())
states = [0,0,0]
for i in range(3):
    states[i] = long(raw_input())
m,c = crack_unknown_multiplier(states, p)
#print crack_unknown_multiplier([6473702802409947663, 6562621845583276653, 4483807506768649573], 9223372036854775783)


print "\n"
lcg = LCGPrng(states[2], m, c, p)
for i in range(3):
    print lcg.next()
