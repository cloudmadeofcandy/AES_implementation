from aesUtils import xorMatrix, matToString, stringToMat, matToHexa, hexaToMat, _4x4print, b64d, b64e
import encryption as en
import decryption as de
import numpy as np

def encrypt(state = None, key = None, b64 = False, mode = "ECB", IV = None, hexain = False, hexakey = False, hexaIV = False, hexaout = False, cipher = None):
    
    ret = ""
    lenkey = 0

    b64 = True if b64 == "True" else False
    hexain = True if hexain == "True" else False
    hexakey = True if hexakey == "True" else False
    hexaIV = True if hexaIV == "True" else False
    hexaout = True if hexaout == "True" else False

    if (hexakey):
        lenkey = len(key) / 2
    else:
        lenkey = len(key)

    while(state == None):
        print("Please insert your plaintext?")
        state = input()
    
    while(key == None or not (lenkey == 16 or lenkey == 32 or lenkey == 24)):
        print("Please insert your cipher key? Your key must be of length 16, 24 or 32")
        key = input()
        if (hexakey):
            lenkey = len(key) // 2
        else:
            lenkey = len(key)
    
    if (b64 == True):
        state = b64e(state)


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

    if (hexain):
        res = [state[y - 32:y] for y in range(32, len(state) + 32, 32)]
        lim = 32 - len(res[-1])
    else:
        res = [state[y - 16:y] for y in range(16, len(state) + 16, 16)]
        lim = 16 - len(res[-1])


    for i in range(0, lim):
        res[-1] += chr(0x00)
    
    key = strConversion[hexakey](key)
    if (lenkey != 16):
        cypherkey = np.transpose(key)
        cypherkey = cypherkey.tolist()
    else: cypherkey = key
    
    if (mode == "CBC"):
        temp = strConversion[hexaIV](IV)
        for i in res:
            sub = strConversion[hexain](i)
            sub = xorMatrix(sub, temp)
            sub = func[lenkey](sub, cypherkey)
            temp = sub
            sub = matConversion[hexaout](sub)
            ret += sub

    elif (mode == "CFB"):
        temp = strConversion[hexaIV](IV)
        for i in res:
            sub = strConversion[hexain](i)
            temp = func[lenkey](temp, cypherkey)
            sub = xorMatrix(sub, temp)
            temp = sub
            sub = matConversion[hexaout](sub)
            ret += sub


    elif (mode == "OFB"):
        temp = strConversion[hexaIV](IV)
        for i in res:
            sub = strConversion[hexain](i)
            temp = func[lenkey](temp, cypherkey)
            sub = xorMatrix(sub, temp)
            sub = matConversion[hexaout](sub)
            ret += sub        

    else: 
        for i in res:
            sub = strConversion[hexain](i)
            sub = func[lenkey](sub, cypherkey)
            sub = matConversion[hexaout](sub)
            ret += sub

    return ret


def decrypt(state = None, key = None, b64 = False, mode = "ECB", IV = None,  hexain = False, hexakey = False, hexaIV = False, hexaout = False, cipher = None):
    
    ret = ""
    lenkey = 0

    b64 = True if b64 == "True" else False
    hexain = True if hexain == "True" else False
    hexakey = True if hexakey == "True" else False
    hexaIV = True if hexaIV == "True" else False
    hexaout = True if hexaout == "True" else False

    if (hexakey):
        lenkey = len(key) / 2
    else:
        lenkey = len(key)

    while(state == None):
        print("Please insert your plaintext?")
        state = input()
    
    while(key == None or not (lenkey == 16 or lenkey == 32 or lenkey == 24)):
        print("Please insert your cipher key? Your key must be of length 16, 24 or 32")
        key = input()
        if (hexakey):
            lenkey = len(key) / 2
        else:
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

    matConversion = {
        True: matToHexa,
        False: matToString
    }

    strConversion = {
        False: stringToMat,
        True: hexaToMat
    }

    if (hexain):
        res = [state[y - 32:y] for y in range(32, len(state) + 32, 32)]
        lim = 32 - len(res[-1])
    else:
        res = [state[y - 16:y] for y in range(16, len(state) + 16, 16)]
        lim = 16 - len(res[-1])

    for i in range(0, lim):
        res[-1] += chr(0x00)
    
    key = strConversion[hexakey](key)
    if (lenkey != 16):
        cypherkey = np.transpose(key)
        cypherkey = cypherkey.tolist()
    else: cypherkey = key

    if (mode == "CBC"):
        temp = strConversion[hexaIV](IV)
        for i in res:
            sub = strConversion[hexain](i)
            sub = func[lenkey](sub, cypherkey)
            sub = xorMatrix(sub, temp)
            sub = matConversion[hexaout](sub)
            temp = strConversion[hexain](i)
            ret += sub
    
    elif (mode == "CFB"):
        temp = strConversion[hexaIV](IV)
        for i in res:
            sub = strConversion[hexain](i)
            temp = enfunc[lenkey](temp, cypherkey)
            sub = xorMatrix(sub, temp)
            temp = strConversion[hexain](i)
            sub = matConversion[hexaout](sub)
            ret += sub


    elif (mode == "OFB"):
        temp = strConversion[hexaIV](IV)
        for i in res:
            sub = strConversion[hexain](i)
            temp = enfunc[lenkey](temp, cypherkey)
            sub = xorMatrix(sub, temp)
            sub = matConversion[hexaout](sub)
            ret += sub
            

    else:
        for i in res:
            sub = strConversion[hexain](i)
            sub = func[lenkey](sub, cypherkey)
            sub = matConversion[hexaout](sub)
            ret += sub

    ret = ret.rstrip(chr(0x00))

    if (b64 == True):
        ret = b64d(ret)

    return ret