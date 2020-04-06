# coding=utf-8

import binascii
import os
import random

def b2n(b):
    res = 0
    for i in b:
        res *= 2
        res += i
    return res

def n2b(n, length):
    tmp = bin(n)[2:]
    tmp = '0'*(length-len(tmp)) + tmp
    return [int(i) for i in tmp]

def s2n(s):
    return int(binascii.hexlify(s), 16)

def crc64(msg, const):
    msg = n2b(s2n(msg), len(msg)*8)
    msg += const
    for shift in range(len(msg)-64):
        if msg[shift]:
            for i in range(65):
                msg[shift+i] ^= poly[i]
    res = msg[-64:]
    return b2n(res)

const = n2b(0xdeadbeeffeedcafe, 64)
poly  = n2b(0x10000000247f43cb7, 65)
crc = n2b(0x1337733173311337, 64)

msg1 = input()
msg1 = bytes.fromhex(msg1)
msg2 = input()
msg2 = bytes.fromhex(msg2)
before = crc64(msg1, [0] * 64)
msg2 = n2b(s2n(msg2), len(msg2) * 8) + const
reverse = n2b(0, len(msg2)) + crc

for shift in range(len(msg2) - 1, -1, -1):
    if msg2[shift] != reverse[shift + 64]:
        for i in range(65):
            reverse[shift + i] ^= poly[i]

after = b2n(reverse[:64])
print(hex(before ^ after)[2:])