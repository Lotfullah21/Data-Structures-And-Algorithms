def pairSum(arr, x):
    "Returns True if summation of a pair in the given array arr results to x"
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+arr[j]==x:
                return True, arr[i],arr[j]
    return False

arr = [1,2,3,4,5,6,7,8]
result = pairSum(arr, 9)
print(result)