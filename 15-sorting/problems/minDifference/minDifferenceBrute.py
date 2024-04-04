def minDifference(arr: list) -> int:
    "Returns the min difference between two arrays."
    n = len(arr)
    ans = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            ans = min(ans, abs(arr[i]-arr[j]))
    return ans


arr = [1,92,32 ,4321, 2132, 42, 433,45]
result = minDifference(arr)
print(result)