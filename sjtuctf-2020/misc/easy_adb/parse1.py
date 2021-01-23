import codecs
import re

f = open('usbdata.txt','r')
lines = f.readlines()
f.close()
f = open('parse1.txt', 'w')
data = []
for line in lines:
    raw = bytes(line.strip(),'utf8')
    raw = codecs.decode(raw, 'hex')
    raw = raw.decode('ascii', 'ignore')
    raw = re.sub(r"[^\d\w:\'\"\s]", '', raw)
    f.write(raw.strip())
f.close()
