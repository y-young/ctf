from secret import KEY,MASK

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

LENGTH = 64 
assert(KEY.bit_length()==LENGTH)
assert(MASK.bit_length()==LENGTH)
l = lfsr(KEY,MASK,LENGTH)

#file getflag
#getflag: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 2.6.32, BuildID[sha1]=0fa1c13a2d36aa4d3c03504f473af5685807a786, not stripped

with open("getflag","rb") as f:
    data = f.read()

with open("enc","wb") as f:
    for d in data:
        t = ord(d)
        m = 0
        for i in range(7,-1,-1):
            tmp = (t&(1<<i))>>i
            tmp ^= l.next()
            m += (tmp<<i)
        f.write(chr(m))
