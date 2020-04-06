from flag import FLAG
import random
import signal
import hashlib
from Crypto.Util.number import *

class LCGPrng():
    def __init__(self, seed, m, c, p):
        self.state = seed
        self.m = m
        self.c = c
        self.p = p

    def next(self):
        self.state = (self.state * self.m + self.c) % self.p
        return self.state
    
    def secure_next(self):
        return self.next()>>90

def proof_of_work():
    prefix = long_to_bytes(random.getrandbits(64))
    print 'prefix = {}'.format(prefix.encode('hex'))
    challenge = raw_input('> ')
    tmp = hashlib.sha256(prefix + challenge).digest()
    if tmp.startswith('\xdd\xdd\xdd'):
        return True
    else:
        return False

def new_lcg():
    p = getPrime(128)
    m = random.randint(2, p)
    c = random.randint(2, p)
    s = random.randint(2, p)
    return LCGPrng(s,m,c,p)

def challenge4():
    print("challenge 4:")
    lcg = new_lcg()
    print(lcg.p)
    print(lcg.m)
    for i in range(20):
        print(lcg.secure_next())
    for i in range(100):
        res = int(raw_input())
        tmp = lcg.secure_next()
        if res!=tmp:
            exit(-1)

welcome = """
             _                       
 _ _ _  ___ | | ___  ___ ._ _ _  ___ 
| | | |/ ._>| |/ | '/ . \| ' ' |/ ._>
|__/_/ \___.|_|\_|_.\___/|_|_|_|\___.
                                     
"""

def main():
    if not proof_of_work():
        exit(-1)
    signal.alarm(120)
    print(welcome)
    print("welcome to LCGLAB")
    challenge4()
    print(FLAG)

if __name__=="__main__":
    main()