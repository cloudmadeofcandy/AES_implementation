from aesUtils import matToString, stringToMat
import encryption as en
import decryption as de
import numpy as np

def encrypt(state = None, key = None):
    
    ret = ""

    while(state == None):
        print("Please insert your plaintext?")
        state = input()
    
    while(key == None or not (len(key) == 16 or len(key) == 32 or len(key) == 24)):
        print("Please insert your cipher key? Your key must be of length 16, 24 or 32")
        key = input()
    
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
    cypherkey = np.transpose(key)
    cypherkey = cypherkey.tolist()

    for i in res:
        sub = stringToMat(i)
        sub = func[lenkey](sub, cypherkey)
        sub = matToString(sub)
        ret += sub

    return ret


def decrypt(state = None, key = None):
    
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
    cypherkey = np.transpose(key)
    cypherkey = cypherkey.tolist()

    for i in res:
        sub = stringToMat(i)
        sub = func[lenkey](sub, cypherkey)
        sub = matToString(sub)
        ret += sub

    return ret