def removeDuplicates(arr: list) -> list:
    idx = 1
    for i in range(1, len(arr)):
        if arr[i-1]!=arr[i]:
            arr[idx] = arr[i]
            idx+=1
    return arr[:idx]

array = [1, 2, 2, 3, 3, 4, 5, 6, 7,7, 8]
array.sort()
print(array)
unique = removeDuplicates(array)
print("Reversed list", unique)