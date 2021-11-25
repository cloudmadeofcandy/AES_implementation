from aesUtils import *
from Sbox import sbox
import numpy as np

def subBytes(r):
    for i in range(0, 4):
        for j in range(0, 4):
            r[i][j] = sbox[r[i][j]]
    return r

def shiftRows(r):
    r[1][0], r[1][1], r[1][2], r[1][3] = r[1][1], r[1][2], r[1][3], r[1][0]
    r[2][0], r[2][1], r[2][2], r[2][3] = r[2][2], r[2][3], r[2][0], r[2][1]
    r[3][0], r[3][1], r[3][2], r[3][3] = r[3][3], r[3][0], r[3][1], r[3][2]
    return r

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

def gMixColumns(d):
    
    r = list.copy(d)
    r = np.transpose(r)
    r = r.tolist()
    r1 = []

    for i in range(0, 4):
        r[i] = gMixColumn(r[i])
        r1.append(r[i])
    
    r1 = np.transpose(r1)
    r1 = r1.tolist()
    return r1

def AES128(state, cypherkey):
    roundKey = keyExpansion128(cypherkey) # 11 x (4 x 4) array

    result = list.copy(state)

    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = state[i][j] ^ roundKey[0][i][j]

    for q in range(1, 10):
        result = subBytes(result)
        result = shiftRows(result)
        result = gMixColumns(result)
        for i in range(0, 4):
            for j in range(0, 4):
                result[i][j] = result[i][j] ^ roundKey[q][i][j]

    result = subBytes(result)
    result = shiftRows(result)
    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = result[i][j] ^ roundKey[10][i][j]

    return result

def AES192(state, cypherkey):

    roundKey = keyExpansion192(cypherkey) # 11 x (4 x 4) array

    result = list.copy(state)

    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = state[i][j] ^ roundKey[0][i][j]

    for q in range(1, 12):
        result = subBytes(result)
        result = shiftRows(result)
        result = gMixColumns(result)
        for i in range(0, 4):
            for j in range(0, 4):
                result[i][j] = result[i][j] ^ roundKey[q][i][j]

    result = subBytes(result)
    result = shiftRows(result)
    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = result[i][j] ^ roundKey[12][i][j]

    return result

def AES256(state, cypherkey):

    roundKey = keyExpansion256(cypherkey) # 11 x (4 x 4) array

    result = list.copy(state)

    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = state[i][j] ^ roundKey[0][i][j]

    for q in range(1, 14):
        result = subBytes(result)
        result = shiftRows(result)
        result = gMixColumns(result)
        for i in range(0, 4):
            for j in range(0, 4):
                result[i][j] = result[i][j] ^ roundKey[q][i][j]

    result = subBytes(result)
    result = shiftRows(result)
    for i in range(0, 4):
        for j in range(0, 4):
            result[i][j] = result[i][j] ^ roundKey[14][i][j]

    return result