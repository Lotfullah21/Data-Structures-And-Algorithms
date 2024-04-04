def pairSum(arr, sum):
    "Returns True if summation of a pair in the given array arr results to sum"
    n = len(arr)
    s = set()
    for i in range(n):
        # sum = arr[i] + x; x is unknown.
        ans = sum - arr[i]
        if ans in s:
            return True
        s.add(arr[i])
    return False

arr = [1,2,3,4,5,6,7,8]
result = pairSum(arr, 9)
print(result)