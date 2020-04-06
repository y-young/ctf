data = '11100111001101110110010110011010100101000101110010011101010101010001011000101111001011110010101010100101100111100011101010001110'
LEN = 64
LMASK = 2**(LEN+1) - 1
MASK = 0b1111000000001010111111011011010000110111010110110000001110010011
key = 0b0
init = int(data[:LEN-1], 2)

for n in range(0, LEN): # calculate the nth bit of key
    i = init & MASK & LMASK
    output = 0
    for j in range(LEN-1):
        output ^= (i & 1)
        i = i >> 1
    bit = int(data[LEN-n-1]) ^ output
    key |= bit << n
    init = (init >> 1) | (bit << (LEN-2)) # update output sequence

print(bin(key))