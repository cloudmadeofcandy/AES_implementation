def mul2(r):
    b = [0 for i in range(4)]
    for c in range(0, 4):
        h = (r[c] >> 7) & 1
        b[c] = r[c] << 1
        b[c] ^= h * 0x1B
    return b

def mul3(r):
    b = mul2(r);
    for c in range(0, 4):
        b[c] = b[c] ^ r[c]
    return b

def mul9(r):
    b = list.copy(r)
    for i in range(0, 3):
        b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    return b

def mul11(r):
    b = list.copy(r)
    b = mul2(b)
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    return b

def mul13(r):
    b = list.copy(r)
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    b = mul2(b)
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    return b            

def mul14(r):
    b = list.copy(r)
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    b = mul2(b)
    for c in range(0, 4):
        b[c] ^= r[c]
    b = mul2(b)
    return b