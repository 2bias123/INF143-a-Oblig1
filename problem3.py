def shift_left(inp, n):
    return inp[n:] + inp[:n]

print(shift_left("10110011", 3))

#Skal denne kjøre akkurat 4 ganger
def simon_cipher_rounds(inp, roundkey):
    leftBlock = inp[:8]
    rightBlock =inp[8:]

    shift1 = int(shift_left(leftBlock,1),2)
    shift5 = int(shift_left(leftBlock,5),2)

    #Bitwise and of the leftBlock shifted 1 and 5
    and15 = shift1 & shift5

    #Bitwise xor of the rightBlock and the and15
    xorOfRightAndand15 = int(rightBlock,2) ^ and15

    shift2 = int(shift_left(leftBlock,2),2)

    #Bitwise xor of the xorOfRightAndand15 and the leftBlock shifted 2
    xorOfRightAndand15AndShift2 = xorOfRightAndand15 ^ shift2

    #Bitwise xor of the xorOfRightAndand15AndShift2 and the roundkey
    xorOfRightAndand15AndShift2AndRoundkey = bin(xorOfRightAndand15AndShift2 ^ int(roundkey,2))[2:]

    return str(xorOfRightAndand15AndShift2AndRoundkey) + leftBlock

def swapMiddle(inp):
    return inp[8:] + inp[:8]

def simon_cipher(inp, key):
    tmp = inp
    chunks = [key[x:x+8] for x in range(0, len(key), 8)]
    for i in range(4):
        tmp = simon_cipher_rounds(tmp,chunks[i])
        # print(tmp)
    
    return swapMiddle(tmp)

print(simon_cipher("1011001111110000","01000100000110101000101000111000"))

