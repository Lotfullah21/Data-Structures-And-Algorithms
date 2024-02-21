def printSubArray(arr: list) -> list[list]:
    n = len(arr)
    for s in range(n):
        for e in range(s, n+1):
            for i in range(s, e):
                print(arr[i],end="")
            print()
                    
arr  = [1, 2, 3, 4]
result = printSubArray(arr)
print(result)