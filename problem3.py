

def cyclic_shift(inp, shiftdegree: int):
    return inp[shiftdegree:] + inp[:shiftdegree]


#Skal denne kjøre akkurat 4 ganger
def simon_cipher_rounds(inp, roundkey):
    frstBlock = inp[8:]
    sndBlock = inp[:8]

    frstBlockShift1 = cyclic_shift(frstBlock,1)
    frstBlockShift5 = cyclic_shift(frstBlock,5)
    #Logical and of the two cyclic shifts above
    andfirstShifts = frstBlockShift1 & frstBlockShift5

    #xor of the right block and the andfirstShifts
    firstshiftsxored = andfirstShifts ^ sndBlock

    frstBlockShift2 = cyclic_shift(frstBlock,5)

    #xor of firstShiftsxored and frstBlockshift 2
    xored1 = firstshiftsxored ^ frstBlockShift2

    #xor of xored1 with roundkey
    roundkeyxor = xored1 ^ roundkey

    return roundkeyxor + frstBlock

def simon_cipher(inp, key):
    tmp = inp
    chunks = [key[x:x+8] for x in range(0, len(key), 8)]
    for i in range(4):
        tmp = simon_cipher(tmp,chunks[i])
        # print(chunks[i])
    return tmp

simon_cipher(1,"1"*32)