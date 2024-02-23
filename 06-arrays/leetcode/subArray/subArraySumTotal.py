def printSubArraySum(arr: list) -> list:
    n = len(arr)
    pf = [0]*n
    pf[0] = arr[0]
    # Create the prefix array sum.
    for i in range(1,n):
        pf[i] = pf[i-1]+arr[i]
    print(pf)
    # Keep a reference to total variable
    total = 0
    for s in range(n):
        for e in range(s, n):
            if s==0:
                total = pf[e] + total
            else:
                total  = pf[e]-pf[s-1] + total
    return total
                                
arr = [5, 3, -1, 8]
result = printSubArraySum(arr)
print(result)

