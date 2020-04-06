import string
import sys
import random
import hashlib
import itertools

prefix = sys.argv[1].decode('hex')
length = 8
for combo in itertools.combinations_with_replacement(string.lowercase + string.digits, length):
    digest = hashlib.sha256(prefix + ''.join(combo)).digest()
    if digest.startswith('\xdd\xdd\xdd'):
        print(''.join(combo))
        break
