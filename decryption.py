from aesUtils import *
from Sbox import rbox
import numpy as np

def invSubBytes(r):
    for i in range(0, 4):
        for j in range(0, 4):
            r[i][j] = rbox[r[i][j]]
    return r

def invShiftRows(r):
    r[1][0], r[1][1], r[1][2], r[1][3] = r[1][3], r[1][0], r[1][1], r[1][2]
    r[2][0], r[2][1], r[2][2], r[2][3] = r[2][2], r[2][3], r[2][0], r[2][1]
    r[3][0], r[3][1], r[3][2], r[3][3] = r[3][1], r[3][2], r[3][3], r[3][0]
    return r

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

def gInvMixColumns(d):
    
    r = list.copy(d)
    r = np.transpose(r)
    r = r.tolist()
    r1 = []

    for i in range(0, 4):
        r[i] = gInvMixColumn(r[i])
        r1.append(r[i])
    
    r1 = np.transpose(r1)
    r1 = r1.tolist()
    return r1

def AES128(state, cypherkey):
    
    roundKey = keyExpansion128(cypherkey) # 11 x (4 x 4) array

    result = list.copy(state)

    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = state[i][j] ^ roundKey[10][i][j]

    for q in range(9, 0, -1):
        result = invShiftRows(result)
        result = invSubBytes(result)
        for i in range(0, 4):
            for j in range(0, 4):
                result[i][j] = result[i][j] ^ roundKey[q][i][j]
        result = gInvMixColumns(result)

    result = invShiftRows(result)
    result = invSubBytes(result)
    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = result[i][j] ^ roundKey[0][i][j]

    return result


def AES192(state, cypherkey):
    
    roundKey = keyExpansion192(cypherkey) # 11 x (4 x 4) array

    result = list.copy(state)

    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = state[i][j] ^ roundKey[12][i][j]

    for q in range(11, 0, -1):
        result = invShiftRows(result)
        result = invSubBytes(result)
        for i in range(0, 4):
            for j in range(0, 4):
                result[i][j] = result[i][j] ^ roundKey[q][i][j]
        result = gInvMixColumns(result)

    result = invShiftRows(result)
    result = invSubBytes(result)
    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = result[i][j] ^ roundKey[0][i][j]

    return result


def AES256(state, cypherkey):
    
    roundKey = keyExpansion256(cypherkey) # 11 x (4 x 4) array

    result = list.copy(state)

    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = state[i][j] ^ roundKey[14][i][j]

    for q in range(13, 0, -1):
        result = invShiftRows(result)
        result = invSubBytes(result)
        for i in range(0, 4):
            for j in range(0, 4):
                result[i][j] = result[i][j] ^ roundKey[q][i][j]
        result = gInvMixColumns(result)

    result = invShiftRows(result)
    result = invSubBytes(result)
    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = result[i][j] ^ roundKey[0][i][j]

    return result