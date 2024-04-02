def inversionCount(arr: list) -> int:
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                count+=1
    return count


arr = [1, 2, 2, 4, 3, 2]
result = inversionCount(arr)
print("number of inversion counts =",result)