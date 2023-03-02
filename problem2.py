import bit_operations as bit_op

# Adition is basicly bitwise xor
def addition(x: list, k: list):
    retlst: list = []
    for i in range(len(x)):
        retlst.append(x[i] ^ k[i])
    return retlst

irr_pol = [1,1,0,0,0,0]

def shift(x: list, poly: list, shift: int) -> list:
    for _ in range(shift):
        x = [0] + x
        popped = x.pop()
        if popped == 1:
            x = bit_op.lstxor(poly,x)
    return x

def mult(a: list,b: list, output: list, irreducible: list) -> list:
    for i in range(len(a)):
        if b[i] == 1:
            shifted = shift(a,irreducible,i)
            output = bit_op.lstxor(shifted,output)
            # print("u",output)
    return output

def pow(a: list, exp: int, irreducible: list):
    temp = a
    for _ in range(exp-1):
        temp = mult(temp,a,[0,0,0,0,0,0],irreducible)
    return temp

#F (x, k) = x^3 + (x + k)^3 + k
def calculate_function(k,x,irreducible):
    x3 = pow(x,3,irreducible)
    k3 = pow(addition(x,k),3,irreducible)
    add1 = addition(x3,k3)
    add2 = addition(add1,k)
    return add2

def format(x,k,putout):
    x_format = "".join([str(a) for a in x ])
    k_format = "".join([str(a) for a in k ])
    putout_format = "".join([str(a) for a in putout])
    return f"{x_format},{k_format}->{putout_format}\n"

with open("answerTask2.txt","w") as out:
    for i in range(2**6): # iterate over all possible values of x and k
        x = [int(digit) for digit in bin(i)[2:].zfill(6)] # convert integer to binary and pad with zeros
        for j in range(2**6):
            k = [int(digit) for digit in bin(j)[2:].zfill(6)]
            out.write(format(k,x,calculate_function(k,x,irr_pol)))



