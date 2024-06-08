def isSorted(arr: list) -> bool:
    "Returns True if array is sorted"
    i = 1
    newArray = arr[:]
    newArray.sort()
    if arr==newArray:
        return True
    else:
        return False

arr = [1, 2, 6, 7, 9,0]
result = isSorted(arr)
print("Is The Array Sorted:? ", result)