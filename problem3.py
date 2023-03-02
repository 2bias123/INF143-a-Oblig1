import bit_operations as bit_op

#Skal denne kjøre akkurat 4 ganger
def simon_cipher_rounds(inp: list[int], roundkey: list[int]):
    left_block: list = inp[:8]
    right_block: list = inp[8:]

    left_shift_1 = bit_op.left_cyclic_shift(left_block,1)
    left_shift_5 = bit_op.left_cyclic_shift(left_block,5)
    left_shift_2 = bit_op.left_cyclic_shift(left_block,2)

    shift_1_and_shift_5 = bit_op.bitwise_and_lst(left_shift_1,left_shift_5)

    xor_of_and = bit_op.lstxor(right_block,shift_1_and_shift_5)

    xor_shift_2 = bit_op.lstxor(xor_of_and,left_shift_2)

    xor_roundkey = bit_op.lstxor(xor_shift_2,roundkey)

    return xor_roundkey + left_block

plaintext = [1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,0]

roundkey = [0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,0,0]

def roundkey_generator(roundkey, nmbr_of_rounds):
    return [roundkey[i:i + nmbr_of_rounds] for i in range(0, len(roundkey), nmbr_of_rounds)]

def simon_cipher(inp):
    roundkeys = roundkey_generator(roundkey,8)
    tmp = inp
    for i in range(4):
        tmp = simon_cipher_rounds(tmp,roundkeys[i])
    return tmp[8:] + tmp[:8]


print(simon_cipher(plaintext))

