import re

pat = r"devinputevent2: ([\da-f]{4}) ([\da-f]{4}) ([\da-f]{8})"
f = open('parse1.txt', 'r')
raw = f.read()
f.close()
data = re.findall(pat, raw)
f = open('parse2.txt', 'w')
for d in data:
    arg = [int(str(x),16) for x in d]
    if arg[1] == 54 or arg[1] == 53:
        arg[2] /= 2
    f.write('sendevent /dev/input/event1 %d %d %d \n' % (arg[0], arg[1], arg[2]))
