import bit_operations as bit_op

def addition(x: list, k: list) -> list:
    """
    Performs addition of two bit arrays x and k by taking the bitwise xor of each element.

    Parameters:
    x (list): First bit array.
    k (list): Second bit array.

    Returns:
    list: Result of addition operation as a bit array.
    """
    retlst: list = []
    for i in range(len(x)):
        retlst.append(x[i] ^ k[i])
    return retlst

# Define an irreducible polynomial for the finite field.
irr_pol = [1,1,0,0,0,0]

def shift(x: list, poly: list, shift: int) -> list:
    """
    Shifts a bit array x to the left by a number of positions specified by shift. If the
    leftmost element of x is a 1, perform addition with the polynomial poly.

    Parameters:
    x (list): Bit array to shift.
    poly (list): Polynomial for the finite field.
    shift (int): Number of positions to shift x to the left.

    Returns:
    list: Result of the shift operation as a bit array.
    """
    for _ in range(shift):
        x: list = [0] + x
        popped: int = x.pop()
        if popped == 1:
            x: list = bit_op.lstxor(poly,x)
    return x

def mult(a: list,b: list, output: list, irreducible: list) -> list:
    """
    Multiplies two bit arrays a and b using polynomial multiplication over a finite field.

    Parameters:
    a (list): First bit array.
    b (list): Second bit array.
    output (list): Starting value for the output bit array.
    irreducible (list): Polynomial for the finite field.

    Returns:
    list: Result of the multiplication operation as a bit array.
    """
    for i in range(len(a)):
        if b[i] == 1:
            shifted: list = shift(a,irreducible,i)
            output: list = bit_op.lstxor(shifted,output)
    return output

def pow(a: list, exp: int, irreducible: list) -> list:
    """
    Raises a bit array a to the power of an exponent using repeated squaring.

    Parameters:
    a (list): Bit array to be raised to a power.
    exp (int): Exponent to raise a to.
    irreducible (list): Polynomial for the finite field.

    Returns:
    list: Result of the power operation as a bit array.
    """
    temp: list = a
    for _ in range(exp-1):
        temp: list = mult(temp,a,[0,0,0,0,0,0],irreducible)
    return temp

#F (x, k) = x^3 + (x + k)^3 + k
def calculate_function(k: list,x: list,irreducible: list)-> list:
    """
    Calculates the value of the function F(x, k) = x^3 + (x + k)^3 + k for a given bit arrays x and k.

    Parameters:
    k (list): Bit array k.
    x (list): Bit array x.
    irreducible (list): Polynomial for the finite field.

    Returns:
    list: Result of the F function as a bit array.
    """
    x3: list = pow(x,3,irreducible)
    k3: list = pow(addition(x,k),3,irreducible)
    add1: list = addition(x3,k3)
    add2: list = addition(add1,k)
    return add2

def format(x: list,k: list,putout: list) -> str:
    """
    Formats the input and output bit lists of the calculate_function into a string.

    Parameters:
    x (list): The input bit list x used as an argument in calculate_function.
    k (list): The input bit list k used as an argument in calculate_function.
    putout (list): The output bit list returned by calculate_function for the given input x and k.

    Returns:
    str: The formatted string that concatenates the input and output bit lists.
    """
    x_format = "".join([str(a) for a in x ])
    k_format = "".join([str(a) for a in k ])
    putout_format = "".join([str(a) for a in putout])
    return f"{x_format},{k_format}->{putout_format}\n"


def write_output_to_file(filepath):
    """
    Iterates over all possible values of x and k with 'num_bits' bits, and writes to a file 'filepath'
    the result of calling a the calculate_function with each pair of x and k.

    Args:
        filepath (str): path of the output file

    Returns:
        None
    """
    with open(filepath,"w") as out:
        for i in range(2**6): # iterate over all possible values of x and k
            x = [int(digit) for digit in bin(i)[2:].zfill(6)] # convert integer to binary and pad with zeros
            for j in range(2**6):
                k = [int(digit) for digit in bin(j)[2:].zfill(6)]
                out.write(format(k,x,calculate_function(k,x,irr_pol)))



