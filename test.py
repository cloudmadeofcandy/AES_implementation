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

inter = np.array(circulant_MDS)
# inter = inter.T
# print(inter)

listarr = inter.tolist()
hrllo = np.transpose(circulant_MDS)

print(circulant_MDS[1:4][0:1])

print("{:0x}".format(0x7e ^ 0x84 ^ 0x00))