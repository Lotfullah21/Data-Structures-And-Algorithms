def goodIntegers(arr: list) -> list[int]:
    "Returns number of good integers"
    n = len(arr)
    goodIntegers = []
    for i in range(n):
        c = 0
        for j in range(n):
            if arr[i]>arr[j]:
                c+=1
        if c==arr[i]:
            goodIntegers.append(arr[i])
    return goodIntegers


arr = [-1, -2, 2, 3 ,4]
result = goodIntegers(arr)
print(result)