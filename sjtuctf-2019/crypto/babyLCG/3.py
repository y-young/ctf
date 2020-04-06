#from math import gcd
class LCGPrng():
    def __init__(self, seed, m, c, p):
        self.state = seed
        self.m = m
        self.c = c
        self.p = p

    def next(self):
        self.state = (self.state * self.m + self.c) % self.p
        return self.state

def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
def modinv(b, n):
    g, x, _ = egcd(b, n)
    #print g, x
    #if g == 1:
    return x % n
def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return crack_unknown_multiplier(states, modulus)

states=[0,0,0,0,0,0]
for i in range(6):
    states[i] = int(raw_input())

p, m, c = crack_unknown_modulus(states)

print "\n"
lcg = LCGPrng(states[5], m, c, p)
for i in range(3):
    print lcg.next()
