def chocolateFair(arr: list, m: int) -> int:
    "Returns the minimum difference between  chocolate distribution to m number of children"
    if m==0 or len(arr)==0:
        return 0
    if len(arr)<m:
        return -1
    # For 0th index
    arr.sort()
    nums = []
    res = arr[m-1]-arr[0]
    for i in range(1, len(arr)-m+1):
        res = min(res, arr[m+i-1]-arr[i])
        nums.append(arr[i])
    return res
    
    
arr = [1, 4,6, 8, 10, 213,12,34,12]
result = chocolateFair(arr, 3)
print(result)