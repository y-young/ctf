#!/usr/bin/python
# coding=utf-8

from struct import pack, unpack

def enc(msg, pubkey):
    m = int(msg, 16)
    n = len(pubkey)
    data = pubkey[:]
    tmp = [None] * n
    res = range(n)
    for i in bin(m)[:1:-1]:
        if i == '1':
            for k in range(n):
                tmp[k] = res[data[k]]
            res = tmp[:]
        for k in range(n):
            tmp[k] = data[data[k]]
        data = tmp[:]
    return res

if __name__ == '__main__':
    with open('flag') as f:
        flag = f.read()
    msg = flag[5:-1]
    assert flag.startswith('0ops{') and flag.endswith('}') and len(msg) == 16 and msg.islower()

    with open('pubkey', 'rb') as f:
        pubkey = unpack('16384H', f.read())
    res = enc(msg, pubkey)
    with open('result', 'wb') as f:
        f.write(pack('16384H', *res))

