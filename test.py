from typing import *
from Sbox import sbox, rbox, rcon
import numpy as np
import AES as aes
import encryption as ec
import decryption as dc

# ennui = np.array([[0xd4],[0xbf],[0x5d],[0x30]])
# print(ennui)
# circulant_MDS= [[2, 3, 1, 1],
#                 [1, 2, 3, 1],
#                 [1, 1, 2, 3],
#                 [3, 1, 1, 2]]

# roundKeyArray = []

# key_array = [[0x2b, 0x28, 0xab, 0x09],
#              [0x7e, 0xae, 0xf7, 0xcf],
#              [0x15, 0xd2, 0x15, 0x4f], 
#              [0x16, 0xa6, 0x88, 0x3c]]

# roundKeyArray.append(key_array) 

# rconarray = [[rcon[i], 0, 0, 0] for i in rcon]

# init = [0x8a, 0x84, 0xeb, 0x01]

# arr1 = [0x2b, 0x7e, 0x15, 0x16]

# ret = [0,0,0,0]

# for i in range(0, 4):
#     ret[i] = init[i] ^ arr1[i] ^ rinter[i]

# for i in range (0,4):
#     print("{:0x}".format(ret[i]))


hello = [[0x19, 0x3d, 0xe3, 0xbe], [0xa0, 0xf4, 0xe2, 0x2b], [0x9a, 0xc6, 0x8d, 0x2a], [0xe9, 0xf8, 0x48, 0x08]]
rev = [[0xd4,0xe0,0xb8,0x1e],[0x27,0xbf,0xb4,0x41],[0x11,0x98,0x5d,0x52],[0xae,0xf1,0xe5,0x30]]

hello = np.transpose(hello)

# for i in range(0, 4):
#     for j in range(0, 4):
#         print("{:0x}".format(hello[i][j]))
he = ec.subBytes(hello)

he = ec.shiftRows(he)
he = dc.invShiftRows(he)

for i in range(0, 4):
    for j in range(0, 4):
        print("{:0x}".format(he[i][j]), end=" ");
    print()

