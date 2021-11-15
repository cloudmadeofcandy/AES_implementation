from aesUtils import *

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