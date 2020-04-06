from pwn import *
prefix = b'0ops{'
def solve():
    msg = list(prefix) + [0] * (30 - len(prefix))
    cur = len(prefix)
    cnt = 0
    while cur < 30:
        for i in range(0, 256):
            if cnt % 30 == 0:
                sh = remote(host='', port='10080')
                print(sh.recvline())
                enc_flag = str(sh.recvline(), encoding='ascii')
                print(enc_flag)
                enc_flag = eval(enc_flag[enc_flag.find('flag: ') + 6:-1])
            msg[cur] = i
            request = bytes(msg).hex()
            print(request)
            sh.sendline(request)
            enc_msg = str(sh.recvline(), 'ascii')
            enc_msg = enc_msg[enc_msg.find('ciphertext: ') + 12:-1]
            enc_msg = eval(enc_msg)
            cnt += 1
            if enc_msg[:5] == enc_flag[:5]:
                print('Matched: ', request)
                print(sum(bytes.fromhex(request)))
                return
        cur += 1
    sh.close()

solve()
