from encryption import *
import encryption as en
import decryption as de
from aesUtils import keyExpansion, rotWord
from Sbox import sbox, rbox, rcon
import numpy as np
import AES as aes


# ennui = np.array([[0xd4],[0xbf],[0x5d],[0x30]])
# print(ennui)
# circulant_MDS= [[2, 3, 1, 1],
#                 [1, 2, 3, 1],
#                 [1, 1, 2, 3],
#                 [3, 1, 1, 2]]

# roundKeyArray = []

key_array = [[0x2b, 0x28, 0xab, 0x09],
             [0x7e, 0xae, 0xf7, 0xcf],
             [0x15, 0xd2, 0x15, 0x4f], 
             [0x16, 0xa6, 0x88, 0x3c]]

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


#hello = np.transpose(hello)

# # for i in range(0, 4):
# #     for j in range(0, 4):
# #         print("{:0x}".format(hello[i][j]))
# he = ec.subBytes(hello)

# he = ec.shiftRows(he)
# he = dc.invShiftRows(he)

# for i in range(0, 4):
#     for j in range(0, 4):
#         print("{:0x}".format(he[i][j]), end=" ");
#     print()

# hi = [1, 1, 1, 1]

# hello.append(hi)

# hi = hi.append(1)

# print(hello)

# key = key_array

# retkey = []
# retkey.append(list.copy(key))

# newkey = [];
# interkey = list.copy(retkey[-1]) # 4x4 array

# interkey = np.transpose(interkey)
# interkey = interkey.tolist()

# # print("start")
# # for v in range(0, 4):
# #     for u in range(0, 4):
# #         print("{:0x}".format(interkey[v][u]), end=" ");
# #     print()

# rconarr = [rcon[0], 0, 0, 0]
# workingarr = list.copy(interkey[-1]) # 1x4 array

# workingarr = rotWord(workingarr)

# for q in range(0, 4):
#     workingarr[q] = sbox[workingarr[q]]

# for j in range(0, len(workingarr)):
#     workingarr[j] = workingarr[j] ^ interkey[0][j] ^ rconarr[j]

# newkey.append(list.copy(workingarr))

# # print("start")
# # for u in range(0, 4):
# #     print("{:0x}".format(workingarr[u]), end=" ");
# # print()

# print("start")
# for v in range(0, 4):
#     for u in range(0, 4):
#         print("{:0x}".format(interkey[v][u]), end=" ");
#     print()

# for k in range(1, 4):
#     for j in range(0, 4):
#         workingarr[j] = workingarr[j] ^ interkey[k][j]
#     newkey.append(list.copy(workingarr))
# newkey = np.transpose(newkey)
# newkey = newkey.tolist()
# for v in range(0, 4):
#     for u in range(0, 4):
#         print("{:0x}".format(newkey[v][u]), end=" ");
#     print()
# retkey.append(newkey)

# a = keyExpansion(key_array)

# for i in range(0, len(a)):
#     for j in range(0, 4):
#         for k in range(0, 4):
#             print("{:0x}".format(a[i][j][k]), end=" ");
#         print()
#     print("__________________________\n")



state = [[0x32, 0x88, 0x31, 0xe0],
         [0x43, 0x5a, 0x31, 0x37],
         [0xf6, 0x30, 0x98, 0x07],
         [0xa8, 0x8d, 0xa2, 0x34]]

cypherkey = [[0x2b, 0x28, 0xab, 0x09],
             [0x7e, 0xae, 0xf7, 0xcf],
             [0x15, 0xd2, 0x15, 0x4f],
             [0x16, 0xa6, 0x88, 0x3c]]

# roundKey = keyExpansion(cypherkey) # 11 x (4 x 4) array

# result = list.copy(state)

# for i in range(0, 4):
#     for j in range(0, 4):
#         result[i][j] = state[i][j] ^ roundKey[0][i][j]

# for q in range(1, 10):
#     result = subBytes(result)
#     result = shiftRows(result)
#     result = gMixColumns(result)
#     for i in range(0, 4):
#         for j in range(0, 4):
#             result[i][j] = result[i][j] ^ roundKey[q][i][j]
#     for v in range(0, 4):
#         for u in range(0, 4):
#             print("{:0x}".format(result[v][u]), end=" ");
#         print()
#     print("___________________")

# result = subBytes(result)
# result = shiftRows(result)
# for i in range(0, 4):
#     for j in range(0, 4):
#         result[i][j] = result[i][j] ^ roundKey[10][i][j]

result = aes.aesEncrypt(state, cypherkey)

for v in range(0, 4):
    for u in range(0, 4):
        print("{:0x}".format(result[v][u]), end=" ");
    print()
print("___________________")
