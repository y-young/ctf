class LCGPrng():
    def __init__(self, seed, m, c, p):
        self.state = seed
        self.m = m
        self.c = c
        self.p = p

    def next(self):
        self.state = (self.state * self.m + self.c) % self.p
        return self.state

p = int(raw_input())
m = int(raw_input())
state1 = int(raw_input())
state2 = int(raw_input())

def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return increment

c = crack_unknown_increment([state1, state2], p, m)

print "\n"
lcg = LCGPrng(state2, m, c, p)
for i in range(3):
    print lcg.next()
