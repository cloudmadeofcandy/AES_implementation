
from encryption import gMixColumns, shiftRows, subBytes
from decryption import gInvMixColumns, invShiftRows, invSubBytes
from aesUtils import keyExpansion128, rotWord
from Sbox import sbox, rbox, rcon
import numpy as np


def aesEncrypt128(state, cypherkey):
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

def aesDecrypt128(state, cypherkey):
    
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