from typing import List
from Sbox import sbox, rbox
import numpy as np
import AES as aes
# ennui = np.array([[0xd4],[0xbf],[0x5d],[0x30]])
# print(ennui)
circulant_MDS= [[2, 3, 1, 1],
                [1, 2, 3, 1],
                [1, 1, 2, 3],
                [3, 1, 1, 2]]

key_array = [[], [], [], []]

print("{:0x}".format(0x7e ^ 0x84 ^ 0x00))