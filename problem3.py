import bit_operations as bit_op

def simon_cipher_rounds(inp: list[int], roundkey: list[int]) -> list[int]:
    # Split the input block into left and right halves
    left_block: list = inp[:8]
    right_block: list = inp[8:]

    # Perform cyclic shifts on the left half
    left_shift_1: list = bit_op.left_cyclic_shift(left_block,1)
    left_shift_5: list = bit_op.left_cyclic_shift(left_block,5)
    left_shift_2: list = bit_op.left_cyclic_shift(left_block,2)

    # Perform bitwise AND operation on the shifted left half
    shift_1_and_shift_5: list = bit_op.bitwise_and_lst(left_shift_1,left_shift_5)

    # Perform XOR operation between the result and the right half
    xor_of_and: list = bit_op.lstxor(right_block,shift_1_and_shift_5)

    # Perform XOR operation between the result and the shifted left half
    xor_shift_2: list = bit_op.lstxor(xor_of_and,left_shift_2)

    # Perform XOR operation between the result and the round key
    xor_roundkey: list = bit_op.lstxor(xor_shift_2,roundkey)

    # Return the result by combining the left and right halves
    return xor_roundkey + left_block

# Split the given key into multiple subkeys of specified length
def roundkey_generator(roundkey: list, nmbr_of_rounds: int) ->list[list[int]]:
    return [roundkey[i:i + nmbr_of_rounds] for i in range(0, len(roundkey), nmbr_of_rounds)]


#Defines a function that performs the Simon Cipher for each roundkey
def simon_cipher(inp: list,key: list) -> list:
    tmp: list = inp
    for i in range(4):
        tmp: list = simon_cipher_rounds(tmp,key[i])
    return tmp[8:] + tmp[:8]

#Encrypts the plaintext and writes the ciphertext to a file
def encrypt(plaintext_file: str,key_file: str) -> list:
    with open(plaintext_file,"r") as plaintext, open(key_file,"r") as key, open("answerTask3Encrypted.txt","w") as out:
        plaintext_line = [int(char) for char in plaintext.readline().strip()]
        key_line = [int(char) for char in key.readline().strip()]
        encrypted = simon_cipher(plaintext_line,roundkey_generator(key_line,8))
        out.write("".join([str(i) for i in encrypted]))
        

#Decrypts the ciphertext and writes the plaintext to a file
def decrypt(ciphertext_file: str,key_file: str) -> list:
    with open(ciphertext_file,"r") as ciphertext, open(key_file,"r") as key, open("answerTask3Decrypyted.txt","w") as out:
        plaintext_line = [int(char) for char in ciphertext.readline().strip()]
        key_line = [int(char) for char in key.readline().strip()]
        decrypted = simon_cipher(plaintext_line,roundkey_generator(key_line,8)[::-1])
        out.write("".join([str(i) for i in decrypted]))

encrypt("sample_data\cipher_in2.txt","sample_data\cipher_key.txt")
decrypt("answerTask3Encrypted.txt","sample_data\cipher_key.txt")