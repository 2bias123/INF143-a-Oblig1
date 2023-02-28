initial = [1 if i==0 or i==29 else 0 for i in range(30)]

# Polynomial: x^30 + x^23 + x^2 + x^1 + 1
    
#The polynomial represented as where the indexes of the feedbacklines are located
pol = [0,1,2,23]
pol2 = [0,1,2,3,5,7,11,13,16,17]

def xor(n1,n2):
    if (n1==n2):
        return 0
    return 1

def lfsr(polynomial: list, initialState: list, itr: int, returnval: list) -> list:
    if len(initialState) == 30 and itr > 0:

        selectedcells: list = []

        for i in polynomial:
            selectedcells.append(initialState[29-i])

        res: int = selectedcells[0]
        for i in range(1,len(selectedcells)):
            #res ^= selectedcells[i]
            res = xor(res, selectedcells[i])

        returnval.append(initialState.pop())
        initialState.insert(0,res)
        return lfsr(pol,initialState,itr-1,returnval)
    elif itr <= 0:
        return returnval


outs: list = lfsr(pol,initial,500,[])
with open("outputTask1.txt","w") as out:
    for i in outs:
        out.write(str(i))