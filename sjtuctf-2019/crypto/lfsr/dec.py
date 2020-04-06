import struct

class lfsr():
    def __init__(self, init, mask, length):
        self.init = init
        self.mask = mask
        self.lengthmask = 2**(length+1)-1

    def next(self):
        nextdata = (self.init << 1) & self.lengthmask
        i = self.init & self.mask & self.lengthmask
        output = 0
        while i != 0:
            output ^= (i & 1)
            i = i >> 1
        nextdata ^= output
        self.init = nextdata
        return output

MASK = 0b1111000000001010111111011011010000110111010110110000001110010011
KEY = 0b1001110001100010110101110100011110001111011010001011001010110011
LENGTH = 64
l = lfsr(KEY, MASK, LENGTH)

with open('enc', 'rb') as f:
    data = f.read()

with open('getflag', 'wb') as f:
    for ch in data:
        tmp = 0
        for i in range(7, -1, -1):
            tmp += l.next() << i
        t = ch ^ tmp
        f.write(struct.pack('B', t))