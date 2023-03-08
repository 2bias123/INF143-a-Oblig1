def lstxor(a: list, b: list) -> list:
    outs: list = []
    for i in range(len(a)):
        outs.append(a[i] ^ b[i])
    return outs

def bitwise_and_lst(a:list, b:list) -> list:
    return_val: list = []
    for i in range(len(a)):
        if a[i] == 1 and b[i] == 1:
            return_val.append(1)
        else:
            return_val.append(0)
    return return_val

def left_cyclic_shift(to_be_shifted: list, shift_value: int) -> list:
    shifted_list:list = to_be_shifted.copy()
    for _ in range(shift_value):
        shifted_list.append(shifted_list.pop(0))
    return shifted_list

def right_cyclic_shift(to_be_shifted: list, shift_value: int) -> list:
    shifted_list: list = to_be_shifted.copy()
    for _ in range(shift_value):
        popped: int = shifted_list.pop()
        shifted_list.insert(0,popped)
    return shifted_list

def xor(n1,n2):
    if (n1==n2):
        return 0
    return 1
