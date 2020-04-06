import random
from flag import FLAG
import hashlib
import signal
from Crypto.Cipher import AES
from Crypto.Util.number import *

def pad(s):
    padnum = 16 - len(s) % 16
    return s + padnum * chr(padnum)

tmp = ""
for i in range(4):
    tmp += str(random.random())
key = hashlib.md5(tmp).digest()
aes = AES.new(key,AES.MODE_ECB)
enc_flag = aes.encrypt(pad(FLAG))

def proof_of_work():
    prefix = long_to_bytes(random.getrandbits(64))
    print 'prefix = {}'.format(prefix.encode('hex'))
    challenge = raw_input('> ')
    tmp = hashlib.sha256(prefix + challenge).digest()
    if tmp.startswith('\xdd\xdd\xdd'):
        return True
    else:
        return False

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
    print welcome
    print "welcome to AESLAB"
    print enc_flag.encode("hex")
    for _ in range(160):
        key = raw_input("input your key:").strip()
        if len(key)!=16:
            exit(-1)
        iv = long_to_bytes(random.getrandbits(128)).rjust(16,"\x00")
        aes = AES.new(key,AES.MODE_CBC,iv)
        msg = raw_input("input your msg:").strip()
        enc = aes.encrypt(pad(msg))
        print (iv+enc).encode("hex")
    return

if __name__=="__main__":
    main()