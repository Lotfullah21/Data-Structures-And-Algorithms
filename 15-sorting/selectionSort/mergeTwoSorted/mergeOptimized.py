def mergeTwoSorted(arrayM: list, arrayN: list) ->list:
    a = 0
    b = 0
    arrayL = [0]*(len(arrayM)+len(arrayN))
    c = 0
    N = len(arrayN)
    M = len(arrayM)
    # If or is used instead of and; and one of the arrays are already empty, it will give out of bound error.
    while (a<M and b<N):
        if arrayM[a]<arrayN[b]:
            arrayL[c]= arrayM[a]
            a+=1
            c+=1
        else:
            arrayL[c] = arrayN[b]
            b+=1
            c+=1
    while a<M:
        arrayL[c]= arrayM[a]
        a+=1
        c+=1
    while b<N:
        arrayL[c]= arrayN[b]
        b+=1
        c+=1
    return arrayL

# Example Solution        
a = [1, 2]
b = [0,-32,12]
result = mergeTwoSorted(a, b)
print(result)