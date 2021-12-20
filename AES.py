from aesUtils import xorMatrix, matToString, stringToMat, matToHexa, hexaToMat, _4x4print, b64d, b64e
import encryption as en
import decryption as de
import numpy as np

def encrypt(state = None, key = None, b64 = False, mode = "ECB", IV = None, hexa = False):
    
    ret = ""

    while(state == None):
        print("Please insert your plaintext?")
        state = input()
    
    while(key == None or not (len(key) == 16 or len(key) == 32 or len(key) == 24)):
        print("Please insert your cipher key? Your key must be of length 16, 24 or 32")
        key = input()
    
    if (b64 == True):
        state = b64e(state)

    lenkey = len(key)

    func = {
        16: en.AES128,
        24: en.AES192,
        32: en.AES256
    }

    matConversion = {
        True: matToHexa,
        False: matToString
    }

    strConversion = {
        False: stringToMat,
        True: hexaToMat
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

    elif (mode == "CFB"):
        temp = stringToMat(IV)
        for i in res:
            sub = stringToMat(i)
            temp1 = func[lenkey](temp, cypherkey)
            sub = xorMatrix(sub, temp1)
            temp = sub
            sub = matToString(sub)
            ret += sub


    elif (mode == "OFB"):
        pass

    else: 
        for i in res:
            sub = stringToMat(i)
            sub = func[lenkey](sub, cypherkey)
            sub = matToString(sub)
            ret += sub

    return ret


def decrypt(state = None, key = None, b64 = False, mode = "ECB", IV = None, hexa = False):
    
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

    enfunc = {
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
            sub = func[lenkey](sub, cypherkey)
            sub = xorMatrix(sub, temp)
            sub = matToString(sub)
            temp = stringToMat(i)
            ret += sub
    
    elif (mode == "CFB"):
        temp = stringToMat(IV)
        for i in res:
            sub = stringToMat(i)
            temp = enfunc[lenkey](temp, cypherkey)
            sub = xorMatrix(sub, temp)
            temp = stringToMat(i)
            sub = matToString(sub)
            ret += sub


    elif (mode == "OFB"):
        pass

    else:
        for i in res:
            sub = stringToMat(i)
            sub = func[lenkey](sub, cypherkey)
            sub = matToString(sub)
            ret += sub

    ret = ret.rstrip(chr(0x00))

    if (b64 == True):
        ret = b64d(ret)

    return ret