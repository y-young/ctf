import random
from string import *
from itertools import cycle
from secret import key, message

assert len(key) < 50
assert all(c in (digits + ascii_letters + punctuation + ' \n') for c in key + message)

t = list(ascii_lowercase)
random.shuffle(t)
d = dict(zip(ascii_lowercase, t))
d.update({k.upper(): v.upper() for k, v in d.items()})
mapping = str.maketrans(d)
enc = bytes(ord(x) ^ ord(y) for x, y in zip(message.translate(mapping), cycle(key)))
with open('output', 'wb') as f:
    f.write(enc)
