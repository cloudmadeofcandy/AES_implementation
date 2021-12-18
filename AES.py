from aesUtils import xorMatrix, matToString, stringToMat
import encryption as en
import decryption as de
import numpy as np
import base64 as b64

def encrypt(state = None, key = None, b64 = False, mode = "ECB", IV = None):
    
    ret = ""

    while(state == None):
        print("Please insert your plaintext?")
        state = input()
    
    while(key == None or not (len(key) == 16 or len(key) == 32 or len(key) == 24)):
        print("Please insert your cipher key? Your key must be of length 16, 24 or 32")
        key = input()
    
    if (b64 == True):
        state = state.encode("ascii")
        state = b64.b64decode(state)
        state = state.decode("ascii")

    lenkey = len(key)

    func = {
        16: en.AES128,
        24: en.AES192,
        32: en.AES256
    }

    res = [state[y - 16:y] for y in range(16, len(state) + 16, 16)]

    lim = 16 - len(res[-1])

    for i in range(0, lim):
        res[-1] += chr(0x00)
    
    key = stringToMat(key)
    if (lenkey != 16):
        cypherkey = np.transpose(key)
        cypherkey = cypherkey.tolist()
    else: cypherkey = key
    
    if (mode == "CBC"):
        temp = stringToMat(IV)
        for i in res:
            sub = stringToMat(i)
            sub = xorMatrix(sub, temp)
            sub = func[lenkey](sub, cypherkey)
            temp = sub
            sub = matToString(sub)
            ret += sub

    else: 
        for i in res:
            sub = stringToMat(i)
            sub = func[lenkey](sub, cypherkey)
            sub = matToString(sub)
            ret += sub

    return ret


def decrypt(state = None, key = None, b64 = False, mode = "ECB", IV = None):
    
    ret = ""

    while(state == None):
        print("Please insert your plaintext?")
        state = input()
    
    while(key == None or not (len(key) == 16 or len(key) == 32 or len(key) == 24)):
        print("Please insert your cipher key? Your key must be of length 16, 24 or 32")
        key = input()
    
    lenkey = len(key)

    func = {
        16: de.AES128,
        24: de.AES192,
        32: de.AES256
    }

    res = [state[y - 16:y] for y in range(16, len(state) + 16, 16)]

    lim = 16 - len(res[-1])

    for i in range(0, lim):
        res[-1] += chr(0x00)
    
    key = stringToMat(key)
    if (lenkey != 16):
        cypherkey = np.transpose(key)
        cypherkey = cypherkey.tolist()
    else: cypherkey = key

    if (mode == "CBC"):
        temp = stringToMat(IV)
        for i in res:
            sub = stringToMat(i)
            sub = func[lenkey](sub, cypherkey)
            sub = xorMatrix(sub, temp)
            sub = matToString(sub)
            temp = stringToMat(i)
            ret += sub
    else:
        for i in res:
            sub = stringToMat(i)
            sub = func[lenkey](sub, cypherkey)
            sub = matToString(sub)
            ret += sub

    if (b64 == True):
        ret = ret.encode("ascii")
        ret = b64.b64encode(ret)
        ret = ret.decode("ascii")

    return ret