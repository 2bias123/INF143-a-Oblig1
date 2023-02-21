initial = [1 if i==0 or i==29 else 0 for i in range(30)]

# Polynomial: x^30 + x^23 + x^2 + x^1 + 1
def lfsr(initialState: list, itr: int, returnval: list) -> list:
    if len(initialState) == 30 and itr > 0:
        one: int = initialState[30-1]
        two: int = initialState[30-2]
        three: int = initialState[30-3]
        t23: int = initialState[6]
        xored: int = one ^ two ^ three ^ t23
        returnval.append(initialState.pop())
        initialState.insert(0,xored)
        return lfsr(initialState,itr-1,returnval)
    elif itr <= 0:
        return returnval


outs: list = lfsr(initial,40,[])
with open("outputTask1.txt","w") as out:
    for i in outs:
        out.write(str(i))