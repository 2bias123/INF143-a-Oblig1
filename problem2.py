# Adition is basicly bitwise xor

def addition(x: list, k: list):
    retlst: list = []
    for i in range(len(x)):
        retlst.append(x[i] ^ k[i])
    return retlst


def lstxor(a: list, b: list):
    outs: list = []
    for i in range(len(a)):
        outs.append(a[i] ^ b[i])
    return outs


irr_pol = [1,1,0,0,0,0]



def shift(x: list, poly: list, shift: int) -> list:
    for _ in range(shift):
        x = [0] + x
        popped = x.pop()
        if popped == 1:
            x = lstxor(poly,x)
    return x

def mult(a: list,b: list, output: list, irreducible: list) -> list:
    for i in range(len(a)):
        if b[i] == 1:
            shifted = shift(a,irreducible,i)
            output = lstxor(shifted,output)
        return output

def pow(a: list, exp: int, irreducible: list):
    for _ in range(exp):
        a = mult(a,a,[0,0,0,0,0,0],irreducible)
    return a

def calculate_function(k,x,irreducible):
    frstpart = pow(x,3,irreducible)
    middle_of_parentheses = addition(k,x)
    pow_parentheses = pow(middle_of_parentheses,3,irreducible)
    frsttwo = addition(frstpart,pow_parentheses)
    therest = addition(frsttwo,k)
    return therest

# print(calculate_function([0,0,0,0,0,0],[0,0,0,0,0,0],irr_pol))

def format(x,k,putout):
    x_format = "".join([str(a) for a in x ])
    k_format = "".join([str(a) for a in k ])
    putout_format = "".join([str(a) for a in putout])
    return f"{x_format},{k_format}->{putout_format}\n"

with open("outputTask2.txt","w") as out:
    for i in range(2**6): # iterate over all possible values of x and k
        x = [int(digit) for digit in bin(i)[2:].zfill(6)] # convert integer to binary and pad with zeros
        for j in range(2**6):
            k = [int(digit) for digit in bin(j)[2:].zfill(6)]
            out.write(format(k,x,calculate_function(k,x,irr_pol)))

