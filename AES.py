from encryption import gMixColumns, shiftRows, subBytes
import decryption as de
from aesUtils import keyExpansion, rotWord
from Sbox import sbox, rbox, rcon
import numpy as np


def aesEncrypt(state, cypherkey):
    roundKey = keyExpansion(cypherkey) # 11 x (4 x 4) array

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