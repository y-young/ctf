from string import *

key = "secret_xor_key_for_u_to_crack"
with open('output', 'rb') as f:
    with open('map', 'w') as out:
        data = f.read()
        i = 0
        for c in data:
            out.write(chr(ord(key[i]) ^ c))
            i = (i + 1) % len(key)
        
        
