from typing import List


def mul2(r):
    b = [0 for i in range(4)]
    for c in range(0, 4):
        h = (r[c] >> 7) & 1
        b[c] = r[c] << 1
        b[c] ^= h * 0x1B
    return b

def mul3(r):
    b = mul2(r);
    for c in range(0, 4):
        b[c] = b[c] ^ r[c]
    return b

def mul9(r):
    b = list.copy(r)
    for i in range(0, 3):
        b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    return b

def mul11(r):
    b = list.copy(r)
    b = mul2(b)
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    return b

def mul13(r):
    b = list.copy(r)
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    b = mul2(b)
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    return b            

def mul14(r):
    b = list.copy(r)
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    b = mul2(b)
    return b

def gMixColumn(r):

    a = [0, 0, 0, 0] #[0 for i in range(4)]
    b = [0, 0, 0, 0] #[0 for i in range(4)]
    r1 = [0, 0, 0, 0]

    for c in range(0, 4):
        a[c] = r[c]
        h = (r[c] >> 7) & 1
        b[c] = r[c] << 1
        b[c] ^= h * 0x1B

    r1[0] = (b[0] ^ a[3] ^ a[2] ^ b[1] ^ a[1]) % 256
    r1[1] = (b[1] ^ a[0] ^ a[3] ^ b[2] ^ a[2]) % 256
    r1[2] = (b[2] ^ a[1] ^ a[0] ^ b[3] ^ a[3]) % 256
    r1[3] = (b[3] ^ a[2] ^ a[1] ^ b[0] ^ a[0]) % 256

    return r1

def gInvMixColumn(r):

    a = mul9(r)
    b = mul11(r)
    c = mul13(r)
    d = mul14(r)

    ret = [0, 0, 0, 0]

    ret[0] = (d[0] ^ b[1] ^ c[2] ^ a[3]) % 256
    ret[1] = (a[0] ^ d[1] ^ b[2] ^ c[3]) % 256
    ret[2] = (c[0] ^ a[1] ^ d[2] ^ b[3]) % 256
    ret[3] = (b[0] ^ c[1] ^ a[2] ^ d[3]) % 256

    return ret