
from encryption import *
import encryption as en
import decryption as de
from aesUtils import rotWord
from Sbox import sbox, rbox, rcon
import numpy as np
import AES as aes

key_array = [[0x2b, 0x28, 0xab, 0x09],
             [0x7e, 0xae, 0xf7, 0xcf],
             [0x15, 0xd2, 0x15, 0x4f], 
             [0x16, 0xa6, 0x88, 0x3c]]

hello = [[0x19, 0x3d, 0xe3, 0xbe], [0xa0, 0xf4, 0xe2, 0x2b], [0x9a, 0xc6, 0x8d, 0x2a], [0xe9, 0xf8, 0x48, 0x08]]
rev = [[0xd4,0xe0,0xb8,0x1e],[0x27,0xbf,0xb4,0x41],[0x11,0x98,0x5d,0x52],[0xae,0xf1,0xe5,0x30]]

state = [[0x32, 0x88, 0x31, 0xe0],
         [0x43, 0x5a, 0x31, 0x37],
         [0xf6, 0x30, 0x98, 0x07],
         [0xa8, 0x8d, 0xa2, 0x34]]

copyofstate = [[0x32, 0x88, 0x31, 0xe0],
               [0x43, 0x5a, 0x31, 0x37],
               [0xf6, 0x30, 0x98, 0x07],
               [0xa8, 0x8d, 0xa2, 0x34]]

cypherkey = [[0x2b, 0x28, 0xab, 0x09],
             [0x7e, 0xae, 0xf7, 0xcf],
             [0x15, 0xd2, 0x15, 0x4f],
             [0x16, 0xa6, 0x88, 0x3c],
             [0xf6, 0x30, 0x98, 0x07],
             [0xa8, 0x8d, 0xa2, 0x34]]

cypherkey192 = [[0x2b, 0x28, 0xab, 0x09],
             [0x7e, 0xae, 0xf7, 0xcf],
             [0x15, 0xd2, 0x15, 0x4f],
             [0x16, 0xa6, 0x88, 0x3c]]

cipherstate = [[0x39, 0x02, 0xdc, 0x19],
               [0x25, 0xdc, 0x11, 0x6a],
               [0x84, 0x09, 0x85, 0x0b],
               [0x1d, 0xfb, 0x97, 0x32]]

key256 = [[0x60, 0x3d, 0xeb, 0x10], 
          [0x15, 0xca, 0x71, 0xbe],
          [0x2b, 0x73, 0xae, 0xf0],
          [0x85, 0x7d, 0x77, 0x81],
          [0x1f, 0x35, 0x2c, 0x07],
          [0x3b, 0x61, 0x08, 0xd7],
          [0x2d, 0x98, 0x10, 0xa3],
          [0x09, 0x14, 0xdf, 0xf4]]

a = keyExpansion256(key256)

for i in range(0, len(a)):
    for j in range(0, len(a[0])):
        for k in range(0, len(a[0][0])):
            print("{:0x}".format(a[i][j][k]), end=" ")
        print()
    print("\n")
print("_____________________________________")