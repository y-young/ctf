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
    p = 0
    m = getPrime(63)
    c = random.randint(2**62,2**63)
    s = random.randint(2**62,2**63)
    while p<m or p<c or p<s:
        p = getPrime(64)
    return LCGPrng(s,m,c,p)

def challenge0():
    print("challenge 0:")
    lcg = new_lcg()
    print(lcg.p)
    print(lcg.m)
    print(lcg.c)
    print(lcg.state)
    for i in range(3):
        res = int(raw_input())
        if res!=lcg.next():
            exit(-1)

def challenge1():
    print("challenge 1:")
    lcg = new_lcg()
    print(lcg.p)
    print(lcg.m)
    print(lcg.state)
    print(lcg.next())
    for i in range(3):
        res = int(raw_input())
        if res!=lcg.next():
            exit(-1)

def challenge2():
    print("challenge 2:")
    lcg = new_lcg()
    print(lcg.p)
    print(lcg.state)
    print(lcg.next())
    print(lcg.next())
    for i in range(3):
        res = int(raw_input())
        if res!=lcg.next():
            exit(-1)

def challenge3():
    print("challenge 3:")
    lcg = new_lcg()
    print(lcg.state)
    print(lcg.next())
    print(lcg.next())
    print(lcg.next())
    print(lcg.next())
    print(lcg.next())
    for i in range(3):
        res = int(raw_input())
        if res!=lcg.next():
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
    signal.alarm(60)
    print(welcome)
    print("welcome to LCGLAB")
    challenge0()
    challenge1()
    challenge2()
    challenge3()
    print(FLAG)

if __name__=="__main__":
    main()
