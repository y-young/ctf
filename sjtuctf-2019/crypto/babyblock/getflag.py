from pwn import *

sh = remote(host='', port='10080')
print(sh.recvline())
enc_flag = str(sh.recvline(), encoding='ascii')
print(enc_flag)
enc_flag = eval(enc_flag[enc_flag.find('flag: ') + 6:-1])
request = '306f70737bffffffffffffffffbf00000000000000000000000000000000'
msg = bytes.fromhex(request)
sh.sendline(request)
enc_msg = str(sh.recvline(), 'ascii')
enc_msg = enc_msg[enc_msg.find('ciphertext: ') + 12:-1]
enc_msg = eval(enc_msg)

flag = str()
for i in range(30):
    flag += chr((msg[i] ^ enc_msg[i]) ^ enc_flag[i])
print(flag)
