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
c = int(raw_input())
state = int(raw_input())

print "\n"
lcg = LCGPrng(state, m, c, p)
for i in range(3):
    print lcg.next()
