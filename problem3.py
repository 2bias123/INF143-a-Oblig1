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

# print(ed[::-1])
generated_roundkey = roundkey_generator(roundkey,8)

#Reverserer listen for å dekryptere
def simon_cipher(inp,key):
    tmp = inp
    for i in range(4):
        tmp = simon_cipher_rounds(tmp,key[i])
    return tmp[8:] + tmp[:8]


def encrypt(plaintext_file: str,key_file: str):
    with open(plaintext_file,"r") as plaintext, open(key_file,"r") as key, open("answerTask3Encrypted.txt","w") as out:
        plaintext_line = [int(char) for char in plaintext.readline().strip()]
        key_line = [int(char) for char in key.readline().strip()]
        out.write("".join([str(i) for i in simon_cipher(plaintext_line,roundkey_generator(key_line,8))]))
        

def decrypt(ciphertext_file: str,key_file: str):
    with open(ciphertext_file,"r") as ciphertext, open(key_file,"r") as key, open("answerTask3Decrypyted.txt","w") as out:
        plaintext_line = [int(char) for char in ciphertext.readline().strip()]
        key_line = [int(char) for char in key.readline().strip()][::-1]
        out.write("".join([str(i) for i in simon_cipher(plaintext_line,roundkey_generator(key_line,8))]))

decrypt("answerTask3.txt","sample_data\cipher_key.txt")
# print(simon_cipher(plaintext,generated_roundkey))

