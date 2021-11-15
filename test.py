from typing import *
from Sbox import sbox, rbox, rcon
import numpy as np
import AES as aes

# ennui = np.array([[0xd4],[0xbf],[0x5d],[0x30]])
# print(ennui)
# circulant_MDS= [[2, 3, 1, 1],
#                 [1, 2, 3, 1],
#                 [1, 1, 2, 3],
#                 [3, 1, 1, 2]]

key_array = [[0x2b, 0x28, 0xab, 0x09], [0x7e, 0xae, 0xf7, 0xcf], [0x15, 0xd2, 0x15, 0x4f], [0x16, 0xa6, 0x88, 0x3c]]

key_array = np.transpose(key_array)

rinter = [rcon[0], 0, 0, 0]

init = [0x8a, 0x84, 0xeb, 0x01]

arr1 = [0x2b, 0x7e, 0x15, 0x16]

ret = [0,0,0,0]

for i in range(0, 4):
    ret[i] = init[i] ^ arr1[i] ^ rinter[i]

for i in range (0,4):
    print("{:0x}".format(ret[i]))
